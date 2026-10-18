# Q-327 (writer2 s20): T10P263 P-head @108261 — geometry?

Own first-hand bed 108261..108608 (census RC=0
missing=0), staged p263-patch.txt, sweep
348/348 err 0 (try-p263; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 02550300 NEW, PB1 5d45ad06
  NEW, PBA-SPLIT6/2/8 6a56d46a x6
  @108263-68 + 6c56d46a x2 @108269-70 +
  5056d46a x8 @108271-78 (VPOS 10:
  b4+M8 b9-12,76-79 + split-b0; b5
  const 4d; NO pair in tier).
- C10-2SIG sandwich EXACT map: 6645ad06
  x5 @108279-83 + b3a25603 x1 @108284 +
  6645ad06 x4 @108285-88 (VPOS 18:
  b4,b5+M16 b0-3,11,13-19,80-83; b5-carry
  4d->4e @108287->108288 ff->01
  LAST-INTERNAL edge; 10/10 diverge).
- QUADms 3-sig e08e177f x16 (row0) +
  00825f6e x32 (rows1-2) + 60857f72 x16
  (row3) NEW (VPOS 20: b4+QM7+b19+R7+T4;
  b5 const 4e).
- T88-RING 06000000, 88B payload (VPOS
  17 = b4,b5+TM8+TR7 partition over
  0..87).
- Next P264 PB0 @108609+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b12-14,76-79 shared 16/16 x3
  vs row0.
- b19: row-ADD A=[0,1,1,0] 64/64 AND
  XOR X=[00,01,01,00] 64/64 — TIE
  first-hand (r0==r3 tab, r1==r2 tab
  =r03+1; staged ADD by b19-family
  precedent P231/P239, flagged as tie).
- R7 sig-led b0-3,16-18 r1==r2
  MID-PAIRED 3/4 EXACT (00825f6e963d30
  x2; r0 e08e177fd756f2 + r3
  60857f72d1c04a distinct).
- Tails row-shared 4/4 distinct
  ea36c61a/c1362ebe/05372ebe/ceebb136;
  r1/r2 share last 3B 362ebe (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P262T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [28-31,80-83]
  by COL 16/16; TR7 [20-22,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const 00ad0fa0 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 108261..108608: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x83+2off)&FF 256/256;
  b5=0x4e+(off>=63)+(off>=191) 256/256;
  edges 108415->108416 ff/4e->01/4f +
  108543->108544 ff/4f->01/50?
- Consts ALL 4: PBA 74 (b5-const), C10
  66 (b5-carry), quad 64 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
