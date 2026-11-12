#!/usr/bin/env python3
"""lz4 (pbz4) outer wrapper. Derived black-box from /usr/bin/aa I/O only.

Model V0+K+A33+gates+blocks: Knuth-12 buckets (2048x5 distinct-keyed LRU,
shift H12>>1) continuous within each block, RESET at each block start
(block-relative chunk index: no rescan on block-first chunks); match
interior inserts mstart, mstart+1 (P1 iff gap%5!=4), mstart+8 on
rescan-path matches only, end-2/end-1 iff next has literals
(self-consistent: skipped if they'd flip the next lookup to a hit);
greedy one-pass (first hit wins, extend to max); window 65535; last-127 of
each non-final 64KB chunk never inserted (K=127 exact, clean reads);
two match gates: anchor-rem>=129 (no search once anchor leaves <129B)
AND gpos-rem>=126.
Known residual (rare random-pressure occ-choice, e.g. rzc 7B:
mtime-sensitive bucket eviction; needs hash/eviction refit).
Framing: 64KB chunks bv41+u32le unc+u32le len+block / bv4-+u32+raw stored /
terminal bv4$; outer pbz4 4MB blocks + 16B gaps; store rules razor-verified.
"""
import os
import struct
import sys

K = 2654435761
CHUNK = 65536
NEVER_K = 127


def H(b4):
    v = int.from_bytes(bytes(b4), "little")
    return ((v * K) & 0xFFFFFFFF) >> 20


def emit_seq(out, litbytes, ml, off):
    tok = (min(len(litbytes), 15) << 4) | (min(ml - 4, 15) if ml else 0)
    out.append(tok)
    if len(litbytes) >= 15:
        x = len(litbytes) - 15
        while x >= 255:
            out.append(255)
            x -= 255
        out.append(x)
    out += litbytes
    if ml:
        out.append(off & 0xFF)
        out.append((off >> 8) & 0xFF)
        if ml - 4 >= 15:
            x = ml - 4 - 15
            while x >= 255:
                out.append(255)
                x -= 255
            out.append(x)


def lz4_encode(inner, buckets=2048, slots=5, hashmode="shift",
              blocksize=4 * 1024 * 1024):
    """Full-inner V0+K+A33 encode -> list of (unc, block) per 64KB chunk.
    Table (A-33): buckets x slots distinct-keyed LRU (re-insert refreshes,
    no double-count); lookup validates 4B + window. hashmode: shift
    (H12>>1), mod (H12%B), native11 (((v*K)>>(32-11))).
    Per-block independent streams (mb): table resets at each block
    start; rescan/finality are block-relative (block-first chunk
    behaves like ci=0: no rescan)."""
    chunks = []
    nblk = (len(inner) + blocksize - 1) // blocksize or 1

    def BKT(b4):
        h = H(b4)
        if hashmode == "shift":
            return h >> 1
        if hashmode == "mod":
            return h % buckets
        v = int.from_bytes(bytes(b4), "little")
        return ((v * K) & 0xFFFFFFFF) >> 21

    def lookup(gpos):
        bkt = table.get(BKT(inner[gpos:gpos + 4]))
        if not bkt:
            return None
        g = inner[gpos:gpos + 4]
        for (gram, occ) in bkt:
            if gram == g and 0 < gpos - occ <= 65535:
                return occ
        return None

    def tput(gpos, gram):
        b = BKT(gram)
        bkt = table.get(b)
        if bkt is None:
            table[b] = [(gram, gpos)]
            return
        for i, (gr, oc) in enumerate(bkt):
            if gr == gram:
                del bkt[i]
                bkt.append((gram, gpos))
                return
        bkt.append((gram, gpos))
        if len(bkt) > slots:
            del bkt[0]

    for bi in range(nblk):
        table = {}
        bbase = bi * blocksize
        blen = min(blocksize, len(inner) - bbase)
        nchb = (blen + CHUNK - 1) // CHUNK or 1
        for bci in range(nchb):
            base = bbase + bci * CHUNK
            # block-capped: the last chunk of a non-final block must end
            # at the block end (blocksize need not be a 64K multiple).
            # len(inner)-base alone overruns into the next block.
            n = min(CHUNK, bbase + blen - base)
            final = bci == nchb - 1
            ilim = None if final else base + CHUNK - NEVER_K
            # finding bounds (two gates, both required):
            # A (search gate on ANCHOR): anchor+4 <= FBOUND (n-125),
            #   no match once anchor leaves <129B (z92/z93 flip, p98
            #   matches at gpos-rem126 with anchor-rem134).
            # B (match gate on GPOS): gpos+4 <= BBOUND (n-122, rem>=126,
            #   prior universal-126): s1 ABC-repeat refused at rem44.
            FBOUND = base + n - 125
            BBOUND = base + n - 122
            out = bytearray()
            anchor = 0
            ip = 0

            def put(gpos):
                if ilim is not None and gpos >= ilim:
                    return
                if gpos + 4 > len(inner):
                    return
                tput(gpos, bytes(inner[gpos:gpos + 4]))

            while ip < n:
                gpos = base + ip
                if ip + 12 >= n:
                    break
                occ = None
                rseed = False
                if gpos >= 16 and gpos + 4 <= BBOUND and \
                        base + anchor + 4 <= FBOUND:
                    occ = lookup(gpos)
                    # rescan-path seed flag: main-table miss at
                    # chunk start (before rescan below).
                    rseed = occ is None and ip == 0 and bci >= 1
                    # chunk-start tail rescan (miss-only): at ip==0 of
                    # chunk bci>=1 with table miss, scan prev tail
                    # [gpos-8,gpos-5] nearest-first for 4B match.
                    # bed-derived (bis c2-pos0 needs c1-end-8; +1/-0).
                    # block-relative: no rescan at block starts (mb).
                    if rseed:
                        _g = bytes(inner[gpos:gpos + 4])
                        for _o in range(gpos - 4, gpos - 9, -1):
                            if _o + 4 <= gpos and \
                                    bytes(inner[_o:_o + 4]) == _g:
                                occ = _o
                                break
                LIM = base + n - 121
                if occ is not None:
                    # u64 extension: 1st u64 unconditional; rest iff
                    # dst+8 <= LIM (C=121 proven 4836/4836 single).
                    # Mismatch refines within u64; bound-fail never refines.
                    ml = 4
                    dst = gpos + 4
                    off = gpos - occ
                    first = True
                    while True:
                        if not first and dst + 8 > LIM:
                            break
                        if dst + 8 > base + n:  # safety: MFLIMIT excludes
                            while gpos + ml < base + n and \
                                    occ + ml < len(inner) and \
                                    inner[gpos + ml] == inner[occ + ml]:
                                ml += 1
                            break
                        if inner[dst:dst + 8] == \
                                inner[dst - off:dst - off + 8]:
                            ml += 8
                            dst += 8
                            first = False
                            continue
                        end = dst + 8
                        while gpos + ml < end and gpos + ml < base + n and \
                                occ + ml < len(inner) and \
                                inner[gpos + ml] == inner[occ + ml]:
                            ml += 1
                        break
                    emit_seq(out, inner[base + anchor:gpos], ml, off)
                    mend = gpos + ml
                    put(gpos)
                    if gpos + 1 < mend:
                        # P1 skipped iff gap%5==4 (gap = literals since
                        # last match). bed-derived: 53/53 stale-critical
                        # gaps ==4mod5, 448/448 bearing-criticals !=4mod5;
                        # battery +4/-0, all stale first-divs resolve.
                        # mechanism OPEN (Q-31).
                        if (gpos - (base + anchor)) % 5 != 4:
                            put(gpos + 1)
                    # P8 (rescan-path seed): chunk-start table-miss
                    # that emits a match also inserts mstart+8
                    # (p8_262144 chunk3 occ=131080). interior-bounded.
                    if rseed and gpos + 8 < mend:
                        put(gpos + 8)
                    # ends iff next has literals (self-consistent lookahead)
                    if mend - base < n - 12:
                        if lookup(mend) is None:
                            e2, e1 = mend - 2, mend - 1
                            # would ends-insertion flip mend to a hit?
                            s = BKT(inner[mend:mend + 4])
                            flip = False
                            for e in (e2, e1):
                                if e > gpos + 1 and BKT(inner[e:e + 4]) == s and \
                                        inner[e:e + 4] == inner[mend:mend + 4]:
                                    flip = True
                            if not flip:
                                if e2 > gpos + 1:
                                    put(e2)
                                if e1 > gpos + 1:
                                    put(e1)
                    anchor = ip + ml
                    ip = anchor
                else:
                    if gpos != 0:
                        put(gpos)
                    ip += 1
            emit_seq(out, inner[base + anchor:base + n], 0, 0)
            chunks.append((n, bytes(out)))
    return chunks


def wrap_pbz4(inner, blocksize=4 * 1024 * 1024, chunks=None):
    """pbz4 outer. Split inner by blocksize; per block frame (concat
    64KB-chunk bv41/bv4- + bv4$) iff c0*16 <= u*15 else raw store.
    Per chunk: bv41 iff blk < unc else bv4-. chunks: prebuilt [(n,blk)]
    (else lz4_encode(inner, blocksize=blocksize))."""
    if chunks is None:
        chunks = lz4_encode(inner, blocksize=blocksize)
    # regroup 64KB chunks into bs blocks (last block = rest)
    blocks = []
    cur = []
    curu = 0
    for (n, blk) in chunks:
        cur.append((n, blk))
        curu += n
        if curu >= blocksize:
            blocks.append(cur)
            cur = []
            curu = 0
    if cur:
        blocks.append(cur)
    if not blocks:
        blocks = [[(0, b"")]]
    # per block: framed payload (chunk frames + bv4$) vs raw store
    out = []
    base = 0
    framed_blocks = []
    for chs in blocks:
        u = sum(n for n, _ in chs)
        pay = bytearray()
        b2 = base
        for (n, blk) in chs:
            if len(blk) < n:
                pay += b"bv41" + struct.pack("<II", n, len(blk)) + blk
            else:
                pay += b"bv4-" + struct.pack("<I", n) + inner[b2:b2 + n]
            b2 += n
        pay += b"bv4$"
        if len(pay) * 16 <= u * 15:
            framed_blocks.append((u, bytes(pay)))
        else:
            framed_blocks.append((u, bytes(inner[base:base + u])))
        base += u
    out.append(struct.pack(">4sIIIIII", b"pbz4", 0, blocksize, 0,
                           framed_blocks[0][0], 0, len(framed_blocks[0][1])))
    for i, (u, payload) in enumerate(framed_blocks):
        out.append(payload)
        if i + 1 < len(framed_blocks):
            nu, npay = framed_blocks[i + 1][0], len(framed_blocks[i + 1][1])
            out.append(struct.pack(">IIII", 0, nu, 0, npay))
    return b"".join(out)


if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, _HERE)
    from rawenc import build_inner
    inner = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(wrap_pbz4(inner))
