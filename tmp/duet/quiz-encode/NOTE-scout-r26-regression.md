# NOTE-scout-r26-regression: fresh r26 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r26/
  scratch (regr/, regr-t2/, regr-t3/),
  TMPDIR r26/, oracle /usr/bin/aa. First-hand
  in r26, tip 142e8d4 (= r25 baseline tip, no
  lane movement).
- T0-CONTAINER GREEN (t0-smoke rc=0 x3: base +
  T2 + T3 legs; base leg exit 0 + T1 banner
  proves T0 pass via set -eu chain).
- T1-CONTAINER GREEN (p0..p7 incl. p3/p4/p5/p6/
  p7, x3 legs).
- T2-SEED7 GREEN (q0..q9 incl. q8 arch + framing
  + lz4raw-neg + corners; q9 verify/fix; q7-seed).
- T3-SEED8 GREEN (same shape, disjoint seed).
