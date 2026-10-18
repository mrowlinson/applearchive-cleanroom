# Q-300 (writer2 s20): T10P236 P-head @98865 — geometry?

Own first-hand bed 98865..99212 (census RC=0
missing=0), staged p236-patch.txt, sweep
348/348 err 0 (try-p236; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 83470100 NEW, PB1 45f45702
  NEW, PBA 5c447f25 NEW (VPOS 7: b4+M6
  b6,7,76-79; b5 const 04; NO pair in
  tier).
- C10-2SIG EXACT map: a826a902 x3
  @98883-85 + 54935401 x7 @98886-92
  (VPOS 19: b4+M18 b0-3,6-11,48-51,
  80-83; b5 const 04; 10/10 diverge).
- QUAD f4344915 NEW (VPOS 19:
  b4,b5+M7+R6+T4; b5-carry 04->05
  @98943->98944 ff->01 edge).
- T88-RING 01000000 (==P231/232T sig),
  88B payload (VPOS 17 = b4,b5+M9+R6
  partition over 0..87).
- Next @99213 93540100 NEW + 99214
  b590ac02 NEW + 99215.. 609bd720 NEW
  (x14 probed).

## 2. quad + T-ring?
- Quad M7 b9-11,76-79 shared 16/16 x3
  vs row0.
- R6 b6,7,48-51 r1==r2==r3
  TRIPLE-PAIRED 2/4 EXACT (d1dec3de4951
  x3; r0 distinct).
- Tails row-shared 4/4 distinct
  bec350e6/4906c3ab/7306c3ab/9d06c3ab;
  r1/r2/r3 share last 3B 06c3ab
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P235T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [8-11,19,76-79]
  by COL 16/16; R6 [13,14,80-83] by ROW
  16/16 UNPAIRED (16 distinct); tails
  INVERTED b76-79 col / b80-83 row;
  b84-87 const 09a5a2f2 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 98865..99212: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x1b+2off)&FF 256/256;
  b5=0x05+(off>=115)+(off>=243) 256/256;
  edges 99071->99072 ff/05->01/06 +
  99199->99200 ff/06->01/07?
- Consts ALL 4: PBA 77 (b5-const), C10
  65 (b5-const), quad 65 (b5 varies
  carry), T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
