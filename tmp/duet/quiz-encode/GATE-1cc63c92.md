# GATE 1cc63c92 b360 T10P252 pins 104433..104780 (1500 tiers) PASS-functional

Seat sweep2-r53, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r53/w360 @1cc63c92.
Band = 11bc6a4f (py merge w2b@65790536 partial, +6 tiers, +62 pins)
+ 1cc63c92 (C port). Base 0b7920eb (b359 tip, 1494 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build360/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 879f3338 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52 builds;
  band touches no aae sources per numstat; aae sha1
  7d8dd3a2 also matches b359 pinned value).
- RGRAMC-PYID 7370/7370 covered=7370/7370 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14740/14740 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14740/14740 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 14740/14740).
- PINS-RGRAM cells set-eq 7370/7370 (xor 0, PINS base-N
  set vs for-list; PASS-names vs PINS-names xor 0);
  PINS 14742 rows (2 hdr + 14740 = PASS lines, +62 vs base
  14680). For-list union +31 (104433 104434 104435 104436
  104441 104447 104448 104450 104451 104454 104455 104456
  104459 104460 104461 104469 104476 104477 104492 104493
  104501 104508 104509 104524 104525 104575 104576 104653
  104703 104704 104780), 0 removed, range 104433..104780
  exact. Each for-N yields 2 PASS lines (g-zN-closed +
  g-zN); 31x2 = 62 = 14740-14678.
  The 31 = S0/S1 (2) + A head/mid/carry-pair/tail (6) +
  C head/mids/sig/tail (6) + Q head/mids/tail (10) +
  ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P252 C-vs-py, script-compared, TABAUDIT-GREEN
  71 PASS 0 FAIL (tabaudit252.py rc=0): S0/S1 168ch
  EXACT sigs 80fc0200 NEW / 5d169d05 NEW (both strings
  NEW vs P251), AM 16/16 6B distinct, CM 10/10 17B
  distinct, M 16/16 9B distinct, QR 4/4 6B, QT 4/4 4B,
  RM 16/16 8B distinct, RQ 16/16 8B distinct, AC 76/76,
  CC 65/65, QC 63/63, RC 70/70; C _N decls 76/65/63/70
  match actual; byte-coverage unions exact every block
  (84/84/84/88, 0 overlap, b4/b5 in no const set).
  CM sig-map exact order: 8cc03106 x4 @104451-54 +
  46e01803 x1 @104455 + 8cc03106 x5 @104456-60 (2
  distinct sigs, 10/10 diverge NO pair).
  QR r1==r2 PAIRED 1f2fdb590062 x2, r0 f969885a06c1
  distinct, r3 1f2fdc590062 1B-off (db-vs-dc).
  QT values f470a4a5/6e2ac0e5/982ac0e5/9951481b
  (r1/r2 share last 3B 2ac0e5; 4/4 distinct).
  M col-15-frag 7d x15 + 69 @c15 EXACT.
  AC b0-3 dc65d159 (PBA sig in consts, not mtab);
  CC b9 const-staged (skipped in mtab); QC b1-3
  091c63 + b0 sig-led in M tab; RC b0-3 06000000 NEW;
  RC b84-87 e0a4c350 ring-wide.
  RM/RQ UNPAIRED, tails SPLIT (RM b76-79 by COL
  16/16, RQ b80-83 by ROW 16/16).
  Code-consts vs A-600 INCL (PBA 76 / C10 66 / quad 64 /
  T88 70): impl 76/70 identical on PBA/T88 (b5 carry /
  counter vary), 65/63 = memo-1 on C10/quad (b5 const 30
  both, standing incl/excl bookkeeping - A-600 S3
  explicitly no-finding). M-tails 16/16 ALL NEW vs P251T
  (P251RQ 16 rows 16B-wide re-read first-hand, tails =
  last 8 hex per b38,39,46,47,76-79 TR8 order).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=104433 (PB0 sig 80fc0200 NEW, lenB 84), S1
  n=104434 (fat PB1 sig 5d169d05 NEW, lenB 84),
  A 104435-104450 PBA16 single-sig (sig dc65d159 NEW
  via AC b0-b3, AM 16/16 distinct 6B, mtab b6,7,76-79,
  b5-carry 2f->30 @104447->104448 raw lencode),
  C 104451-104460 C10-2SIG sandwich (sig map exact order
  above, CM 10/10 distinct 17B diverge 10/10, mtab
  b0-3,6-8,10,11,48-51,80-83 b9-skipped sig-bytes-in-tab,
  b5 const 30),
  Q 104461-104524 QUADms col-15-frag (frag 7d091c63x15
  +69091c63@c15 per row x4 via M b0-led + QC b1-3,
  QM9 b0,9-12,76-79 M 16/16 distinct 9B + R6
  b6,7,48-51 pair/1B-off above + QT tails above, b5
  const 30 raw lencode),
  R 104525-104780 T88-ring STANDARD (sig 06000000 NEW,
  TM8 b8-10,19,76-79 by COL RM 16/16 distinct, TR8
  b13-16,80-83 by ROW RQ 16/16 distinct UNPAIRED, tails
  SPLIT b76-79 col / b80-83 row SWAPPED vs P251, b84-87
  const e0a4c350 ring-wide, b4=(0x9b+2off)&FF,
  b5=0x30+(off>=51)+(off>=179)). C blocks carry
  T69035/69040/69045/69060/69077/69101 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact, temps _t5336-5353 (base max
  _t5335, no reuse) + _b3258-3267/_i3259-3268 (base max
  _b3256/_i3257, no reuse), all 6 verified. Insert position
  exact both sides: after T10P251R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-600/A-363 geometry (PB0/PB1 NEW, PBA16 VPOS 8 b5
  carry 13+3 split @104447->104448, C10-2SIG VPOS 18 b9
  skipped b5 const 30 10/10 diverge NO pair, QUAD VPOS
  20 col-15-frag R-pair + 1B-off + 3B tail-share +
  M-tails NEW, T88 VPOS 18 STANDARD SPLIT-swapped +
  b84-87 e0a4c350, lencode 348/348 whole-tier, ring edges
  104575->104576 + 104703->104704, NO D dips) incl exact
  values (CM 2-sig map, QR pair + 1B-off, QT tails +
  3B-share, ring TM8/TR8 16/16 UNPAIRED, tails SPLIT,
  consts stand).
- Edges via counter formula first-hand: PBA carry
  104447 (ff/2f) -> 104448 (01/30); ring 104575 (off50,
  ff/30) -> 104576 (off51, 01/31); 104703 (off178,
  ff/31) -> 104704 (off179, 01/32); all six pins + tail
  104780 in for-list + 2 PASS lines each py+C. A b5set
  {2f,30} (single carry), C b5set {30}, Q b5set {30}
  NO carry. A head e7/2f tail 05/30, C head 07/30 tail
  19/30, Q head 1b/30 tail 99/30, R head 9b/30 tail
  99/32. Ring counter == raw lencode 256/256, 0 mismatch.
  Odd-lencode 348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del
  (rgramc.c) + 238/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 605 content + 5 blank-only
  `+` lines (verified bare) / 0 del; fine-norm
  (rgramc.c scope, TNP/_tN/_iN/_bN, BSD tools,
  empty-excluding) del-subset-add 0 missing (del-uniq
  0, add-uniq 170).
- Wall on band diff added lines (scope 0b7920eb..
  1cc63c92, 911 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 610/0, rgram.py 238/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 536->538 +2 / ranges 460->464 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1400->1406 +6, C singletons
  531->533 +2 (C-vs-py 5-offset pre-existing, unchanged),
  C ranges 460->464 +4, seal 1494->1500 +6: all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-600-q764-
  t10p252 verdict CONFIRM (shape 12/12 + quad/ring 12/12
  + counters 11/11 as sectioned; verdict line reads
  36/36 as-filed; file present, counts verified;
  exact-value corroboration incl CM 2-sig map, QR pair +
  1B-off, QT tails + 3B-share, M-tails NEW, ring edges
  + consts re-checked above) + A-363 viewer corroboration
  (all 3 legs CONFIRM). No CONFIRM-P252.md file; A-600
  suffices per rule. Agrees with cport commit msg (PYID
  7370, RGRAM 14740).
- Quiz: no conflicting CLAIM/GATE/FLAG on b360. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r53/ (build360.log,
  pyid360.log, rgram360py/c.log, cmp360.py/.c,
  for360-old/-new.nums, pins360.basen, smoke360.log,
  tables360.log, tabaudit252.py, edges252.py,
  edges360.log, numstat360.txt, added360.txt,
  add/delnorm360.txt, banddiff360.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
