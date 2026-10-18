# A-252 (Q-246): T10P187 P-head geometry — DERIVED

Bed: census N=81813..81904 own bed (.rav[12:-4]). First-hand; P186-M from own P186
census row0 81493..81508 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 f6020000 (REPEAT of P186 PB0 sig); PB1 fat
  3b070500 NEW.
- PBA 81815..81830 single sig 3b075d00 NEW; SING 81831 sig 3b070500
  (SING-echoes-PB1, sig only — 3rd CONFIRM).
- MID9 81832..81840: 8x sig 3bee0200 + 1x PB1-echo 3b070500 @81834 (new MID
  variant CONFIRM: echo 3rd cell, rest uniform).
- QUAD 81841..81904 single sig 3b072500 NEW.
- PBA VPOS [4,36,37,38,76,77,78,79] EXACT (7B M, b5 const 0x7f);
  MID VPOS [1,2,4,11,19-27,32-35,37-43,80-83] EXACT (28 = b4+27tab; 27B M
  incl sig b1,b2; b5 const 0x7f).

## 2. quad rows: CONFIRM
- M 8B pos[34,35,42,43,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each
  row (heads 14/16 quads each row), shared all 4 rows 16/16.
- R 6B b36-41 row-only, DOUBLE pairing (new): rows0==1 exact 685af1e56f97
  AND rows2==3 exact 28dbb0b28f12, 64/64.
- tails b80..83 row-const 66ae942e/9eae942e/02d39b28/3bd39b28 (rows0,1 share
  b1..3 ae942e; rows2,3 share b1..3 d39b28; differ b0).
- M-novelty vs P186M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 16/16
  triples — full); MID M 27B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x7f whole tier (single tier [0x7f], no step anywhere).
- varpos partitioned exact (PBA 8=b4+7tab; MID 28=b4+27tab; quad 19=
  b4+R6+M8+tails), 0 stragglers. NO D-class dips. Next tier @81905 sig
  3b07f502 (81905+81906 both).

## geometry agrees on all 3 legs
