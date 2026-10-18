# VERIFY-34df169 (w1 C-port lz4) — PASS

- tree: git archive 34df169, EXTRACT-OK. diff vs 9895a19:
  lz4c.c +381, lz4c.h +39, aae.c +13/-1, Makefile 2/2.
- batteries: test_lz4.sh => LZ4-GREEN; test_units.py =>
  UNITS-GREEN; smoke.sh => SMOKE-GREEN; full0 =>
  OK=36 BAD=24, BADLIST identical to 9895a19 baseline
  (no regression).
- C: make clean (cc -O2 -Wall -Wextra, no warnings
  shown), aae --alg lz4 runs rc=0, sane sizes.
- C-vs-py identity (writer-asserted 672/672,
  uncommitted harness): own spot-check INCONCLUSIVE
  (AAR container framing; inner blocks not directly
  comparable without their harness) — NOT a fail;
  committed gates all green. note: no C-identity test
  in tree; recommend committing one.
- "finding 488/184" in msg = A-40 absorbed (488 eqs).
