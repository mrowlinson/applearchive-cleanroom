# A-258 (Q-252): T10P190 P-head geometry — DERIVED

Bed: census N=82857..82948 own bed (.rav[12:-4]). First-hand; P189-M from own P189
census row0 82537..82552 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 1e030000 (REPEAT of P189 PB0 sig); PB1 fat
  614e0700 (== P189 SING sig, own bed ref).
- PBA 82859..82874 single sig 614e7300 NEW; SING 82875 sig 614e0700
  (SING-echoes-PB1, sig only — 4th CONFIRM).
- PBB9 82876..82884 sig 37070300 NEW OWN-SIG; QUAD 82885..82948 single sig
  614e3300 (REPEAT of P189 QUAD sig, own bed ref).
- PBA VPOS [4,34,35,42,43,76,77,78,79] EXACT (8B M, b5 const 0x87);
  PBB VPOS [4,34,35,41,42,43,44,45,46,80,81,82,83] EXACT (12B M, b5 const 0x87).

## 2. quad rows: CONFIRM structure + CORRECTION (one byte)
- M 7B pos[48,49,50,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 16/16 triples each row — full), shared all 4 rows 16/16.
- R 8B b34,35,41-46 row-only, 64/64: rows0==2 exact 16e89cc03ff2fe33; row1
  fde43cc61792a93a; row3 d1eb2cc86f72d630.
- CORRECTION: tails are 4/4 distinct as tuples (5b7cb5af/0bf1e8f7/5af29be7/
  76f73116 CONFIRM) but byte sharing is 15/16, NOT 16/16: value f7 appears
  twice (row1-b83 AND row3-b81). "No byte sharing" fails on one value.
- M-novelty vs P189M tails: ALL NEW (0/16). PBA M 8B 16/16 (heads 15/16
  quads); PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x87,0x88} via lencode (Q3-internal step @82944: 82943 ff/87->
  82944 01/88).
- varpos partitioned exact (PBA 9=b4+8tab; PBB 13=b4+12tab; quad 21=
  b4+b5+R8+M7+tails), 0 stragglers. NO D-class dips. Next tier @82949 sig
  17e63403 (82949+82950 both).

## geometry agrees on legs 1+3, leg 2 agrees modulo tail bytes (15/16 not 16/16)
