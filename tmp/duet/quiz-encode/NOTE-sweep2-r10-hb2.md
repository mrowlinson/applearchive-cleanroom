# NOTE-sweep2-r10-hb2 (b170 audits green, battery running)

- Inherit b170 vs b168: HYGIENE 13 IDENTICAL,
  CONTAM 43 IDENTICAL, LIBC 3 IDENTICAL
  (src/aad.c), lane-file CPAT/LIBC/DEPLOAD 0.
- Tables-new 3/3 EQ (AC/BC/QC T10P127).
  Full: 1D 166/0 + 2D 800/0 + char 233/0 +
  char* 968/0 + dicts 11/0. Added-string 7/7,
  _N 3/3 (AC_N=76 BC_N=70 QC_N=65).
- gate-tip + ownbuild + pyid + cbatt +
  ownloop running in background (r10-267690f).
