# VERIFY-b3c9aa60 b296 T10P188 pins 82161..82252 (1056 tiers): PASS

viewer-r31, first-hand, detached tree NVME tmp/encode-viewer/r31/
tree-b3c9aa60 @b3c9aa60 (base e4676a40), seat build build296/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2511224 B, sha256 rgramc ba28f0f3 / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5582/5582 covered=5582/5582 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11164/11164 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11164/11164 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11164/11164).
- PINS-RGRAM cell set-eq 11164/11164 (cmp-identical).
  (GATE's "5582/5582" is N-set method = half the cells;
  for-list count 5582 confirmed; cell-level set-eq is
  full 11164. Method note, not FAIL.)
- PINS 11166 rows = 2 hdr + 11164, +32 vs base (11134).
  For-list +16 exactly: 82161 82162 82163 82175 82176
  82179 82180 82184 82188 82189 82204 82205 82221 82237
  82251 82252. 0 removed (== GATE).
- Own-loop 82161..82252 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers b5 step @82176 empirically mid-range.)
- Tables P188 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 74/74,
  BM 9/9, BC 71/71, M 16/16, QR 4/4, QT 4/4, QC 65/65
  (py-hex vs C-decimal normalized). C _N counts 74/71/65
  match actual rows (== GATE). Sigs first-hand:
  S0=f6020000 (REPEAT x3 P186/P187), S1=3b070500
  (== P187 PB1), S2=e83d0600 (NEW); A b0-3 AC=b7735000
  (NEW); BC lacks b0 (per-N var in mtab), b1-3=1e0300
  const (== GATE).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=82161 / S1 n=82162 singletons; A 82163-82178
  off=n-82163, mtab 8B b6-9/76-79; S2 n=82179
  singleton; B 82180-82188 off=n-82180, mtab 11B
  b0/6-11/80-83; Q 82189-82252 off=n-82189 m=off&15
  q=off>>4, M 6B b13,15/76-79, R 7B b0/6-11 (sigrb7),
  T 4B b80-83; all paylen 84, raw lencode b4/b5
  (no special-case; step @82176 emergent, own-loop
  green through it). C blocks carry T52301/06/11/26/
  31/47 py-line mirrors (== GATE). Insert position
  exact both sides: after T10R185 close (py L52298-52299,
  R185 n<=82160 / C L142722-142725), before T10R186
  (n<=82508, base 82253; py L52370 / C L142887).
  (== GATE.)
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1517 del / 1972 add
  (grep; +6 empty-plus = 1978 numstat), fine-norm
  del-uniq 1478 (== GATE exact) / add-uniq 1766,
  del-subset-add 0 missing.
- GATE PROSE SLIP (PROSE-01, code PASS unaffected):
  GATE claims "raw grep 1517 del / 1978 add (numstat
  identical, no blank-only lines)". First-hand: grep
  gives 1972 (1978 = numstat incl 6 empty-plus lines,
  which DO exist — same 6 as every band); add-uniq
  fine is 1766, GATE's 1767 = +1 empty-line counting.
  Verdict leg (0 missing) agrees. sweep2-r36 slip
  count this round: 1 (b298 GATE still to be VERIFYed).
- Wall on band diff added lines (e4676a40..b3c9aa60, 2178
  grep-added lines + 6 empty = 2184 numstat == GATE):
  vendor/disasm/depload/libcompression/shebang 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-402-q393 T10P188 verdict CONFIRM
  26/26 checks, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose otherwise CORRECT (build+sha, counts,
  for-list, tables, _N decls, guards, sigs, mtab byte
  lists, T-mirrors, insert position, R186 ceiling/base,
  flip [82176]).

Agrees with GATE-b3c9aa60 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r31/
(*296* files).

Verdict: PASS. Ready for parent PV + merge.
