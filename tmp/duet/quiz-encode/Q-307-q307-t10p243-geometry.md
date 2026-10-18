# Q-307 (writer2 s20): T10P243 P-head @101301 — geometry?

Own first-hand bed 101301..101648 (census RC=0
missing=0), staged p243-patch.txt, sweep
348/348 err 0 (try-p243; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 4b620100 REPEAT (==P242PB0),
  PB1 3d31c602 NEW, PBA 0080773c x16
  (==P242Q sig; VPOS 7: b4+M6
  b36,37,76-79; b5 const 17; NO pair
  in tier).
- B10 single-sig 3d31c602 x10 (==PB1
  sig; VPOS 12: b4+M11 b36-42,80-83;
  b5 const 17; 10/10 diverge; b42 IN
  M-range first!).
- QUAD 0080773c x64 (==PBA sig; VPOS
  23: b4,b5+QM10+b42+R6+T4; b5-carry
  17->18 @101375->101376 ff->01 edge).
- T88-RING 02000000 (==P242T sig),
  88B payload (VPOS 21 =
  b4,b5+TM8+TR11 partition over 0..87).
- Next P244 PB0 @101649 44620100 NEW
  + 101650 3d319602 + 101651.. de136329
  x14 probed.

## 2. quad + T-ring?
- Quad QM10 b14,15,23,34,35,43,76-79
  shared 16/16 x3 vs row0.
- b42 row-xor X=[00,0c,0c,0c] (col-vec
  4-valued {86,46,06,c6}; ADD-04-tie
  flagged, staged XOR by family
  precedent).
- R6 b36-41 r1==r2==r3 TRIPLE 2/4
  EXACT (36db363b3135 x3; r0 ed596928b1d5
  distinct).
- Tails row-shared 4/4 distinct
  8469e6f6/5d42faad/928403ae/bc8403ae;
  r2/r3 share last 3B 8403ae.
- M-tails 16/16 ALL NEW vs P242T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [52-55,80-83]
  by COL 16/16; TR11 [18,19,27,38,39,
  46,47,76-79] by ROW 16/16 UNPAIRED
  (16 distinct, widest R yet); tails
  SPLIT b80-83 col / b76-79 row;
  b84-87 const cdead45d (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 101301..101648: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x23+2off)&FF 256/256;
  b5=0x18+(off>=111)+(off>=239) 256/256;
  edges 101503->101504 ff/18->01/19 +
  101631->101632 ff/19->01/1a?
- Consts ALL 4: PBA 77 (b5-const), B10
  72 (b5-const), quad 61 (b5 varies
  carry), T88 67 (88-21)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
