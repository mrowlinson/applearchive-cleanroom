# A-222 (Q-216): T10P172 P-head geometry — DERIVED

Bed: census N=76593..76684 own bed (.rav[12:-4]).
First-hand; P171-M tails from own P171 census
row0 76273..76288 (this seat).

## 1. shape: CONFIRM (PB1-echoes-prior-PBB + b0 PBB)
- 76593 100B/84B sig 4b000000 (PB0; NEW PB0
  sig); 76594 100B/84B fat sig 56640000 (==
  P171-PBB sig, 1st PB1-echoes-prior-PBB,
  per-N exact); PBA 76595..76610 sig 6f450600
  NEW; SINGLETON 76611 sig fca00000 NEW.
- PBB9 76612..76620 MIXED b0 per-N exact =
  71,73,71,73,72,72,71,72,72 (b1 const 0x50,
  b2,3 const 0000; 12th mixed-sig PBB, 1st
  b0-varying).
- QUAD 76621..76684 MULTI-SIG (2nd): rows0-2
  52070500, row3 51070500 (differ b0 only),
  both NEW, 64/64.
- 92x100B exact. PBA VPOS [4,6,7,76-79]
  exact (6B M, b5 const 0x56); PBB VPOS
  [0,4,6-11,80-83] exact (11B M incl sig b0,
  b5 const 0x56).

## 2. quad rows: CONFIRM
- M 8B pos[13,14,15,16,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  16/16 quads each row — full), shared all 4
  rows 16/16 positional.
- sig+R 7B b0,6,7,8,9,10,11 row-only:
  rows0==2 exact 5264b83f4c0cad (6th 0==2
  pairing, incl sig); row1 5214b77fe5a317;
  row3 5118b2ff6a488b, 64/64.
- Tails b80..83 row-const 68b2bd91/dcf9700f/
  e6b2bd91/ec36d71b (rows0,2 share b1..3,
  differ b0).
- M-novelty vs P171M tails: ALL NEW (0/16).
  PBA M 6B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 step inside Q3 @76672 (76671=56,
  76672=57; via lencode).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 12 = b4+11tab; quad 21 = b4+b5+sigR7+
  M8+tails), 0 stragglers. NO D-class dips.
- Next tier @76685 sig (bed ends 76684; no
  data — writer to probe).

## geometry agrees on all 3 legs
