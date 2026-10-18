# A-196 (Q-190): T10P159 P-head geometry — DERIVED

Bed: census N=72069..72160 own bed (.rav[12:-4]).
First-hand; P158-M tails from own P158 census
row0 71749..71764 (this seat).

## 1. shape: CONFIRM
- 72069 100B/84B sig 07000000 (PB0); 72070
  100B/84B fat sig 870f0000 NEW; PBA
  72071..72086 sig 07f80000 NEW; SINGLETON
  72087 sig 800f0000 NEW; PBB9 72088..72096
  sig c0070000 NEW; QUAD 72097..72160 single
  sig 047c0000 NEW.
- 92x100B exact. PBA VPOS [4,13,14,15,76-79]
  exact (b5 const 0x33); PBB VPOS [4,13-19,
  80-83] exact (11B M).

## 2. quad rows: CONFIRM
- M 7B pos[20,21,22,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  14/16 each row), shared all 4 rows 16/16
  positional.
- R-band 7B b13-19 row-only: rows1==3 exact
  4fbc41182d62cc (2nd 1==3 pairing); row0
  4afca5b883abcd; row2 bf7ce5d87d04cd, 64/64.
- Tails b80..83 row-const 56604634/410d33ca/
  b34b5d65/ce0d33ca (rows1,3 share 0d33ca,
  differ b0).
- M-novelty vs P158M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x33 WHOLE tier (no step anywhere).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 12 = b4+11tab; quad 19 = b4+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @72161 sig 2cd80700.

## geometry agrees on all 3 legs
