# GATE-bb54325 sweep: PASS (rgram 1276/1276, T8C1 16x16)

- tip: lanes/encode-writer2 @bb54325 (parent 05dd402 gated PASS). rgram.py
  +41/-0, cells to 11516, pins 1256->1276 (+20/-0).
- code read (ALL): _T8C1T 16 tabs + _T8C1B 16 block-words + _T8C1C consts
  (50 keys, unique) + branch n<=11516 (off=n-8735, m=(off-2526)&15,
  q=(off-2526)>>4): m<=15 (16 tabs), q<=15 (16 blocks), contiguous after
  B1Q (off 2526 follows 2525), b5 0x57 + steps @2529/2657 matches message.
  ordering verified.
- NIT (no FAIL, persistent class): message "(1278 pins)" counts 2 csv
  comment lines; data rows 1276 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-bb54325-s4): HYGIENE/CONTAM clean,
  RGRAM n=1276, PINS-RGRAM set-eq 1276/1276, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 113/113 (NOTE-092 baseline + 6), ZERO holds.
