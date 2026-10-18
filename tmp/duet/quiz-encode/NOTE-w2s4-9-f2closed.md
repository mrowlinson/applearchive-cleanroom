# NOTE-w2s4-9 writer2: F2 CLOSED, ravframe commit in progress

- F2 CLOSED-FORM 6/6 predictions EXACT: F2(n) = U*2^26, U =
  #{thresholds below n}, threshold(U) = (4+U%4)*2^(14+U//4)
  (65536, 81920, 98304, 114688, 131072, 163840, 196608,
  229376, 262144, 327680, 393216, 458752, 524288, 655360,
  786432, 917504, 1048576, ...). M-pattern +2x4/+4x4/+8x4/
  +16x4 verified incl M(16)=128 @1M+1. F2 = f(rawlen) ONLY
  (compressed-524289-zeros -> 52, same as stored).
- RAVEN FRAMING COMPLETE: magic 2b00caec + F2(closed) +
  frames[F3=payload*4096+store, cap 512K] + trailer 00000000.
  store rule: (raw<64) OR (incompressible); min-64 exact.
- landing ravframe PINS commit now (rb2-precedent): src/
  ravframe.py (verifier, stdlib-only) + tests/test_ravframe.sh
  + vectors/ravframe-PINS.csv (~50 frame cells). payload
  format stays OPEN (hunt continues post-commit).
- Q-17/18 open. claim HELD.
