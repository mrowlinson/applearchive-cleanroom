#!/usr/bin/env python3
"""aad.py — decode prototype v1 (REFERENCE ONLY, not the deliverable).

Covers: outer 28B container (PRE-001) + STORED/raw + inner TLV + extract.
Codec payloads: zlib only in v1 (stdlib). Validated vs oracle, never vs OSS.
"""
import os
import struct
import sys
import zlib

INNER_MAGICS = (b"AA01", b"YAA1")
UINT_W = {ord("1"): 1, ord("2"): 2, ord("4"): 4, ord("8"): 8}
BLOB_W = {ord("A"): 2, ord("B"): 4, ord("C"): 8}
HASH_L = {ord("F"): 4, ord("G"): 20, ord("H"): 32, ord("I"): 48, ord("J"): 64}
TS_L = {ord("S"): 8, ord("T"): 12}


class FmtErr(Exception):
    pass


def parse_outer(data):
    """-> (inner_bytes, meta). meta: alg, stored, unc, comp."""
    if bytes(data[:4]) in INNER_MAGICS:
        return bytes(data), {"alg": "raw", "stored": True,
                             "unc": len(data), "comp": len(data)}
    if bytes(data[:3]) != b"pbz" or len(data) < 28:
        raise FmtErr("bad outer magic")
    magic = bytes(data[:4])
    z4, bsize, z12, unc, z20, comp = struct.unpack(">4sI4sI4sI", data[4:28])
    if z4 != b"\0\0\0\0" or z12 != b"\0\0\0\0" or z20 != b"\0\0\0\0":
        raise FmtErr("outer zero fields nonzero")
    if len(data) != 28 + comp:
        raise FmtErr("outer size mismatch %d != 28+%d" % (len(data), comp))
    payload = bytes(data[28:28 + comp])
    meta = {"alg": magic.decode("ascii"), "stored": comp == unc,
            "unc": unc, "comp": comp, "bsize": bsize}
    if comp == unc:
        return payload, meta
    if magic == b"pbzz":
        raw = zlib.decompress(payload)
        if len(raw) != unc:
            raise FmtErr("zlib size %d != %d" % (len(raw), unc))
        return raw, meta
    raise FmtErr("codec %s not in v1" % magic.decode("ascii"))


def parse_header(data, pos):
    """-> (entries, endpos). entries: list of (key, subtype, value)."""
    if bytes(data[pos:pos + 4]) not in INNER_MAGICS:
        raise FmtErr("bad inner magic at %d" % pos)
    (hsize,) = struct.unpack_from("<H", data, pos + 4)
    end = pos + hsize
    p = pos + 6
    entries = []
    while p < end:
        key = bytes(data[p:p + 3])
        st = data[p + 3]
        p += 4
        if st == ord("*"):
            val = None
        elif st in UINT_W:
            w = UINT_W[st]
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in BLOB_W:
            w = BLOB_W[st]
            val = int.from_bytes(data[p:p + w], "little")
            p += w
        elif st in HASH_L:
            val = bytes(data[p:p + HASH_L[st]])
            p += HASH_L[st]
        elif st in TS_L:
            val = bytes(data[p:p + TS_L[st]])
            p += TS_L[st]
        elif st == ord("P"):
            (ln,) = struct.unpack_from("<H", data, p)
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


def extract(items, root):
    os.makedirs(root, exist_ok=True)
    for entries, blobs in items:
        _, typ = _get(entries, b"TYP")
        _, pat = _get(entries, b"PAT")
        if pat is None or len(pat) == 0:
            continue
        target = safe_join(root, pat)
        if typ == ord("D"):
            os.makedirs(target, exist_ok=True)
        elif typ == ord("F"):
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(target, "wb") as f:
                f.write(blobs.get(b"DAT", b""))
        elif typ == ord("L"):
            _, lnk = _get(entries, b"LNK")
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            if os.path.lexists(target):
                os.remove(target)
            os.symlink(lnk.decode("utf-8", "surrogateescape"), target)
        else:
            raise FmtErr("entry type %r" % typ)


def main(argv):
    if len(argv) != 3:
        print("usage: aad.py IN.aar OUTDIR", file=sys.stderr)
        return 2
    with open(argv[1], "rb") as f:
        data = f.read()
    inner, meta = parse_outer(data)
    print("meta:", meta, file=sys.stderr)
    extract(parse_inner(inner), argv[2])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
