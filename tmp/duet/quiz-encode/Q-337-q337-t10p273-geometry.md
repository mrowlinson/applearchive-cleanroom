# Q-337 (writer2 s20): T10P273 P-head @111741 — geometry?

Own first-hand bed 111741..112088 (census RC=0
missing=0), staged p273-patch.txt, sweep
348/348 err 0 (try-p273; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 f22a0700 NEW (f62a-family
  f2 variant), PB1 25bd5c0e
  SAME-as-P272PB1, PBA16-CARRY c0935ff8
  x16 @111743-58 (VPOS 10: b4,b5+M8
  b48-51,76-79; b0 const c0, b5
  68+step1; NO pair in tier).
- C10-5SIG EXACT map: 25bd5c0e x5
  @111759-63 + 25bdbc0c x1 @111764 +
  25bdec0a x1 @111765 + 25bd3c0b x1
  @111766 + 25bdcc0b x2 @111767-68
  (VPOS 14: b4+M13 b2,3,35,46-51,80-83;
  b5 const 69; 10/10 diverge).
- QUAD2s 2-sig 5dd2cbc1 x16 (row0) +
  5dd2cbc6 x48 (rows1-3) (VPOS 20:
  b4+QM8+R7+T4; b5 const 69).
- T88-RING 0d000000, 88B payload (VPOS
  17 = b4,b5+TM7+TR8 partition over
  0..87).
- Next P274 PB0 @112089+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM8 b6-9,76-79 shared 16/16 x3
  vs row0; NO frags (all positions
  COL-pure or ROW-pure, 0 MIXED).
- R7 b3,46-51 r1==r2==r3 LAST3-PAIRED
  2/4 EXACT (r123 c65dbe71ff5f90 x3;
  r0 c1a44d51e1d77d distinct).
- Tails row-shared 4/4 distinct
  ae2d1859/53bca1aa/1d7423ac/427423ac;
  r2/r3 share last 3B 7423ac.
- M-tails 16/16 ALL NEW vs P272T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [9-11,80-83]
  by COL 16/16; TR8 [6,7,12,13,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const 277bfb46 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 111741..112088: 348/348
  exact (whole tier incl 88B cells)?
- PBA b4=(0xff+2off)&FF 16/16;
  b5=0x68+(off>=1) 16/16; edge
  111743->111744 ff/68->01/69 (first-
  cell carry o=0->1)?
- T88-ring b4=(0xb3+2off)&FF 256/256;
  b5=0x69+(off>=39)+(off>=167) 256/256;
  edges 111871->111872 ff/69->01/6a +
  111999->112000 ff/6a->01/6b?
- Consts ALL 4: PBA 74 (b5-step), C10
  70 (b5-const), quad 64 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
