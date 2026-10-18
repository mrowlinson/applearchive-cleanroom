# A-202 (Q-196): T10P162 P-head geometry — DERIVED

Bed: census N=73113..73204 own bed (.rav[12:-4]).
First-hand; P161-M tails from own P161 census
row0 72793..72808 (this seat).

## 1. shape: CONFIRM (new PB0 sig + PB1-echo)
- 73113 100B/84B sig 08000000 PB0 (NEW PB0
  sig); 73114 100B/84B fat sig 81100000 NEW;
  PBA 73115..73130 sig 11080100 NEW.
- SINGLETON 73131 sig 81100000 (== PB1 sig,
  2nd PB1-echo; pay differs PB1 @32B exact).
- PBB9 73132..73140 sig 40080000 NEW; QUAD
  73141..73204 single sig a6850000 NEW.
- 92x100B exact. PBA VPOS [4,20,21,76-79]
  exact (b5 const 0x3b); PBB VPOS [4,20-26,
  80-83] exact (11B M).

## 2. quad rows: CONFIRM
- M 7B pos[19,26,27,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  14/16 triples each row); b26 = A[m] XOR
  B[q] with B=(00,03,01,02) exact 64/64 zero
  viol (1st XOR-split M byte; rest of M
  shared all rows 16/16 x3).
- R-band 6B b20-25 row-only, all 4 distinct:
  c25c7999906f/ac5fd90830d2/ebde37bbb011/
  0cdf026a90a4, 64/64.
- Tails b80..83 row-const ALL distinct
  de7800c1/8ffc19f3/76f4028e/803199a0.
- M-novelty vs P161M tails: ALL NEW (0/16).
  PBA M 6B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x3b WHOLE tier (no step anywhere).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 12 = b4+11tab; quad 18 = b4+R6+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @73205 sig 1c2d0800.

## geometry agrees on all 3 legs
