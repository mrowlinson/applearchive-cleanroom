# GATE 42856cae b354 T10P246 pins 102345..102692 (1464 tiers) PASS-functional

Seat sweep2-r50, first-hand, WT tmp/wt-encode-sweep2 @42856cae,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r50.
Band = 23ce1eb8 (py merge w2b@a192a6c7 partial, +6 tiers, +62 pins)
+ 42856cae (C port). Base dbbeec8b (b353 tip, 1458 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build354/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 329d4031 / aae d6e27c97
  (aae identical to b288-b353 builds: aae.c untouched).
  (First attempt rc=2 ENOSPC: NVME 100% full, env issue
  not code; space freed by another party, rebuild rc=0.)
- RGRAMC-PYID 7184/7184 covered=7184/7184 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14368/14368 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14368/14368 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 14368/14368).
- PINS-RGRAM cells set-eq 7184/7184 (diff 0, PINS base-N
  set vs for-list); PINS 14370 rows (2 hdr + 14368 =
  PASS lines). For-list union +31 (102345 102346 102347
  102348 102354 102358 102361 102362 102363 102365 102366
  102369 102371 102372 102373 102381 102389 102399 102400
  102405 102413 102421 102429 102436 102437 102527 102528
  102565 102655 102656 102692), 0 removed, range
  102345..102692 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 14368-14306.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C
  head/mids/tail (6) + Q head/carry-pair/mids/tail
  (10) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var).
- Tables audit P246 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 74/74, CC 67/67,
  QC 62/62, RC 72/72; C _N decls 74/67/62/72
  match actual (tabc246.py rc=0, 6-block PBA/
  C10-2SIG/quad/T88-ring, nothing else).
  Code-consts vs A-581 (PBA 75 / C10 68 /
  quad 62 / T88 72 INCL): impl -1 on PBA/C10
  is the standing incl/excl bookkeeping (writer
  dual-accounts, excl 74/67 — A-581 §3 explicitly
  no-finding); quad 62 + T88 72 identical (b5-carry
  / b5-counter, varying — memo predicts identical);
  byte-coverage proven A 74+10, C 67+17,
  Q 62+22, R 72+16 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=102345 (PB0 sig acdf0200 NEW, b4/b5 93/1f ==
  lencode, lenB 84), S1 n=102346 (fat PB1 sig 7d38be05
  ==P245C10a, b4/b5 95/1f == lencode, lenB 84),
  A 102347-102362 PBA16 single-sig (sig 2085c74e NEW
  via AC b0-b3, AM 16/16 distinct 8B, mtab
  b34,35,42,43,76-79, b5 const 1f raw lencode),
  C 102363-102372 C10 2-SIG 3+7 (sig map exact order:
  7d38be05 x3 @102363-65 + 7d38de02 x7 @102366-72,
  ==P245C10 map, CC b0,b1 const 7d,38 sig-head,
  CM 10/10 distinct 15B diverge 10/10, mtab
  b2,3,34,35,41-47,80-83 sig-bytes-in-tab, b5 const
  1f), Q 102373-102436 single-sig quad 2085c72e
  (==P245PBA via QC b0-b3, triple r1==r2==r3
  0684f4980f3390be x3, r0 68a3b49f6fb343aa distinct,
  b42 ROW-LED 0x9f=159 r0 vs 0x98=152 r123 verified
  first-hand; QM8 b48-51,76-79 M16 16/16 distinct 8B;
  R8 b34,35,41-46 lenB 8; tails 4/4 a5790fa5/98d6bdbc/
  c2d6bdbc/ecd6bdbc; M-tails 16/16 NEW vs P245M, 0/16
  vs P245T; b5-carry 1f->20 @102399->102400 ff->01
  edge raw lencode), R 102437-102692 T88-ring STANDARD
  (sig 02000000 ==P245T, TM6 b6,7,80-83 by COL RM 16/16
  distinct, TR8 b52-55,76-79 by ROW RQ 16/16 distinct
  UNPAIRED, tails SPLIT, b84-87 const 03edd298
  ring-wide, b4=(0x4b+2off)&FF, b5=0x20+(off>=91)+
  (off>=219)). C blocks carry T67594/599/604/619/636/
  659 py-line mirrors, bounds + byte positions exact,
  all 6 verified. Insert position exact both sides:
  after T10P245R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-581 geometry (PB0 NEW
  / PB1 ==P245C10a, PBA16 VPOS 9 b5 const 1f, C10-2SIG
  3+7 VPOS 16 b5 const 1f 10/10 diverge, QUAD VPOS 22
  b5-carry, T88 VPOS 16, lencode 348/348 whole-tier,
  ring edges 102527->102528 + 102655->102656, carry edge
  102399->102400, NO D dips) incl exact values (QR
  triple, b42 row-led, tails 4/4, M-tails NEW, ring
  TM6/TR8 16/16 UNPAIRED, tails SPLIT, b84-87 03edd298,
  consts stand).
- Tail-share figure: QT r1/r2/r3 = 98d6bdbc/c2d6bdbc/
  ecd6bdbc, byte0 0x98/0xc2/0xec differ, common suffix
  3B d6bdbc — confirms A-581 §2 (TRUE 3B, memo
  re-verified programmatically; descriptive only, cut
  SAFE, no DISSENT; exact tail values CONFIRMED, pins
  PASS).
- Edges via counter formula first-hand: 102527 (off90,
  ff/20) -> 102528 (off91, 01/21); 102655 (off218,
  ff/21) -> 102656 (off219, 01/22); Q b5-carry pair
  102399 (ff/1f) -> 102400 (01/20); all six pins
  2 PASS lines each py+C. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del; raw
  grep 605 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 384).
- Wall on band diff added lines (scope dbbeec8b..
  42856cae, 911 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  shebang//usr/bin/aa/nominated 0 hits. Files touched:
  rgramc.c 610/0, rgram.py 238/0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 524->526 +2 / ranges 436->440 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1458->1464 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-581-q638-
  t10p246 verdict CONFIRM (33/33 = 11/11 shape +
  13/13 quad/ring + 9/9 counters; file present,
  counts verified; exact-value corroboration incl
  QR triple, b42 row-led, tails 4/4, M-tails NEW,
  ring edges + consts re-checked above). No
  CONFIRM-P246.md file; A-581 suffices per rule.
  Agrees with cport commit msg (PYID 7184, RGRAM
  14368).
- Quiz: no conflicting CLAIM/GATE/FLAG on b354. Newest
  PARENT-* is QNUM-11 (w2f Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r50/ (build354.log,
  pyid354.log, rgram354py/c.log, cmp354.py/.c, for354-
  42856cae/dbbeec8b, for354-added, pins354.basen,
  smoke354.log, tables354.log, tabc246.py,
  bycov246.py, bycov354.log, sig246.py/.log, numstat354,
  added354, add/delnorm354).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
