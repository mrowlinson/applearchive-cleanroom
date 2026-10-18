# A-234 (Q-228): T10P178 P-head geometry — DERIVED

Bed: census N=78681..78772 own bed (.rav[12:-4]). First-hand; P177-M from own P177 census
row0 78361..78376 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 54010000 NEW; PB1 fat 78540100 NEW; PBA 78683..78698
  single sig 8e471500 NEW; SING 78699 sig f1a80200 NEW; PBB9 78700..78708 sig
  78540100 (== PB1 sig, PBB-echoes-PB1).
- QUAD 78709..78772 MULTI-SIG: row0 2b801600, rows1-2 4d601700, row3 1be71700 (all NEW).
- PBA VPOS [4,20,21,22,76,77,78,79] (7B M, b5 const 0x66); PBB VPOS [4,20,21,22,23,24,25,26,
  80,81,82,83] (11B M, b5 const 0x66).

## 2. quad rows: CONFIRM
- M 7B pos[20,26,27,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 16/16 triples each row — full), shared all 4 rows 16/16.
- sigR 7B b0,1,2,18,19,24,25 row-only: rows1==2 exact 4d6017468da0eb (new pairing);
  row0 2b801686e991e3; row3 1be7178697c4db, 64/64.
- tails b80..83 row-const e854c1b2/5308d684/6c5465f8/05219146 (rows0,2 share b1=0x54, else differ).
- M-novelty vs P177M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 15/16 triples); PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x66,0x67} via lencode (Q0-internal step @78720: 78719 ff/66->78720 01/67).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 12=b4+11tab; quad 20=b4+b5+sigR7+M7+tails),
  0 stragglers. NO D-class dips. Next tier @78773 sig 0d235701.

## geometry agrees on all 3 legs
