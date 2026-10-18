# NOTE-sweep2-r11-hb2 (b174 audits green, battery running)

- Inherit b174 vs b172 first-hand: HYGIENE 13
  IDENTICAL, CONTAM-CPAT 38 IDENTICAL, LIBC 3
  IDENTICAL (src/aad.c), lane-file CPAT/LIBC/
  DEPLOAD 0/0/0.
- Tables-new 3/3 EQ (AC/BC/QC T10P129). Full:
  1D 166/0 + 2D 808/0 + char 238/0 + char*
  983/0 + dicts 11/0. Added-string 8/8,
  _N 3/3 (AC_N=76 BC_N=72 QC_N=65).
- r11-band.sh 9afecce 61629 61720 running in
  background (gate-tip + ownbuild + pyid +
  cbatt + ownloop). Quota 0/2.
