# A-250 (Q-244): T10P186 P-head geometry — DERIVED

Bed: census N=81465..81556 own bed (.rav[12:-4]). First-hand; P185-M from own P185
census row0 81145..81160 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 f6020000 (NEW PB0 sig); PB1 fat 04f60200 NEW.
- PBA 81467..81482 single sig 4d602f00 NEW; SING 81483 sig 7d940500 NEW.
- PBB9 81484..81492 sig 04f60200 (== PB1 sig, PBB-echoes-PB1 returns).
- QUAD 81493..81556 MULTI-SIG: row0 f51a2d00, rows1-3 e76d2e00 (per-row
  singletons, 16/16 each row).
- PBA VPOS [4,20,21,22,76,77,78,79] EXACT (7B M, b5 const 0x7c);
  PBB VPOS [4,20,21,22,23,24,25,26,80,81,82,83] EXACT (11B M, b5 const 0x7c).

## 2. quad rows: CONFIRM
- M 8B pos[20,21,26,27,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each
  row (heads 15/16 quads each row), shared all 4 rows 16/16.
- sigR 7B b0,1,2,11,19,24,25 row-only, 64/64: rows1==2==3 exact e76d2e76854d42
  (triple); row0 f51a2d66eea14c.
- tails b80..83 row-const b0c9d426/084a8299/6e98ca9a/07d1ca9a (rows2,3 share
  b2..b3 ca9a, differ b0..b1 6e98/07d1).
- M-novelty vs P185M tails: ALL NEW (0/16). PBA M 7B 16/16 (heads 15/16
  triples); PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x7c,0x7d} via lencode (Q2-internal step @81536: 81535 ff/7c->
  81536 01/7d).
- varpos partitioned exact (PBA 8=b4+7tab; PBB 12=b4+11tab; quad 21=
  b4+b5+sigR7+M8+tails), 0 stragglers. NO D-class dips. Next tier @81557 sig
  f51af502 (81557+81558 both).

## geometry agrees on all 3 legs
