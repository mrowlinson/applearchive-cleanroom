# A-240 (Q-234): T10P181 P-head geometry — DERIVED

Bed: census N=79725..79816 own bed (.rav[12:-4]). First-hand; P180-M from own P180 census
row0 79405..79420 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 67010000 (NEW PB0 sig, ends 54010000 x3 run); PB1 fat
  68ce0200 NEW; PBA 79727..79742 single sig 2d882d00 NEW.
- SING 79743 sig 274f0400 NEW (b0,b1 == QUAD b0,b1).
- PBB9 79744..79752 sig dfce0200 NEW (shares b1..3 ce0200 with PB1, differs b0).
- QUAD 79753..79816 single sig 274f2c00 NEW.
- PBA VPOS [4,20,26,27,76,77,78,79] (7B M, b5 const 0x6e); PBB VPOS [4,11,18,19,25,26,27,
  28,29,30,80,81,82,83] (13B M, b5 const 0x6f).

## 2. quad rows: CONFIRM
- M 8B pos[32,33,34,35,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 13/16 quads each row), shared all 4 rows 16/16.
- R 8B b20,21,25-30 row-only, all 4 rows distinct (no pairing): row0 899d62f84d736f45;
  row1 298d04f86973963a; row2 a9be2cf8c8f3244b; row3 29b302782b737030, 64/64.
- tails b80..83 row-const a53b4cdd/55fc5396/4afab7aa/46f0cd8e (4/4 distinct, 16/16 bytes
  distinct — no byte sharing).
- M-novelty vs P180M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 13/16 triples);
  PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x6e,0x6f} via lencode (step @79744 PBB start: 79743 ff/6e->79744 01/6f).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 14=b4+13tab; quad 21=b4+R8+M8+tails),
  0 stragglers. NO D-class dips. Next tier @79817 sig 274f4802.

## geometry agrees on all 3 legs
