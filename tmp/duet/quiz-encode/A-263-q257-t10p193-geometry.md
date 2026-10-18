# A-263 (Q-257): T10P193 P-head geometry — DERIVED

Bed: census N=83901..84248 own bed (.rav[12:-4]). First-hand; P192-T tails from own
P192 census (M-by-col tails 83645..83660, this seat).

## 1. shape: CONFIRM
- 83901..84248 = 348/348 100B/84B exact: PB0 83901 sig 20030000 (REPEAT of
  P192 PB0 PREDICTED-exact); PB1 83902 sig 47a20700.
- PBA 83903..83918 sig 47a26700 (VPOS [4,48,49,50,51,76,77,78,79] = b4+M8
  EXACT, b5 const 0x8f single-tier; heads FULL 16/16 quads).
- PBB2 83919..83920 sig 47a20700 (== PB1; VPOS b4+M11 b23,46-51,80-83 EXACT;
  2-diverge: 2/2 distinct bodies).
- SING 83921 sig 1b330300 NEW; SING 83922 sig 47a20700 (== PB1).
- PBC6 83923..83928 sig 1b330300 (== 83921; VPOS b4+M12 b35,45-51,80-83 EXACT;
  6-diverge 6/6; 83921 NOT member CONFIRM).
- QUAD 83929..83992 single sig b1313300 NEW (VPOS 20 EXACT); T-RING 83993..
  84248 256x single sig 101b3303 NEW (VPOS 14 EXACT).
- Next @84249: PB0 sig 48030000 NEW, PB1 84250 20900600 NEW, PBA 84251..84252
  sig 0a026900 NEW (probed 2 cells, both match).

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,76-79: row-indep 16/16 x4, shared 16/16; heads b6,7 FULL 16/16
  pairs (CLASSIC-heads return).
- R8 b35,45-51: all 4 distinct, no pairing (row0 91aeca2b71fce733; row1
  b1aedd4971e9ffbd; row2 c12e3e68b16cd7ca; row3 812e092bf1c1afa1).
- Tails 4/4 distinct (63c302fe/c2c12b4d/ac2b5d19/c35f9f83), 14/16 bytes.
- M-tails ALL NEW vs P192T (0/16).
- T-ring TRANSPOSED (3rd) CONFIRM: M6 b13,14,76-79 by COL off&15 16/16; Q6
  b6,7,72-75 by ROW off>>4 16/16.

## 3. counters + dips: CONFIRM + 1 CORRECTION, NONE
- Odd-lencode all 83901..83992: 92/92 exact.
- T-ring b4=(0x33+2off)&FF 256/256; b5=0x90+(off>=103)+(off>=231) 256/256;
  edges 84095->84096 ff/90->01/91 + 84223->84224 ff/91->01/92.
- CORRECTION: consts are 75/72/71/64/70, not 74/72/71/64/70 — PBA VPOS is 9
  (b4+M8, b5 const 0x8f) so 84-9=75. Third instance of this exact slip
  (P192-PBA 75 + heads 16/16 in A-262, now P193-PBA 75): writer's consts
  formula drops one on PBA blocks — check 84-VPOS arithmetic there.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all legs modulo PBA consts (75 not 74)
