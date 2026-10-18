# A-244 (Q-238): T10P183 P-head geometry — DERIVED

Bed: census N=80421..80512 own bed (.rav[12:-4]). First-hand; P182-M from own P182
census row0 80101..80116 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 ce020000 (REPEAT of P182 PB0 sig); PB1 fat
  ada10500 NEW.
- PBA 80423..80438 single sig a81a5a00 NEW; SING 80439 sig aba10500 NEW
  (shares b1..3 a10500 with PB1, differs b0 ad/ab).
- PBB9 80440..80448 sig d5d00200 NEW OWN-SIG; QUAD 80449..80512 single sig
  580d2d00 NEW.
- PBA VPOS [4,9,10,11,76,77,78,79] EXACT (7B M, b5 const 0x74);
  PBB VPOS [4,13,14,15,16,17,18,19,80,81,82,83] EXACT (11B M, b5 const 0x74).

## 2. quad rows: CONFIRM
- M 7B pos[20,21,22,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 13/16 triples each row), shared all 4 rows 16/16.
- R 7B b13-19 row-only, 64/64: rows1==3 exact 983c90996ab20b (new pairing);
  row0 fabcc0f9941a11; row2 dd7cd53957ae0f.
- tails b80..83 row-const 0df3ebdf/a2fb466e/a5b90b71/17fc466e (rows1,3 share
  b2..b3 466e, differ b0..b1 a2fb/17fc).
- M-novelty vs P182M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 15/16
  triples); PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x74,0x75} via lencode (Q3-internal step @80512: 80511 ff/74->
  80512 01/75, last cell).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 12=b4+11tab; quad 20=
  b4+b5+R7+M7+tails), 0 stragglers. NO D-class dips. Next tier @80513 sig
  78c4d002 (80513+80514 both).

## geometry agrees on all 3 legs
