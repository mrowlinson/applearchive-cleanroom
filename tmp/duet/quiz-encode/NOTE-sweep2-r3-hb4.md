# NOTE-sweep2 r3-hb4 (b156 claimed, battery running)

- b156 e53abca CUT (cport T10P120 58497..58588, +12
  tiers +26 pins, claims PYID 3694 + C 7388). Backstop
  clean; CLAIM-sweep2-e53abca filed (2/2 quota).
- Meta: lane-diff rgramc.c only (+1439/-951), wall 0.
- Tables 14/14 EQ first-hand: 2D 3/3 + _N 75/72/68
  C==py + S0/S1/S2 STREQ + AM/BM/M/QR/QT STRARREQ.
  Full: 1D 166/0, 2D 772/0, dicts 11/0, STR 218/0,
  STRARR 924/0.
- Inherit vs b155 c9dd7f8: HYG 13 / CONTAM 43 /
  LIBC 3, all IDENTICAL + lane 0s -> OBSERVED-inherited.
- sweep2-band.sh battery running (gate-tip + ownbuild +
  pyid + cbatt + own-loop 58497..58588).
