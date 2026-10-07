#!/usr/bin/env python3
"""aad.py — decode prototype v2 (REFERENCE ONLY, not the deliverable).

Covers: multi-block chain (PRE-002) + all 7 codecs + inner TLV + extract.
Codec backends (prototype-only): stored/raw direct; zlib+xz stdlib;
lzfse/lz4/lzraven via /usr/bin/compression_tool; lzbitmap via libzbm
dylib (MIT, A-006 row 3) at $ZBM_DYLIB. Validated vs oracle, never vs OSS.
"""
import ctypes
import lzma
import os
import stat
import struct
import subprocess
import sys
import zlib

INNER_MAGICS = (b"AA01", b"YAA1")
UINT_W = {ord("1"): 1, ord("2"): 2, ord("4"): 4, ord("8"): 8}
BLOB_W = {ord("A"): 2, ord("B"): 4, ord("C"): 8}
HASH_L = {ord("F"): 4, ord("G"): 20, ord("H"): 32, ord("I"): 48, ord("J"): 64}
TS_L = {ord("S"): 8, ord("T"): 12}


class FmtErr(Exception):
    pass


CTOOL = "/usr/bin/compression_tool"
CTOOL_ALG = {b"pbze": "lzfse", b"pbz4": "lz4", b"pbzm": "lzraven"}
_zbm = None


def _zbm_dec(payload, unc):
    global _zbm
    if _zbm is None:
        path = os.environ.get("ZBM_DYLIB")
        if not path:
            raise FmtErr("ZBM_DYLIB unset for lzbitmap block")
        _zbm = ctypes.CDLL(path)
        _zbm.zbm_decompress.argtypes = [ctypes.c_void_p, ctypes.c_size_t,
                                        ctypes.c_void_p, ctypes.c_size_t,
                                        ctypes.POINTER(ctypes.c_size_t)]
        _zbm.zbm_decompress.restype = ctypes.c_int
    out = ctypes.create_string_buffer(unc)
    n = ctypes.c_size_t(0)
    r = _zbm.zbm_decompress(out, unc, payload, len(payload), ctypes.byref(n))
    if r != 0 or n.value != unc:
        raise FmtErr("zbm decode r=%d n=%d unc=%d" % (r, n.value, unc))
    return bytes(out.raw)


def _ctool_dec(payload, alg, unc):
    p = subprocess.run([CTOOL, "-decode", "-a", alg], input=payload,
                       capture_output=True)
    if p.returncode != 0:
        raise FmtErr("compression_tool %s exit %d" % (alg, p.returncode))
    if len(p.stdout) != unc:
        raise FmtErr("ctool %s size %d != %d" % (alg, len(p.stdout), unc))
    return p.stdout


def decode_block(magic, payload, unc, comp):
    """Decode one block payload -> inner bytes (A-007 frame rule)."""
    if comp == unc:
        return bytes(payload)
    if magic == b"pbzz":
        raw = zlib.decompress(bytes(payload))
    elif magic == b"pbzx":
        raw = lzma.decompress(bytes(payload))
    elif magic in CTOOL_ALG:
        return _ctool_dec(bytes(payload), CTOOL_ALG[magic], unc)
    elif magic == b"pbzb":
        return _zbm_dec(bytes(payload), unc)
    else:
        raise FmtErr("unknown codec %r" % magic)
    if len(raw) != unc:
        raise FmtErr("codec %r size %d != %d" % (magic, len(raw), unc))
    return raw


def parse_chain(data):
    """-> (inner_bytes, metas). PRE-002: 12B prefix + [16B hdr + comp]*."""
    if bytes(data[:4]) in INNER_MAGICS:
        return bytes(data), [{"alg": "raw", "stored": True,
                              "unc": len(data), "comp": len(data)}]
    if bytes(data[:3]) != b"pbz" or len(data) < 28:
        raise FmtErr("bad outer magic")
    magic = bytes(data[:4])
    if data[4:8] != b"\0\0\0\0":
        raise FmtErr("prefix zeros nonzero")
    bsize = struct.unpack(">I", data[8:12])[0]
    inner, metas, off = bytearray(), [], 12
    while off < len(data):
        if off + 16 > len(data):
            raise FmtErr("block header past EOF at %d" % off)
        z1, unc, z2, comp = struct.unpack(">4sI4sI", data[off:off + 16])
        if z1 != b"\0\0\0\0" or z2 != b"\0\0\0\0":
            raise FmtErr("block zeros nonzero at %d" % off)
        payload = bytes(data[off + 16:off + 16 + comp])
        if len(payload) != comp:
            raise FmtErr("block data past EOF at %d" % off)
        inner += decode_block(magic, payload, unc, comp)
        metas.append({"alg": magic.decode("ascii"), "stored": comp == unc,
                      "unc": unc, "comp": comp, "bsize": bsize})
        off += 16 + comp
    if off != len(data):
        raise FmtErr("chain overrun")
    return bytes(inner), metas


def parse_header(data, pos):
    """-> (entries, endpos). entries: list of (key, subtype, value)."""
    if pos + 6 > len(data):
        raise FmtErr("header past EOF at %d" % pos)
    if bytes(data[pos:pos + 4]) not in INNER_MAGICS:
        raise FmtErr("bad inner magic at %d" % pos)
    (hsize,) = struct.unpack_from("<H", data, pos + 4)
    end = pos + hsize
    if end > len(data) or hsize < 6:
        raise FmtErr("header size past EOF at %d" % pos)
    p = pos + 6
    entries = []
    while p < end:
        if p + 4 > end:
            raise FmtErr("entry tag past end at %d" % p)
        key = bytes(data[p:p + 3])
        st = data[p + 3]
        p += 4
        if st == ord("*"):
            val = None
        elif st in UINT_W:
            w = UINT_W[st]
            if p + w > end:
                raise FmtErr("uint past end at %d" % p)
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in BLOB_W:
            w = BLOB_W[st]
            if p + w > end:
                raise FmtErr("bloblen past end at %d" % p)
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in HASH_L:
            if p + HASH_L[st] > end:
                raise FmtErr("hash past end at %d" % p)
            val = bytes(data[p:p + HASH_L[st]])
            p += HASH_L[st]
        elif st in TS_L:
            if p + TS_L[st] > end:
                raise FmtErr("timespec past end at %d" % p)
            val = bytes(data[p:p + TS_L[st]])
            p += TS_L[st]
        elif st == ord("P"):
            if p + 2 > end:
                raise FmtErr("pathlen past end at %d" % p)
            (ln,) = struct.unpack_from("<H", data, p)
            if p + 2 + ln > end:
                raise FmtErr("path past end at %d" % p)
            val = bytes(data[p + 2:p + 2 + ln])
            p += 2 + ln
        else:
            raise FmtErr("bad subtype 0x%02x at %d" % (st, p - 4))
        entries.append((key, st, val))
    if p != end:
        raise FmtErr("header overrun at %d" % pos)
    return entries, end


def parse_inner(data):
    """-> list of (entries, blobs dict)."""
    items, pos = [], 0
    while pos < len(data):
        entries, end = parse_header(data, pos)
        blobs, bp = {}, end
        for key, st, val in entries:
            if st in BLOB_W:
                if bp + val > len(data):
                    raise FmtErr("blob past EOF at %d" % bp)
                blobs[key] = bytes(data[bp:bp + val])
                bp += val
        items.append((entries, blobs))
        pos = bp
    return items


def _get(entries, key):
    for k, st, v in entries:
        if k == key:
            return st, v
    return None, None


def safe_join(root, rel):
    parts = rel.split(b"/")
    out = os.path.abspath(root)
    for part in parts:
        if part in (b"", b"."):
            continue
        if part == b"..":
            raise FmtErr("path traversal")
        out = os.path.join(out, part.decode("utf-8", "surrogateescape"))
    base = os.path.abspath(root)
    if out != base and not out.startswith(base + os.sep):
        raise FmtErr("path escape")
    return out


_libc = None


def _lib():
    global _libc
    if _libc is None:
        _libc = ctypes.CDLL("/usr/lib/libc.dylib", use_errno=True)
    return _libc


def _ts_ns(raw):
    sec = int.from_bytes(raw[:8], "little")
    ns = int.from_bytes(raw[8:12], "little") if len(raw) == 12 else 0
    return sec * 1000000000 + ns


def apply_xattr_blob(target, blob, islink):
    from ctypes import c_char_p, c_int, c_size_t, c_void_p
    libc = _lib()
    libc.setxattr.argtypes = [c_char_p, c_char_p, c_void_p, c_size_t, c_int,
                              c_int]
    libc.setxattr.restype = c_int
    pos = 0
    while pos + 4 <= len(blob):
        size = int.from_bytes(blob[pos:pos + 4], "little")
        if size < 4 or pos + size > len(blob):
            raise FmtErr("bad xattr record at %d" % pos)
        rec = blob[pos + 4:pos + size]
        nul = rec.find(b"\0")
        if nul < 0:
            raise FmtErr("xattr name unterminated at %d" % pos)
        name, val = bytes(rec[:nul]), bytes(rec[nul + 1:])
        r = libc.setxattr(target.encode("utf-8", "surrogateescape"), name,
                          val, len(val), 0, 1 if islink else 0)
        if r != 0:
            raise FmtErr("setxattr %r failed" % name)
        pos += size


def apply_meta(target, entries, blobs, islink):
    _, mod = _get(entries, b"MOD")
    _, uid = _get(entries, b"UID")
    _, gid = _get(entries, b"GID")
    _, mtm = _get(entries, b"MTM")
    if not islink:
        if mod is not None:
            os.chmod(target, mod & 0o7777)
        if uid is not None or gid is not None:
            try:
                os.chown(target, -1 if uid is None else uid,
                         -1 if gid is None else gid)
            except PermissionError:
                pass
    if mtm is not None:
        ns = _ts_ns(mtm)
        os.utime(target, ns=(ns, ns), follow_symlinks=False)
    xat = blobs.get(b"XAT")
    if xat:
        apply_xattr_blob(target, xat, islink)


def _show(bs):
    return bs.decode("utf-8", "surrogateescape")


def _unimpl(pat):
    print("Error 0xc8055000\nnot implemented yet\ncreating fs object: %s"
          % _show(pat), file=sys.stderr)


def extract(items, root):
    os.makedirs(root, exist_ok=True)
    deferred = []
    hlc_first = {}
    hlinks = []
    failed = 0
    scount = 0
    for entries, blobs in items:
        _, typ = _get(entries, b"TYP")
        _, pat = _get(entries, b"PAT")
        if pat is None or len(pat) == 0:
            continue
        target = safe_join(root, pat)
        if typ == ord("D"):
            os.makedirs(target, exist_ok=True)
            deferred.append((target, entries, blobs))
        elif typ == ord("F"):
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            _, hlc = _get(entries, b"HLC")
            if hlc is not None and hlc in hlc_first:
                if os.path.lexists(target):
                    os.remove(target)
                os.link(hlc_first[hlc], target)
            else:
                with open(target, "wb") as f:
                    f.write(blobs.get(b"DAT", b""))
                if hlc is not None:
                    hlc_first[hlc] = target
            apply_meta(target, entries, blobs, False)
        elif typ == ord("L"):
            _, lnk = _get(entries, b"LNK")
            if lnk is None:
                raise FmtErr("YAA link entry has no LNK field: %r" % pat)
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            if os.path.lexists(target):
                os.remove(target)
            os.symlink(lnk.decode("utf-8", "surrogateescape"), target)
            apply_meta(target, entries, blobs, True)
        elif typ == ord("P"):
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            if os.path.lexists(target):
                os.remove(target)
            os.mkfifo(target, 0o600)
            apply_meta(target, entries, blobs, False)
        elif typ == ord("S"):
            _unimpl(pat)
            failed += 1
            scount += 1
        elif typ == ord("H"):
            _, lnk = _get(entries, b"LNK")
            if lnk is None:
                raise FmtErr("YAA link entry has no LNK field: %r" % pat)
            hlinks.append((target, lnk))
        elif typ == ord("B") or typ == ord("C"):
            _, dev = _get(entries, b"DEV")
            if dev is None:
                raise FmtErr("YAA device entry has no DEV field: %r" % pat)
            _unimpl(pat)
            failed += 1
            scount += 1
        else:
            pass  # unknown TYP: silent skip (oracle parity, measured)
    for target, lnk in hlinks:
        try:
            src = safe_join(root, lnk)
        except FmtErr:
            print("invalid path: %s\ninvalid 'H' LNK" % _show(lnk),
                  file=sys.stderr)
            failed += 1
            continue
        try:
            st = os.lstat(src)
        except FileNotFoundError:
            st = None
        if st is None or not stat.S_ISREG(st.st_mode):
            print("'H' LNK not a regular file: %s" % _show(lnk),
                  file=sys.stderr)
            failed += 1
            continue
        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)
        if os.path.lexists(target):
            os.remove(target)
        try:
            os.link(src, target)
        except OSError as e:
            print("link %r failed: %s" % (target, e), file=sys.stderr)
            failed += 1
            continue
    for target, entries, blobs in reversed(deferred):
        apply_meta(target, entries, blobs, False)
    if scount:
        print("%d entries failed to extract" % scount, file=sys.stderr)
    return 1 if failed else 0


def main(argv):
    if len(argv) != 3:
        print("usage: aad.py IN.aar OUTDIR", file=sys.stderr)
        return 2
    with open(argv[1], "rb") as f:
        data = f.read()
    try:
        inner, metas = parse_chain(data)
        print("blocks:", len(metas), metas[0] if metas else {},
              file=sys.stderr)
        return extract(parse_inner(inner), argv[2])
    except FmtErr as e:
        print("%s" % e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
