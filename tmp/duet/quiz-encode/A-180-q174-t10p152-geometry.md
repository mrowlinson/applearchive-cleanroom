# A-180 (Q-174): T10P152 P-head geometry — DERIVED

Bed: census N=69633..69724 own bed (.rav[12:-4]).
First-hand; P151-M tails from own P151 census
row0 69313..69328 (this seat).

## 1. shape: CONFIRM (3-sig multi-sig quad)
- 69633 100B/84B sig 03000000; 69634 100B/84B
  fat sig de060000 NEW; PBA 69635..69650 sig
  e26d0000 NEW; SINGLETON 69651 sig de060000
  (=PB1, per-N exact); PBB9 69652..69660 sig
  6f030000 NEW.
- QUAD 69661..69724 per-row sigs: rows0,2
  5c370000, row1 873c0000, row3 863d0000
  (all NEW, 4th multi-sig quad, 1st 3-sig),
  64/64.
- 92x100B exact. PBA VPOS [4,32,33,34,76-79]
  exact (b5 const 0x20); PBB VPOS [4,32,33,
  34,35,36,37,38,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 7B pos[32,38,39,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  b32,38,39 14/16 distinct triples each row).
- R-band 8B row-only: rows0==2 exact
  5c37fdca26fe7ef5; row1 873c7dca12fe15d4;
  row3 863d7d4acddf90e4, 64/64.
- b2,3 const 0x00. Tails b80..83 row-const
  ALL distinct 8620138e/fae80b0f/1c21138e/
  df109348.
- M-novelty vs P151M: ALL NEW (0/16 tails;
  7B vs 6B layout). PBA M 7B 16/16; PBB M
  11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x20 whole tier (no step).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 12 = b4+11tab; quad 20 = b4+R8+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 69725 (sig 2dbd0300).

## geometry agrees on all 3 legs
