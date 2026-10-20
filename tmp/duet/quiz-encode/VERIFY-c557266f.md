# VERIFY-c557266f b297 T10P189 pins 82509..82600 (1062 tiers): PASS

viewer-r31, first-hand, detached tree NVME tmp/encode-viewer/r31/
tree-c557266f @c557266f (base b3c9aa60), seat build build297/
rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01), fast batteries
(FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2528040 B, sha256 rgramc cf5511bc / aae d6e27c97
  (GATE cites rc/warnings only; size+sha own).
- RGRAMC-PYID 5598/5598 covered=5598/5598 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11196/11196 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11196/11196 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11196/11196).
- PINS-RGRAM cell set-eq 11196/11196 (cmp-identical).
- PINS 11198 rows = 2 hdr + 11196, +32 vs base (11166).
  For-list +16 exactly: 82509 82510 82511 82518 82527 82528
  82532 82536 82537 82552 82553 82559 82560 82569 82585 82600.
  0 removed (== GATE).
- Own-loop 82509..82600 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  92 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P189 C-vs-py mechanical, all 11 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, AC 75/75,
  BM 9/9, BC 69/69, M 16/16, QR 4/4, QT 4/4, QC 63/63
  (py-hex vs C-decimal normalized). Sigs first-hand (all
  NEW per impl comments): S0=1e030000, S1=fe1e0300,
  S2=614e0700 (b0,b1==QUAD); A b0-3 AC=99573100;
  B b0-3 BC=ff1e0300.
- Dispatch by eye both impls, 6 tiers in order: S0
  n=82509 / S1 n=82510 singletons; A 82511-82526
  off=n-82511, mtab 7B b20/26,27/76-79; S2 n=82527
  singleton; B 82528-82536 off=n-82528, mtab 13B
  b11/18,19/25-30/80-83; Q 82537-82600 off=n-82537
  m=off&15 q=off>>4, M 8B b32-35/76-79, R 7B
  b20,21/25/27-30 (sigrb7), T 4B b80-83; all paylen 84,
  raw lencode b4/b5 l16=((n<<1)|1)&0xFFFF (no
  special-case). C blocks carry T52494/99/04/19/24/40
  py-line mirrors. Insert position exact both sides:
  after T10R186 close (py L52491-52492, R186 n<=82508 /
  C L143226-143229), before T10R187 (n<=82856, base
  82601; py L52563 / C L143394).
- py diff pure addition: rgram.py +173/0, test_rgram.sh
  +1/-1, PINS +32/0.
- C diff renumber-only + new: raw 1500 del / 1955 add
  (grep; +6 empty-plus = 1961 numstat == GATE), fine-norm
  del-uniq 1478 / add-uniq 1755, del-subset-add 0 missing.
  Coarse-norm ([0-9]+ -> N): del-uniq 916 == GATE exact,
  add-uniq 1035 vs GATE 1036 = +1 empty-line counting
  (method note, verdict leg 0-missing agrees everywhere).
- Wall on band diff added lines (b3c9aa60..c557266f, 2161
  grep-added lines + 6 empty = 2167 numstat == GATE):
  vendor/disasm/depload/libcompression/shebang 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line 1/1),
  PINS (+32/+0). Py side purely additive.
- CONFIRM evidence: A-404-q420 T10P189 verdict CONFIRM
  33/33 checks, no DISSENT (CONVERT-01 rule b; == GATE).
- GATE prose: CORRECT on every claimed value (build rc/w,
  counts, for-list, tables, guards, mtab byte lists).

Agrees with GATE-c557266f (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r31/
(*297* files).

Verdict: PASS. Ready for parent PV + merge.
