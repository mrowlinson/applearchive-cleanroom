# PV-eb766e3: parent-verify first-hand + merged 13d7580

Worktree tmp/wt-pv-eb766e3 (detached @eb766e3), TMPDIR=NVME
pv-eb766e3/work, binary + build on NVME.
- C-BUILD: make -C src/c rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1411/1411 covered=1411/1411 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: diff c12fcc6..eb766e3 (rgramc.c +23810/-6846)
  grep 0 hits.
- Merge: 13d7580 --no-ff under merge.lock.d, clean.
  GATE-eb766e3 functional PASS + VERIFY-eb766e3 PASS +
  PARENT-032 ruling. Cport bands 1-4 ALL merged.
