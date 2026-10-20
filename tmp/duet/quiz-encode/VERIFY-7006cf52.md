# VERIFY-7006cf52 b305 T10P197 pins 85293..85640 (1136 tiers): PASS

viewer-r33, first-hand, detached tree NVME tmp/encode-viewer/r33/
tree-7006cf52 @7006cf52 (base cdfc644d = b304 tip), seat build
build305/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2630584 B, sha256 rgramc e7047839 / aae d6e27c97
  (GATE cites aae sha only == match; rgramc sha first-hand).
- RGRAMC-PYID 5801/5801 covered=5801/5801 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11602/11602 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11602/11602 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11602/11602).
- PINS-RGRAM cell set-eq 11602/11602 (cmp-identical; == GATE).
  PINS N-set == for-list 5801/5801 (== GATE).
- PINS 11604 rows = 2 hdr + 11602, +64 vs base (11540).
  For-list +32 exactly: 85293 85294 85295 85302 85310 85311
  85312 85313 85316 85320 85321 85328 85336 85337 85344
  85352 85353 85360 85368 85369 85375 85376 85384 85385
  85464 85503 85504 85624 85625 85631 85632 85640.
  0 removed (== GATE).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 85293..85640 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P197 C-vs-py mechanical, ALL 16 EXACT: S0/S1
  168-hex-char singletons 1/1 each; AM 16/16, BM 2/2,
  CM 8/8, M 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 15/15;
  AC 75/75, BC 70/70, CC 69/69, QC 62/62, RC 67/67,
  TC 75/75 (py-hex vs C-decimal normalized); C _N decls
  75/70/69/62/67/75 match actual rows (== GATE). Excl-b5
  accounting confirmed in-table: no (5,v) entry in any of
  the 6 const tables (== GATE). Sigs first-hand: S0=
  72030000 (BREAKS 48030000 chain: P196 S0 head 48030000),
  S1=fd1b0500; A=fd1b6d00, B=63160500, C=36720300,
  Q=63163500, R=6316c103, T=6316c503 (== GATE).
- Dispatch by eye both impls, 8 tiers in order: S0
  n=85293 / S1 n=85294 singletons (offs 0/1); A 85295-
  85310 off=n-85295, mtab 7B b20/26/27/76-79; B 85311-
  85312 off=n-85311, mtab 12B b20,21/25-30/80-83; C
  85313-85320 off=n-85313, mtab 13B b11/18/19/25-30/
  80-83; Q 85321-85384 off=n-85321 m=off&15 q=off>>4,
  M 8B b32-35/76-79, QR b20,21/25-30, QT b80-83; R
  85385-85624 off=n-85385 (0..239) c=off&15 r=off>>4
  TRANSPOSED, M7 b37-39/76-79 by COL, Q8 b21-23/31/
  72-75 by ROW; T 85625-85640 off=n-85385 (240..255)
  k=n-85625, RM[k] positional + TC consts; R+T
  full-ring counter b4=(0x13+2off)&FF b5=0x9b+(off>=
  119)+(off>=247); A/B/C/Q raw lencode, all paylen 84.
  Counter arithmetic first-hand: quad b5-carry @off55
  (85375->85376 ff/9a->01/9b), ring edge 85503->85504
  ff/9b->01/9c (off 118->119, single step), tail 9c x7
  (off 240..246) -> 9d x9 (off 247..255) ff->01 @85631->
  85632 off247 (== GATE). C blocks carry T54566/571/
  576/591/607/623/646/665 py-line mirrors (8/8 exact
  line numbers == GATE). Insert position exact both
  sides: after T10P196R close, before dispatch-tail
  fallthrough ("N out of scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +298/-0 in 2 hunks
  (tables after _T10P196RC, dispatch in main()),
  test_rgram.sh +1/-1, PINS +64/+0.
- C diff renumber-only + new: numstat 2336 add / 1500 del;
  raw grep 2328 add / 1500 del + 8 blank-only `+` / 0
  blank-only `-` (all == GATE; 2328+8=2336 consistent).
  Coarse-norm ([0-9]+ -> N, cut-c2) del-uniq 965 /
  add-uniq 1164 / 0 missing (== GATE exact). Fine-norm
  (r31 recipe) del-uniq 1496 / add-uniq 1937 / 0 missing.
- Wall on band diff added lines (cdfc644d..7006cf52, 2699
  added lines == GATE scope): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line),
  PINS (+64/+0). Py side purely additive.
- CONFIRM evidence: A-430-q429-t10p197 verdict CONFIRM
  100/100 (22+17+11+50 section headers == GATE), no
  DISSENT (CONVERT-01 rule b); A-267 corroborates PB0
  BREAKS chain, PBB2/PBC8 VPOS, r0==r2 R8, split-row
  ring, consts 76/71/70/62/67/75 incl (== GATE). GATE's
  A-430 cites (VPOS A/B/C, QUAD VPOS 22 r0==r2-paired,
  T-240 TRANSPOSED 15 rows, TAIL16 row-15 own-sig M
  positional == 240M, carry, edge, tail 9c x7 -> 9d x9)
  all verbatim in file. For-list +32 carries carry pair
  85375/76 + edge 85503/04 + tail pair 85631/32 (DET32
  per A-430 §3). Memo code consts 75/70/69/62/67/75 ==
  code tables; incl 76/71/70/62/67/75 consistent (QC 62
  both: quad b5-carry).
- GATE prose CORRECT throughout (build, counts, for-list,
  tables incl RQ 15/15 + TC 75/75, _N decls, excl-b5
  note, sigs, mtab byte lists, counter formulas, step
  arithmetic, T-mirrors, insert position, blank-line
  accounting, coarse renumber counts, A-430/A-267 recon).
  No slips. (GATE omits rgramc sha; recorded first-hand
  above. Not a slip — no claim made.)

Agrees with GATE-7006cf52 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r33/
(*305* files).

Verdict: PASS. Ready for parent PV + merge.
