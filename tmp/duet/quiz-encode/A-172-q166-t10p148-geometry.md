# A-172 (Q-166): T10P148 P-head geometry — DERIVED

Bed: census N=68241..68332 own bed (.rav[12:-4]).
First-hand; P147-M tails from own P147 census
row0 67921..67936 (this seat).

## 1. shape: CONFIRM (mixed PBB + alternating quad)
- 68241 100B/84B sig 03000000; 68242 100B/84B
  fat sig ca040000 NEW; PBA 68243..68258 sig
  a0480000 NEW; SINGLETON 68259 sig 6f030000
  NEW.
- PBB9 68260..68268 MIXED b0 per-N exact =
  6a,69,6a,6a,6a,69,6a,69,6a (b1..3 const
  030000; 4th mixed-sig PBB, irregular).
- QUAD 68269..68332 per-row sigs: rows0,2
  92360000, rows1,3 91360000 (both NEW, 3rd
  multi-sig quad, 1st alternating), 64/64.
- 92x100B exact. PBA VPOS [4,6,7,9,76-79]
  exact (b5 const 0x15); PBB VPOS [0,4,6,7,
  8,9,10,11,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 7B pos[13,14,15,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 distinct triples each row).
- R-band 7B row-only: rows0==2 exact
  92feb7de53a10d AND rows1==3 exact
  910ebf3eb1a2ec (1st alternating pairing).
- b1,2,3 const 0x36,0x00,0x00. Tails
  c6eef767/5d35ea0c/61eff767/f835ea0c
  (rows0,2 + rows1,3 differ b0 only).
- M-novelty vs P147M: ALL NEW (0/16 tails;
  7B vs 8B layout). PBA M 7B 16/16; PBB M
  11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x15 whole tier (no step).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 12 = b4+11tab; quad 19 = b4+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 68333 (sig 42690300).

## geometry agrees on all 3 legs
