# A-270 (Q-264): T10P200 P-head geometry — DERIVED

Bed: census N=86337..86684 own bed (.rav[12:-4]). First-hand; P199-T tails from own
P199 census (M-by-slot tails 86081..86096, this seat).

## 1. shape: CONFIRM
- 86337..86684 = 348/348 100B/84B exact: PB0 86337 sig 74030000 (as P199-next
  PREDICTED); PB1 86338 sig 51de0500.
- PBA 86339..86354 sig 51de6d00 (VPOS [4,32,33,34,76,77,78,79] = b4+M7 EXACT,
  b5 const).
- PBB2 86355..86356 sig 51de0500 (== PB1; VPOS b4+M10 b22,23,30,36-38,80-83
  EXACT, b5 const).
- 8 SINGLES 86357..86364 sigs EXACTLY 83260300, 97bb0300, 5f950300, 7f7f0300,
  832e0300, 97bb0300 (=86358), 7f7f0300 (=86360), 832e0300 (=86361) ALL NEW.
- QUAD 86365..86428 single sig 51de3500 NEW (VPOS 20 EXACT = b4,b5+R7+M7+
  tails; b5 carry @off35: 86399 ff/a2 -> 86400 01/a3, tiers {0xa2,0xa3}).
- T-RING 86429..86684 256x single sig 51de9103 NEW (VPOS 15 EXACT).
- Next @86685: PB0 sig 74030000 (REPEAT of own PB0!), PB1 86686 sig 51de0500
  (repeat!), PBA 86687..86688 sig 51de6d00 (repeat!, probed 2 cells).

## 2. sharers + quad + T-ring: CONFIRM
- Sig-sharer diffs EXACT: 86358/62 5B [4,80,81,82,83]; 86360/63 4B [4,80,81,
  82]; 86361/64 3B [4,80,81].
- Quad M7 b36-38,76-79: row-indep 16/16 x4, shared 16/16 (heads b36,37 15/16).
- R7 b22,23,30-34 (derived from VPOS) BOTTOM-paired r2==r3 a0cbc5fc5362ca
  (3/4 distinct: r0 e5ee53bf13b8dc, r1 e7f285bf33bcc1 — 2nd bottom-pair).
- Tails 4/4 distinct (1d3c14b7/34bcc771/a33264dc/d73264dc), 13/16 bytes.
- M-tails ALL NEW vs P199T (0/16).
- T-ring TRANSPOSED (10th) CONFIRM: M6 b42,43,76-79 by COL off&15 16/16; Q7
  b36-38,72-75 by ROW off>>4 16/16.

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 86337..86428: 92/92 exact.
- T-ring b4=(0x3b+2off)&FF 256/256; b5=0xa3+(off>=99)+(off>=227) 256/256;
  edges 86527->86528 ff/a3->01/a4 + 86655->86656 ff/a4->01/a5; quad b5 carry
  off35 (ff->01) CONFIRM.
- Consts (84-VPOS) ALL 4 EXACT: PBA 76, PBB 73, quad 64, T 69.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
