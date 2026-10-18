# NOTE-scout-r27-regression: fresh r27 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r27/
  scratch (regr/, regr-t2/, regr-t3/),
  TMPDIR r27/, oracle /usr/bin/aa. First-hand
  in r27, tip 142e8d4 (= r26 baseline tip, no
  lane movement).
- T0-CONTAINER GREEN (x3 legs; T1 banner proves
  T0 pass via set -eu chain).
- T1-CONTAINER GREEN (p0..p7, x3 legs).
- T2-SEED7 GREEN (q0..q9 incl. q9 verify/fix,
  q7-seed).
- T3-SEED8 GREEN (same shape, disjoint seed).
