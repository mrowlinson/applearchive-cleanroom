# GATE-66c84ba sweep: PASS (rgram 1936/1936, T9I1 16x16)

- tip: lanes/encode-writer2 @66c84ba (parent 6c3855a gated PASS). rgram.py
  +47/-0, cells to 14996, pins 1912->1936 (+24/-0).
- code read (ALL): _T9I1T 16 tabs (7B) + _T9I1B5 16 b5-vals + _T9I1W 16
  words (2B) + _T9I1C consts (53 keys, unique; tab/word bytes excluded) +
  branch n<=14996 (off=n-14741, m=off&15, q=off>>4): m<=15 (16 tabs),
  q<=15 (B5/W/H3QT-rot len 16 each), b5=B5[q]+(m>=11&q in 6,14), blk=
  H3QT[q][0:8] (4B reuse). contiguous after H3Q (14741 follows 14740),
  paylen 68. ordering verified.
- NIT (no FAIL, persistent class): message "(1938 pins)" counts 2 csv
  comments; data rows 1936 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-66c84ba-s4): HYGIENE/CONTAM clean,
  RGRAM n=1936, PINS-RGRAM set-eq 1936/1936, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 138/138 (NOTE-092 baseline + 31), ZERO holds.
