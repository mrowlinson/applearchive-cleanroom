# GATE 5d63fca7 b344 T10P236 pins 98865..99212 (1404 tiers) PASS-functional

Seat sweep2-r48, first-hand, WT tmp/wt-encode-sweep2 @5d63fca7,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r48.
Band = b4e3657b (py merge w2b@36766756 partial, +6 tiers, +62 pins)
+ 5d63fca7 (C port). Base 6242a462 (b343 tip, 1398 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build344/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc b077a09a / aae d6e27c97
  (aae identical to b288-b343 builds: aae.c untouched).
- RGRAMC-PYID 6874/6874 covered=6874/6874 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13748/13748 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 13748/13748 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 13748/13748).
- PINS-RGRAM cells set-eq 6874/6874 (diff 0, PINS base-N
  set vs for-list); PINS 13750 rows (2 hdr + 13748 =
  PASS lines). For-list union +31 (98865 98866 98867
  98868 98874 98882 98883 98884 98885 98886 98889
  98891 98892 98893 98900 98908 98909 98924 98925
  98940 98941 98943 98944 98945 98956 98957 99071
  99072 99199 99200 99212), 0 removed, range
  98865..99212 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 13748-13686.
  The 31 = S0/S1 (2) + A head/mids/tail (4) + C
  head/mids/tail (7) + Q head/mids/carry-pair/tail
  (12) + ring head/edge-pairs/tail (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P236 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 76/76, CC 64/64,
  QC 65/65, RC 71/71; C _N decls 76/64/65/71
  match actual (tabc236.py rc=0, 6-block PBA/
  C10-2SIG/quad/T88-ring, nothing else).
  Code-consts vs A-549/A-306 (PBA 77 / C10 65 /
  quad 65 / T88 71 INCL): impl -1 on PBA/C10
  is the standing incl/excl bookkeeping (writer
  dual-accounts, excl 76/64 — A-549 §3 explicitly
  no-finding; quad 65 + T88 71 identical both
  since b5-varying); byte-coverage proven A 76+8,
  C 64+20, Q 65+19, R 71+17 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=98865 (PB0 sig 83470100 NEW, b4/b5 63/04 ==
  lencode), S1 n=98866 (fat PB1 sig 45f45702 NEW,
  b4/b5 65/04 == lencode), A 98867-98882 PBA16
  single-sig (sig 5c447f25 NEW, AM 16/16 distinct
  6B, mtab b6,7,76-79, b5 const 04 raw lencode),
  C 98883-98892 C10 2-SIG (sig map exact order:
  a826a902 x3 @98883-85 + 54935401 x7 @98886-92;
  CM 10/10 distinct 18B diverge 10/10, mtab
  b0-3,6-11,48-51,80-83 sig-bytes-in-tab, b5
  const 04 raw lencode), Q 98893-98956 single-sig
  quad (sig f4344915 NEW, M7 b9-11,76-79 M16
  16/16 distinct 7B, R6 b6,7,48-51 TRIPLE-PAIRED
  r1==r2==r3 d1dec3de4951 x3 r0 0dc9f25f207c
  distinct, b42 const 0x06 via consts NO b42 leg,
  tails 4/4 bec350e6/4906c3ab/7306c3ab/9d06c3ab
  r1/r2/r3 share 06c3ab, M-tails 16/16 NEW vs
  P235M, QT overlap 0/4 vs P235T, b5-carry
  04->05 @98943->98944 ff->01 edge),
  R 98957-99212 T88-ring STANDARD (sig 01000000
  ==P231T, M9 b8-11,19,76-79 by COL RM 16/16
  distinct, R6 b13,14,80-83 by ROW RQ 16/16
  distinct UNPAIRED, tails INVERTED, b84-87
  const 09a5a2f2 ring-wide, b4=(0x1b+2off)&FF,
  b5=0x05+(off>=115)+(off>=243)).
  C blocks carry T65003/008/013/028/045/068
  py-line mirrors, bounds + byte positions exact,
  ring consts 27/115/243, all 6 verified. Insert
  position exact both sides: after T10P235R close,
  at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-549 geometry (PB0 83470100
  NEW, PB1 45f45702 NEW ==P235next, PBA16 VPOS 7
  b5 const 04, C10-2SIG map VPOS 19 b5 const 04,
  QUAD64 VPOS 19 b5-carry, T88 VPOS 17, lencode
  348/348 whole-tier, ring edges 99071->99072 +
  99199->99200, NO D dips) and A-306 (R6 TRIPLE
  2/4 exact values, tails 4/4 exact + 06c3ab
  share, M-tails 16/16 NEW, ring M9/R6 16/16
  UNPAIRED, tails INVERTED explicit, b84-87
  09a5a2f2, consts stand).
- Edges via counter formula first-hand: 99071 (off114,
  ff/05) -> 99072 (off115, 01/06); 99199 (off242,
  ff/06) -> 99200 (off243, 01/07); all four pins
  PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del; raw
  grep 605 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 437).
- Wall on band diff added lines (scope 6242a462..
  5d63fca7, 910 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  610/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 504->506 +2 / ranges 396->400 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1398->1404 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-549-q628-
  t10p236 verdict CONFIRM (33/33 = 15/15 shape +
  10/10 quad/ring + 8/8 counters; file present,
  counts verified; A-306 corroborates incl-consts
  ALL-4-EXACT + QR/QT/R6/tails exact values +
  ring edges re-checked above). No CONFIRM-P236.md
  file; A-549 suffices per rule. Agrees with cport
  commit msg (PYID 6874, RGRAM 13748).
- Quiz: no conflicting CLAIM/GATE/FLAG on b344. Newest
  PARENT-* is QNUM-09 (w2e Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r48/ (build344.log,
  pyid344.log, rgram344py/c.log, cmp344.py/.c, for344-
  6242a462/5d63fca7, for344-added, pins344.basen,
  smoke344.log, tables344.log, tabc236.py, bycov236.py,
  bycov344.log, sig236.py/.log, banddiff344, added344,
  numstat344, add/delnorm344).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
