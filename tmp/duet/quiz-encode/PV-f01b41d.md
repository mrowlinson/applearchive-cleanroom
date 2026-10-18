# PV-f01b41d (parent): band168 T10P126 (n<=60676, 808 tiers) — GREEN, merged

First-hand parent PV in fresh detached worktree tmp/wt-pv-f01b41d @f01b41d
(TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f01b41d), pv-band.sh 4/4.

- C-BUILD: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings (ids 37f303a5)
- C-IDENT: RGRAMC-PYID 3843/3843 covered GREEN (own bin)
- PYID-RERUN: RGRAMC-PYID 3843/3843 GREEN (rerun, independent legs agree)
- CBAT: RGRAM_BIN=own C, 7686 PASS / 0 FAIL, RGRAM-GREEN
- PYBAT: python impl, 7686 PASS / 0 FAIL, RGRAM-GREEN
- OWN-LOOP: fresh-oracle 60585..60676, 92/92 pass, pins 24/24
- Wall (86ae4e6..f01b41d, PARENT-032 scope): 0 hits
- GATE-f01b41d PASS (sweep) + VERIFY-f01b41d PASS (viewer2) + no FLAG

Merged --no-ff oldest-first under tmp/duet/merge.lock.d; post-merge
git show f01b41d:src/c/rgramc.c | cmp - src/c/rgramc.c IDENTICAL.
