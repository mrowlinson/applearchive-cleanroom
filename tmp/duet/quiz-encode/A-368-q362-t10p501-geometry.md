# A-368 (viewer r26): Q-362 T10P501 191085..191432 — CONFIRM all

First-hand bed 191085..191782 (own
698-cell census, oracle regen, rc=0
missing=0; 10-cell re-probe byte-
identical). Payload .rav[12:-4]. Bed +
scripts: NVME encode-viewer/q362-r26/.

## 1. shape: CONFIRM
- 350 cells 191085..191434 ALL raw104/
  pay88. PB0 191085 b8020000; PB1
  191086 aa700500.
- MID16 191087..102: sigs f6c04d00 x4
  + fec04d00 x4 + 86dc4d00 x7 +
  8edc4d00 x1 EXACT; M8 b0,1,19,27,
  80-83 16/16; b5-const d4; consts
  78 (base 86 excl b4/b5).
- C10 191103..112 sig 947f0500; M5
  b26,84-87 10/10; b4/b5 ff/d4 01/d5
  03/d5 .. 11/d5 (b5 step @191104);
  consts 81.
- QUAD88 191113..176 sig 941f5700:
  M7 b32-34,80-83 16/16 per row,
  row-seqs IDENTICAL (row-shared);
  tails b80-83 16/16 per row; R1 b84
  rows 08/28/48/68 row-const, NO
  pairing (M7 identical across rows,
  b84 differs); b5-const d5; consts 78.
- T88-RING 191177..432 sig 94cf7105
  (column-major o=c*16+r): TM7 b40-
  42,80-83 16/16 per COL; TR7 b32-
  34,76-79 16/16 per ROW; UNPAIRED
  (TR7 col-const, TM7 row-const);
  b5 = d5+(o>=55)+(o>=183) all 256;
  b84-87 = 88de6c00 all 256; consts 72.
- Next: P502 PB0 @191433 b8020000
  REPEAT-sig, body[4:] diff 33/84;
  PB1 @191434 92720500.

## 2. verdict: CONFIRM (36/36 checks)
- Every Q-362 byte claim reproduces
  from own bed. w2d tier cut SAFE.
