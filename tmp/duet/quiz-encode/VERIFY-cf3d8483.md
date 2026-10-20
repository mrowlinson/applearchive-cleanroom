# VERIFY-cf3d8483 b298 T10P190 pins 82857..82948 (1068 tiers): PASS

viewer-r31, first-hand, detached tree NVME tmp/encode-viewer/r31/
tree-cf3d8483 @cf3d8483 (base c557266f), seat build build298/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2528328 B, sha256 rgramc 9b5ae83e / aae d6e27c97
  (== GATE exact).
- RGRAMC-PYID 5614/5614 covered=5614/5614 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11228/11228 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11228/11228 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11228/11228).
- PINS-RGRAM cell set-eq 11228/11228 (cmp-identical).
  (GATE's "5614/5614" is N-set method = half the cells;
  for-list count 5614 confirmed; cell-level set-eq is
  full 11228. Method note, not FAIL.)
- PINS 11230 rows = 2 hdr + 11228, +32 vs base (11198).
  For-list +16 exactly: 82857 82858 82859 82866 82875
  82876 82880 82884 82885 82900 82901 82917 82933 82943
  82944 82948. 0 removed (== GATE).
- Own-loop 82857..82948 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
  (Covers flip [82944] Q3-internal empirically mid-range.)
- Tables P190 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 74/74,
  BM 9/9, BC 70/70, M 16/16, QR 4/4, QT 4/4, QC 63/63
  (py-hex vs C-decimal normalized). C _N counts 74/70/63
  match actual rows (== GATE). Sigs first-hand:
  S0=1e030000 (REPEAT P189), S1=614e0700 (== P189 SING),
  S2=614e0700 (echoes PB1); A b0-3 AC=614e7300 (NEW);
  B b0-3 BC=37070300 (NEW).
- Dispatch by eye both impls, 6 tiers in order: S0
  n=82857 / S1 n=82858 singletons; A 82859-82874
  off=n-82859, mtab 8B b34,35/42,43/76-79; S2 n=82875
  singleton; B 82876-82884 off=n-82876, mtab 12B
  b34,35/41-46/80-83; Q 82885-82948 off=n-82885
  m=off&15 q=off>>4, M 7B b48-50/76-79, R 8B
  b34,35/41-46 (sigrb8), T 4B b80-83; all paylen 84,
  raw lencode b4/b5 (no special-case; flip [82944]
  emergent, own-loop green through it). C blocks carry
  T52686/91/96/11/16/32 py-line mirrors (== GATE).
  Insert position exact both sides: after T10R187 close
  (py L52683-52684, R187 n<=82856 / C L143735-143738),
  before T10R188 (n<=83204, base 82949; py L52755 /
  C L143903). (== GATE.)
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1481 del / 1936 add
  (grep; +6 empty-plus = 1942 numstat), fine-norm
  del-uniq 1469 (== GATE exact) / add-uniq 1762,
  del-subset-add 0 missing.
- GATE PROSE SLIP (PROSE-01, code PASS unaffected, 2nd
  instance same clause): GATE claims "raw grep 1481 del
  / 1942 add (numstat identical, no blank-only lines)".
  First-hand: grep gives 1936 (1942 = numstat incl 6
  empty-plus lines, which DO exist); add-uniq fine is
  1762, GATE's 1763 = +1 empty-line counting. Verdict
  leg (0 missing) agrees. sweep2-r36 slip count this
  round: 2 (b296 + b298, same repeated clause; below
  the 3rd-slip PROD trigger).
- Wall on band diff added lines (c557266f..cf3d8483, 2142
  grep-added lines + 6 empty = 2148 numstat == GATE):
  vendor/disasm/depload/libcompression/shebang 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-407-q421 T10P190 verdict CONFIRM
  32/32 checks, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose otherwise CORRECT (build+sha, counts,
  for-list, tables, _N decls, guards, sigs, mtab byte
  lists, T-mirrors, insert position, R188 ceiling/base,
  flip [82944]).

Agrees with GATE-cf3d8483 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r31/
(*298* files).

Verdict: PASS. Ready for parent PV + merge.
