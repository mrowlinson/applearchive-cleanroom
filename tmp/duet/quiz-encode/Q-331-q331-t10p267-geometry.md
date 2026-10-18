# Q-331 (writer2 s20): T10P267 P-head @109653 — geometry?

Own first-hand bed 109653..110000 (census RC=0
missing=0), staged p267-patch.txt, sweep
348/348 err 0 (try-p267; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 a0740300 SAME-as-P266PB0,
  PB1 1d18e406 NEW, PBA16-PLAIN c0822772
  x16 @109655-70 (VPOS 7: b4+M6
  b36,37,76-79; b0 const c0, b5
  const 58; NO pair in tier).
- C10-1SIG single-sig EXACT map: 1d18e406
  x10 @109671-80 (VPOS 12: b4+M11
  b36-42,80-83; b5 const 58; 10/10
  diverge; head-sig == PB1 sig).
- QUAD1s 1-sig c0822772 x64 (VPOS 20:
  b4,b5+QM7+b42+R6+T4; b5 step o>=15).
- T88-RING 06000000, 88B payload (VPOS
  18 = b4,b5+TM8+TR8 partition over
  0..87).
- Next P268 PB0 @110001+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b34,35,43,76-79 shared 16/16
  x3 vs row0.
- b42: row-XOR X=[00,0f,0f,0f] 64/64 AND
  row-ADD A=[0,3,3,3] 64/64 — TIE
  first-hand (r1==r2==r3 tab shape =
  X42-family P243/P251; staged XOR by
  b42-family precedent P211-P259,
  flagged as tie).
- R6 b36-41 r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 bfdd8c6dd153 x3; r0
  24dfb205518e distinct; FIRST
  last-three-paired quad).
- Tails row-shared 4/4 distinct
  9e2c5289/71bf4a51/96bf4a51/bbbf4a51;
  r1/r2/r3 share last 3B bf4a51
  (tails echo the R last3-pairing).
- M-tails 16/16 ALL NEW vs P266T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [52-55,80-83]
  by COL 16/16; TR8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const de93eef2 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 109653..110000: 348/348
  exact (whole tier incl 88B cells)?
- Quad b4=(0xe3+2off)&FF 64/64;
  b5=0x58+(off>=15) 64/64; edge
  109695->109696 ff/58->01/59 (end of
  row0 o=14->15)?
- T88-ring b4=(0x63+2off)&FF 256/256;
  b5=0x59+(off>=79)+(off>=207) 256/256;
  edges 109823->109824 ff/59->01/5a +
  109951->109952 ff/5a->01/5b?
- Consts ALL 4: PBA 77 (b5-const), C10
  72 (b5-const), quad 64 (b5-step),
  T88 70 (88-18)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
