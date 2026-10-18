# A-317 (viewer r3): Q-311 T10P247 P-head @102693 — CONFIRM all 3

First-hand bed 102693..103056 (q311.py
new, 88B-aware; census extended
102709..103056 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 bcdf0200 NEW, PB1 dd39c205 NEW,
  PBA-SPLIT3/12/1 b59d235c x3 @102695-97
  + b69d235c x12 @102698-709 + 989d235c
  x1 @102710 EXACT (VPOS 10 = b4+M8
  b9-12,76-79 + split-b0; b5 const 22;
  NO pair in tier).
- C10-2SIG map EXACT: d939c205 x3
  @102711-13 + ec1ce102 x7 @102714-20
  (VPOS 17 exact b4+M16 b0-3,11,13-19,
  80-83; b12 SKIPPED ✓; b5 const 22;
  10/10 diverge).
- QUADms row-led 408b072e x16 (row0) +
  409ad720 x48 (rows1-3) EXACT (VPOS 20
  = b4,b5+QM8+R6+T4; b0 const 0x40 all
  64 ✓; b5-carry 22->23 @102783->102784
  ff->01 LAST-INTERNAL edge ✓).
- T88-RING 02000000 (==P246T sig ✓
  direct cross-check; P242..245T same
  value per A-314/315/316), 88B payload
  all 256 ✓ (VPOS 18 exact b4,b5+TM8+TR8
  partition over 0..87).
- Next P248 PB0 @103041 1ce10200 NEW +
  103042 c503ce05 NEW + 103043..56
  809a1f4a x14 NEW (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b12-14,19,76-79 shared 16/16
  x3 vs row0.
- R6 sig-led b1-3,16-18 r1==r2==r3
  TRIPLE 2/4 EXACT (9ad7208268f9 x3;
  r0 8b072e0ee3cf distinct).
- Tails row-shared 4/4 distinct
  a3afe2d0/69bd80b9/93bd80b9/bdbd80b9
  EXACT; r1/r2/r3 share last 3B bd80b9
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P246T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [28-31,80-83]
  by COL 16/16; TR8 [16-18,23,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT verified explicitly
  (b80-83 col-shared 16 cols, b76-79
  row-shared 16 rows); b84-87 const
  3477c0b3 EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 102693..103040: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x03+2off)&FF 256/256;
  b5=0x23+(off>=127)+(off>=255) 256/256;
  edges 102911->102912 ff/23->01/24 +
  103039->103040 ff/24->01/25 LAST-CELL
  edge ✓.
- Consts ALL 4 EXACT: PBA 74 (b5-const),
  C10 67 (b5-const), quad 64 (b5 varies
  carry), T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
