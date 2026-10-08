#!/usr/bin/env python3
"""craft.py — deterministic archive-structure crafts for battery cells.

All crafts preserve lengths except where noted; outer stored blocks
get comp/unc fixups. Raw (AA01) and stored-single-block inputs only.
Usage: craft.py CMD IN OUT ARGS...
  killxat IN OUT IDX...       corrupt 1st XAT record size (items by idx)
  killxatpat IN OUT PAT...    same, items by PAT string
  settyp IN OUT IDX LETTER    set item TYP value byte
  settyppat IN OUT PAT LETTER set TYP value byte by PAT
  setmod IN OUT PAT OCT       set first MOD u16 of item with PAT (octal)
  setmtm IN OUT PAT EPOCH     set MTM u64 LE of item with PAT
  addxat IN OUT PAT NAME VAL  append XAT record (exact-size; extends blob)
  blanktyp IN OUT N           blank Nth b"TYP" occurrence (0-based)
  blankdat IN OUT PAT         blank DAT key of item with PAT
  zeropat IN OUT PAT          empty PAT (removes bytes, fixes hsize)
  setmagic IN OUT IDX HEX4    replace item magic (8 hex chars)
  hsdelta IN OUT IDX D        add signed delta to item hsize
  setsub IN OUT PAT KEY SUB   flip entry subtype byte in place
  setbloblen IN OUT PAT KEY N set blob-len field (width-kept)
  settyprec IN OUT IDX HEX    replace whole TYP record, fix hsize
  append IN OUT HEX           append raw hex bytes at EOF
  setbsize IN OUT HEX16       patch outer bsize u64be (16 hex chars)
  setblk IN OUT BLK HEX32     replace block BLK 16B header (32 hex chars)
  mbcat IN OUT EXTRA          append EXTRA's blocks to IN (same magic+bsize)
"""
import struct
import sys

UW = {0x31: 1, 0x32: 2, 0x34: 4, 0x38: 8}
BW = {0x41: 2, 0x42: 4, 0x43: 8}
HL = {0x46: 4, 0x47: 20, 0x48: 32, 0x49: 48, 0x4A: 64}
TL = {0x53: 8, 0x54: 12}


def entries_of(hdr):
    p, end, out = 6, len(hdr), []
    while p + 4 <= end:
        k, st = bytes(hdr[p:p + 3]), hdr[p + 3]
        if st in UW:
            out.append((k, st, p + 4, UW[st])); p += 4 + UW[st]
        elif st in BW:
            out.append((k, st, p + 4, BW[st])); p += 4 + BW[st]
        elif st == 0x50:
            ln = struct.unpack("<H", hdr[p + 4:p + 6])[0]
            out.append((k, st, p + 4, 2 + ln)); p += 6 + ln
        elif st in HL:
            out.append((k, st, p + 4, HL[st])); p += 4 + HL[st]
        elif st in TL:
            out.append((k, st, p + 4, TL[st])); p += 4 + TL[st]
        elif st == 0x2A:
            out.append((k, st, p + 4, 0)); p += 4
        else:
            raise SystemExit("bad subtype 0x%02x" % st)
    return out


def items_of(raw):
    out, pos = [], 0
    while pos + 6 <= len(raw):
        mg = bytes(raw[pos:pos + 4])
        if mg not in (b"AA01", b"YAA1"):
            break
        hsz = struct.unpack("<H", raw[pos + 4:pos + 6])[0]
        ents = entries_of(raw[pos:pos + hsz])
        blen = 0
        for k, st, voff, w in ents:
            if st in BW:
                blen += int.from_bytes(raw[pos + voff:pos + voff + w],
                                       "little")
        out.append([pos, hsz, ents])
        pos += hsz + blen
    return out


def pat_of(raw, pos, ents):
    for k, st, voff, w in ents:
        if k == b"PAT" and st == 0x50:
            ln = struct.unpack("<H", raw[pos + voff:pos + voff + 2])[0]
            return bytes(raw[pos + voff + 2:pos + voff + 2 + ln])
    return None


def blob_off(raw, pos, ents, key):
    bp = pos + struct.unpack("<H", raw[pos + 4:pos + 6])[0]
    for k, st, voff, w in ents:
        if st in BW:
            ln = int.from_bytes(raw[pos + voff:pos + voff + w], "little")
            if k == key:
                return bp, pos + voff, w, ln
            bp += ln
    return None


def load(path):
    d = bytearray(open(path, "rb").read())
    if d[:4] in (b"AA01", b"YAA1"):
        return d, bytearray(d), False
    assert d[:3] == b"pbz", "outer magic"
    unc = struct.unpack(">I", d[16:20])[0]
    comp = struct.unpack(">I", d[24:28])[0]
    assert unc == comp, "stored only"
    assert 28 + comp == len(d), "single block only"
    return d, bytearray(d[28:28 + comp]), True


def save(d, raw, stored, path):
    if not stored:
        open(path, "wb").write(bytes(raw))
        return
    d[28:28 + (len(d) - 28)] = bytes(raw)
    struct.pack_into(">I", d, 16, len(raw))
    struct.pack_into(">I", d, 24, len(raw))
    open(path, "wb").write(bytes(d))


def blocks_of(d):
    assert bytes(d[:3]) == b"pbz" and len(d) >= 12, "outer magic"
    out, off = [], 12
    while off < len(d):
        assert off + 16 <= len(d), "blk hdr"
        raw, pay = struct.unpack(">QQ", d[off:off + 16])
        assert off + 16 + pay <= len(d), "blk data"
        out.append((off, raw, pay))
        off += 16 + pay
    assert off == len(d), "chain overrun"
    return out


def outer_cmd(cmd, src, dst, args):
    d = bytearray(open(src, "rb").read())
    if cmd == "setbsize":
        v = bytes.fromhex(args[0])
        assert len(v) == 8 and len(d) >= 12 and bytes(d[:3]) == b"pbz"
        d[4:12] = v
    elif cmd == "setblk":
        blks = blocks_of(d)
        off, _, _ = blks[int(args[0])]
        v = bytes.fromhex(args[1])
        assert len(v) == 16
        d[off:off + 16] = v
    elif cmd == "mbcat":
        extra = bytearray(open(args[0], "rb").read())
        assert bytes(extra[:4]) == bytes(d[:4]), "magic match"
        assert bytes(extra[4:12]) == bytes(d[4:12]), "bsize match"
        blocks_of(d)
        blocks_of(extra)
        d += extra[12:]
    else:
        raise SystemExit("unknown outer cmd")
    open(dst, "wb").write(bytes(d))


def main():
    cmd, src, dst, args = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    if cmd in ("setbsize", "setblk", "mbcat"):
        outer_cmd(cmd, src, dst, args)
        return
    d, raw, stored = load(src)
    items = items_of(raw)

    def find_pat(pat):
        for i, (pos, hsz, ents) in enumerate(items):
            if pat_of(raw, pos, ents) == pat:
                return i
        raise SystemExit("no PAT %r" % pat)

    if cmd == "killxat":
        for s in args:
            pos, hsz, ents = items[int(s)]
            r = blob_off(raw, pos, ents, b"XAT")
            assert r, "no XAT"
            bp, _, _, _ = r
            raw[bp:bp + 4] = struct.pack("<I", 0xFFFFFF)
    elif cmd == "killxatpat":
        for s in args:
            i = find_pat(s.encode())
            pos, hsz, ents = items[i]
            r = blob_off(raw, pos, ents, b"XAT")
            assert r, "no XAT"
            bp, _, _, _ = r
            raw[bp:bp + 4] = struct.pack("<I", 0xFFFFFF)
    elif cmd in ("settyp", "settyppat"):
        if cmd == "settyp":
            i, let = int(args[0]), args[1].encode()
        else:
            i, let = find_pat(args[0].encode()), args[1].encode()
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == b"TYP" and st in UW:
                raw[pos + voff] = let[0]
                break
        else:
            raise SystemExit("no TYP")
    elif cmd == "setmod":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == b"MOD" and st in UW:
                raw[pos + voff:pos + voff + w] = int(args[1], 8).to_bytes(
                    w, "little")
                break
        else:
            raise SystemExit("no MOD")
    elif cmd == "setmtm":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == b"MTM" and st in TL:
                raw[pos + voff:pos + voff + 8] = int(args[1]).to_bytes(
                    8, "little")
                break
        else:
            raise SystemExit("no MTM")
    elif cmd == "addxat":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        name, val = args[1].encode(), args[2].encode()
        rec = struct.pack("<I", 4 + len(name) + 1 + len(val)) + name + \
            b"\x00" + val
        r = blob_off(raw, pos, ents, b"XAT")
        assert r, "no XAT"
        bp, loff, w, ln = r
        raw[bp + ln:bp + ln] = rec
        raw[loff:loff + w] = (ln + len(rec)).to_bytes(w, "little")
    elif cmd == "blanktyp":
        n, j, found = int(args[0]), 0, -1
        for _ in range(n + 1):
            found = bytes(raw).find(b"TYP", j)
            assert found >= 0
            j = found + 1
        raw[found:found + 3] = b"XXX"
    elif cmd == "blankdat":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == b"DAT":
                raw[pos + voff - 4:pos + voff - 1] = b"XXX"
                break
        else:
            raise SystemExit("no DAT")
    elif cmd == "zeropat":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == b"PAT" and st == 0x50:
                ln = struct.unpack("<H", raw[pos + voff:pos + voff + 2])[0]
                del raw[pos + voff + 2:pos + voff + 2 + ln]
                struct.pack_into("<H", raw, pos + 4, hsz - ln)
                raw[pos + voff:pos + voff + 2] = struct.pack("<H", 0)
                break
        else:
            raise SystemExit("no PAT")
    elif cmd == "setmagic":
        pos, hsz, ents = items[int(args[0])]
        raw[pos:pos + 4] = bytes.fromhex(args[1])
    elif cmd == "hsdelta":
        pos, hsz, ents = items[int(args[0])]
        raw[pos + 4:pos + 6] = struct.pack("<H", hsz + int(args[1]))
    elif cmd == "setsub":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        p, end = pos + 6, pos + hsz
        while p + 4 <= end:
            if bytes(raw[p:p + 3]) == args[1].encode():
                raw[p + 3] = args[2].encode()[0]
                break
            p += 4
            st = raw[p - 1]
            if st in UW:
                p += UW[st]
            elif st in BW:
                p += BW[st]
            elif st in HL:
                p += HL[st]
            elif st in TL:
                p += TL[st]
            elif st == 0x50:
                p += 2 + struct.unpack("<H", raw[p:p + 2])[0]
        else:
            raise SystemExit("no key")
    elif cmd == "setbloblen":
        i = find_pat(args[0].encode())
        pos, hsz, ents = items[i]
        for k, st, voff, w in ents:
            if k == args[1].encode() and st in BW:
                raw[pos + voff:pos + voff + w] = int(args[2]).to_bytes(
                    w, "little")
                break
        else:
            raise SystemExit("no blob key")
    elif cmd == "settyprec":
        i = int(args[0])
        pos, hsz, ents = items[i]
        rec = bytes.fromhex(args[1])
        p, end = pos + 6, pos + hsz
        while p + 4 <= end:
            if bytes(raw[p:p + 3]) == b"TYP":
                q = p + 4
                st = raw[p + 3]
                if st in UW:
                    q += UW[st]
                elif st in BW:
                    q += BW[st]
                elif st in HL:
                    q += HL[st]
                elif st in TL:
                    q += TL[st]
                elif st == 0x50:
                    q += 2 + struct.unpack("<H", raw[q:q + 2])[0]
                raw[p:q] = rec
                struct.pack_into("<H", raw, pos + 4,
                                 hsz + (len(rec) - (q - p)))
                break
            p += 4
            st = raw[p - 1]
            if st in UW:
                p += UW[st]
            elif st in BW:
                p += BW[st]
            elif st in HL:
                p += HL[st]
            elif st in TL:
                p += TL[st]
            elif st == 0x50:
                p += 2 + struct.unpack("<H", raw[p:p + 2])[0]
        else:
            raise SystemExit("no TYP")
    elif cmd == "append":
        raw += bytes.fromhex(args[0])
    else:
        raise SystemExit("unknown cmd")
    save(d, raw, stored, dst)


if __name__ == "__main__":
    main()
