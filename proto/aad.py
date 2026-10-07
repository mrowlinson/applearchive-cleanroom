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


# inner parse failure classes (oracle wrapper per class; prefix kept)
(PF_OK, PF_TAIL, PF_BADMAGIC, PF_HDRCUT, PF_ENDMISMATCH,
 PF_VALUEOVERRUN, PF_BADSUBTYPE, PF_BLOBOVERRUN) = range(8)


class _PFail(Exception):
    def __init__(self, cls, sub=0):
        super().__init__(cls, sub)
        self.cls = cls
        self.sub = sub


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
        try:
            raw = zlib.decompress(bytes(payload))
        except zlib.error:
            try:
                # adler-broken streams decode (case188: oracle exit 0)
                raw = zlib.decompress(bytes(payload[2:]), -15)
            except zlib.error:
                raise FmtErr("codec pbzz decode")
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
        raise _PFail(PF_TAIL)
    if bytes(data[pos:pos + 4]) not in INNER_MAGICS:
        raise _PFail(PF_BADMAGIC)
    (hsize,) = struct.unpack_from("<H", data, pos + 4)
    end = pos + hsize
    if end > len(data) or hsize < 6:
        raise _PFail(PF_VALUEOVERRUN)
    p = pos + 6
    entries = []
    while p < end:
        if p + 4 > end:
            raise _PFail(PF_HDRCUT)
        key = bytes(data[p:p + 3])
        st = data[p + 3]
        p += 4
        if st == ord("*"):
            val = None
        elif st in UINT_W:
            w = UINT_W[st]
            if p + w > end:
                raise _PFail(PF_VALUEOVERRUN)
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in BLOB_W:
            w = BLOB_W[st]
            if p + w > end:
                raise _PFail(PF_VALUEOVERRUN)
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in HASH_L:
            if p + HASH_L[st] > end:
                raise _PFail(PF_VALUEOVERRUN)
            val = bytes(data[p:p + HASH_L[st]])
            p += HASH_L[st]
        elif st in TS_L:
            if p + TS_L[st] > end:
                raise _PFail(PF_VALUEOVERRUN)
            val = bytes(data[p:p + TS_L[st]])
            p += TS_L[st]
        elif st == ord("P"):
            if p + 2 > end:
                raise _PFail(PF_VALUEOVERRUN)
            (ln,) = struct.unpack_from("<H", data, p)
            if p + 2 + ln > end:
                raise _PFail(PF_VALUEOVERRUN)
            val = bytes(data[p + 2:p + 2 + ln])
            p += 2 + ln
        else:
            raise _PFail(PF_BADSUBTYPE, st)
        entries.append((key, st, val))
    if p != end:
        raise _PFail(PF_ENDMISMATCH)
    return entries, end


def parse_inner(data):
    """-> (items, fcls, fsub). Prefix kept on failure."""
    items, pos, fcls, fsub = [], 0, PF_OK, 0
    while pos < len(data):
        try:
            entries, end = parse_header(data, pos)
        except _PFail as e:
            fcls, fsub = e.cls, e.sub
            break
        blobs, bp = {}, end
        bad = False
        for key, st, val in entries:
            if st in BLOB_W:
                if bp + val > len(data):
                    fcls, bad = PF_BLOBOVERRUN, True
                    break
                blobs[key] = bytes(data[bp:bp + val])
                bp += val
        if bad:
            break
        items.append((entries, blobs))
        pos = bp
    return items, fcls, fsub


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
    if pos != len(blob):
        raise FmtErr("xattr trailing bytes")


def apply_xattr_only(target, entries, blobs, islink):
    xat = blobs.get(b"XAT")
    if xat:
        apply_xattr_blob(target, xat, islink)


def apply_rest(target, entries, blobs, islink):
    _, mod = _get(entries, b"MOD")
    _, uid = _get(entries, b"UID")
    _, gid = _get(entries, b"GID")
    _, mtm = _get(entries, b"MTM")
    if not islink:
        if mod is not None:
            try:
                os.chmod(target, mod & 0o7777)
            except OSError:
                pass
        if uid is not None or gid is not None:
            try:
                os.chown(target, -1 if uid is None else uid,
                         -1 if gid is None else gid)
            except OSError:
                pass
    if mtm is not None:
        try:
            ns = _ts_ns(mtm)
            os.utime(target, ns=(ns, ns), follow_symlinks=False)
        except OSError:
            pass


def _show(bs):
    return bs.decode("utf-8", "surrogateescape")


def print_hdr(done, code):
    if not done[0]:
        print("Error 0x%08x" % code, file=sys.stderr)
        done[0] = True


def eisdir_err(done, path):
    s = path.rstrip("/") or "/"
    b = os.path.basename(s) or s
    a = s if os.path.isabs(s) else os.path.join(os.getcwd(), s)
    print_hdr(done, 0xc305ac15)
    print("Is a directory: %s\nIs a directory: %s\nopening output file: %s"
          % (b, a, a), file=sys.stderr)


def extract(items, root, fcls=0, fsub=0):
    os.makedirs(root, exist_ok=True)
    files = []
    dirs = []
    scols = []
    fsts = []
    eis = []
    hlc_first = {}
    hlinks = []
    failed = 0
    scount = 0
    hdr = [False]
    dirfail = False
    aborted = False

    def abort(msg):
        if msg:
            print(msg, file=sys.stderr)
        return True

    # phase 1: create everything, forward. aborts stop creation only.
    for entries, blobs in items:
        if aborted:
            break
        tst, typ = _get(entries, b"TYP")
        pst, pat = _get(entries, b"PAT")
        if typ is None:
            print("Extraction failed\nextract failedError 0xbd03ac00\n"
                  "Invalid entry: no TYP field\n"
                  "archive stream read error (header)\nstream cancelled",
                  file=sys.stderr)
            failed += 1
            hdr[0] = True
            aborted = True
            break
        if tst not in UINT_W:
            tn = {ord("P"): 2, ord("S"): 4, ord("T"): 4, ord("*"): 0,
                  ord("F"): 3, ord("G"): 3, ord("H"): 3, ord("I"): 3,
                  ord("J"): 3}.get(tst)
            if tn is not None:
                print("Extraction failed\nextract failedError 0xe509b400\n"
                      "invalid type %d, expected UINT\n"
                      "Invalid entry: no TYP field\n"
                      "archive stream read error (header)\nstream cancelled"
                      % tn, file=sys.stderr)
            else:
                print("aad: TYP non-uint subtype 0x%02x" % tst,
                      file=sys.stderr)
            failed += 1
            hdr[0] = True
            aborted = True
            break
        if pat is None or pst != ord("P"):
            continue
        if len(pat) == 0:
            if typ == ord("D"):
                dirs.append((root, entries, blobs))
            elif typ == ord("F"):
                eis.append(root)
                failed += 1
                scount += 1
            continue
        try:
            target = safe_join(root, pat)
        except FmtErr:
            aborted = abort("aad: bad path")
            failed += 1
            hdr[0] = True
            break
        if typ == ord("D"):
            try:
                os.makedirs(target, exist_ok=True)
            except OSError:
                aborted = abort("aad: mkdir %s" % target)
                failed += 1
                hdr[0] = True
                break
            dirs.append((target, entries, blobs))
        elif typ == ord("F"):
            parent = os.path.dirname(target)
            if parent:
                try:
                    os.makedirs(parent, exist_ok=True)
                except OSError:
                    aborted = abort("aad: mkdir %s" % target)
                    failed += 1
                    hdr[0] = True
                    break
            _, hlc = _get(entries, b"HLC")
            if hlc is not None and hlc in hlc_first:
                try:
                    if os.path.lexists(target):
                        os.remove(target)
                    os.link(hlc_first[hlc], target)
                except OSError:
                    aborted = abort("aad: link %s" % target)
                    failed += 1
                    hdr[0] = True
                    break
            elif b"DAT" not in blobs:
                fsts.append(entries)
                failed += 1
                continue
            else:
                try:
                    with open(target, "wb") as f:
                        f.write(blobs[b"DAT"])
                except IsADirectoryError:
                    eis.append(target)
                    failed += 1
                    scount += 1
                    continue
                except OSError:
                    aborted = abort("aad: open %s" % target)
                    failed += 1
                    hdr[0] = True
                    break
                if hlc is not None:
                    hlc_first[hlc] = target
            files.append((target, entries, blobs, False))
        elif typ == ord("L"):
            _, lnk = _get(entries, b"LNK")
            if lnk is None:
                aborted = abort("YAA link entry has no LNK field: %s"
                                % _show(pat))
                failed += 1
                hdr[0] = True
                break
            parent = os.path.dirname(target)
            if parent:
                try:
                    os.makedirs(parent, exist_ok=True)
                except OSError:
                    aborted = abort("aad: mkdir %s" % target)
                    failed += 1
                    hdr[0] = True
                    break
            try:
                if os.path.lexists(target):
                    os.remove(target)
                os.symlink(lnk.decode("utf-8", "surrogateescape"), target)
            except OSError:
                aborted = abort("aad: symlink %s" % target)
                failed += 1
                hdr[0] = True
                break
            files.append((target, entries, blobs, True))
        elif typ == ord("P"):
            parent = os.path.dirname(target)
            if parent:
                try:
                    os.makedirs(parent, exist_ok=True)
                except OSError:
                    aborted = abort("aad: mkdir %s" % target)
                    failed += 1
                    hdr[0] = True
                    break
            try:
                if os.path.lexists(target):
                    os.remove(target)
                os.mkfifo(target, 0o600)
            except OSError:
                aborted = abort("aad: mkfifo %s" % target)
                failed += 1
                hdr[0] = True
                break
            files.append((target, entries, blobs, False))
        elif typ == ord("S"):
            scols.append(entries)
            failed += 1
            scount += 1
        elif typ == ord("H"):
            _, lnk = _get(entries, b"LNK")
            if lnk is None:
                aborted = abort("YAA link entry has no LNK field: %s"
                                % _show(pat))
                failed += 1
                hdr[0] = True
                break
            hlinks.append((target, lnk))
        elif typ == ord("B") or typ == ord("C"):
            _, dev = _get(entries, b"DEV")
            if dev is None:
                aborted = abort("YAA device entry has no DEV field: %s"
                                % _show(pat))
                failed += 1
                hdr[0] = True
                break
            scols.append(entries)
            failed += 1
            scount += 1
        else:
            pass  # unknown TYP: silent skip (oracle parity, measured)
    # parse-fail wrapper (after phase 1, before meta; not on abort)
    if fcls and not aborted:
        failed += 1
        hdr[0] = True
        if fcls == PF_TAIL:
            print("Extraction failed\nextract failedError 0xbd011800\n"
                  "No more data\nread error\ntruncated stream\n"
                  "archive stream read error (header)\nstream cancelled",
                  file=sys.stderr)
        elif fcls == PF_BADMAGIC:
            print("Extraction failed\nextract failedError 0xe501e800\n"
                  "invalid header magic\ncorrupted archive header\n"
                  "parsing entry header\n"
                  "archive stream read error (header)\nstream cancelled",
                  file=sys.stderr)
        elif fcls in (PF_HDRCUT, PF_ENDMISMATCH):
            print("Extraction failed\nextract failedError 0xe5022800\n"
                  "truncated header\ncorrupted archive header\n"
                  "parsing entry header\n"
                  "archive stream read error (header)\nstream cancelled",
                  file=sys.stderr)
        elif fcls == PF_VALUEOVERRUN:
            print("Extraction failed\nextract failedError 0xe502a400\n"
                  "truncated header\ncorrupted archive header\n"
                  "parsing entry header\n"
                  "archive stream read error (header)\nstream cancelled",
                  file=sys.stderr)
        elif fcls == PF_BADSUBTYPE:
            print("Extraction failed\nextract failedError 0xe5029c00\n"
                  "invalid field subtype: %d\ncorrupted archive header\n"
                  "parsing entry header\n"
                  "archive stream read error (header)\nstream cancelled"
                  % fsub, file=sys.stderr)
        elif fcls == PF_BLOBOVERRUN:
            print("Extraction failed\nextract failedError 0xbd011800\n"
                  "No more data\nread error\n"
                  "archive stream read error (blob)\nstream cancelled",
                  file=sys.stderr)
            scount += 1
    # phase 2: files meta, strict reverse
    for target, entries, blobs, islink in reversed(files):
        try:
            apply_xattr_only(target, entries, blobs, islink)
        except FmtErr:
            _, pat = _get(entries, b"PAT")
            print_hdr(hdr, 0xe8012000)
            print("invalid XAT blob\ninvalid XAT blob", file=sys.stderr)
            print("applyEntryAttributes failed: %s" % _show(pat),
                  file=sys.stderr)
            failed += 1
            scount += 1
        else:
            apply_rest(target, entries, blobs, islink)
    # S-flush, forward
    for entries in scols:
        _, pat = _get(entries, b"PAT")
        print_hdr(hdr, 0xc8055000)
        print("not implemented yet\ncreating fs object: %s" % _show(pat),
              file=sys.stderr)
    # EISDIR flush, forward
    for path in eis:
        eisdir_err(hdr, path)
    # F-no-DAT flush, forward
    for entries in fsts:
        _, pat = _get(entries, b"PAT")
        print_hdr(hdr, 0xc8039000)
        print("invalid entry final state 0: %s" % _show(pat),
              file=sys.stderr)
    # H pass (runs even on abort; trailer iff failure)
    hfailed = False
    for target, lnk in hlinks:
        try:
            src = safe_join(root, lnk)
        except FmtErr:
            print_hdr(hdr, 0xc8104800)
            print("invalid path: %s\ninvalid 'H' LNK" % _show(lnk),
                  file=sys.stderr)
            failed += 1
            hfailed = True
            continue
        try:
            st = os.lstat(src)
        except FileNotFoundError:
            st = None
        if st is None or not stat.S_ISREG(st.st_mode):
            print_hdr(hdr, 0xc8104800)
            print("'H' LNK not a regular file: %s" % _show(lnk),
                  file=sys.stderr)
            failed += 1
            hfailed = True
            continue
        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)
        if os.path.lexists(target):
            os.remove(target)
        try:
            os.link(src, target)
        except OSError:
            print_hdr(hdr, 0xc8104800)
            print("aad: link %s" % target, file=sys.stderr)
            failed += 1
            hfailed = True
            continue
    if hfailed:
        print("process hlinks", file=sys.stderr)
    # phase 3: dirs meta, reverse (children-first); root=outdir in place
    for target, entries, blobs in reversed(dirs):
        try:
            apply_xattr_only(target, entries, blobs, False)
        except FmtErr:
            print_hdr(hdr, 0xe8012000)
            print("invalid XAT blob\ninvalid XAT blob", file=sys.stderr)
            print("applyEntryAttributes failed", file=sys.stderr)
            failed += 1
            dirfail = True
        else:
            apply_rest(target, entries, blobs, False)
    if dirfail:
        print("process dirs", file=sys.stderr)
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
        items, fcls, fsub = parse_inner(inner)
        return extract(items, argv[2], fcls, fsub)
    except FmtErr as e:
        print("%s" % e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
