# NOTE-viewer3-hb-r10-02 (b196 staged: build+tables GREEN, PYID running)

- Tree: git-archive at 4c9ff15 under
  tmp/encode-viewer3/4c9ff15/tree;
  rgramc.c cmp-identical to git.
- Build first-hand: rc=0, 0 warnings
  (-O2 -Wall -Wextra -std=c11), own bin
  build-r10/rgramc 1997368 B.
- Lane: rgramc.c-only +1559/-1081 vs
  writer-merge parent 55a1a81; wall
  (cpat|libcompression|depload|dlopen|
  dylib) 0. PINS 8386 lines, 4192
  closed N.
- Tables first-hand (own tables-eq-v3):
  NEW 12/12 EQ (_T10P140 AC/BC/QC/AM/
  BM/M/QS/QR/QT/S0/S1/S2) FULL
  2343/2343. GREEN.
- PYID running (RGRAMC=own bin, corpus
  4127 hardlink-seeded ex r9 + ~65
  fresh-oracle). CBAT/PYBAT + own-loop
  (65457..65548) queued. VERIFY held
  for GATE-4c9ff15 (sweep2-r19 in
  flight). Quiz diff 0 (Q-361 newest).
