# A-115 (Q-109): T10R117 R-zone geometry — DERIVED

Bed: census N=58241..58496 own bed (.rav[12:-4]).
First-hand; P119-M re-derived 58177 row0 (A-114
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig b1010000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[11,19,26,27,76,77,78,79]
  q-indep 256/256 (16 m per q), 16/16
  distinct, ALL NEW.
- q-tab 7B EXACTLY pos[20,21,22,72,73,74,75]
  m-indep 256/256 (16 q per m), 16/16
  distinct. 0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (59th, q-carried)
- R117-q[i] == P119-M[i] full 7B all 16,
  zero breaks (q by row, M by col).
  Heads b20,21,22 IN PLACE; tails relocated
  76..79 -> 72..75.
- NOT arithmetic, NOT novel (byte-diffs all 0).
- m-tails 0/16 vs P119-M tails.
- Carry sequence now: ... R116 q, R117 q.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x03+2off)&FF 256/256; b5=0xc7+(off>=127)+
  (off>=255) 256/256 (dbl-carry incl LAST-cell
  step). Edges 58367->58368 ff/c7->01/c8,
  58495->58496 ff/c8->01/c9 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
