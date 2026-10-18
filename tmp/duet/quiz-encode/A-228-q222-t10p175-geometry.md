# A-228 (Q-222): T10P175 P-head geometry — DERIVED

Bed: census N=77637..77728 own bed (.rav[12:-
4]). First-hand; P174-M tails from own P174
census row0 77317..77332 (this seat).

## 1. shape: CONFIRM (double singletons)
- 77637 100B/84B sig a0000000 (PB0; NEW PB0
  sig); 77638 100B/84B fat sig cfa00000 NEW;
  PBA 77639..77654 sig 0f0c0a00 NEW.
- SINGLETON-1 77655 sig 81410100 (== PBB sig,
  singleton-echoes-PBB); SINGLETON-2 77656
  sig c0a00000 NEW; PBB8 77657..77664 sig
  81410100 NEW uniform; QUAD 77665..77728
  single sig 10181400 NEW.
- 92x100B exact. PBA VPOS [4,13,14,15,76-79]
  exact (7B M, b5 const 0x5e); PBB VPOS
  [4,13-19,80-83] exact (11B M, b5 const
  0x5e).

## 2. quad rows: CONFIRM
- M 7B pos[20,21,22,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  11/16 triples each row), shared all 4 rows
  16/16.
- R-band 7B b13-19 row-only: rows0==2 exact
  2e3cd1194760c1; row1 a1bc6639a372c2; row3
  adfc75799d56c0, 64/64.
- Tails b80..83 row-const 5c296dca/44026c5b/
  d7296dca/448a57af (rows0,2 share b1..3,
  differ b0).
- M-novelty vs P174M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 11B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 step inside Q1 @77696 (77695 ff/5e ->
  77696 01/5f; via lencode).
- Varpos partitioned exact (PBA 8=b4+7tab;
  PBB 12=b4+11tab; quad 20=b4+b5+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @77729 sig 96904101.

## geometry agrees on all 3 legs
