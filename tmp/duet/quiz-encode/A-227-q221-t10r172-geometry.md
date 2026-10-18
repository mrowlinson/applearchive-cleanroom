# A-227 (Q-221): T10R172 R-zone geometry — DERIVED

Bed: census N=77381..77636 own bed (.rav[12:-
4]). First-hand; P174-M from own P174 census
row0 77317..77332 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig bbeda000. NO
  head singletons.
- m-tab 8B EXACTLY pos[6,7,8,9,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails 0/16 + m-heads 0/16 vs P174M;
  m-tails IN PLACE).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,
  75] m-indep 256/256, 16/16 distinct. 0
  violations.

## 2. verbatim reuse: CONFIRM 16/16 positional
- R172-q[i] == P174-M[i] full 8B all 16, zero
  breaks (heads b48-51 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x8b+2off)&FF 256/256; b5=0x5c+
  (off>=59)+(off>=187) 256/256 (dbl-carry).
- Edges per-N exact: 77439->77440 ff/5c->
  01/5d; 77567->77568 ff/5d->01/5e.
- Varpos EXACTLY tabs+{4,5} (18), 66 consts,
  0 stragglers. NO D-class dips.
- Next tier @77637: PB0 a0000000, PB1
  cfa00000, PBA 0f0c0a00.

## geometry agrees on all 3 legs
