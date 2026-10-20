# GATE 76e7bf34 b310 T10P202 pins 87033..87380 (1182 tiers) PASS-functional

Seat sweep2-r39, first-hand, WT tmp/wt-encode-sweep2 @76e7bf34,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r39.
Band = 242c46be (py merge w2b@cce3cd63 partial, +11 tiers +58 pins)
+ 76e7bf34 (C port). Base 27d39094 (b309 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build310/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1c798145 / aae d6e27c97
  (aae identical to b288-b308 builds: aae.c untouched).
- RGRAMC-PYID 5952/5952 covered=5952/5952 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11904/11904 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11904/11904 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11904/11904).
- PINS-RGRAM cells set-eq 5952/5952 (diff 0, PINS base-N
  set vs for-list); PINS 11906 rows (2 hdr + 11904 =
  PASS lines). For-list union +29 (87033 87034 87035
  87039 87040 87050 87051 87052 87053 87056 87060
  87061 87068 87076 87077 87084 87092 87093 87100
  87108 87109 87116 87124 87125 87167 87168 87295
  87296 87380), 0 removed (`; do` stripped before
  tokenize). Each for-N yields 2 PASS lines (g-zN-closed
  + g-zN). The 29 ARE the DET29 set (flips 87040/87168/
  87296 + ring edges 87167/87168 + 87295/87296 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P202 C-vs-py, script-compared, all EXACT:
  S0/S1/S2/S3 1/1, AM 16/16, BM 8/8, WM 16/16, AC 75/75,
  BC 71/71, WAC 73/73, WBC 73/73, WC0C 73/73, WC1C 73/73,
  RM 16/16, RQ 16/16, RC 67/67; C _N decls 75/71/73/73/
  73/73/67 match actual; M/QR/QT/QC absent-both 0/0
  (non-Q band, QC_N-probe N/A per rule; tabc202.py rc=0).
  Code-consts PBA 75 / PBB8 71 / rows 73x4 / T 67 match
  A-439 exactly (PBA uses 75 per §4 ruling, Q's 74 typo
  rejected).
- Dispatch eye-verified both sides, 11 tiers in order:
  S0 n=87033 (PB0 sig 9e030000 NEW chain), S1 n=87034
  (fat PB1 sig 7c3d0700), A 87035-87050 PBA16 (sig
  c8d77300 NEW, mtab b20-22,76-79, b5 CARRY @87040:
  87039 ff/a7 -> 87040 01/a8, raw lencode), S2 n=87051
  (SING sig df830600 NEW), S3 n=87052 (SING sig 4f4c0600
  NEW), B 87053-87060 PBB8 (sig be9e0300, mtab b20-26,
  80-83, b5 const, raw lencode), WA 87061-87076 ROW16a
  (sig 4f3a3b00 NEW), WB 87077-87092 ROW16b (sig ff683a00
  NEW), WC0 87093-87108 + WC1 87109-87124 ROW32 halves
  (sig 37163900 NEW), all 4 rows shared-M9 WM b20,21,22,
  26,27,76-79 + own consts + raw lencode, R 87125-87380
  T-ring TRANSPOSED (12th) sig c7489e03 NEW (M7 b32-34,
  76-79 by COL off&15, Q8 b24-27,72-75 by ROW off>>4,
  b4=(0xab+2off)&FF, b5=0xa8+(off>=43)+(off>=171)).
  C blocks carry T55941/946/951/966/971/976/992/007/
  022/037/052 py-line mirrors (T55941 = S0 ... T56052
  = R). Insert position exact both sides: after T10P201R
  close, at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-439 geometry (VPOS A 9 / B 12 /
  rows 10/10/11 / R 17, sigs, lencode 92/92, M9 shared
  16/16 all 3 groups, ROW32 halves identical ex-b4+b80,
  constdiffs a-b 10B / a-c0 12B, M-tails ALL NEW vs
  P201T, T-ring edges 87167->87168 ff/a8->01/a9 +
  87295->87296 ff/a9->01/aa, flips {87040,87168,87296},
  DET29 29 cells).
- C diff renumber-only + new: numstat 2489 add / 1544 del;
  raw grep 2478 add / 1544 del (11 blank-only `+` lines,
  verified; 0 blank `-`); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1540, add-uniq
  1973). Same pipeline as b304-b308 (b302-validated).
- Wall on band diff added lines (scope 27d39094..76e7bf34,
  2856 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c 2489/1544, rgram.py +319/+0
  purely additive, test_rgram.sh 1/1, PINS +58/+0.
- CONFIRM evidence (CONVERT-01 rule b): A-439-q434-t10p202
  verdict CONFIRM (36/37 + bookkeeping FINDING on PBA
  code-consts 74-vs-75, ruled: code uses 75; file present,
  counts verified; A-272 corroborates incl-consts). No
  CONFIRM-P202.md file; A-439 suffices per rule. Agrees
  with cport commit msg (PYID 5952, RGRAM 11904).
- Quiz: no conflicting CLAIM/GATE/FLAG on b310. Newest
  PARENT-* is QNUM-03 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r39/ (build310.log,
  pyid310, rgram310py/c, cmp310.py/.c, for310-27d39094/
  76e7bf34, for310-added, pins310.csv/.cells, seteq310,
  smoke310, tables310.log, tabc202.py, cdiff310,
  cdiff310.del/.add, del/addnorm310, cdiff310.miss,
  banddiff310, added310, numstat310).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
