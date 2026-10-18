# NOTE-sweep2-r19-hb4 (GATE-b192 filed, b194 claimed)

- GATE-bd1ca6d PASS-functional filed:
  RGRAM py 8280/8280, PYID 4140/4140,
  C-batt 8280/8280 cmp-equal, own-loop
  92/92 pins 26/26, added 4/4 EQ,
  audits 167+844+11+263+1041 all 0
  mism, inherit-vs-b190 IDENTICAL
  (HYG/CONTAM/LIBCOMP), OUTER2 clean
  284/284 first try, wall 0.
- Cport poll: b194 676626e T10P139
  (n<=65200, 860 tiers) cut 15:13.
  CLAIM-sweep2-676626e filed,
  backstop clear; b193 odd untouched.
- Wall b194: a36744a..676626e =
  rgramc.c only +1523/-1075, wall 0.
- sweep2-band.sh 676626e 65109 65200
  running.
