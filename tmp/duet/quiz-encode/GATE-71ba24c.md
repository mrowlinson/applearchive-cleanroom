# GATE-71ba24c sweep: PASS (rgram 1852/1852, T9F2Q 3x16+4)

- tip: lanes/encode-writer2 @71ba24c (parent 0ca588b gated PASS). rgram.py
  +43/-0, cells to 14381, pins 1836->1852 (+16/-0).
- code read (ALL): _T9F2QT 16 tabs + _T9F2Q5 16 b5-vals + _T9F2QB 4
  block-words + _T9F2QC consts (53 keys, unique; tab/block bytes excluded)
  + branch n<=14381 (off=n-14330, m=off&15, q=off>>4): m<=15 (16 tabs),
  q<=3 (3x16+4 = 52 rows), b5=Q5[m]+(q>=1&m<6), blk=QB[q]/QB[q+1] k15
  carry (m=15&q=3 needs off 63 > max 51, unreachable — safe). contiguous
  after T9F2 (14330 follows 14329), paylen 68. ordering verified.
- NIT (no FAIL, persistent class): message "(1854 pins)" counts 2 csv
  comments; data rows 1852 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-71ba24c-s4): HYGIENE/CONTAM clean,
  RGRAM n=1852, PINS-RGRAM set-eq 1852/1852, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 135/135 (NOTE-092 baseline + 28), ZERO holds.
