# A-205 (Q-199): T10R161 R-zone geometry — DERIVED

Bed: census N=73553..73808 own bed (.rav[12:-4]).
First-hand; P163-M from own P163 census rows
73489..73552 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 73000800 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[44,45,50,51,72,73,74,
  75] q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[34,42,43,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (103rd)
- R161-q[i] == P163-M[i] full 7B all 16,
  zero breaks, IN PLACE heads+tails
  (q-carried) — matches P163 rows0,1,2
  exactly 16/16 x3; vs row3 0/16 full
  (b42 row3-flip), tails 16/16.
- m-tails 0/16 vs P163-M (16/16 distinct):
  CONFIRM under m-tab-tail reading (m-tab
  tail part 72..75; same note as A-186).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xa3+2off)&FF 256/256; b5=0x3e+
  (off>=47)+(off>=175) 256/256 (dbl-carry).
  Edges 73599->73600 ff/3e->01/3f, 73727->
  73728 ff/3f->01/40 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
