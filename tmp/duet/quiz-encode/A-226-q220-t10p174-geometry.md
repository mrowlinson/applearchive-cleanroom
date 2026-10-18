# A-226 (Q-220): T10P174 P-head geometry — DERIVED

Bed: census N=77289..77380 own bed (.rav[12:-
4]). First-hand; P173-M tails from own P173
census row0 76969..76984 (this seat).

## 1. shape: CONFIRM (singleton + PBB9 + multi-sig quad)
- 77289 100B/84B sig 50000000 (PB0; REPEAT of
  P173 PB0 sig); 77290 100B/84B fat sig
  abaa0000 NEW; PBA 77291..77306 sig db0e0800
  NEW.
- SINGLETON 77307 sig abaa0000 (== PB1 sig,
  PB1-echo); PBB9 77308..77316 b1 per-N exact
  6a,aa,6a,aa,aa,aa,aa,aa,aa (b0 const 0xab,
  b2,3 const 0000; b1-varying).
- QUAD 77317..77380 MULTI-SIG: rows0-2
  db0e0a00, row3 db0e0400 (== P173-quad sig),
  per-N exact.
- 92x100B exact. PBA VPOS [4,34,42,43,76-79]
  exact (7B M, b5 const 0x5b); PBB VPOS
  [1,4,5,34,35,41-51,80-83] exact (18B M incl
  sig b1; b5 step INSIDE PBB @77312:
  77308..77311=5b, 77312..77316=5c).

## 2. quad rows: CONFIRM
- M 8B pos[48,49,50,51,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  16/16 quads each row — full), shared all 4
  rows 16/16.
- sig+R 17B b2,23,32-39,41-47 row-only:
  rows0==1==2 exact 0a158b0e96274d5c342e87c3
  43522582bd (triple, incl sig b2); row3
  04952b2e27107468e2a2f7c83f3114fe5e, 64/64.
- Tails b80..83 row-const 05fa51d0/43fa51d0/
  81fa51d0/dd2c988c (rows0,1,2 share b1..3,
  differ b0).
- M-novelty vs P173M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 18B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 tier {0x5b,0x5c} via lencode (PBB-
  internal step @77312).
- Varpos partitioned exact (PBA 8=b4+7tab;
  PBB 20=b4+b5+18tab; quad 30=b4+sigR17+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @77381 sig bbeda000.

## geometry agrees on all 3 legs
