# A-236 (Q-230): T10P179 P-head geometry — DERIVED

Bed: census N=79029..79120 own bed (.rav[12:-4]). First-hand; P178-M from own P178 census
row0 78709..78724 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 54010000 (REPEAT of P178 PB0); PB1 fat f91e0100 NEW;
  PBA 79031..79046 single sig d73d1700 NEW; SING 79047 sig 2fe30200 NEW (b0 0x2f == PBB b0).
- PBB9 79048..79056 sig 2f630100 NEW OWN-SIG (not PB1 echo — new variant).
- QUAD 79057..79120 single sig d73d1300 NEW.
- PBA VPOS [4,36,37,76,77,78,79] (6B M, b5 const 0x69); PBB VPOS [4,32,33,37,38,39,40,41,42,
  80,81,82,83] (12B M, b5 const 0x69).

## 2. quad rows: CONFIRM
- M 8B pos[23,34,35,43,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 12/16 quads each row), shared all 4 rows 16/16.
- b42 row-xor: X=[00,00,01,0f], b42^X[q]==M42[m] 64/64.
- R6 b36-41 row-only: rows0==1 exact 7edc986ecfbc (new pairing); row2 d5db551e2f28;
  row3 c35e3b278ff0, 64/64.
- tails b80..83 row-const 5ab30558/96b30558/c3f06f0a/463a5931 (rows0,1 share b1..3, differ b0).
- M-novelty vs P178M tails: ALL NEW (0/16). PBA M 6B 16/16 (heads 14/16 pairs); PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x69,0x6a} via lencode (Q2-internal step @79104: 79103 ff/69->79104 01/6a).
- varpos partitioned exact (PBA 7=b4+6tab; PBB 13=b4+12tab; quad 21=b4+b5+R6+M8+X42+tails),
  0 stragglers. NO D-class dips. Next tier @79121 sig d73d5301.

## geometry agrees on all 3 legs
