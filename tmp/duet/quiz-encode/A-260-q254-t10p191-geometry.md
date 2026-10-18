# A-260 (Q-254): T10P191 P-head geometry — DERIVED

Bed: census N=83205..83296 own bed (.rav[12:-4]). First-hand; P190-M from own P190
census row0 82885..82900 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 1e030000 (REPEAT x3 of P189/P190 PB0 sig); PB1
  fat 6a410600 NEW.
- PBA 83207..83222 single sig d2166400 NEW; SING 83223 sig 6d410600 NEW
  (shares b1..3 410600 with PB1, differs b0 6d/6a).
- PBB9 83224..83232 sig b6200300 NEW OWN-SIG; QUAD 83233..83296 single sig
  6e0b3200 NEW.
- PBA VPOS [4,9,10,11,76,77,78,79] EXACT (7B M, b5 const 0x8a);
  PBB VPOS [4,13,14,15,16,17,18,19,80,81,82,83] EXACT (11B M, b5 const 0x8a).

## 2. quad rows: CONFIRM
- M 7B pos[20,21,22,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 16/16 triples each row — full), shared all 4 rows 16/16.
- R 7B b13-19 row-only, all 4 rows distinct (no pairing): row0 15bce27900441a;
  row1 ed7c8699d99b1d; row2 30bc319929e81b; row3 bbfcc2b998ae18, 64/64.
- tails b80..83 row-const a66b22b3/81789fbc/cf2d91d2/8c2cc302 (16/16 bytes
  distinct — true no sharing CONFIRM).
- M-novelty vs P190M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 13/16
  triples); PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x8a whole tier (single tier [0x8a], no step anywhere).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 12=b4+11tab; quad 19=
  b4+R7+M7+tails), 0 stragglers. NO D-class dips. Next tier @83297 sig
  de652003 (83297+83298 both).

## geometry agrees on all 3 legs
