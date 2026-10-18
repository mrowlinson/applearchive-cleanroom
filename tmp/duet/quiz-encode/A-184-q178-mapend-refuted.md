# A-184 (Q-178): map end @70328 — REFUTED (grammar continues)

Bed: census N=70329..70684 own bed + sparse
71000/72000/80000/100000/16777216/33554432
(.rav[12:-4]). First-hand, compression_tool
oracle, macOS 27.0.1; disputed cells
70329/70330/71000/80000/16777216 re-probed
independently byte-identical.

## 1. boundary: REFUTE (0/156 literal)
- 70328 = 100B/84B sig 783c0300 b4=0x71
  b5=0x25 (R151 off255, as writer).
- 70329 = 100B/84B sig 03000000 (P-head
  PB0-slot), NOT 53B literal sig 01500200.
- 70329..70484: 156/156 100B/84B grammar,
  ZERO 53B cells, ZERO 01500200 sigs. Sig
  runs: 03000000 x1 + 71070000 x1 + 1e770000
  x16 + b8030000 x10 + 8c3a0000 x64 +
  94890300 x64 = T10P154 (92) + R152 head.

## 2. literal rule: REFUTE (no such regime)
- No 53B frame anywhere in 70329..70484 or
  sparse probes. 71000/72000/80000/100000 =
  100B/84B grammar (sigs acaf0300/36a00700/
  274f4802/eeadf614).
- 16777216/33554432 = 1996B/3916B frames sig
  07800000 (multi-KB class), pay[3]=0x00
  both — NOT 53B, NOT pay[3]=0x01/0x02.
- Writer's 53B/37B/pay==input regime does not
  exist for zeros-N on this oracle. Likely
  writer bed bug (input recipe or stale bed):
  re-probe with stated recipe before WT commit.

## 3. scope: MOOT (nothing to rule)
- No literal fallback observed at any N
  probed (70329..70684 + 6 sparse to 33M).
  Map continues normally:
  T10P154 @70329..70420 (PB0 03000000, PB1
  71070000, PBA16 1e770000, NO singleton,
  PBB10 b8030000, QUAD64 single 8c3a0000;
  PBA VPOS [4,20,21,76-79] b5=0x25; PBB VPOS
  [4,20-26,80-83]; quad M 7B [19,26,27,76-
  79], R 7B b20-26, varpos 19, counters
  92/92, b5 step inside quad row2) +
  T10R152 @70421..70676 (single sig 94890300;
  m-tab 7B [32,33,34,72-75], q-tab 6B
  [26,27,76-79], 16/16 x2) + T10P155 from
  70677 (PB0 03000000, PB1 51070000).
- No T10LIT handler needed; no parent ruling
  needed unless writer reproduces 53B cells
  with recipe. Writer: re-derive P154/R152.

## verdict: REFUTE legs 1-2, leg 3 MOOT
