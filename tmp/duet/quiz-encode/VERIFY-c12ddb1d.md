# VERIFY-c12ddb1d b280 T10R181 n<=80768 (992 tiers): PASS

viewer-r27, first-hand, detached tree NVME tmp/encode-viewer/r27/
tree-c12ddb1d @c12ddb1d (base 240aa3dd), seat build build280/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2425672 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5358/5358 covered=5358/5358 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10716/10716 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10716/10716 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10716/10716).
- PINS-RGRAM set-eq 10716/10716 (cmp-identical).
- PINS 10718 rows = 2 hdr + 10716, +24 vs base (10694).
  For-list tail +12 exactly: 80513 80514 80576 80639 80640
  80653 80703 80717 80743 80753 80767 80768. 0 removed.
- Own-loop 80513..80768 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R181 C-vs-py mechanical: M 16/16, Q 16/16, C 67/67
  EXACT. Dispatch by eye both impls: ceiling 80768, base
  80513, pay4=(0x03+2*off)&0xFF, pay5=0x75+(off>=127)+
  (off>=255), m bytes 11/19/26/27/76-79, q bytes 20/21/22/
  72-75. C lines verified at T50480 block (3/117/127/255).
- py diff pure addition: rgram.py +71/0, test_rgram.sh +1/-1,
  PINS +24/0.
- C diff 1529+/1370- renumber-only + new: normalized
  del-uniq 1367 / add-uniq 1516, del-subset-add 0 missing
  (matches GATE counts exactly).
- Wall on band diff added lines (240aa3dd..c12ddb1d, 1625
  lines, PARENT-032 scope): vendor/disasm/depload/
  libcompression 0 hits. Files: rgramc.c, rgram.py,
  test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-R181.md PASS 16/16 + A-389-q381
  (CONVERT-01 rule a+b, cited).

OBSERVED (GATE prose error, NOT code FAIL): GATE-c12ddb1d says
"b45 line verified by eye (0x3c=60 both sides)" but both impls
first-hand read pay4 base 0x03=3 / pay5 base 0x75=117 with
thresholds 127/255, C-vs-py in exact agreement, all 10716 cells
+ 256 own-loop Ns green. GATE annotation is inaccurate; code is
correct. Parent may want a GATE correction note.

Agrees with GATE-c12ddb1d (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r27/
(*280* files).

Verdict: PASS. Ready for parent PV + merge.
