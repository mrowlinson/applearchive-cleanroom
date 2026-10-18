# Q-296 (writer2 s20): T10P232 P-head @97473 — geometry?

Own first-hand bed 97473..97820 (census RC=0
missing=0), staged p232-patch.txt, sweep
348/348 err 0 (try-p232; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 053b0100 NEW, PB1 dd1a3f01
  NEW, PBA-SPLIT8 dd1adf14 x8 @97475..82
  + dd1a2f16 x8 @97483..90 NEW (VPOS 11:
  b4+M8+split2 b21-23,31,76-79 + b2/b3
  df14/2f16; b22,23 const in half1; b5
  const f9).
- PAIR 97491..97492 dd1a7f02 NEW (diff
  b4+b80 only).
- PBC8 dd1a3f01 (==PB1) NEW (VPOS 13:
  b4+M12 b22,23,30-35,80-83; b5 const
  f9).
- QUAD dd1abf13 NEW (VPOS 22:
  b4,b5+M8+R8+T4; b5-carry f9->fa
  @97535->97536 ff->01 edge).
- T88-RING 01000000 (==P231T sig), 88B
  payload (VPOS 19 = b4,b5+M9+R8
  partition over 0..87).
- Next @97821 043b0100 NEW + 97822
  dd1a3f01 (==P232PB1) + 97823..
  dd1abf13 (==P232Q sig; x14 probed).

## 2. quad + T-ring?
- Quad M8 b36-39,76-79 shared 16/16 x3
  vs row0.
- R8 b22,23,30-35 r1==r2 PAIRED 3/4
  EXACT (21578e7f54512a07 x2; r0/r3
  distinct).
- Tails row-shared 4/4 distinct
  aeef66e5/acab63db/d6ab63db/d3703d27;
  r1/r2 share last 3B ab63db (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P231T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9
  [18,27,39,46,47,80-83] by COL 16/16;
  R8 [40-43,76-79] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b80-83 col / b76-79 row; b84-87
  const (1 ring-wide)?

## 3. counters + dips?
- Odd-lencode ALL 97473..97820: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x3b+2off)&FF 256/256;
  b5=0xfa+(off>=99)+(off>=227) 256/256;
  edges 97663->97664 ff/fa->01/fb +
  97791->97792 ff/fb->01/fc?
- Consts ALL 4: PBA 73 (b5-const),
  PBC 71 (b5-const), quad 62 (b5 varies
  carry), T88 69 (88-19)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
