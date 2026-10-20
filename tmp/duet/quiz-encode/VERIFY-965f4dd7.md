# VERIFY-965f4dd7 b288 T10R189 LAST R n<=83552 (1008 tiers): PASS

viewer-r29, first-hand, detached tree NVME tmp/encode-viewer/r29/
tree-965f4dd7 @965f4dd7 (base 85522530), seat build build288/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2442824 B (GATE states sha256 only; recorded).
- RGRAMC-PYID 5454/5454 covered=5454/5454 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10908/10908 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10908/10908 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10908/10908).
- PINS-RGRAM cell set-eq 10908/10908 (cmp-identical).
  (GATE's "5454/5454" is N-set method = half the cells;
  cell-level set-eq is full 10908. Method note, not FAIL.)
- PINS 10910 rows = 2 hdr + 10908, +24 vs base (10886).
  For-list +12 exactly: 83297 83298 83327 83328 83361
  83425 83455 83456 83489 83537 83551 83552. 0 removed
  (== GATE list; `; do` stripped before tokenize).
- Own-loop 83297..83552 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R189 C-vs-py mechanical: M 16/16, Q 16/16, C 67/67
  EXACT; M hexlen 16 (8B), Q hexlen 14 (7B). Dispatch by
  eye both impls: ceiling 83552, base 83297, paylen 84,
  pay4=(0xc3+2*off)&0xFF, pay5=0x8a+(off>=31)+(off>=159),
  m 8B b11/b19/b26/b27/b76-79, q 7B b20/b21/b22/b72-75.
  C: 195/138/31/159 exact.
- b45 const line first-hand: byte 45 = 0x3c = 60 BOTH sides
  (py (45,0x3c), C {45,60}). GATE's "({45,60}=0x3c both
  sides)" is CORRECT under the natural parse (byte 45 =
  60 = 0x3c); no error flagged. Clarity note only: the
  braces are ambiguous (byte 60 is actually 0x31=49 both
  sides: py (60,0x31), C {60,49}); the two entries sit on
  different source lines so the singular "const line" can
  only mean byte 45's line. Suggest "byte45=0x3c=60" style.
- py diff pure addition: rgram.py +70/0, test_rgram.sh +1/-1,
  PINS +24/0.
- C diff renumber-only + new: raw 1378 del / 1536 add (grep;
  numstat 1537/1378 == GATE raw incl 1 blank), normalized
  del-uniq 1375 / add-uniq 1523 (== GATE exact),
  del-subset-add 0 missing.
- Wall on band diff added lines (85522530..965f4dd7, 1630
  grep-added lines; GATE cites 1632 = numstat total):
  vendor/disasm/depload/libcompression 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-R189.md PASS 16/16 + A-417-q401
  CONFIRM 16/16 + 16/16 (CONVERT-01 rule a+b; LAST R).
- GATE prose: CORRECT (see b45 clarity note above, not error).

Agrees with GATE-965f4dd7 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r29/
(*288* files).

Verdict: PASS. Ready for parent PV + merge.
