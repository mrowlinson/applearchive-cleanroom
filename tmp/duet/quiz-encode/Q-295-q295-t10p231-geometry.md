# Q-295 (writer2 s20): T10P231 P-head @97125 — geometry?

Own first-hand bed 97125..97472 (census RC=0
missing=0), staged p231-patch.txt, sweep
348/348 err 0 (try-p231; base paylen
allowlist += 88 for T88).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 329d0000 NEW, PB1 f1053b01
  NEW, PBA 2d5eb013 NEW (VPOS 8: b4+M7
  b9-11,76-79; b5 const f6).
- PBB10 e0053b01 NEW single-sig (VPOS 13:
  b4,b5+M11 b13-19,80-83; b5-carry
  f6->f7 @97151->97152 ff->01 edge;
  10/10 diverge; NO pair/C8).
- QUADms 15-sig NEW (VPOS 20:
  b4+M8+R6+b19+T4; b5 const f7).
- T88-RING 01000000 NEW, 88B payload
  (VPOS 18 = b4,b5+M7+R9 partition).
- Next @97473 053b0100 NEW + 97474
  dd1a3f01 NEW + 97475.. dd1adf14 /
  dd1a2f16 NEW.

## 2. quad + T-ring?
- Quad M8 b0-2,11,76-79 shared 16/16 x3
  vs row0 (sig-led cols b0-2: 15 sigs
  d33d/d63d/d73d/dd3d x2/a895/aa95/ae95/
  b095/b295/b895/b78d/b88d/bd8d/be8d/
  c18d by column).
- b19 row-add A=[0,9,9,-11] 64/64 vs
  row-0 M19 (col-vector 2-valued
  35/b5; r1==r2 rows; r3 -11). NOTE:
  XOR X=[00,0b,0b,1f] fits equally (2
  col values) — staged ADD by b31
  precedent; flag if XOR preferred.
- R6 b13-18 r1==r2 PAIRED 3/4 EXACT
  (b2fc01da137e x2; r0/r3 distinct).
- Tails row-shared 4/4 distinct
  2738643c/d7ecaf3d/01edaf3d/4beeaca6;
  r1/r2 share last 2B af3d (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P230T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [29-31,80-83] by
  COL 16/16; R9 [16-19,23,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const? (verify 88B tail layout).

## 3. counters + dips?
- Odd-lencode ALL 97125..97472: 348/348
  exact (whole tier)?
- T88-ring b4=(0x83+2off)&FF 256/256;
  b5=0xf7+(off>=63)+(off>=191) 256/256;
  edges 97279->97280 ff/f7->01/f8 +
  97407->97408 ff/f8->01/f9?
- Consts ALL 4: PBA 76 (b5-const), PBB
  71 (b5 varies carry), quad 64
  (b5-const), T88 70 (88-18)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
