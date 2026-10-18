# A-204 (Q-198): T10P163 P-head geometry — DERIVED

Bed: census N=73461..73552 own bed (.rav[12:-4]).
First-hand; P162-M tails from own P162 census
row0 73141..73156 (this seat).

## 1. shape: CONFIRM (double + PBA-internal step)
- 73461 100B/84B sig 08000000 (PB0); 73462
  100B/84B fat sig 56100000 NEW; PBA
  73463..73478 sig 73000100 NEW.
- DOUBLE singletons 73479 sig 33160000 NEW +
  73480 sig 2f040000 NEW (3rd double, per-N
  exact); PBB8 73481..73488 sig 5e080000
  NEW; QUAD 73489..73552 single sig 33860000
  NEW.
- 92x100B exact. PBA VPOS [4,5,38,39,76-79]
  exact (b5 step INSIDE PBA @73472 per-N:
  73463..73471=3d, 73472..73478=3e); PBB
  VPOS [4,29-31,37-42,80-83] exact (13B M).

## 2. quad rows: CONFIRM
- M 7B pos[34,42,43,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 triples each row); b42 = A[m] XOR
  B[q] with B=(00,00,00,01) exact 64/64 zero
  viol (rows0,1,2 same 16/16; row3 flipped;
  2nd XOR-split, 1st row3-only-XOR; rest of
  M shared all rows 16/16 x3).
- R-band 7B b32,33,37-41 row-only: rows0==1
  exact 0aee8f7de30f1e (4th 0==1 pairing);
  row2 8a90a375c78f5f; row3 2a9ff770a3efa0,
  64/64.
- Tails b80..83 row-const bdb69ccd/01b79ccd/
  533b620e/b6394a6a (rows0,1 share b79ccd,
  differ b0).
- M-novelty vs P162M tails: ALL NEW (0/16).
  PBA M 6B 16/16; PBB M 13B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5: 0x3d->0x3e step @73472 (PBA); const
  0x3e rest incl whole quad.
- Varpos partitioned exact (PBA 8 = b4+b5+
  6tab; PBB 14 = b4+13tab; quad 19 = b4+R7+
  M7+tails), 0 stragglers. NO D-class dips.
- Next tier @73553 sig 73000800.

## geometry agrees on all 3 legs
