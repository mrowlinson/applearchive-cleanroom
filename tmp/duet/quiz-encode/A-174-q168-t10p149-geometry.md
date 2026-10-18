# A-174 (Q-168): T10P149 P-head geometry — DERIVED

Bed: census N=68589..68680 own bed (.rav[12:-4]).
First-hand; P148-M tails from own P148 census
row0 68269..68284 (this seat).

## 1. shape: CONFIRM (triple-paired R-band)
- 68589 100B/84B sig 03000000; 68590 100B/84B
  fat sig 69030000 NEW; PBA 68591..68606 sig
  92360000 NEW; NO extra singleton; PBB10
  68607..68616 sig 68030000 NEW; QUAD
  68617..68680 single sig 8c360000 NEW.
- 92x100B exact. PBA VPOS [4,19,26,27,76-79]
  exact (b5 const 0x17); PBB VPOS [4,5,11,18,
  19,25,26,27,28,29,30,80-83] exact (15B, b5
  0x17->0x18 step @68608 per-N: 68607=17,
  68608..68616=18).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, full 16/16 distinct each row
  (heads b32,33,34 16/16 distinct triples
  each row, 3rd full-heads).
- R-band 8B row-only: rows1==2==3 exact
  ec26678437f28512 (1st triple pairing);
  row0 f4ff0791ef727314, 64/64.
- Tails b80..83 row-const 4ce9cff6/3ba7ae30/
  88a7ae30/d5a7ae30 (rows1,2,3 share a7ae30,
  differ b0).
- M-novelty vs P148M: ALL NEW (0/16 tails;
  7B vs 7B layout). PBA M 7B 16/16; PBB M
  13B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x17 PBA; 0x17->0x18 step @68608
  (PBB); const 0x18 quad.
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 15 = b4+b5+13tab; quad 20 = b4+R8+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 68681 (sig c1240300).

## geometry agrees on all 3 legs
