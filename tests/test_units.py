#!/usr/bin/env python3
"""tests/test_units.py — synthetic shape tests (no oracle). exit 0/1."""
import os
import stat
import sys
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "src"))
import rawenc

fail = 0


def check(name, cond, extra=""):
    global fail
    print(("PASS" if cond else "FAIL") + " " + name + (" " + str(extra) if extra else ""))
    if not cond:
        fail = 1


# int widths (A-6(b) rule)
check("u8", rawenc.put_int(b"", b"UID", 20) == b"UID1\x14")
check("u16", rawenc.put_int(b"", b"UID", 501) == b"UID2\xf5\x01")
check("u16max", rawenc.put_int(b"", b"UID", 65535) == b"UID2\xff\xff")
check("u32", rawenc.put_int(b"", b"UID", 99999) == b"UID4\x9f\x86\x01\x00")
check("u32bnd", rawenc.put_int(b"", b"GID", 65536) == b"GID4\x00\x00\x01\x00")
check("flg0", rawenc.put_int(b"", b"FLG", 0) == b"FLG1\x00")
check("flghidden", rawenc.put_int(b"", b"FLG", 0x8000) == b"FLG2\x00\x80")

# synthetic block/char entries (A-6(e) shape: DEV'4' after PAT, no DAT/XAT)
rawenc.ROOTB = b"/nonexistent-unit"
mkst = lambda mode, rdev: types.SimpleNamespace(
    st_mode=mode, st_uid=0, st_gid=0, st_flags=0, st_rdev=rdev,
    st_mtime_ns=1000000000_000000000)
st = mkst(stat.S_IFBLK | 0o606, 0x01000001)
e = rawenc.encode_entry(b"blk", st, b"B")
check("blk-typ", b"TYP1B" in e)
check("blk-dev", b"DEV4\x01\x00\x00\x01" in e)
check("blk-nodev-pos", e.index(b"DEV") < e.index(b"UID"))
check("blk-nodat", b"DAT" not in e)
check("blk-noxat", b"XAT" not in e)
check("blk-hdrsize", int.from_bytes(e[4:6], "little") == len(e),
      "hdr=%d len=%d" % (int.from_bytes(e[4:6], "little"), len(e)))
st = mkst(stat.S_IFCHR | 0o606, 0x03000002)
e = rawenc.encode_entry(b"ch", st, b"C")
check("chr-dev", b"DEV4\x02\x00\x00\x03" in e)
check("chr-nodat", b"DAT" not in e)
check("chr-hdrsize", int.from_bytes(e[4:6], "little") == len(e))

check("datA", rawenc.dat_kind(0) == (b"A", b"\x00\x00"))
check("datAmax", rawenc.dat_kind(65535) == (b"A", b"\xff\xff"))
check("datB", rawenc.dat_kind(65536) == (b"B", b"\x00\x00\x01\x00"))
check("datBmax", rawenc.dat_kind(0xFFFFFFFF) == (b"B", b"\xff\xff\xff\xff"))
check("datC", rawenc.dat_kind(0x100000000) == (b"C", b"\x00\x00\x00\x00\x01\x00\x00\x00"))
check("datCbed", rawenc.dat_kind(4831838208) == (b"C", (4831838208).to_bytes(8, "little")))

print("UNITS-GREEN" if fail == 0 else "UNITS-RED")
sys.exit(fail)
