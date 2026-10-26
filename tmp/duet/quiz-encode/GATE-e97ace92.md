# GATE e97ace92 b348 T10P240 pins 100257..100604 (1428 tiers) PASS-functional

Seat sweep2-r49, first-hand, WT tmp/wt-encode-sweep2 @e97ace92,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r49.
Band = f2d995a2 (py merge w2b@a384b5f1 partial, +6 tiers, +62 pins)
+ e97ace92 (C port). Base 5f75b749 (b347 tip, 1422 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build348/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 92a65098 / aae d6e27c97
  (aae identical to b288-b347 builds: aae.c untouched).
- RGRAMC-PYID 6998/6998 covered=6998/6998 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13996/13996 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 13996/13996 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 13996/13996).
- PINS-RGRAM cells set-eq 6998/6998 (diff 0, PINS base-N
  set vs for-list); PINS 13998 rows (2 hdr + 13996 =
  PASS lines; 6998 g-zN + 6998 g-zN-closed rows). For-list
  union +31 (100257 100258 100259 100260 100266 100274
  100275 100276 100277 100278 100279 100281 100284 100285
  100292 100300 100301 100308 100316 100317 100324 100332
  100333 100340 100348 100349 100351 100352 100479 100480
  100604), 0 removed, range 100257..100604 exact. Each
  for-N yields 2 PASS lines (g-zN-closed + g-zN);
  31x2 = 62 = 13996-13934. The 31 = S0/S1 (2) + A
  head/mids/tail (4) + C head/mids/tail (7) + Q
  head/mids/tail (12) + ring head/edge-pairs/tail (6).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS,
  default oracle backend, no BACKEND var).
- Tables audit P240 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 72/72, CC 62/62,
  QC 66/66, RC 71/71; C _N decls 72/62/66/71
  match actual (tabc240.py rc=0, 6-block PBA/
  C10-2SIG/quad/T88-ring, nothing else).
  Code-consts vs A-561 (PBA 73 / C10 63 /
  quad 67 / T88 71 INCL): impl -1 on PBA/C10/
  quad is the standing incl/excl bookkeeping
  (writer dual-accounts, excl 72/62/66 — A-561
  §3 explicitly no-finding; T88 71 identical
  since b5-varying); byte-coverage proven A 72+12,
  C 62+22, Q 66+18, R 71+17 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=100257 (PB0 sig 3f550100 NEW, b4/b5 43/0f ==
  lencode), S1 n=100258 (fat PB1 sig 4dc2a402 NEW,
  == own-tier C sig1, b4/b5 45/0f == lencode),
  A 100259-100274 PBA16 single-sig (sig a0955736,
  AM 16/16 distinct 10B, mtab b14,15,21,22,23,31,
  76,77,78,79, b5 const 0f raw lencode), C 100275-
  100284 C10 2-SIG (sig map exact order: 4dc2a402
  x3 @100275-77 + 4dc25401 x7 @100278-84, CM 10/10
  distinct 20B diverge 10/10, mtab b2,3,20-27,30-35,
  80-83, sig-bytes-in-tab CC b2/b3 VAR, b5 const
  0f), Q 100285-100348 single-sig quad (sig 4dc25415
  NEW, M6 b36,37,76-79 M16 16/16 distinct 6B, R6
  b22,23,30,32,33,34 TRIPLE-PAIRED r1==r2==r3
  f14c2234156e x3 r0 2540eeb42b46 distinct, b42
  const 0x9f via consts NO coupling leg, tails 4/4
  58bdc6b0/ce29d41d/f829d41d/f9b1c924, M-tails 16/16
  NEW vs P239M (0/16 vs P239T), QT overlap 0/4 vs
  P239T, b5 const 0f), R 100349-100604 T88-ring
  STANDARD (sig 01000000 ==P231T, M9 b19,27,39,46,47,
  80-83 by COL RM 16/16 distinct, R6 b40,41,76-79
  by ROW RQ 16/16 distinct UNPAIRED, tails SPLIT,
  b84-87 const 0237bbef ring-wide, b4=(0xfb+2off)
  &FF, b5=0x0f+(off>=3)+(off>=131)). C blocks carry
  T65974/979/984/T66000/018/041 py-line mirrors,
  bounds + byte positions exact, ring consts
  251/15/3/131, all 6 verified. Insert position
  exact both sides: after T10P239R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-561 geometry (PB0/PB1 NEW, PBA16 VPOS 11 b5
  const 0f, C10-2SIG map VPOS 21 b5 const 0f 10/10
  diverge, QUAD64 VPOS 17 b5 const 0f, T88 VPOS 17,
  lencode 348/348 whole-tier, ring edges 100351->
  100352 + 100479->100480, NO D dips) incl exact
  values (QR triple 2/4, tails 4/4, M-tails 16/16
  NEW, ring M9/R6 16/16 UNPAIRED, tails SPLIT,
  b84-87 0237bbef, consts stand).
- Tail-share figure: QT r1/r2 = ce29d41d/f829d41d,
  byte0 0xce vs 0xf8 differ, common suffix 3B 29d41d
  — confirms A-561 §2 (TRUE 3B, memo re-verified
  programmatically; descriptive only, cut SAFE,
  no DISSENT; exact tail values CONFIRMED, pins PASS).
- Edges via counter formula first-hand: 100351 (off2,
  ff/0f) -> 100352 (off3, 01/10); 100479 (off130,
  ff/10) -> 100480 (off131, 01/11); all four pins
  PASS. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del; raw
  grep 605 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 414).
- Wall on band diff added lines (scope 5f75b749..
  e97ace92, 911 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/CT-shim/shebang/
  /usr/bin/aa/nominated 0 hits. Files touched: rgramc.c
  610/0, rgram.py +238/+0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 512->514 +2 / ranges 412->416 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1422->1428 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-561-q632-
  t10p240 verdict CONFIRM (33/33 = 15/15 shape +
  10/10 quad/ring + 8/8 counters; file present,
  counts verified; exact-value corroboration incl
  QR triple, tails 4/4, M-tails NEW, ring edges +
  consts re-checked above). No CONFIRM-P240.md file;
  A-561 suffices per rule. Agrees with cport commit
  msg (PYID 6998, RGRAM 13996).
- Quiz: no conflicting CLAIM/GATE/FLAG on b348. Newest
  PARENT-* is QNUM-10 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r49/ (build348.log,
  pyid348.log, rgram348py/c.log, cmp348.py/.c, for348-
  e97ace92/5f75b749, for348-added, pins348.basen,
  smoke348.log, tables348.log, tabc240.py, bycov240.py,
  bycov348.log, sig240.py/.log, banddiff348.stat,
  numstat348, added348, add/delnorm348).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
