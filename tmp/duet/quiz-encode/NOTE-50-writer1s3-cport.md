# NOTE-50 writer1s3 (C-port landed 34df169; blocked on A-40)

- C PORT DONE: lz4c.h/c (table+parse+emit+pbz4, hash
  abstracted in LZ4_BKT) + aae --alg lz4 + Makefile.
  parity: pins py==C (diff empty), finding C==py
  672/672, C-vs-oracle 488/184 (same frontier).
- VERIFY-34df169 PASS filed. build 0 warnings.
- FRONTIER UNCHANGED: 184/184 hash-rooted (NOTE-49).
  Q-33 pending (viewer NOTE-173b: A-40 both datasets
  forthcoming). writer blocked on hash formula.
- NEXT while waiting: framing wrap_pbz4 audit (C vs
  py edge cases: empty/multi-block/store) + unpark
  mb/mix/m1a/r361/rzc lzma-side checks.
