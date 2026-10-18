# A-246 (Q-240): T10P184 P-head geometry — DERIVED

Bed: census N=80769..80860 own bed (.rav[12:-4]). First-hand; P183-M from own P183
census row0 80449..80464 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 d0020000 (NEW PB0 sig); PB1 fat 9f340400 NEW.
- PBA 80771..80786 single sig 9f345800 NEW; SING 80787 sig 9f340400
  (SING-echoes-PB1, sig only — 2nd CONFIRM).
- MID9 80788..80796 all-sig-mixed, per-N sigs EXACTLY b38e0200,a71b0200,
  73360200,c3ee0200,73360200,c3ee0200,a71b0200,8baf0200,a71b0200 (no
  singleton/PBB split — new variant CONFIRM).
- QUAD 80797..80860 single sig 9f342c00 NEW.
- PBA VPOS [4,32,33,34,35,76,77,78,79] EXACT (8B M, b5 const 0x77);
  MID VPOS [0,1,4,30,31,36,37,38,80,81,82,83] EXACT (11B M incl sig b0,b1;
  b5 const 0x77).

## 2. quad rows: CONFIRM
- M 6B pos[36,37,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 16/16 pairs each row — full), shared all 4 rows 16/16.
- R 7B b22,23,30-34 row-only, all 4 rows distinct (no pairing): row0
  ac636fbf93315a; row1 fc6cf0fc339748; row2 e26b1dfcb31e54; row3
  fc6cf1fc339748, 64/64. rows1,3 differ ONLY b30 (f0/f1, diffidx [2]).
- tails b80..83 row-const 42e3ba25/80cdb485/d619af7d/b65ed108 (4/4 distinct,
  16/16 bytes distinct — no byte sharing).
- M-novelty vs P183M tails: ALL NEW (0/16). PBA M 8B 16/16 (heads 16/16
  quads — full); MID M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x77 whole tier (single tier [0x77], no step anywhere).
- varpos partitioned exact (PBA 9=b4+8tab; MID 12=b4+11tab; quad 18=
  b4+R7+M6+tails), 0 stragglers. NO D-class dips. Next tier @80861 sig
  9f34d402 (80861+80862 both).

## geometry agrees on all 3 legs
