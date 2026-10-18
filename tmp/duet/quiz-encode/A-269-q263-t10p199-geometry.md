# A-269 (Q-263): T10P199 P-head geometry — DERIVED

Bed: census N=85989..86336 own bed (.rav[12:-4]). First-hand; P198-T tails from own
P198 census (M-by-col tails 85733..85748, this seat).

## 1. shape: CONFIRM
- 85989..86336 = 348/348 100B/84B exact: PB0 85989 sig 72030000 (REPEAT of
  P198 PB0 PREDICTED-exact); PB1 85990 sig c7e90600.
- PBA 85991..86006 sig 749c6e00 NEW (VPOS [4,9,10,11,76,77,78,79] = b4+M7
  EXACT, b5 const).
- PBB2 86007..86008 sig c7e90600 (== PB1; VPOS b4+M10 b13,15-19,80-83 EXACT —
  b14 SKIPPED CONFIRM, b5 const).
- PBC8 86009..86016 sig e3740300 NEW (VPOS b4,b5+M11 b13-19,80-83 EXACT; b5
  CARRY 9f->a0 @86016 last cell: 86015 ff/9f -> 86016 01/a0).
- QUAD 86017..86080 single sig 3e4e3700 NEW (VPOS 18 EXACT = b4+R6+M7+tails,
  b5 const 0xa0, b16 const gap in R-band CONFIRM).
- MOTIF-RING 86081..86336 256x sigs {97127403, 98127403, d3127403} ALL NEW,
  per-slot assignment (2+6+8)x16 EXACT (slots 0-1 / 2-7 / 8-15); motif sigs
  16/16 repeats exact; sig b1..3 const 127403 all 3 sigs (b0-only variation
  97/98/d3).
- Next @86337: PB0 sig 74030000 NEW (BREAKS 72030000 chain!), PB1 86338
  51de0500 NEW, PBA 86339..86340 sig 51de6d00 NEW (probed 2 cells).

## 2. quad + motif: CONFIRM
- Quad M7 b20-22,76-79: row-indep 16/16 x4, shared 16/16 (heads b20,21 15/16).
- R6 b13-15,17-19 BOTTOM-paired r2==r3 a3bce6fb896b (3/4 distinct: r0
  b2bce636d76f, r1 bafc87608e67 — first bottom-pair CONFIRM).
- Tails 4/4 distinct (c1bdf941/2bbc5b06/f67cea6a/2a7dea6a), 14/16 bytes.
- M-tails ALL NEW vs P198T (0/16).
- MOTIF-ring TRANSPOSED (9th) CONFIRM: slot-tab 9B b0,11,19,26,27,76-79 by
  SLOT off&15 16/16; Q7 b20-22,72-75 by REPEAT off>>4 16/16; all 3 block-types
  16/16 distinct Q across repeats (A/B/C each 16/16).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 85989..86080: 92/92 exact.
- Motif b4=(0x83+2off)&FF 256/256; b5=0xa0+(off>=63)+(off>=191) 256/256;
  edges 86143->86144 ff/a0->01/a1 + 86271->86272 ff/a1->01/a2 (post-edge cells
  slot15 rep3/rep11, both inside C8 blocks — the 2 b5-carry C8 instances).
- Consts (84-VPOS) ALL 5 EXACT: PBA 76, PBB 73, PBC 71, quad 66 (b5-in),
  motif 66.
- varpos partitioned exact throughout (motif 18 = slot9+Q7+b4+b5 EXACT), 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
