# GATE-44a5f94 sweep: PASS (rgram 1122/1122, T8W 16x16)

- tip: lanes/encode-writer2 @44a5f94 (parent 39ef22c gated PASS). rgram.py
  +39/-0, cells to 10472, pins 1114->1122 (+8/-0).
- code read (ALL): _T8WT 16 tabs + _T8WC consts (50 keys, unique) + branch
  n<=10472 (off=n-8735, m=(off-1482)&15, q=(off-1482)>>4): m<=15 (16 tabs),
  q<=15 (_T8V4T 16), contiguous after V4 (off 1482 follows 1481), b5 steps
  @1505/1633 match message. ordering verified.
- battery: GATE-PASS (outdir gate-w2-44a5f94-s4): HYGIENE/CONTAM clean,
  RGRAM n=1122, PINS-RGRAM set-eq 1122/1122, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 90/90 writer tips gated (90 battery-PASS, ZERO holds).
