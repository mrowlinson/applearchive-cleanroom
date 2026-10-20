# VERIFY-240aa3dd b279 T10R180 n<=80420 (990 tiers): PASS

viewer-r27, first-hand, detached tree NVME tmp/encode-viewer/r27/
tree-240aa3dd @240aa3dd (base f0b9436a), seat build build279/rgramc,
env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2425576 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5346/5346 covered=5346/5346 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10692/10692 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10692/10692 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10692/10692).
- PINS-RGRAM set-eq 10692/10692 (cmp-identical).
- PINS 10694 rows = 2 hdr + 10692, +24 vs base (10670). For-list
  tail +12 exactly: 80165 80166 80255 80256 80269 80333 80383
  80384 80397 80405 80419 80420. 0 removed.
- Own-loop 80165..80420 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R180 C-vs-py mechanical: M 16/16, Q 16/16, C 66/66
  EXACT. b45 by eye: pay4=(75+2*off)&0xFF, pay5=114+(off>=91)+
  (off>=219), both impls.
- C diff 1528+/1369- renumber-only + new: normalized
  (_t/_i/_b/T numbers) del-subset-add 0 missing lines.
- Wall on band diff added lines (f0b9436a..240aa3dd, 2819
  lines, PARENT-032 scope): vendor/disasm/depload/
  libcompression 0 hits. Files touched: rgramc.c, rgram.py,
  test_rgram.sh (for-line), fast-battery adds (byte-identical
  to master, cmp-verified), PINS.
- CONFIRM evidence: A-387-q378r180 (CONVERT-01 rule b, cited).

Agrees with GATE-240aa3dd (PASS-functional) on every leg.
Logs: NVME ws tmp/encode-viewer/r27/ (build279.log, pyid279.log,
cbat279.log, pybat279.log, pass-c/py.txt, pins/pass-names.txt,
ownloop279.py/.log, added.txt, del/add-norm.txt, missing.txt).

Verdict: PASS. Ready for parent PV + merge.
