# Q-320 (writer2 s20): T10P256 P-head @105825 — geometry?

Own first-hand bed 105825..106172 (census RC=0
missing=0), staged p256-patch.txt, sweep
348/348 err 0 (try-p256; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 641a0300 NEW, PB1 e58c3506
  NEW, PBA a0802f7c NEW (VPOS 11:
  b4+M10 b14,15,21-23,31,76-79; b5
  const 3a; NO pair in tier).
- C10-2SIG sandwich EXACT map: e58c3506
  x4 @105843-46 + e58c1503 x3 @105847-49
  + e58c3506 x3 @105850-52 (VPOS 15:
  b4+M14 b2,3,22,23,30-35,80-83; b5
  const 3a; 10/10 diverge).
- QUADms pair-led 1B-off a0802f7c x32
  (rows 0-1) + a0802f3c x32 (rows 2-3)
  NEW (VPOS 23: b4,b5+QM7+R10+T4;
  b5-carry 3a->3b @105855->105856 ff->01
  EARLY edge).
- T88-RING 06000000 (==P252/253T sig),
  88B payload (VPOS 16 =
  b4,b5+TM7+TR7 partition over 0..87).
- Next P257 PB0 @106173+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0.
- R10 sig-led b3,15,22,23,30-35 r0==r1
  PAIRED EXACT (7c1a33e6d67f356a6afc x2;
  r2 3c8db35b04fad4c1fe7f + r3
  3c8db35b08fad4c1fe7f 1B-off 04-vs-08;
  b3 row-sigs 7c/7c/3c/3c pair-led).
- Tails row-shared 4/4 distinct
  10299170/36299170/6c301f67/87aa49cb;
  r0/r1 share last 3B 299170 (matching
  R-pair); r2/r3 distinct.
- M-tails 16/16 ALL NEW vs P255T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [39,46,47,80-83]
  by COL 16/16; TR7 [40-42,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const edf84115 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 105825..106172: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x7b+2off)&FF 256/256;
  b5=0x3b+(off>=67)+(off>=195) 256/256;
  edges 105983->105984 ff/3b->01/3c +
  106111->106112 ff/3c->01/3d?
- Consts ALL 4: PBA 73 (b5-const), C10
  69 (b5-const), quad 61 (b5 varies
  carry), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
