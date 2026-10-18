# A-106 (Q-100): T10P115 P-head geometry — DERIVED

Bed: census N=56757..56848 own bed (.rav[12:-4]).
First-hand; P114-M own bed present (A-104).

## 1. shape: CONFIRM (PBB8 + 2 fat singletons real)
- PB0 56757 96B sig 00bf9e01 NEW; PB1 56758 100B
  fat 01000000 (7th); PBA 56759..56774 (16, 100B/84B
  sig 18000000 NEW); SINGLETONS 56775,56776 (2,
  100B/84B sig 01000000); PBB 56777..56784 (8 ONLY,
  96B/80B sig d67947c7); QUAD 56785..56848 (64=4x16,
  ALL 100B/84B, SINGLE sig 0c000000 =P114-quad, 7th
  consec). 9x96B + 83x100B. PBB 10->9->8, sing
  0->1->2 CONFIRM.
- PBA VPOS [4,38,39,76-79] EXACT; PBB8 VPOS
  [4,25,26,27,33,34,35,36,37,76-79] EXACT;
  SING-pair VPOS [4,30,31,37,38,39,40,41,42,80-83]
  EXACT (pair-distinct 2/2).

## 2. quad rows: CONFIRM + M-novelty ANSWERED
- M 7B pos[44,45,46,76,77,78,79] row-indep 16/16
  x4, 16/16 distinct x4.
- row-bytes b29,30,31,37,38,39,40,41 EXACT as
  writer: 966d5edb8af62cec / 966d5e1b8bf62cec /
  56be5f9b6ef68cf5 / 160d53dbd1960ce3.
- tails b80..83 row-const 6744d92d/428715e5/
  08d9864a/79a74376 all distinct.
- PBA M 6B pos[38,39,76-79] 16/16; PBB8 M 12B
  pos[25,26,27,33,34,35,36,37,76-79] 8/8.
- M-novelty vs P114-M: ALL NEW first-hand (0/16
  tails, 0/16 heads in P114-M set).

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF 92/92 whole tier;
  tier b4 base 0x6b, b5 0xbb->0xbc at 56832
  (56831 255/187 -> 56832 1/188, quad row2).
- quad b4=(0xa3+2off) 64/64 1 wrap.
- consts PBA 77 / PBB8 67 / quad 63 EXACT, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
