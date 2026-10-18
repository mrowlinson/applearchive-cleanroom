# A-220 (Q-214): T10P171 P-head geometry — DERIVED

Bed: census N=76245..76336 own bed (.rav[12:-4]).
First-hand; P170-M tails from own P170 census
row0 75925..75940 (this seat).

## 1. shape: CONFIRM (repeat PB0 + near-PBB singleton)
- 76245 100B/84B sig 25000000 (PB0; REPEAT
  of P170 PB0 sig, 1st repeat PB0); 76246
  100B/84B fat sig 504d0000 NEW; PBA
  76247..76262 sig 1c1d0400 NEW.
- SINGLETON 76263 sig 56a40000 NEW (shares
  b0=0x56 with PBB sig 56640000, differs b1;
  1st near-PBB singleton, per-N exact).
- PBB9 76264..76272 sig 56640000 NEW uniform;
  QUAD 76273..76336 single sig 1c1d0600 NEW.
- 92x100B exact. PBA VPOS [4,38,39,76-79]
  exact (6B M, b5 const 0x53); PBB VPOS
  [4,32,33,37-42,80-83] exact (12B M, b5
  const 0x53).

## 2. quad rows: CONFIRM
- M 9B pos[23,34,35,42,43,76,77,78,79] with
  b42=A[m]^B[q] B42X=(00,01,00,06) 64/64
  zero viol (3rd XOR-split); other 8B
  row-indep 16/16 x4, 16/16 distinct each
  row (heads 12/16 quads each row), shared
  all 4 rows 16/16 x3.
- R-band 7B b32,33,37,38,39,40,41 row-only:
  rows0==2 exact 2bdb30d06a8f49 (5th 0==2
  pairing); row1 8bab40d48e0f4e; row3
  ab5900e572efb2, 64/64.
- Tails b80..83 row-const ALL distinct
  673a7c2f/712d20cd/d8329733/f1f8734d.
- M-novelty vs P170M tails: ALL NEW (0/16).
  PBA M 6B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 step inside Q0 @76288 (76287=53,
  76288=54; last cell of row0; via lencode).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 13 = b4+12tab; quad 22 = b4+b5+M9+R7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @76337 sig 1c1d4a00.

## geometry agrees on all 3 legs
