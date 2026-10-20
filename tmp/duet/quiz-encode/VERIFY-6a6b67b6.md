# VERIFY-6a6b67b6 b306 T10P198 pins 85641..85988 (1143 tiers): PASS

viewer-r33, first-hand, detached tree NVME tmp/encode-viewer/r33/
tree-6a6b67b6 @6a6b67b6 (base 7006cf52 = b305 tip), seat build
build306/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2647480 B, sha256 rgramc d7ffd963 / aae d6e27c97
  (BOTH == GATE).
- RGRAMC-PYID 5829/5829 covered=5829/5829 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11658/11658 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11658/11658 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11658/11658).
- PINS-RGRAM cell set-eq 11658/11658 (cmp-identical).
  PINS N-set == for-list 5829/5829 (== GATE).
- PINS 11660 rows = 2 hdr + 11658, +56 vs base (11604).
  For-list +28 exactly: 85641 85642 85643 85650 85658 85659
  85660 85661 85664 85668 85669 85676 85684 85685 85692
  85700 85701 85708 85716 85717 85724 85732 85733 85759
  85760 85887 85888 85988. 0 removed (== GATE; `; do`
  stripped before tokenize). 5829x2 = 11658 PASS lines
  (== GATE). +28 carries T-ring edges 85759/60 + 85887/88
  (== GATE DET28 note).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 85641..85988 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P198 C-vs-py mechanical, ALL EXACT: S0/S1
  168-hex-char singletons 1/1 each, S2 absent-both 0/0;
  AM 16/16, BM 2/2, M 16/16, QR 4/4, QT 4/4, CM 8/8,
  RM 16/16, RQ 16/16; AC 75/75, BC 71/71, QC 62/62,
  CC 70/70, RC 68/68 (py-hex vs C-decimal normalized);
  C _N decls 75/71/70/62/68 match actual rows (== GATE).
  Sigs first-hand: S0=72030000 (REPEAT P197) S1=63160500
  (==P197-PBB2); A=63166100, B=63160500 (==PB1/S1),
  C=7f800300, Q=63163500 (REPEAT P197Q), R=37665103
  (== GATE).
- Dispatch by eye both impls, 7 tiers in order: S0
  n=85641 / S1 n=85642 singletons; A 85643-85658
  off=n-85643, mtab 7B b34/42/43/76-79; B 85659-85660
  off=n-85659, mtab 11B b34/41-46/80-83; C 85661-85668
  off=n-85661, mtab 12B b34,35/41-46/80-83; Q 85669-
  85732 off=n-85669 m=off&15 q=off>>4, M 8B b48-51/
  76-79, QR b34,35/41-46, QT b80-83, b5 const 9d
  (=0x9d whole quad, lencode arith-ok); R 85733-85988
  off=n-85733 c=off&15 r=off>>4 TRANSPOSED classic,
  b4=(0xcb+2off)&FF b5=0x9d+(off>=27)+(off>=155), M6
  b6,7/76-79 by COL, Q8 b48-51/72-75 by ROW; A/B/C/Q
  raw lencode, all paylen 84. Ring edges arith-ok:
  85759->85760 + 85887->85888 ff->01 at off 26->27 /
  154->155; flips {85760,85888} (== GATE). C blocks
  carry T54850/855/860/875/891/907/930 py-line mirrors
  (7/7 exact == GATE). Insert position exact both sides:
  after T10P197T close, at dispatch tail ("N out of
  scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +269/-0 in 2 hunks
  (tables after _T10P197TC, dispatch in main()),
  test_rgram.sh +1/-1, PINS +56/+0.
- C diff renumber-only + new: numstat 2231 add / 1508 del;
  raw grep 2224 add / 1508 del + 7 blank-only `+` / 0
  blank-only `-` (all == GATE; 2224+7=2231 consistent).
  Fine-norm (_t/_i/_b/T) del-uniq 1504 / add-uniq 1910 /
  0 missing (== GATE exact; 1910 counts the blank-plus
  uniq-empty — blanks-excluded variant is 1909, miss 0
  either way, same accounting as b304).
- Wall on band diff added lines (7006cf52..6a6b67b6, 2557
  added lines == GATE scope): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa 0 hits.
  Files: rgramc.c 2231/1508, rgram.py +269/+0 purely
  additive, test_rgram.sh 1/1, PINS +56/+0.
- CONFIRM evidence: A-431-q430-t10p198 verdict CONFIRM
  38/38 (20+11+7 sections + 38/38 verdict line; ==
  GATE "38/38 checks; file present, counts verified"),
  A-268 corroborates geometry + const convention (==
  GATE), no DISSENT (CONVERT-01 rule b). No
  CONFIRM-P198.md file (== GATE; A-431 suffices per
  rule). GATE's A-431 cites (VPOS A b4+M7 / B b4+M11 /
  C b4+M12 / Q 21 / R 16, sigs, lencode 92/92, M8
  row-indep 16/16x4 shared, R8 all-distinct, tails 4/4
  no-sharing, M-tails ALL NEW vs P197T, edges, flips,
  DET28) all verbatim in file. Memo code consts
  75/71/70/62/68 == code tables; incl 76/72/71/63/68
  consistent (A-268 §3: PBA 76, PBB 72, PBC 71, quad 63
  b5-in, T 68). Agrees with cport commit msg (PYID
  5829, RGRAM 11658; == GATE).
- GATE prose CORRECT throughout (build incl both shas,
  counts, for-list + tokenize note, tables incl S2
  absent-both, _N decls, sigs incl S1==P197-PBB2 +
  Q REPEAT P197Q, mtab byte lists, counter formulas,
  edge arithmetic, T-mirrors, insert position,
  blank-line accounting, fine renumber counts,
  A-431/A-268 recon, QNUM-03-newest true at filing:
  GATE 13:53, QNUM-03 13:50, QNUM-04/05 14:08/14:14
  after). No slips.

Agrees with GATE-6a6b67b6 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r33/
(*306* files).

Verdict: PASS. Ready for parent PV + merge.
