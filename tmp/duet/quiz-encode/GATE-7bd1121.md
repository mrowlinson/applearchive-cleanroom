# GATE-7bd1121 sweep: PASS (rgram 1490/1490, T9D4 10-row dip band)

- tip: lanes/encode-writer2 @7bd1121 (parent 982922d gated PASS). rgram.py
  +31/-0, cells to 12588, pins 1486->1490 (+4/-0).
- code read (ALL): _T9D4T 10 rows + _T9D4C consts (54 keys, unique; tab
  bytes 5-9,60-63 excluded) + branch n<=12588 (off=n-12579, paylen 64,
  lencode, tab[off]): off 0..9 (10 = len). contiguous after T9D3 (12579
  follows 12578). ordering verified.
- NIT (no FAIL, persistent class): message "(1492 pins)" counts 2 csv
  comments; data rows 1490 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-7bd1121-s4): HYGIENE/CONTAM clean,
  RGRAM n=1490, PINS-RGRAM set-eq 1490/1490, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 122/122 (NOTE-092 baseline + 15), ZERO holds.
- DONE-writer1s3 read (w1 DONE @94c8d61, hash parked): NOT joint DONE —
  w2 actively landing (this tip). seat stays alive per protocol.
