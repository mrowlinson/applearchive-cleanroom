# GATE-bed1c8b sweep: PASS (rgram 2048/2048, T9K2Q 16x16)

- tip: lanes/encode-writer2 @bed1c8b (parent 40a0146 gated PASS). rgram.py
  +44/-0, cells to 15692, pins 2028->2048 (+20/-0).
- code read (ALL): _T9K2QT 16 tabs (8B) + _T9K2B5 16 b5-vals + _T9K2QC
  consts (52 keys, unique; tab/word bytes excluded) + branch n<=15692
  (off=n-15437, m=off&15, q=off>>4): m<=15 (16 tabs), q<=15 (B5/K1QT-rot
  len 16 each), b5=B5[q]+(m>=3&q in 3,11), blk=K1QT[q] (6B reuse),
  tab=QT[m] (8B). contiguous after T9K1Q (15437 follows 15436), paylen 68.
  ordering verified.
- NIT (no FAIL, persistent class): message "(2050 pins)" counts 2 csv
  comments; data rows 2048 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-bed1c8b-s4): HYGIENE/CONTAM clean,
  RGRAM n=2048, PINS-RGRAM set-eq 2048/2048, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 142/142 (NOTE-092 baseline + 35), ZERO holds.
- quizmate: NOTE-405b read (viewer concurs GATE-40a0146, joint HELD).
