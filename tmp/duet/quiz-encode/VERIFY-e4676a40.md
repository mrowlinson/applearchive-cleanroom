# VERIFY-e4676a40 b295 T10P187 pins 81813..81904 (1050 tiers): PASS

viewer-r31, first-hand, detached tree NVME tmp/encode-viewer/r31/
tree-e4676a40 @e4676a40 (base 015711bc), seat build build295/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2510952 B, sha256 rgramc e11a781c / aae d6e27c97
  (GATE cites rc/warnings only; size+sha own).
- RGRAMC-PYID 5566/5566 covered=5566/5566 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11132/11132 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11132/11132 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11132/11132).
- PINS-RGRAM cell set-eq 11132/11132 (cmp-identical).
- PINS 11134 rows = 2 hdr + 11132, +32 vs base (11102).
  For-list +16 exactly: 81813 81814 81815 81822 81830 81831
  81832 81834 81840 81841 81856 81857 81873 81889 81903 81904.
  0 removed (== GATE).
- Own-loop 81813..81904 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P187 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 75/75,
  BM 9/9, BC 55/55, M 16/16, QR 4/4, QT 4/4, QC 64/64
  (py-hex vs C-decimal normalized). Sigs first-hand:
  S0=f6020000 (REPEAT of P186 PB0 per impl comment),
  S1=3b070500 (NEW), S2=3b070500 (== S1, SING-echoes-PB1
  sig only); A b0-3 AC=3b075d00 (NEW); B b0-3
  BC=3b00e4b3.
- Dispatch by eye both impls, 6 tiers in order: S0
  n=81813 / S1 n=81814 singletons; A 81815-81830
  off=n-81815, mtab 7B b36-38/76-79; S2 n=81831
  singleton; B 81832-81840 off=n-81832, mtab 27B
  b1,2,11/19-27/32-35/37-43/80-83; Q 81841-81904
  off=n-81841 m=off&15 q=off>>4, M 8B
  b34,35/42,43/76-79, R 6B b36-41 (rb6), T 4B b80-83;
  all paylen 84, raw lencode b4/b5
  l16=((n<<1)|1)&0xFFFF (no special-case). C blocks carry
  T52106/11/16/31/36/55 py-line mirrors. Insert position
  exact both sides: after T10R184 close (py L52103-52104,
  R184 n<=81812 / C L142198-142201), before T10R185
  (n<=82160, base 81905; py L52178 / C L142379).
- py diff pure addition: rgram.py +174/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1535 del / 1990 add
  (grep; +6 empty-plus = 1996 numstat == GATE), fine-norm
  del-uniq 1484 / add-uniq 1761, del-subset-add 0 missing.
  Coarse-norm ([0-9]+ -> N): del-uniq 905 == GATE exact,
  add-uniq 1023 vs GATE 1024 = +1 empty-line counting
  (method note, verdict leg 0-missing agrees everywhere).
- Wall on band diff added lines (015711bc..e4676a40, 2197
  grep-added lines + 6 empty = 2203 numstat == GATE):
  vendor/disasm/depload/libcompression/shebang 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-398-q392 T10P187 verdict CONFIRM
  25/25 checks, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose: CORRECT on every claimed value (build rc/w,
  counts, for-list, tables, _N counts, guards, sigs
  implied by eye-notes, mtab byte lists, insert
  position unstated in GATE but verified own).

Agrees with GATE-e4676a40 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r31/
(*295* files).

Verdict: PASS. Ready for parent PV + merge.
