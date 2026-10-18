# NOTE-w2s5-14 GRAMMAR-v1: raven payload field layout (zeros-family beds)

All first-hand (compression_tool -a lzraven, LSB-first bit numbering).
Base: zeros128 -> 44B payload (bits 0-351); mid-dev -> 48B (bits 0-383).

## G1 length code (zeros-N, N>=64 compressed; N<=63 stored-verbatim)
- tier bounds EXACT: 63/64, 127/128, 255/256 (512+ shape-change open).
- BYTE4 = (offset<<1)|1 where offset = N - tierbase (128/128 tier1 sweep;
  holds at every tier base 64/128/256/512/1024/2048/4096/8192). bits 33-39
  = O0-O6 linear, bit32 const-1. ONLY head length bits (0-95 scan).
- tier codes: b8 = 07/08/09 (tiers 0/1/2); b1 = 00/08/10; b0 varies (tier0:
  0x40@64, 0x00@126 — carries length high bits, open sub-map).

## G2 tail echo (lossy, deterministic): bits 307-310 = (off+3)&15 (wrap
verified 63->15/64->0); bits 272-273 = (off+3)>>6 (transitions exact at
off+3=64,128). MIDDLE bits 4-5 NOWHERE in full 352-bit scan (48 states for
128 offsets; byte4 authoritative). purpose open (2nd-run token?).

## G3 mid-dev value (single-AA@pos, pos in 19..76): SPLIT NIBBLES —
V0-3 @ bits 50-53, V4-7 @ bits 377-380 (pos30/50/76 identical). pos19
(tier edge): V4-7 @ 335-338 + V0-3 @ 380-383 (swapped packing!).
neighbors: bits 40-49/54-63 zeros; bit66 = dev-present; bit365=1, bit383=1.

## G4 two-dev packing (ONE +4B token carries both): dev@30 keeps V0-3@50-53,
high nibble MOVES to 381-383+307; dev@50: V0-2@7-9, V3@11 (bit10 SKIPPED,
const-0, tag?), V4-7@54-57. bits 44/48/62/73/79 = lownib-nonzero flags
(single-sweep pattern 11110000; parse-dependent, B50-const-0 puzzle open).
FF TRAP: swept-V == fixed-V causes global resync (~100 bits) — equal-valued
devs interact; future 2-param sweeps avoid V-collision.

## G5 capacity/cost: ~2 DISTINCT literals per +4B token (1-2dev->48B,
3dev->52B, 4-5dev->56B); same-valued devs MUTUALLY MATCH (5xAA->48B < 4xAA
->52B). position encoded DIFFUSELY (30v50: 44 scattered bits) — no position
field; position lives in match/length structure.

## Open for viewer field-level beds: TAG-01 vs TAG-0000 width ID at nibble
fields (which tag wraps V0-3@50-53 / V4-7@377-380?); bit10 role; G2 middle
bits; tier3+ (512+) shape; pos19 swap rule. tools: tfbed.py, tparse2.py
(bed-w2s4-order/raven/), all beds reproducible via stated recipes.
