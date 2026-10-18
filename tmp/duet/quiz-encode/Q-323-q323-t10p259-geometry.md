# Q-323 (writer2 s20): T10P259 P-head @106869 — geometry?

Own first-hand bed 106869..107216 (census RC=0
missing=0), staged p259-patch.txt, sweep
348/348 err 0 (try-p259; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 20370300 (==P258PB0), PB1
  05016206 NEW, PBA e0921f7a x16
  (P258Q-adjacent 3a->7a; VPOS 10:
  b4,b5+M8 b36-39,76-79; b5-carry 42->43
  @106879->106880 ff->01 edge; NO pair
  in tier).
- B10 single-sig 05016206 x10 (==PB1
  sig; VPOS 12: b4+M11 b36-42,80-83;
  b42 IN M-range; b5 const 43; 10/10
  diverge).
- QUAD e0921f7a x64 (==PBA sig; VPOS
  19: b4+QM7+b42+R6+T4; b5 const 43).
- T88-RING 06000000 (==P252/253/256T
  sig), 88B payload (VPOS 18 =
  b4,b5+TM8+TR8 partition over 0..87).
- Next P260 PB0 @107217+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b34,35,43,76-79 shared
  16/16 x3 vs row0.
- b42: row-XOR X=[00,3e,05,09] 64/64
  AND ADD A=[0,02,fb,f7] 64/64 — TIE
  first-hand (M42 col-vector 4-valued
  {5f,df,9f,1f}, low-nibble const f,
  16 distinct = 4x4; staged XOR by
  b42-family precedent, flagged as tie).
- R6 b36-41 UNPAIRED 4/4 EXACT
  (d7df932a3163/bc5c041831f7/
  8d5e1c80319e/605e2317914d).
- Tails row-shared 4/4 distinct
  5288342d/5ed4036f/fca81ac3/fa92adc7
  (no shared suffix).
- M-tails 16/16 ALL NEW vs P258T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [52-55,80-83]
  by COL 16/16; TR8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const 37634be0 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 106869..107216: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xa3+2off)&FF 256/256;
  b5=0x43+(off>=47)+(off>=175) 256/256;
  edges 107007->107008 ff/43->01/44 +
  107135->107136 ff/44->01/45?
- Consts ALL 4: PBA 74 (b5-carry), B10
  72 (b5-const), quad 65 (b5-const),
  T88 70 (88-18)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
