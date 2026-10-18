# A-248 (Q-242): T10P185 P-head geometry — DERIVED

Bed: census N=81117..81208 own bed (.rav[12:-4]). First-hand; P184-M from own P184
census row0 80797..80812 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 d0020000 (REPEAT of P184 PB0 sig); PB1 fat
  9b540200 NEW.
- PBA 81119..81134 single sig 9f342c00 (== P184 QUAD sig, own bed ref);
  SING 81135 sig 9f340400 (== P184 PB1 sig, own bed ref — cross-tier echo).
- PBB9 81136..81144 sig 9b540300 NEW (shares b0,b1,b3 9b,54,00 with PB1,
  differs b2 03/02); QUAD 81145..81208 single sig b0493500 NEW.
- PBA VPOS [4,48,49,50,76,77,78,79] EXACT (7B M, b5 const 0x79);
  PBB VPOS [4,35,45,46,47,48,49,50,51,80,81,82,83] EXACT (12B M, b5 const 0x79).

## 2. quad rows: CONFIRM
- M 7B pos[6,7,8,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 16/16 triples each row — full), shared all 4 rows 16/16.
- R 8B b35,45-51 row-only, 64/64: rows1==3 exact 191d71ac51d99f45; row0
  399d9a72b1a8ef12; row2 291d8b8bd1b1f7dd.
- tails b80..83 row-const ed928715/5a0b9b84/3607b5fd/cd0b9b84 (rows1,3 share
  b1..3 0b9b84, differ b0 5a/cd).
- M-novelty vs P184M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 16/16
  triples — full); PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x79,0x7a} via lencode (Q0-internal step @81152: 81151 ff/79->
  81152 01/7a).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 13=b4+12tab; quad 21=
  b4+b5+R8+M7+tails), 0 stragglers. NO D-class dips. Next tier @81209 sig
  049b5403 (81209+81210 both).

## geometry agrees on all 3 legs
