# Q-318 (writer2 s20): T10P254 P-head @105129 — geometry?

Own first-hand bed 105129..105476 (census RC=0
missing=0), staged p254-patch.txt, sweep
348/348 err 0 (try-p254; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 e4180300 NEW, PB1 6d4b3306
  (==P253C10a sig), PBA a096b766 x16
  (==P253PBA sig; VPOS 8: b4+M7
  b34,42,43,76-79; b5 const 35; NO pair
  in tier).
- C10-2SIG sandwich EXACT map: 6d4b3306
  x4 @105147-50 + 6d4b1303 x4 @105151-54
  + 6d4b3306 x2 @105155-56 (VPOS 16:
  b4+M15 b2,3,34,35,41-47,80-83; b5
  const 35; 10/10 diverge).
- QUADms row-led a096b766 x16 (row0) +
  a096b726 x48 (rows1-3) (VPOS 26:
  b4,b5+QM8+b47+R11+T4; b5-carry 35->36
  @105215->105216 ff->01 edge).
- T88-RING 02000000 (back to 02 after
  P252/253 06), 88B payload (VPOS 17 =
  b4,b5+TM6+TR9 partition over 0..87).
- Next P255 PB0 @105477+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM8 b48-51,76-79 shared 16/16 x3
  vs row0.
- b47 2x2-FRAG 64/64: (r0,c<3)=f2,
  (r0,c>=3)=f4, (r123,c<3)=f9,
  (r123,c>=3)=fa (no uniform xor/add —
  staged inline 4-literal frag).
- R11 sig-led b3,14,15,34,35,41-46
  r2==r3 PAIRED 3/4 EXACT
  (261a8c74d5b8856f93b4e1 x2; r0
  669a18d8c5b889d7146914 + r1
  261a8c14de588a5f53caf9 distinct).
- Tails row-shared 4/4 distinct
  b6a8543e/e95abd76/ef6138db/196238db;
  r2/r3 share last 3B 6238db (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P253T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM6 [6,7,80-83] by
  COL 16/16; TR9 [51-55,76-79] by ROW
  16/16 UNPAIRED (16 distinct, widest R
  yet); tails SPLIT b80-83 col / b76-79
  row; b84-87 const 655bbd76
  (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 105129..105476: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x0b+2off)&FF 256/256;
  b5=0x36+(off>=123)+(off>=251) 256/256;
  edges 105343->105344 ff/36->01/37 +
  105471->105472 ff/37->01/38?
- Consts ALL 4: PBA 76 (b5-const), C10
  68 (b5-const), quad 58 (b5 varies
  carry), T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
