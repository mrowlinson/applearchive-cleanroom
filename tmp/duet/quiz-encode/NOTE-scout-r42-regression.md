# NOTE-scout-r42-regression: fresh r42 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r42/
  scratch (leg1/, leg2/, leg3/, leg-t2/,
  leg-t3/, + leg-t2b/leg-t3b count legs),
  TMPDIR r42/, oracle /usr/bin/aa.
  First-hand in r42, tip 142e8d4 (= r41
  baseline tip, no lane movement, worktree
  clean).
- T0-CONTAINER GREEN (x3 fresh-dir legs,
  rc=0 each, implied by T1 reach + rc=0).
- T1-CONTAINER GREEN (p0..p7, x3 fresh-dir
  legs, rc=0 each).
- T2-SEED7 GREEN (88 PASS, 0 FAIL, rc=0).
- T3-SEED8 GREEN (88 PASS, 0 FAIL, rc=0).
- r31 lesson honored: one FRESH workdir per
  leg (t1-pinned.sh:130 mv reuse artifact
  avoided); no RED seen. No /tmp use.
