# VERIFY-19d62d80 b286 T10R187 n<=82856 (1004 tiers): PASS

viewer-r28, first-hand, detached tree NVME tmp/encode-viewer/r28/
tree-19d62d80 @19d62d80 (base 747e6583), seat build build286/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2442664 B (GATE states no size; recorded, no cmp).
- RGRAMC-PYID 5430/5430 covered=5430/5430 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 10860/10860 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 10860/10860 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (10860/10860).
- PINS-RGRAM cell set-eq 10860/10860 (cmp-identical).
  (GATE's "5430/5430" is N-set method = half the cells;
  cell-level set-eq is full 10860. Method note, not FAIL.)
- PINS 10862 rows = 2 hdr + 10860, +24 vs base (10838).
  For-list +12 exactly: 82601 82602 82687 82688 82701
  82765 82815 82816 82829 82841 82855 82856. 0 removed
  (== GATE list).
- Own-loop 82601..82856 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  256 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables R187 C-vs-py mechanical: M 16/16, Q 16/16, C 67/67
  EXACT; M hexlen 12 (6B), Q hexlen 18 (9B). Q-VARYING-SIG
  confirmed first-hand: Q q0-7 cf-first, q8-15 d3-first
  (mechanical prefix check + eye-read of table). Dispatch by
  eye both impls: ceiling 82856, base 82601, paylen 84,
  pay4=(0x53+2*off)&0xFF, pay5=0x85+(off>=87)+(off>=215),
  m 6B b37/b38/b76-79, q 9B b2/b21/b22/b23/b31/b72-75.
  C: 83/133/87/215 exact.
- py diff pure addition: rgram.py +70/0, test_rgram.sh +1/-1,
  PINS +24/0.
- C diff renumber-only + new: raw 1376 del / 1534 add (grep;
  numstat 1535/1376 == GATE raw), normalized del-uniq 1373 /
  add-uniq 1522, del-subset-add 0 missing. (GATE cites uniq
  1376/1525 — normalizer granularity; verdict leg 0-missing
  agrees.)
- Wall on band diff added lines (747e6583..19d62d80, 1627
  grep-added lines; GATE cites 1630 = numstat total):
  vendor/disasm/depload/libcompression 0 hits. Files:
  rgramc.c, rgram.py, test_rgram.sh (for-line), PINS.
- CONFIRM evidence: CONFIRM-R187.md PASS 18/18 + A-403-q395
  (CONVERT-01 rule a+b; Q-VARYING-SIG tier per memo + DONE-R
  log, cf/d3 @off128).

OBSERVED (GATE prose error, NOT code FAIL): GATE-19d62d80 line
23 says "b45 line verified by eye (0x3c=60 both sides)" but
first-hand both impls read pay4 base 0x53=83 (py 0x53, C 83)
with pay5 base 0x85=133 thr 87/215, C-vs-py in exact agreement,
all 10860 cells + 256 own-loop Ns green. The GATE's own line 25
dispatch note (b4 0x53+2off, b5 0x85 thr 87/215) is CORRECT —
line 23 contradicts it. Fourth sweep2 b45 eye-error in two rounds
(r32: b280 0x3c, b282 0x9d; r33: b284 0xd3, b286 0x3c); note the
wrong value 0x3c=60 repeats b280's wrong note verbatim, suggesting
copy-paste eye-notes rather than first-hand re-reads. Code
correct; parent may want GATE corrections + a firm word with
sweep2.

Agrees with GATE-19d62d80 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r28/
(*286* files).

Verdict: PASS. Ready for parent PV + merge.
