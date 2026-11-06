#!/usr/bin/env python3
"""lzbitmap literal-class ZBM stream encoder (prototype).
Black-box derived from /usr/bin/aa -a lzbitmap I/O only. Pure Python,
no dependencies.

Covers LITERAL-ONLY streams: every 32KB chunk is incompressible (oracle
emits 00 + raw, no match section). Verified byte-identical vs oracle on
random (match-free) inputs 0..100000 bytes, single + multi chunk.

MATCH CLASS REFUSED (not replicated): the oracle's match grammar is
globally planned and multi-modal (34/44/f3 match descriptors with a
bitmap prefix + fc epilogue; a dimer-codebook mode exploiting dense
2-gram repeats; a sparse order-0 mode for symbol-skewed inputs; a
cross-section dictionary with a 64KB match window). Same local match
encodes differently by global context, so zbm_encode_literal() would
emit valid-but-different ZBM there (silent divergence). Instead both
entry points below RAISE LzBitmapMatchFound on every input outside the
proven-parity class (exact refusal predicate _refuse_reason()); the
caller (encode.py) converts it to SystemExit, mirroring lzraven's
LzRavenUnclosed pattern. The predicate is conservative: inputs inside
the class are oracle-literal (battery-proven, zero silent divergence);
inputs outside are refused honestly (never mis-encoded).

Grammar (bedded, all integers little-endian):
  stream = magic(5a424d) ver(09) u16 X 00 u16 hunc body [trailer]
  trailer = 06 00 00 00 00 00, present iff total unc > 0
  X = len(first-section excluding trailer) + 5
  single (unc <= 32768): hunc = unc; first-section = body
    empty: body = 00
    nonempty: body = 00 + raw
  chunked (unc > 32768): hunc = 32768; section0 = 00 + raw[0:32768]
    section[i>=1] = u16(6+r) 00 u16(r) 00 + raw, r = chunk length
    (X2 = section length excluding final trailer)

Outer pbzb framing lives in wrap_pbzb() below (same 12B prefix +
16B chain + 15/16 store rule as the other codecs, bedded NOTE-008).
"""
import os
import struct
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

CHUNK = 32768

# --- refusal predicate (exact boundary, all constants black-box bedded) ---
# Oracle bed findings (libcompression 0x702 stream probes, single variable
# swept at a time; see lane commit message for the full table):
#  WIN      = 65535  max match offset: repeat at distance 65000 taken,
#                     at 65536 ignored (sections share a dictionary).
#  G1 (16/20/32)     k-gram count in window reaches 16 (4-grams), 20
#                     (3-grams), 32 (2-grams): a fire is then economically
#                     possible (desc savings exceed the ~35B overhead in
#                     every cost scenario), so refuse. Single-file TLV
#                     structure stays below (9/15/25); random far below.
#  G2 M=4/C=2/S>=32 relaxed-DP LZ savings over window; sound for pure
#                     len>=4 wins (every descriptor costs >= 2B, overhead
#                     >= 0, ties go literal, so model_sav > 35 > 32).
#                     Covers low-count long matches (cross-chunk repeats).
#  G3 MDIST=8        >=8 DISTINCT 2-/3-grams with >=4 occurrences spanning
#                     <=64B: concentrated sub-4 matches (dimer-codebook
#                     mode, e.g. 200x4 tiled dimers). TLV/random have <=1.
#  G4 HM1=28         sparse order-0 single-hot mass c*(8-log2(c/n))/8-3:
#                     run-free single-hot flip <= 34.5, TLV structure <=
#                     22.1, random <= 5. (Multi-hot skew does not exist:
#                     shuffled 30^3 with hm2=26.2 stays literal; observed
#                     multi-hot fires are run/periodicity desc fires.)
# Fancy modes need n >= 145 per section (probed: dense/skew/run encodings
# all literal at <=144, including a skewed 100B tail section); the
# predicate needs no floor carve-out because the guards above already
# refuse small runs (conservative = safe).
WIN = 65535
K4 = 16
K3 = 20
K2 = 32
DP_M = 4
DP_C = 2
DP_SAV = 32
SPAN_K = 4
SPAN_W = 64
MDIST = 8
HM1_T = 28.0


class LzBitmapMatchFound(Exception):
    """Input outside the proven-parity (literal-only) class: the oracle
    would (or might) use its globally-planned match grammar here, so
    emitting literal bytes would silently diverge. Refuse honestly."""


def _lcp(W, a, b, cap):
    """Longest common prefix of W[a:], W[b:] capped at cap (binary lift)."""
    ml = len(W) - a if a > b else len(W) - b
    if cap > ml:
        cap = ml
    l = 0
    k = 1
    while k <= cap:
        k <<= 1
    k >>= 1
    while k:
        if l + k <= cap and W[a + l:a + l + k] == W[b + l:b + l + k]:
            l += k
        k >>= 1
    return l


def _dp_savings(W):
    """Relaxed optimal-parse LZ savings over W (matches len>=DP_M at cost
    DP_C, any offset; every real parse maps to a relaxed path, so this
    overestimates true savings: refuse-more = safe direction)."""
    m = len(W)
    if m < DP_M + 1:
        return 0
    four = {}
    rep4 = False
    for i in range(m - 3):
        g = W[i:i + 4]
        l = four.get(g)
        if l is None:
            four[g] = [i]
        else:
            l.append(i)
            rep4 = True
    if not rep4:
        return 0
    import heapq
    INF = 1 << 60
    f = [INF] * (m + 1)
    f[0] = 0
    active = []  # (value, expiry)
    starts = []  # (start, value, expiry), start ascending by construction
    si = 0
    for j in range(m + 1):
        while si < len(starts) and starts[si][0] <= j:
            _, v, x = starts[si]
            heapq.heappush(active, (v, x))
            si += 1
        while active and active[0][1] < j:
            heapq.heappop(active)
        if active and active[0][0] < f[j]:
            f[j] = active[0][0]
        if j >= m:
            break
        if f[j] + 1 < f[j + 1]:
            f[j + 1] = f[j] + 1
        if j + DP_M > m:
            continue
        occ = four.get(W[j:j + DP_M])
        if not occ:
            continue
        lm = 0
        for o in occ:
            if o == j:
                continue
            l = _lcp(W, j, o, m - j)
            if l >= 34:
                return DP_SAV  # one match alone suffices: instant refuse
            if l > lm:
                lm = l
                if lm >= m - j:
                    break
        if lm >= DP_M:
            starts.append((j + DP_M, f[j] + DP_C, j + lm))
    return m - f[m]


def _refuse_reason(data):
    """Exact refusal predicate -> None (proven-parity: emit literal) or a
    reason string (outside class: caller must refuse, never mis-encode).
    Analysis window per 32KB chunk = chunk + <=WIN prior block bytes
    (bedded 64KB cross-section dictionary)."""
    import math
    from collections import Counter
    n = len(data)
    for s in range(0, n, CHUNK):
        c = data[s:s + CHUNK]
        # G4: sparse order-0 single-hot mass (chunk-local; skew sections
        # never reference history, so history cannot create skew fires).
        if c:
            cc = Counter(c)
            nn = len(c)
            v = max(cc.values())
            hm = v * (8.0 + math.log2(v / nn)) / 8.0 - 3.0
            if hm >= HM1_T:
                return ("order0-hot1 chunk@%d mass=%.1f" % (s, hm))
        h0 = s - WIN if s > WIN else 0
        W = data[h0:s + len(c)]
        m = len(W)
        if m < 2:
            continue
        # G1+G3: single pass over window (early exit on first breach).
        # G3 keeps a sliding window of the last SPAN_K positions per
        # gram for each k, and counts DISTINCT grams that ever cluster.
        from collections import deque
        c4 = {}
        c3 = {}
        c2 = {}
        pos2 = {}
        pos3 = {}
        tight2 = set()
        tight3 = set()
        for i in range(m):
            if i + 4 <= m:
                g = W[i:i + 4]
                k = c4.get(g, 0) + 1
                if k >= K4:
                    return ("4gram-x%d window@%d" % (k, s))
                c4[g] = k
            if i + 3 <= m:
                g = W[i:i + 3]
                k = c3.get(g, 0) + 1
                if k >= K3:
                    return ("3gram-x%d window@%d" % (k, s))
                c3[g] = k
                e = pos3.get(g)
                if e is None:
                    pos3[g] = deque([i])
                else:
                    e.append(i)
                    if len(e) == SPAN_K:
                        if i - e[0] <= SPAN_W and g not in tight3:
                            tight3.add(g)
                            if len(tight2) + len(tight3) >= MDIST:
                                return ("mdist window@%d" % s)
                        e.popleft()
            if i + 1 < m:
                g = W[i:i + 2]
                k = c2.get(g, 0) + 1
                if k >= K2:
                    return ("2gram-x%d window@%d" % (k, s))
                c2[g] = k
                e = pos2.get(g)
                if e is None:
                    pos2[g] = deque([i])
                else:
                    e.append(i)
                    if len(e) == SPAN_K:
                        if i - e[0] <= SPAN_W and g not in tight2:
                            tight2.add(g)
                            if len(tight2) + len(tight3) >= MDIST:
                                return ("mdist window@%d" % s)
                        e.popleft()
        # G2: relaxed-DP economics (runs only when a 4-gram repeats,
        # i.e. len>=4 matches exist at all; else savings are 0).
        if _dp_savings(W) >= DP_SAV:
            return ("lz-savings window@%d" % s)
    return None


def zbm_encode_literal(inner):
    """Literal-only ZBM stream for proven-parity input -> bytes. Raises
    LzBitmapMatchFound on any input outside the proven-parity class."""
    inner = bytes(inner)
    r = _refuse_reason(inner)
    if r is not None:
        raise LzBitmapMatchFound(r)
    n = len(inner)
    if n == 0:
        return b"ZBM\x09" + struct.pack("<H", 6) + b"\x00" + struct.pack("<H", 0) + b"\x00"
    if n <= CHUNK:
        body = b"\x00" + inner
        return (b"ZBM\x09" + struct.pack("<H", len(body) + 5) + b"\x00"
                + struct.pack("<H", n) + body + b"\x06\x00\x00\x00\x00\x00")
    out = [b"ZBM\x09" + struct.pack("<H", CHUNK + 6) + b"\x00" + struct.pack("<H", CHUNK)]
    out.append(b"\x00" + inner[:CHUNK])
    for i in range(CHUNK, n, CHUNK):
        c = inner[i:i + CHUNK]
        out.append(struct.pack("<H", 6 + len(c)) + b"\x00"
                     + struct.pack("<H", len(c)) + b"\x00" + c)
    out.append(b"\x06\x00\x00\x00\x00\x00")
    return b"".join(out)


def wrap_pbzb(inner, blocksize=4 * 1024 * 1024):
    """pbzb outer: split inner by blocksize; per block ZBM-literal payload
    iff c*16 <= u*15 else raw store (15/16 rule, NOTE-008). Raises
    LzBitmapMatchFound (via zbm_encode_literal) when any block leaves
    the proven-parity class. Blocks are independent streams (bedded:
    no cross-block dictionary), so each block is analyzed alone."""
    inner = bytes(inner)
    blocks = [inner[i:i + blocksize] for i in range(0, len(inner), blocksize)] or [b""]
    framed = []
    for blk in blocks:
        comp = zbm_encode_literal(blk)
        if len(comp) * 16 <= len(blk) * 15:
            framed.append((len(blk), comp))
        else:
            framed.append((len(blk), blk))
    out = [struct.pack(">4sIIIIII", b"pbzb", 0, blocksize, 0,
                       framed[0][0], 0, len(framed[0][1]))]
    for i, (u, payload) in enumerate(framed):
        out.append(payload)
        if i + 1 < len(framed):
            nu, npay = framed[i + 1][0], len(framed[i + 1][1])
            out.append(struct.pack(">IIII", 0, nu, 0, npay))
    return b"".join(out)


if __name__ == "__main__":
    sys.path.insert(0, _HERE)
    from rawenc import build_inner
    inner = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(wrap_pbzb(inner))
