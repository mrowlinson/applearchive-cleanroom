# A-242 (Q-236): T10P182 P-head geometry — DERIVED

Bed: census N=80073..80164 own bed (.rav[12:-4]). First-hand; P181-M from own P181
census row0 79753..79768 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 ce020000 (NEW PB0 sig); PB1 fat 274f0400
  (== P181 SING sig, own A-240).
- PBA 80075..80090 single sig 274f4c00 NEW; SING 80091 sig 274f0400
  (SING-echoes-PB1, sig only — new variant CONFIRM).
- PBB9 80092..80100 sig bf5b0200 NEW OWN-SIG; QUAD 80101..80164 single sig
  274f2c00 (REPEAT of P181 QUAD sig, own A-240).
- PBA VPOS [4,34,35,42,43,76,77,78,79] EXACT (8B M, b5 const 0x71);
  PBB VPOS [4,34,35,41,42,43,44,45,46,80,81,82,83] EXACT (12B M, b5 const 0x71).

## 2. quad rows: CONFIRM
- M 8B pos[48,49,50,51,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each
  row (heads 15/16 quads each row), shared all 4 rows 16/16.
- R 8B b34,35,41-46 row-only, 64/64: rows0==2 exact 4aedf9c13b32c49e
  (pairing returns); row1 41e5d9cd0f12d496; row3 cae679c077125b94.
- tails b80..83 row-const 356f0ded/fc762c8a/aa6f0ded/8a78e288 (rows0,2 share
  b1..3 6f0ded, differ b0 35/aa).
- M-novelty vs P181M tails: ALL NEW (0/16). PBA M 8B 16/16 (heads 16/16
  quads — full); PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x71,0x72} via lencode (Q1-internal step @80128: 80127 ff/71->
  80128 01/72).
- varpos partitioned exact (PBA 9=b4+8tab; PBB 13=b4+12tab; quad 22=
  b4+b5+R8+M8+tails), 0 stragglers. NO D-class dips. Next tier @80165 sig
  77f2c402 (80165+80166 both).

## geometry agrees on all 3 legs
