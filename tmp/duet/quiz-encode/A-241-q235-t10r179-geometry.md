# A-241 (Q-235): T10R179 R-zone geometry — DERIVED

Bed: census N=79817..80072 own bed (.rav[12:-4]). First-hand; P181-M from own P181
census row0 79753..79768 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 274f4802 NEW. NO head singletons.
- CLASSIC layout returns: m-tab 6B EXACTLY pos[37,38,76,77,78,79] q-indep
  256/256, 16/16 distinct, ALL NEW (m-tails 0/16 vs P181M; IN PLACE).
- q-tab 8B EXACTLY pos[21,22,23,31,72,73,74,75] m-indep 256/256, 16/16
  distinct (tails RELOCATED 76..79->72..75). 0 violations.

## 2. partial verbatim reuse: CONFIRM structure + CORRECTION (one number)
- q-tails == P181-M tails 16/16 POSITIONAL (relocated); q-b31 == P181M-b32
  16/16 positional (relocated 32->31). CONFIRM.
- CORRECTION: q-b22 set-novelty is 4/16 COLLIDE, not 0/16. q-b22 takes 2
  values {ef x4 (q0,1,2,15), ff x12}; ef IS in the P181M row0 head set
  ([32..35] x16 rows, 17 distinct values incl ef). q-b21 {c0,00} 0/16 and
  q-b23 {35,44,45} 0/16 CONFIRM novel.
- Positional novelty holds everywhere: q-b22 vs P-b32/b33/b34/b35 each 0/16;
  vs 4-row head set still 4/16 (same ef rows). No positional reuse — the
  R171-style 5/8-verbatim structure stands; only the set-novelty count for
  b22 changes (chance collision on a 2-valued byte).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x93+2off)&FF 256/256; b5=0x6f+(off>=55)+(off>=183) 256/256 (dbl-carry).
- Edges 79871->79872 ff/6f->01/70, 79999->80000 ff/70->01/71 as writer.
- varpos EXACTLY tabs+{4,5} (16), 68 consts, 0 stragglers. NO D-class dips.
- Next tier @80073: PB0 ce020000 (NEW PB0 sig), PB1 274f0400 (== P181 SING
  sig), PBA 80075..80076 sig 274f4c00 — all 3 as writer.

## geometry agrees on legs 1+3, leg 2 agrees modulo b22 count (4/16 not 0/16)
