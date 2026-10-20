# GATE b74c603f b346 T10P238 pins 99561..99908 (1416 tiers) PASS-functional

Seat sweep2-r48, first-hand, WT tmp/wt-encode-sweep2 @b74c603f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r48.
Band = cb665c1c (py merge w2b@3c494579 partial, +6 tiers, +62 pins)
+ b74c603f (C port). Base fa5e0143 (b345 tip, 1410 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build346/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc f3867663 / aae d6e27c97
  (aae identical to b288-b345 builds: aae.c untouched).
- RGRAMC-PYID 6936/6936 covered=6936/6936 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13872/13872 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 13872/13872 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 13872/13872).
- PINS-RGRAM cells set-eq 6936/6936 (diff 0, PINS base-N
  set vs for-list); PINS 13874 rows (2 hdr + 13872 =
  PASS lines). For-list union +31 (99561 99562 99563
  99564 99570 99578 99579 99580 99581 99582 99583
  99584 99588 99589 99596 99604 99605 99612 99620
  99621 99628 99636 99637 99644 99652 99653 99711
  99712 99839 99840 99908), 0 removed, range
  99561..99908 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 13872-13810.
  The 31 = S0/S1 (2) + A head/mids/tail (4) + C
  head/mids/carry-pair/tail (7) + Q head/mids/tail
  (12) + ring head/edge-pairs/tail (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P238 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 74/74, CC 60/60,
  QC 62/62, RC 72/72; C _N decls 74/60/62/72
  match actual (tabc238.py rc=0, 6-block PBA/
  C10-2SIG/quad/T88-ring, nothing else).
  Code-consts vs A-557/A-308 (PBA 75 / C10 60 /
  quad 63 / T88 72 INCL): impl -1 on PBA/quad
  is the standing incl/excl bookkeeping (writer
  dual-accounts, excl 74/62 — A-557 §3 explicitly
  no-finding; C10 60 + T88 72 identical both
  since b5-varying); byte-coverage proven A 74+10,
  C 60+24, Q 62+22, R 72+16 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=99561 (PB0 sig 93540100 ==P237PB0 REPEAT,
  b4/b5 d3/09 == lencode), S1 n=99562 (fat PB1 sig
  ad52a702 ==P237C10 sig, b4/b5 d5/09 == lencode),
  A 99563-99578 PBA16 single-sig (sig 609bd720
  ==P237PBA NEW geometry VPOS 9, AM 16/16 distinct
  8B, mtab b34,35,42,43,76-79, b5 const 09 raw
  lencode), C 99579-99588 C10 2-SIG (sig map exact
  order: ad52a702 x3 @99579-81 + ad525701 x7
  @99582-88, CM 10/10 distinct 22B diverge 10/10,
  mtab b2,3,20,21,23-27,34,35,41-47,80-83 b22
  SKIPPED verified first-hand, sig-bytes-in-tab,
  b5-carry 09->0a @99583->99584 ff->01 edge),
  Q 99589-99652 single-sig quad (sig ad524715 NEW,
  M8 b48-51,76-79 M16 16/16 distinct 8B, R8
  b34,35,41-46 TRIPLE-PAIRED r1==r2==r3
  5412f085bfb30a9d x3 r0 cc2e70849f53448a
  distinct, b42 2-valued row-split inside R8 NO
  coupling leg, tails 4/4 53b7258b/ee3c65bc/
  183d65bc/e2b560fd, M-tails 16/16 NEW vs P237M,
  QT overlap 0/4 vs P237T, b5 const 0a),
  R 99653-99908 T88-ring STANDARD (sig 01000000
  ==P231T, M6 b6,7,80-83 by COL RM 16/16
  distinct, R8 b52-55,76-79 by ROW RQ 16/16
  distinct UNPAIRED, tails SPLIT, b84-87 const
  85f32659 ring-wide, b4=(0x8b+2off)&FF,
  b5=0x0a+(off>=59)+(off>=187)).
  C blocks carry T65476/481/486/501/519/542
  py-line mirrors, bounds + byte positions exact,
  ring consts 139/59/187, all 6 verified. Insert
  position exact both sides: after T10P237R close,
  at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-557 geometry (PB0 REPEAT,
  PB1 ==P237next, PBA16 VPOS 9 b5 const 09,
  C10-2SIG map VPOS 24 b22-skipped b5-carry,
  QUAD64 VPOS 21 b5 const 0a, T88 VPOS 16,
  lencode 348/348 whole-tier, ring edges
  99711->99712 + 99839->99840, NO D dips)
  and A-308 (R8 TRIPLE 2/4 exact values, tails
  4/4 exact, M-tails 16/16 NEW, ring M6/R8 16/16
  UNPAIRED, tails SPLIT explicit, b84-87 85f32659,
  consts stand).
- Tail-share figure: QT r1/r2 = ee3c65bc/183d65bc,
  byte1 0x3c vs 0x3d differ, common suffix 2B 65bc
  — confirms A-557 §F (descriptive only, cut SAFE,
  no DISSENT; exact tail values CONFIRMED, pins PASS).
- Edges via counter formula first-hand: 99711 (off58,
  ff/0a) -> 99712 (off59, 01/0b); 99839 (off186,
  ff/0b) -> 99840 (off187, 01/0c); all four pins
  PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del; raw
  grep 605 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 390).
- Wall on band diff added lines (scope fa5e0143..
  b74c603f, 910 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  610/0, rgram.py +237/+0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 508->510 +2 / ranges 404->408 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1410->1416 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-557-q630-
  t10p238 verdict CONFIRM (34/35 + finding = 16/16
  shape + 10/11 quad/ring with §F descriptive tail-
  share finding + 8/8 counters; file present, counts
  verified; A-308 corroborates incl-consts ALL-4-EXACT
  + QR/QT/R8/tails exact values + ring edges re-
  checked above). No CONFIRM-P238.md file; A-557
  suffices per rule. Agrees with cport commit msg
  (PYID 6936, RGRAM 13872).
- Quiz: no conflicting CLAIM/GATE/FLAG on b346. Newest
  PARENT-* is QNUM-09 (w2e Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r48/ (build346.log,
  pyid346.log, rgram346py/c.log, cmp346.py/.c, for346-
  fa5e0143/b74c603f, for346-added, pins346.basen,
  smoke346.log, tables346.log, tabc238.py, bycov238.py,
  bycov346.log, sig238.py/.log, banddiff346, added346,
  numstat346, add/delnorm346).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
