# A-116 (Q-110): T10P120 P-head geometry — DERIVED

Bed: census N=58497..58588 own bed (.rav[12:-4]).
First-hand; P119-M re-derived 58177 row0 (this
seat, 58177..58192 in bed).

## 1. shape: CONFIRM
- PB0 58497 96B/80B sig a8f8f002 NEW; PB1 58498
  100B/84B fat sig 03000000; PBA 58499..58514
  (16, 100B/84B sig 36000000 NEW); SINGLETON
  58515 100B/84B sig 03000000 (=PB1); PBB
  58516..58524 (9, 100B/84B sig 01000000, 3rd
  100B PBB); QUAD 58525..58588 (64=4x16, ALL
  100B/84B, SINGLE sig 1b000000 =P118-quad-sig).
- 1x96B + 91x100B exact. PBA VPOS
  [4,32,33,34,35,76-79] exact (b5 const 0xc9);
  PBB VPOS [4,32,33,34,35,36,37,38,80-83]
  exact (12B).

## 2. quad rows: CONFIRM (1st 5B M + 1st xor-row)
- M 5B pos[39,76,77,78,79] row-indep 16/16 x4,
  full-tuple 16/16 distinct each row (heads b39
  12/16 distinct).
- b38 xor-row: rows0,1,3 = M38[m] pat
  b9593979..., row2 = ^0x03 16/16, 64/64 exact.
- R-band 5B b32,34,35,36,37 row-only:
  9267c050c9/3857afb039/34df7cd05b/3957afb039
  (rows1,3 differ b32 only). b33 const 0xbf.
- Tails b80..83 row-const 07fb6cd7/a7f94213/
  f1b531d1/6bfb95a8 exact.
- M-novelty vs P119M: ALL NEW (0/16 full, 0/16
  tails; 5B vs 7B layout). PBA M 8B 16/16; PBB
  M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xc9 PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R5+
  xor+M5+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
