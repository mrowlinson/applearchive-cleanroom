# A-232 (Q-226): T10P177 P-head geometry — DERIVED (1 correction)

Bed: census N=78333..78424 own bed (.rav[12:-4]). First-hand; P176-M from own P176 census
row0 78013..78028 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 41010000 (REPEAT of P176 PB0); PB1 fat 73350100 NEW;
  PBA 78335..78350 single sig df9a1700 (REPEAT of P176 PBA sig).
- SING 78351 sig 73b50200 NEW; PBB9 78352..78360 sig 73350100 (== PB1 sig, PBB-echoes-PB1).
- QUAD 78361..78424 single sig 3f571300 NEW.
- PBA VPOS [4,5,48,49,50,51,76,77,78,79] (8B M; b5 step INSIDE PBA @78336: 78335=0x63,
  78336..=0x64). PBB VPOS [4,35,45,46,47,48,49,50,51,80,81,82,83] (12B M, b5 const 0x64).

## 2. quad rows: CONFIRM values; CORRECT pairing note
- M 8B pos[6,7,8,9,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 14/16 quads each row), shared all 4 rows 16/16.
- R-band 8B row-only: rows0==3 exact 918db88b71d7ff91 (0==3 pairing); row1 a18d41ee71f66766;
  row2 a10d183af16d970a, 64/64.
- tails b80..83 row-const 9b499b4f/235d2d25/5d968721/524a9b4f (4/4 exact).
- CORRECTION: rows0,3 share b2..b3, differ b0..b1 — NOT "share b1..3, differ b0".
  First-hand: row0 b81=0x49 vs row3 b81=0x4a (b0 0x9b vs 0x52; b82,b83 equal 0x9b,0x4f).
- M-novelty vs P176M tails: ALL NEW (0/16). PBA M 8B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x63,0x64} via lencode (PBA-internal step @78336).
- varpos partitioned exact (PBA 10=b4+b5+8tab; PBB 13=b4+12tab; quad 21=b4+R8+M8+tails),
  0 stragglers. NO D-class dips. Next tier @78425 sig f8733501.

## geometry agrees except rows0,3 tail-share note (corrected above)
