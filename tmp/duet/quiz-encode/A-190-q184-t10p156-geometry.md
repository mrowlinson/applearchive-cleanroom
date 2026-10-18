# A-190 (Q-184): T10P156 P-head geometry — DERIVED

Bed: census N=71025..71116 own bed (.rav[12:-4]).
First-hand; P155-M tails from own P155 census
row0 70705..70720 (this seat).

## 1. shape: CONFIRM (new PB0 sig + double + PBA step)
- 71025 100B/84B sig 07000000 PB0 (NEW PB0
  sig); 71026 100B/84B fat sig 360b0000 NEW;
  PBA 71027..71042 sig 65b30000 NEW.
- DOUBLE singletons 71043 sig b50f0000 NEW +
  71044 sig db070000 NEW (2nd double, per-N
  exact); PBB8 71045..71052 sig dc070000 NEW;
  QUAD 71053..71116 single sig b47d0000 NEW.
- 92x100B exact. PBA VPOS [4,5,6,7,9,76-79]
  exact (b5 step INSIDE PBA @71040 per-N:
  71027..71039=2a, 71040..71042=2b); PBB
  VPOS [4,6-11,80-83] exact (b5 const 0x2b).

## 2. quad rows: CONFIRM
- M 7B pos[13,14,15,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 each row), shared all 4 rows 16/16
  positional.
- R-band 6B b6-11 row-only: rows0==1==2 exact
  20b35e6d996b (1st TRIPLE 0,1,2); row3
  f6b13e8a0a40, 64/64.
- Tails b80..83 row-const 107b051c/587b051c/
  a07b051c/d0781ec4 (rows0,1,2 share 7b051c,
  differ b0).
- M-novelty vs P155M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 10B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5: 0x2a->0x2b step @71040 (PBA); const
  0x2b rest incl whole quad.
- Varpos partitioned exact (PBA 9 = b4+b5+
  7tab; PBB 11 = b4+10tab; quad 18 = b4+R6+
  M7+tails), 0 stragglers. NO D-class dips.
- Next tier @71117 sig 6cdb0700.

## geometry agrees on all 3 legs
