# GATE 6a6b67b6 b306 T10P198 pins 85641..85988 (1143 tiers) PASS-functional

Seat sweep2-r38, first-hand, WT tmp/wt-encode-sweep2 @6a6b67b6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r38.
Band = ec45acbb (py merge w2b@bea54489 partial, +7 tiers +56 pins)
+ 6a6b67b6 (C port). Base 7006cf52 (b305 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build306/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc d7ffd963 / aae d6e27c97
  (aae identical to b288-b304 builds: aae.c untouched).
- RGRAMC-PYID 5829/5829 covered=5829/5829 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11658/11658 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11658/11658 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11658/11658).
- PINS-RGRAM cells set-eq 5829/5829 (diff 0, PINS base-N
  set vs for-list); PINS 11660 rows (2 hdr + 11658 =
  PASS lines). For-list union +28 (85641 85642 85643
  85650 85658 85659 85660 85661 85664 85668 85669
  85676 85684 85685 85692 85700 85701 85708 85716
  85717 85724 85732 85733 85759 85760 85887 85888
  85988), 0 removed (`; do` stripped before tokenize).
  Each for-N yields 2 PASS lines (g-zN-closed + g-zN).
  The 28 ARE the DET28 set (T-ring edges 85759/60 +
  85887/88 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P198 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, S2 absent-both 0/0, AM 16/16, BM 2/2,
  M 16/16, QR 4/4, QT 4/4, AC 75/75, BC 71/71,
  QC 62/62, CM 8/8, CC 70/70, RM 16/16, RQ 16/16,
  RC 68/68; C _N decls 75/71/70/62/68 match actual
  (tabc.py rc=0 full Q-band; tabc198.py covers CM/CC/
  RM/RQ/RC rc=0). Code-consts 75/71/70/62/68 match
  A-431 exactly.
- Dispatch eye-verified both sides, 7 tiers in order:
  S0 n=85641 (PB0 sig 72030000 REPEAT P197), S1
  n=85642 (fat PB1 sig 63160500 ==P197-PBB2), A
  85643-85658 PBA16 (sig 63166100 NEW, mtab b34,42,
  43,76-79, b5 const, raw lencode), B 85659-85660
  PBB2 (sig 63160500 ==PB1, mtab b34,41-46,80-83,
  b5 const, raw lencode), C 85661-85668 PBC8 (sig
  7f800300 NEW, mtab b34,35,41-46,80-83, b5 const,
  raw lencode), Q 85669-85732 QUAD64 single-sig
  63163500 REPEAT P197Q (mtab b48-51,76-79 + sigr8
  b34,35,41-46 / tails b80-83 all-distinct, b5 const
  9d, raw lencode), R 85733-85988 T-ring TRANSPOSED
  classic sig 37665103 NEW (M6 b6,7,76-79 by COL
  off&15, Q8 b48-51,72-75 by ROW off>>4, b4=
  (0xcb+2off)&FF, b5=0x9d+(off>=27)+(off>=155)).
  C blocks carry T54850/855/860/875/891/907/930
  py-line mirrors. Insert position exact both sides:
  after T10P197T close, at dispatch tail (N-out-of-
  scope fallthrough follows). Matches A-431 geometry
  (VPOS A b4+M7 / B b4+M11 / C b4+M12 / Q 21 / R 16,
  sigs, lencode 92/92, M8 row-indep 16/16x4 shared,
  R8 all-distinct, tails 4/4 no-sharing, M-tails ALL
  NEW vs P197T, T-ring edges 85759->85760 +
  85887->85888 ff->01, flips {85760,85888}, DET28
  28 cells).
- C diff renumber-only + new: numstat 2231 add / 1508 del;
  raw grep 2224 add / 1508 del (7 blank-only `+` lines,
  verified; 0 blank `-`); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1504, add-uniq
  1910). Same pipeline as b304 (b302-validated).
- Wall on band diff added lines (scope 7006cf52..6a6b67b6,
  2557 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c 2231/1508, rgram.py +269/+0
  purely additive, test_rgram.sh 1/1, PINS +56/+0.
- CONFIRM evidence (CONVERT-01 rule b): A-431-q430-t10p198
  verdict CONFIRM (38/38 checks; file present, counts
  verified; A-268 corroborates). No CONFIRM-P198.md
  file; A-431 suffices per rule. Agrees with cport
  commit msg (PYID 5829, RGRAM 11658).
- Quiz: no conflicting CLAIM/GATE/FLAG on b306. Newest
  PARENT-* is QNUM-03 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r38/ (build306.log,
  build306.sha, pyid306, rgram306py/c, cmp306.py/.c,
  for306-7006cf52/6a6b67b6, for306-added, pins306.csv/
  .cells, seteq306, smoke306, tables306.log,
  tables306b.log, tabc.py, tabc198.py, cdiff306,
  cdiff306.del/.add, del/addnorm306, cdiff306.miss,
  banddiff306, added306, numstat306).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
