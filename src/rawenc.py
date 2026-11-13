#!/usr/bin/env python3
"""Prototype raw AAR encoder. Derived black-box from /usr/bin/aa I/O only.
Usage: rawenc.py SRCDIR OUT.aar
Emits -a raw equivalent bytes for dir/file/symlink trees.
"""
import os
import sys

PROV_NAME = b"com.apple.provenance"
PROV_VAL = bytes.fromhex("0102006697d07abb102c73")  # const 8/8 probes, this host


def put_time(buf, key, sec, nsec):
    if nsec == 0:
        buf += key + b"S" + sec.to_bytes(8, "little")
    else:
        buf += key + b"T" + sec.to_bytes(8, "little") + nsec.to_bytes(4, "little")
    return buf


def xat_records(path, is_link):
    import ctypes
    recs = [(PROV_NAME, PROV_VAL)]
    if is_link:
        return recs  # oracle emits provenance-only on links (p4-l, p6-sl, p8-sl)
    try:
        libc = ctypes.CDLL("/usr/lib/libc.dylib", use_errno=True)
        XATTR_NOFOLLOW = 0x1
        libc.listxattr.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
        libc.listxattr.restype = ctypes.c_ssize_t
        libc.getxattr.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t,
                                  ctypes.c_uint32, ctypes.c_int]
        libc.getxattr.restype = ctypes.c_ssize_t
        n = libc.listxattr(path, None, 0, XATTR_NOFOLLOW)
        if n <= 0:
            return recs
        buf = ctypes.create_string_buffer(n)
        if libc.listxattr(path, buf, n, XATTR_NOFOLLOW) < 0:
            return recs
        names = sorted(buf.raw[:n].split(b"\x00"))
        for nm in names:
            if not nm or nm == PROV_NAME:
                continue
            sz = libc.getxattr(path, nm, None, 0, 0, XATTR_NOFOLLOW)
            if sz < 0:
                continue
            vbuf = ctypes.create_string_buffer(sz if sz > 0 else 1)
            r = libc.getxattr(path, nm, vbuf, sz, 0, XATTR_NOFOLLOW)
            if r < 0:
                continue
            recs.append((nm, vbuf.raw[:r]))
    except OSError:
        pass
    return recs


def crtime_ns(pathb, nofollow):
    import ctypes
    try:
        libc = ctypes.CDLL("/usr/lib/libc.dylib", use_errno=True)

        class AttrList(ctypes.Structure):
            _fields_ = [("bitmapcount", ctypes.c_ushort), ("reserved", ctypes.c_ushort),
                        ("commonattr", ctypes.c_uint), ("volattr", ctypes.c_uint),
                        ("dirattr", ctypes.c_uint), ("fileattr", ctypes.c_uint),
                        ("forkattr", ctypes.c_uint)]

        class Ts(ctypes.Structure):
            _fields_ = [("sec", ctypes.c_long), ("nsec", ctypes.c_long)]

        al = AttrList(5, 0, 0x200, 0, 0, 0, 0)  # ATTR_CMN_CRTIME
        buf = ctypes.create_string_buffer(20)
        libc.getattrlist.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p,
                                     ctypes.c_size_t, ctypes.c_ulong]
        libc.getattrlist.restype = ctypes.c_int
        if libc.getattrlist(pathb, ctypes.byref(al), buf, 20, 0x1 if nofollow else 0) != 0:
            return None
        ts = Ts.from_buffer_copy(buf, 4)
        return ts.sec * 1_000_000_000 + ts.nsec
    except OSError:
        return None


def dat_kind(n):
    if n <= 0xFFFF:
        return b"A", n.to_bytes(2, "little")
    if n <= 0xFFFFFFFF:
        return b"B", n.to_bytes(4, "little")
    return b"C", n.to_bytes(8, "little")


def put_int(buf, key, val):
    if val <= 0xFF:
        return buf + key + b"1" + bytes([val])
    if val <= 0xFFFF:
        return buf + key + b"2" + val.to_bytes(2, "little")
    return buf + key + b"4" + val.to_bytes(4, "little")


def entry(hdr, payloads):
    hdrsize = 6 + len(hdr)
    return b"AA01" + hdrsize.to_bytes(2, "little") + hdr + b"".join(payloads)


def encode_entry(rel, st, typ):
    h = b""
    payloads = []
    h += b"TYP1" + typ
    h += b"PATP" + len(rel).to_bytes(2, "little") + rel
    if typ == b"L":
        tgt = os.readlink(os.path.join(ROOTB, rel))
        h += b"LNKP" + len(tgt).to_bytes(2, "little") + tgt
    if typ in (b"B", b"C"):
        h = put_int(h, b"DEV", st.st_rdev & 0xFFFFFFFF)
    h = put_int(h, b"UID", st.st_uid)
    h = put_int(h, b"GID", st.st_gid)
    h = put_int(h, b"MOD", st.st_mode & 0x0FFF)
    h = put_int(h, b"FLG", getattr(st, "st_flags", 0))  # st_flags macOS-only; 0 elsewhere
    full = os.path.join(ROOTB, rel)
    cns = crtime_ns(full, typ == b"L")
    if cns is None:  # no crtime (non-Apple FS): fall back to mtime
        cns = st.st_mtime_ns
    mns = st.st_mtime_ns
    h = put_time(h, b"CTM", cns // 1_000_000_000, cns % 1_000_000_000)
    h = put_time(h, b"MTM", mns // 1_000_000_000, mns % 1_000_000_000)
    if typ == b"F":
        with open(full, "rb") as f:
            data = f.read()
        k, lb = dat_kind(len(data))
        h += b"DAT" + k + lb
        payloads.append(data)
    if typ in (b"D", b"F", b"L"):
        recs = xat_records(full, typ == b"L")
        xat = b""
        for nm, val in recs:
            rec = len(nm) + 1 + len(val) + 4
            xat += rec.to_bytes(4, "little") + nm + b"\x00" + val
        h += b"XATA" + len(xat).to_bytes(2, "little")
        payloads.append(xat)
    if typ == b"F" and st.st_nlink > 1:
        h += b"HLC1\x00"
    return entry(h, payloads)


def walk(dirb, relb):
    out = []
    try:
        names = sorted(os.listdir(dirb))
    except OSError:
        return out
    for nm in names:
        fb = os.path.join(dirb, nm)
        rb = nm if not relb else relb + b"/" + nm
        st = os.lstat(fb)
        import stat as _s
        if _s.S_ISLNK(st.st_mode):
            out.append(encode_entry(rb, st, b"L"))
        elif _s.S_ISDIR(st.st_mode):
            out.append(encode_entry(rb, st, b"D"))
            out.extend(walk(fb, rb))
        elif _s.S_ISREG(st.st_mode):
            out.append(encode_entry(rb, st, b"F"))
        elif _s.S_ISBLK(st.st_mode):
            out.append(encode_entry(rb, st, b"B"))
        elif _s.S_ISCHR(st.st_mode):
            out.append(encode_entry(rb, st, b"C"))
        elif _s.S_ISSOCK(st.st_mode):
            out.append(encode_entry(rb, st, b"S"))
        # fifo: oracle HANGS reading it (ruling-grade negative); skipped.
    return out


ROOTB = None


def build_inner(rootb):
    global ROOTB
    ROOTB = rootb
    st0 = os.lstat(rootb)
    return b"".join([encode_entry(b"", st0, b"D")] + walk(rootb, b""))


if __name__ == "__main__":
    data = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(data)
