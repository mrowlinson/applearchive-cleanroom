# A-313 (viewer r3): Q-307 T10P243 P-head @101301 — CONFIRM all 3

First-hand bed 101301..101664 (q307.py
new, 88B-aware; census extended
101317..101664 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 4b620100 (==P242PB0 REPEAT ✓), PB1
  3d31c602 NEW, PBA 0080773c x16
  (==P242Q sig ✓; VPOS 7 exact b4+M6
  b36,37,76-79; b5 const 17; NO pair in
  tier).
- B10 single-sig 3d31c602 x10 (==PB1 sig
  ✓; VPOS 12 exact b4+M11 b36-42,80-83;
  b42 IN M-range ✓ first; b5 const 17;
  10/10 diverge).
- QUAD 0080773c x64 (==PBA sig ✓; VPOS
  23 exact b4,b5+QM10+b42+R6+T4;
  b5-carry 17->18 @101375->101376 ff->01
  edge).
- T88-RING 02000000 (==P242T sig ✓
  direct cross-check @101045), 88B
  payload all 256 ✓ (VPOS 21 exact
  b4,b5+TM8+TR11 partition over 0..87).
- Next P244 PB0 @101649 44620100 NEW +
  101650 3d319602 NEW + 101651..64
  de136329 x14 NEW.

## 2. quad + T-ring: CONFIRM
- Quad QM10 b14,15,23,34,35,43,76-79
  shared 16/16 x3 vs row0.
- b42: row-XOR X=[00,0c,0c,0c] 64/64 ✓
  AND ADD A=[0,4,4,4] 64/64 ✓ — TIE
  first-hand (M42 col-vector 4-valued
  06/46/86/c6 EXACT 3+5+5+3 ✓).
  VERDICT: tie — staged XOR stands by
  b42-family precedent. Flagged as tie
  per request.
- R6 b36-41 r1==r2==r3 TRIPLE 2/4
  EXACT (36db363b3135 x3; r0
  ed596928b1d5 distinct).
- Tails row-shared 4/4 distinct
  8469e6f6/5d42faad/928403ae/bc8403ae
  EXACT; r2/r3 share last 3B 8403ae.
- M-tails 16/16 ALL NEW vs P242T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [52-55,80-83]
  by COL 16/16; TR11 [18,19,27,38,39,
  46,47,76-79] by ROW 16/16 UNPAIRED
  (16 distinct, widest R yet ✓); tails
  SPLIT verified explicitly (b80-83
  col-shared 16 cols, b76-79 row-shared
  16 rows); b84-87 const cdead45d EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 101301..101648: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x23+2off)&FF 256/256;
  b5=0x18+(off>=111)+(off>=239) 256/256;
  edges 101503->101504 ff/18->01/19 +
  101631->101632 ff/19->01/1a.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  B10 72 (b5-const), quad 61 (b5 varies
  carry), T88 67 (88-21).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
