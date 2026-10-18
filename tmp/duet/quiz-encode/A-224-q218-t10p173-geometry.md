# A-224 (Q-218): T10P173 P-head geometry — DERIVED

Bed: census N=76941..77032 own bed (.rav[12:-4]).
First-hand; P172-M tails from own P172 census
row0 76621..76636 (this seat).

## 1. shape: CONFIRM (double singletons + PBB8)
- 76941 100B/84B sig 50000000 (PB0; NEW PB0
  sig); 76942 100B/84B fat sig eaa00000 NEW;
  PBA 76943..76958 sig ad2a0b00 NEW.
- SINGLETON-1 76959 sig e7a00000 NEW;
  SINGLETON-2 76960 sig 39280000 NEW (2nd
  extra singleton; PBB shrinks to PBB8,
  per-N exact).
- PBB8 76961..76968 sig 73500000 NEW uniform;
  QUAD 76969..77032 single sig db0e0400 NEW.
- 92x100B exact. PBA VPOS [4,20,26,27,76-79]
  exact (7B M, b5 const 0x59); PBB VPOS
  [4,11,18,19,25-30,80-83] exact (13B M, b5
  const 0x59).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 triples each row), shared all 4 rows
  16/16 positional.
- R-band 7B b21,25,26,27,28,29,30 row-only:
  rows0==2 exact 0c13fc0653340f; row1
  1c9fbca433e60a; row3 12f73c27d3af02, 64/64.
- Tails b80..83 row-const 41331dc5/796b9601/
  be331dc5/0175b603 (rows0,2 share b1..3,
  differ b0).
- M-novelty vs P172M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 13B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x59 whole tier (no step anywhere).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 14 = b4+13tab; quad 19 = b4+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @77033 sig db0e4400.

## geometry agrees on all 3 legs
