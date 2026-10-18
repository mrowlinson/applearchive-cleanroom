# Q-333 (writer2 s20): T10P269 P-head @110349 — geometry?

Own first-hand bed 110349..110696 (census RC=0
missing=0), staged p269-patch.txt, sweep
348/348 err 0 (try-p269; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 a4930300 NEW, PB1 3d502907
  NEW, PBA16-PLAIN 208c277e x16
  @110351-66 (VPOS 7: b4+M6
  b24,25,76-79; b0 const 20, b5
  const 5e; NO pair in tier).
- C10-1SIG single-sig EXACT map: a5322507
  x10 @110367-76 (VPOS 13: b4+M12
  b24-31,80-83; b5 const 5e; 10/10
  diverge).
- QUAD1s 1-sig 208c277e x64 (VPOS 22:
  b4+QM10+R7+T4; b5 const 5e).
- T88-ROWTAIL 07000000, 88B payload (VPOS
  19 = b4,b5+TM7+TR6+TT4 partition over
  0..87; tails ROW-led not col-split).
- Next P270 PB0 @110697+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM10 b14,15,21-23,31,76-79 shared
  16/16 x3 vs row0; NO frags (all
  positions COL-pure or ROW-pure, 0
  MIXED).
- R7 b24-30 r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 23bc65c2d5c02d x3; r0
  957c910d55dd0a distinct).
- Tails row-shared 4/4 distinct
  86296322/7d559c98/a2559c98/c7559c98;
  r1/r2/r3 share last 3B 559c98
  (tails echo the R last3-pairing).
- M-tails 16/16 ALL NEW vs P268T (row-0
  reference, true novelty).
- T88-ring ROWTAIL: TM7 [40-42,76-79]
  by COL 16/16; TR6 [18,19,25-27,35]
  by ROW 15/16 (r14==r15 366722f9e715
  shared; tails disambiguate); tails
  b80-83 ROW-led 16/16 (FIRST T88 with
  row-led tail tab, staged _T10P269TT
  by q); b84-87 const 1b2a6322
  (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 110349..110696: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xd3+2off)&FF 256/256;
  b5=0x5e+(off>=23)+(off>=151) 256/256;
  edges 110463->110464 ff/5e->01/5f +
  110591->110592 ff/5f->01/60?
- Consts ALL 4: PBA 77 (b5-const), C10
  71 (b5-const), quad 62 (b5-const),
  T88 69 (88-19)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
