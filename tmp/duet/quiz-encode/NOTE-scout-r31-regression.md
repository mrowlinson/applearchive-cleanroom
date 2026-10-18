# NOTE-scout-r31-regression: fresh r31 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r31/
  scratch (regr/, regr-t2/, regr-t3/),
  TMPDIR r31/, oracle /usr/bin/aa. First-hand
  in r31, tip 142e8d4 (= r30 baseline tip, no
  lane movement, worktree clean).
- T0-CONTAINER GREEN (x3 fresh-dir legs,
  rc=0 each).
- T1-CONTAINER GREEN (p0..p7, x3 fresh-dir
  legs, rc=0 each).
- T2-SEED7 GREEN (q0..q9 incl. q9 verify/fix,
  q7-seed).
- T3-SEED8 GREEN (same shape, disjoint seed).
- Procedural note (NOT a code RED): one mid-run
  T1 leg went RED (p5-rt-append, mv "Directory
  not empty") after reusing the same regr/
  workdir 3x. Root cause in harness
  tests/container/t1-pinned.sh:130
  (mv rt/app/t1-nested rt/app-nested-away):
  1st run renames, 2nd nests inside, 3rd
  collides. Re-running 3x into FRESH workdirs
  went 3/3 GREEN rc=0. No lane change, no
  verdict change; r32+ must use a fresh (or
  rm -rf'd) workdir per leg.
