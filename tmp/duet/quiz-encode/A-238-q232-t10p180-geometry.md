# A-238 (Q-232): T10P180 P-head geometry — DERIVED

Bed: census N=79377..79468 own bed (.rav[12:-4]). First-hand; P179-M from own P179 census
row0 79057..79072 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 54010000 (REPEAT x3 of P178/P179 PB0); PB1 fat 2f630200 NEW;
  PBA 79379..79394 single sig fb322600 NEW; SING 79395 sig 6cce0200 NEW.
- MID9 79396..79404 per-N exact: 35670100,36670100,36670100,35670100,37670100,
  34670100,36670100,35670100,36670100 (no singleton/PBB split).
- QUAD 79405..79468 MULTI-SIG: rows0==2 46731600, row1 45731600, row3 44731600.
- PBA VPOS [4,6,7,8,76,77,78,79] (7B M, b5 const 0x6c); MID VPOS [0,4,6,7,8,9,10,11,
  80,81,82,83] (11B M incl sig b0; b5 const 0x6c).

## 2. quad rows: CONFIRM
- M 5B pos[13,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 14/16 each row), shared all 4 rows 16/16.
- sigR 7B b0,6,7,8,9,10,11 row-only, all 4 rows distinct (no pairing): row0 464ab49f6df20c;
  row1 45f0bf3fd9ddae; row2 46f8b2ff1a466e; row3 440ebc1f8acefb, 64/64.
- tails b80..83 row-const 5f332244/0c6ed715/9aae8d7d/f97b1cab (4/4 distinct, 16/16 bytes
  distinct — no byte sharing).
- M-novelty vs P179M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 16/16 triples — full);
  MID M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x6c whole tier (no step anywhere).
- varpos partitioned exact (PBA 8=b4+7tab; MID 12=b4+11tab; quad 17=b4+R7+M5+tails),
  0 stragglers. NO D-class dips. Next tier @79469 sig 57346701.

## geometry agrees on all 3 legs
