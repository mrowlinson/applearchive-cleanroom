# A-218 (Q-212): T10P170 P-head geometry — DERIVED

Bed: census N=75897..75988 own bed (.rav[12:-4]).
First-hand; P169-M tails from own P169 census
row0 75577..75592 (this seat).

## 1. shape: CONFIRM (PB1-echo + multi-sig quad)
- 75897 100B/84B sig 25000000 (PB0; NEW PB0
  sig); 75898 100B/84B fat sig ee4b0000 NEW;
  PBA 75899..75914 sig e1be0400 NEW.
- SINGLETON 75915 sig ee4b0000 (== PB1 sig,
  4th PB1-echo).
- PBB9 75916..75924 sig f7250000 NEW uniform.
- QUAD 75925..75988 MULTI-SIG: row0 cca20300,
  row1 e9b10200, row2 cca20300 (== row0 sig),
  row3 4e7f0300, all NEW, 64/64.
- 92x100B exact. PBA VPOS [4,5,20-23,76-79]
  exact (b5 step INSIDE PBA @75904 per-N:
  75899..75903=50, 75904..75914=51); PBB
  VPOS [4,20-26,80-83] exact (11B M, b5
  const 0x51).
- Ordinal notes: "1st PBA-internal" and "1st
  multi-sig" conflict with prior tiers
  (PBA-internal steps @67200/71040/73472;
  multi-sig quads P144/P148/P152/P153/P160);
  geometry itself CONFIRMs — likely means
  1st of this exact pattern.

## 2. quad rows: CONFIRM
- M 6B pos[26,27,76,77,78,79] row-indep 16/16
  x4, 16/16 distinct each row (heads 16/16
  pairs each row — full), shared all 4 rows
  16/16 positional.
- sig+R 7B b0,1,2,18,19,24,25 row-only:
  rows0==2 exact cca2033f5ff19f (4th 0==2
  pairing, incl sig); row1 e9b102dfb12593;
  row3 4e7f035fab1c87, 64/64.
- Row0 vs row2 cells 0/16 identical (tails
  differ). Tails b80..83 row-const ALL
  distinct bae1d43c/98d714cd/b822e73c/d98306fe.
- M-novelty vs P169M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x50,0x51} via lencode
  (PBA-internal step @75904).
- Varpos partitioned exact (PBA 10 = b4+b5+
  8tab; PBB 12 = b4+11tab; quad 18 = b4+
  sigR7+M6+tails), 0 stragglers. NO D-class
  dips.
- Next tier @75989 sig 64df2500.

## geometry agrees on all 3 legs
