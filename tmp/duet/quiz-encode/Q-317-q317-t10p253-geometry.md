# Q-317 (writer2 s20): T10P253 P-head @104781 — geometry?

Own first-hand bed 104781..105128 (census RC=0
missing=0), staged p253-patch.txt, sweep
348/348 err 0 (try-p253; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 e0180300 NEW, PB1 0d4a3706
  NEW, PBA a096b766 NEW (VPOS 8:
  b4+M7 b24-26,76-79; b5 const 32;
  NO pair in tier).
- C10-2SIG sandwich EXACT map: 6d4b3306
  x4 @104799-802 + 6d4b1303 x3
  @104803-05 + 6d4b3306 x3 @104806-08
  (VPOS 17: b4+M16 b2,3,22-31,80-83;
  b5 const 32; 10/10 diverge).
- QUADms pair-led a096b766 x32 (rows
  0-1) + a096b726 x32 (rows 2-3) NEW
  (VPOS 23: b4,b5+QM4+b21+b22+b23+b31+
  R9+T4; b5-carry 32->33 @104831->
  104832 ff->01 edge).
- T88-RING 06000000 (==P252T sig), 88B
  payload (VPOS 16 =
  b4,b5+TM6+TR8 partition over 0..87).
- Next P254 PB0 @105129+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM4 TAILS-ONLY b76-79 shared
  16/16 x3 vs row0.
- b21/b22/b23/b31 PAIR-COLTABS: r01-tab
  vs r23-tab (r0==r1, r2==r3 identical
  all 4; no uniform xor/add — staged
  2x16 tabs each; b21 2-valued 8d/0d,
  b22 6-valued, b23 4-valued, b31
  32 distinct).
- R9 sig-led b3,15,24-30 r2==r3 PAIRED
  3/4 EXACT (26836abc0642d456f1 x2; r0
  66062f7c756835965b + r1
  660668fcc32655f509 distinct; b3
  row-sigs 66/66/26/26 pair-led).
- Tails row-shared 4/4 distinct
  ec5f46a3/9ca27f5e/f7ee27fc/21ef27fc;
  r2/r3 share last 3B ee27fc (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P252T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM6 [40,41,76-79]
  by COL 16/16; TR8 [25-27,35,80-83] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b76-79 col / b80-83 row;
  b84-87 const 2f9db46e (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 104781..105128: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x53+2off)&FF 256/256;
  b5=0x33+(off>=87)+(off>=215) 256/256;
  edges 104959->104960 ff/33->01/34 +
  105087->105088 ff/34->01/35?
- Consts ALL 4: PBA 76 (b5-const), C10
  67 (b5-const), quad 61 (b5 varies
  carry), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
