# A-176 (Q-170): T10P150 P-head geometry — DERIVED

Bed: census N=68937..69028 own bed (.rav[12:-4]).
First-hand; P149-M tails from own P149 census
row0 68617..68632 (this seat).

## 1. shape: CONFIRM (fully-mixed PBB9)
- 68937 100B/84B sig 03000000; 68938 100B/84B
  fat sig d5060000 NEW; PBA 68939..68954 sig
  a56d0000 NEW; SINGLETON 68955 sig 63030000
  NEW.
- PBB9 68956..68964 MIXED b0 per-N exact =
  6f,5f,6f,6e,65,50,6e,5f,6f (b1..3 const
  030000; 5th mixed-sig PBB, 5 distinct b0).
- QUAD 68965..69028 single sig a53d0000 NEW.
- 92x100B exact. PBA VPOS [4,44,45,76-79]
  exact (b5 const 0x1a); PBB VPOS [0,4,11,31,
  41,42,43,48,49,80-83] exact (13B).

## 2. quad rows: CONFIRM
- M 7B pos[48,49,50,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 distinct triples each row).
- R-band 8B row-only: rows2==3 exact
  5f6a27e313717d07 (4th 2==3 pairing); row0
  f26a8fe6bf717108; row1 0f69e7e681d18f06.
- Tails b80..83 row-const 6ec91c69/0a195593/
  799ac301/c59ac301 (rows2,3 differ b0 only).
- M-novelty vs P149M: ALL NEW (0/16 tails;
  7B vs 7B layout). PBA M 6B 16/16; PBB M
  12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x1a PBA/PBB; quad 0x1a->0x1b
  step exactly at 68992 (68991=1a, 68992=1b;
  row1 spans the step).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 13 = b4+12tab; quad 21 = b4+b5+R8+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 69029 (sig 53da0300).

## geometry agrees on all 3 legs
