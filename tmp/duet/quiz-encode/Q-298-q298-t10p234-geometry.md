# Q-298 (writer2 s20): T10P234 P-head @98169 — geometry?

Own first-hand bed 98169..98516 (census RC=0
missing=0), staged p234-patch.txt, sweep
348/348 err 0 (try-p234; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 8c470100 NEW, PB1 ee8c4701
  NEW, PBA16-MS 13-sig NEW (VPOS 11:
  b4,b5+M9 b0-2,11,19,76-79; b5-carry
  fe->ff @98175->98176 ff->01 edge;
  16/16 diverge; NO pair in tier).
- FRAG10 7-sig EXACT map: cd898b02 x3
  @98187-89 + ddfc8f02 + 958d8c02 +
  65358202 + 25b38502 + 3dd58902 +
  85768302 + 958d8c02 (VPOS 14: b4+M13
  b0-2,11,18-22,80-83; b5 const ff;
  10/10 diverge).
- QUAD 40806734 NEW (VPOS 19:
  b4+M7+R7+T4; b5 const ff).
- T88-STEP-RING 02000000 NEW, 88B
  payload (VPOS 17 = b4,b5+M7+R7+b6step
  partition over 0..87).
- Next @98517 8c470100 (==P234PB0
  REPEAT) + 98518 45f44701 NEW +
  98519.. 45f47714 NEW (x14 probed).

## 2. quad + T-ring?
- Quad M7 b24-26,76-79 shared 16/16 x3
  vs row0.
- R7 b13,14,18-22 r0==r3 OUTER-PAIRED
  3/4 EXACT (b49bc46f3243a3 x2; r1/r2
  distinct, differ 1B e8/f8).
- Tails row-shared 4/4 distinct
  2e189304/f98d105d/311be64a/55426037.
- M-tails 16/16 ALL NEW vs P233T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [27,34,35,80-83]
  by COL 16/16; R7 [28-30,76-79] by ROW
  16/16 UNPAIRED (16 distinct); b6
  step-coupled 0x66+(off>=43) 256/256
  (flip rides first b5 step); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const a0a46037 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 98169..98516: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xab+2off)&FF 256/256;
  b5=(0xff+(off>=43)+(off>=171))&FF
  256/256 (WRAP ff->00->01); edges
  98303->98304 ff/ff->01/00 +
  98431->98432 ff/00->01/01?
- Consts ALL 4: PBA 73 (b5 varies
  carry), FRAG 70 (b5-const), quad 65
  (b5-const), T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
