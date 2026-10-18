# A-257 (Q-251): T10R187 R-zone geometry — DERIVED

Bed: census N=82601..82856 own bed (.rav[12:-4]). First-hand; P189-M from own P189
census row0 82537..82552 (this seat).

## 1. two-sig zone: CONFIRM (new R-variant)
- 256/256 100B/84B. sig 614ecf03 for q<8 (82601..82728) / 614ed303 for q>=8
  (82729..82856), per-half singletons 128/128. b2 = 0xcf + 4*(q>=8) 256/256.
  NO head singletons.
- CLASSIC tabs: m-tab 6B EXACTLY pos[37,38,76,77,78,79] q-indep 256/256,
  16/16 distinct, ALL NEW (m-tails 0/16 vs P189M; IN PLACE).
- q-tab 7B EXACTLY pos[21,22,31,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. partial reuse: CONFIRM (R171-style, 129th)
- q-tails == P189-M tails 16/16 POSITIONAL (relocated); q-b31 == P189M-b32
  16/16 positional (relocated 32->31).
- q-b21,22 novel: 0/16 positional vs ALL P189M heads (b32..35 each 0/16),
  0/16 set. 5/7 bytes verbatim, zero breaks.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x53+2off)&FF 256/256; b5=0x85+(off>=87)+(off>=215) 256/256 (dbl-carry).
- Edges 82687->82688 ff/85->01/86, 82815->82816 ff/86->01/87 as writer.
- Half-byte b23 = 0xac q<8 / 0xd2 q>=8, 256/256.
- varpos EXACTLY tabs+{4,5}+sig{2,23} (17), 67 consts, 0 stragglers. NO
  D-class dips.
- Next tier @82857: PB0 1e030000 (repeat of P189 PB0), PB1 614e0700
  (== P189 SING sig, own bed ref), PBA 82859..82860 sig 614e7300.

## geometry agrees on all 3 legs
