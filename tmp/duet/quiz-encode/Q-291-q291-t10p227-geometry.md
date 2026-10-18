# Q-291 (writer2 s20): T10P227 P-head @95733 — geometry?

Own first-hand bed 95733..96080 (census RC=0
missing=0), staged p227-patch.txt, sweep
348/348 err 0 (try-p227).

## 1. shape?
- 348 cells sizes {(100,84)}. PB0 bf250000
  ==P226PB0, PB1 8e634e00 NEW, PBA
  8e63b604 NEW (VPOS 8: b4+M6
  b36,37,76-79; b5-carry eb->ec @95743->
  95744 ff->01 edge).
- PBB10 2-sig 8e639600 x3 + 8e634e00 x7
  (first ==PB1; VPOS 20: b4+M18
  b2,23,32-43,80-83, b5 const ec, 10/10
  diverge; NO pair/C8).
- QUADmotif 8e63ee04 NEW (VPOS 20:
  b4,b5+M8+R6+b42+T4; b5 const ec).
- T-RING a0990745 ==P226T (VPOS 19 =
  b4,b5+M8+R9 partition).
- Next @96081 794b0000 NEW.

## 2. quad + T-ring?
- Quad M8 b2,34,35,43,76-79 shared 16/16
  x3 vs row0 (sig-led col b2: ee x11 / f6
  x5, cols 0-10/11-15).
- b42 row-xor X=[00,03,05,04] 64/64 vs
  row-0 M42 (all-4-lows-distinct
  c/f/9/8).
- R6 b36-41 UNPAIRED 4/4 (cb5bae95f046 /
  9b5a58ebb025 / dddb554c10a8 /
  46de61cff06d, all distinct).
- Tails row-shared 4/4 distinct
  4b696cac/f3c5f3b1/bd589836/5c9fa7af.
- M-tails 16/16 ALL NEW vs P226T rows.
- T-ring STANDARD: M8 [48-51,76-79] by
  COL 16/16; R9 [14,34,35,42,43,72-75]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 95733..96080: 348/348
  exact (whole tier)?
- T-ring b4=(0xa3+2off)&FF 256/256;
  b5=0xec+(off>=47)+(off>=175) 256/256;
  edges 95871->95872 ff/ec->01/ed +
  95999->96000 ff/ed->01/ee?
- Consts ALL 4: PBA 76 (b5 varies carry),
  PBB 65 (b5-const), quad 64 (b5-const),
  T 65?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
