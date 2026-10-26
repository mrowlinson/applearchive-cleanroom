# GATE 26cd06b5 b374 T10P266 pins 109305..109652 (1584 tiers) PASS-functional

Seat sweep2-r56, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r56/w374 @26cd06b5.
Band = 5c96a8d2 (py merge w2b@6d72712a partial, +6 tiers, +62 pins)
+ 26cd06b5 (C port). Base 6ecdbd65 (b373 tip, 1578 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build374/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ce0d8512 / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52/r53/r54/r55
  builds; band touches no aae sources per numstat).
- RGRAMC-PYID 7804/7804 covered=7804/7804 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 15608/15608 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 15608/15608 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 15608/15608).
- PINS-RGRAM cells set-eq 15608/15608 (xor 0, PASS-names vs
  PINS-names); PINS base-N set vs for-list 7804/7804 xor 0;
  PINS 15610 rows (2 hdr + 15608 = PASS lines, +62 vs base
  15548). For-list union 7773->7804 +31 (109305 109306
  109307 109309 109311 109312 109318 109322 109323 109325
  109327 109328 109329 109330 109331 109332 109333 109348
  109349 109364 109365 109380 109381 109396 109397 109439
  109440 109504 109567 109568 109652), 0 removed, range
  109305..109652 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 15608-15546.
  The 31 = S0/S1 (2) + A head/carry-edge/mids/tail (6) + C
  head/mids/all-sig/tail (8) + Q head/row-edge-pairs/
  tail (8) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P266 C-vs-py, script-compared, TABAUDIT-GREEN
  78 PASS 0 FAIL (tabaudit266.py rc=0): S0/S1 168ch
  EXACT sigs a0740300 NEW / 2a40e906 NEW (vs P265
  a0560300 / bdcfaa06, full-string ne),
  AM 16/16 9B distinct, CM 10/10 15B distinct, M 16/16
  7B distinct, QR 4/4 8B, QT 4/4 4B, RM 16/16 7B
  distinct, RQ 16/16 7B distinct, AC 73, CC 67, QC 63,
  RC 72; C _N decls 73/67/63/72 match actual;
  byte-coverage unions exact every block (84/84/84/88,
  0 overlap, b4/b5 in no const set).
  C10-5SIG exact map: 958dec06 x5 @109323-27 +
  e5e87b03/dd767803/6d417603 x1 each + 750e7e03 x2
  @109331-32 (5 distinct in order); full sig in tab
  (CC has no b0-3); CM 10/10 diverge (all distinct);
  CC has no b5 (b5-const memo-1).
  QUAD single-sig c0822772 (QC b0-3); NO frags (code
  has M+QR+QT legs only, eye-verified); R8 DOUBLE-
  PAIRED r0==r3 f216dbb97b532400 x2 AND r1==r2
  32999dc175931007 x2 (FIRST); tails row-shared 4/4
  distinct b3327d33/ceb7d61f/f3b7d61f/23337d33,
  r1/r2 share TRUE 3B b7d61f + r0/r3 share 2B 7d33
  (tails echo the R double-pairing); QC has no b5
  (b5-const memo-1).
  Ring STANDARD: RM tail b80-83 (chars 6:14) 16/16
  distinct by COL, RQ tail b76-79 (chars 6:14) 16/16
  distinct by ROW, UNPAIRED; RC b0-3 03000000 NEW vs
  P265T (P265 b0 split-in-code, b1-3 000000, per P265R
  dispatch comment re-read first-hand); RC b84-87
  28ee7163 ring-wide (P265 had 2032bed2).
  Same-tier RQ rows = M rows 16/16 full-row (staging,
  NOT a finding per precedent).
  Code-consts vs A-638 INCL (PBA 73 / C10 68 / quad 64 /
  T88 72): impl 73/67/63/72 = identical on PBA/T88,
  memo-1 on C10/quad (standing incl/excl bookkeeping;
  b5-const excluded).
  PBA sig 8087f776 NEW (P265 PBA e0932f72 per P265A
  dispatch comment + P264AC code-verified).
  M-tails 16/16 ALL NEW vs P265T (zero overlap vs BOTH
  P265RM-tail and P265RQ-tail sets; P265 RM 16ch / RQ
  12ch rows re-read first-hand).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=109305 (PB0 sig a0740300 NEW, lenB 84), S1
  n=109306 (fat PB1 sig 2a40e906 NEW, lenB 84),
  A 109307-109322 PBA16-CARRY (sig 8087f776 NEW via
  AC b0-b3, b0 const 80, AM 16/16 distinct 9B, mtab
  b12-15,19,76-79, b5 step 55->56 raw lencode),
  C 109323-109332 C10-5SIG (sig map exact above, CM
  10/10 distinct 15B diverge 10/10, mtab
  b0-3,11,18-23,80-83 full-sig-in-tab, b5 const 56),
  Q 109333-109396 QUAD single-sig c0822772 x64
  (QM7 b24-26,76-79 M 16/16 7B shared x3 + R8
  b12-14,18-22 QR 8B DOUBLE-PAIRED above + QT tails
  above, NO frags, b5 const 56 NO carry raw lencode),
  R 109397-109652 T88-ring STANDARD (sig 03000000
  NEW, TM7 b27,34,35,80-83 by COL RM 16/16, TR7
  b28-30,76-79 by ROW RQ 16/16 UNPAIRED, tails
  SPLIT b80-83 col / b76-79 row, b84-87 const
  28ee7163 ring-wide, b4=(0xab+2off)&FF,
  b5=0x56+(off>=43)+(off>=171)). C blocks carry
  T72907/72912/72917/72932/72949/72972 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact (A 9B, C 15B, Q 7/8/4B, R
  7/7B), counter b4=(171+2off)&FF + (off>=43)+
  (off>=171), temps _t5622-5639 (base max _t5621, no
  reuse) + _b3411-3420/_i3412-3421 (base max
  _b3409/_i3410, no reuse), all 6 verified.
  Insert position exact both sides: after T10P265R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-638/A-330 geometry (PB0/PB1 NEW, PBA16
  VPOS 11 b5 55+step5 NO pair, C10-5SIG VPOS 16
  b5 const 56 10/10 diverge NO pair, QUAD VPOS 20
  single-sig + R8 DOUBLE-PAIRED + QT 3B/2B-shares +
  M-tails NEW, T88 VPOS 16 STANDARD SPLIT + b84-87
  28ee7163, lencode 348/348 whole-tier, PBA-carry,
  ring edges 109439->109440 + 109567->109568, NO D
  dips) incl exact values (5SIG map, QR double-pair,
  QT tails, ring TM7/TR7 16/16 UNPAIRED, tails
  SPLIT, consts stand).
- Edges via counter formula first-hand: A head f7/55
  tail 15/56 b5set {55,56} CARRY edge 109311 (o4,
  ff/55) -> 109312 (o5, 01/56); PBA formula == raw
  lencode 16/16; C head 17/56 tail 29/56 b5set {56},
  Q head 2b/56 tail a9/56 b5set {56} NO carry;
  ring 109439 (off42, ff/56) -> 109440 (off43, 01/57);
  109567 (off170, ff/57) -> 109568 (off171, 01/58);
  R head ab/56 tail a9/58; all edge pins + tail 109652
  in for-list + 2 PASS lines each py+C. S0/S1 embedded
  b4/b5 (f3/55, f5/55) match raw lencode. Ring counter
  == raw lencode 256/256, 0 mismatch. Odd-lencode
  348/348. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 610 add / 0 del
  (rgramc.c) + 238/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 605 content + 5 bare-blank
  `+` lines (verified bare, no whitespace) / 0 del;
  fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm, BSD
  tools, empty-excluding) del-subset-add 0 missing
  (del-uniq 0, add-uniq 397).
- Wall on band diff added lines (scope 6ecdbd65..
  26cd06b5, 911 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 610/0, rgram.py 238/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, dispatch-guards
  singletons 564->566 +2 / ranges 516->520 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1484->1490 +6, C singletons
  564->566 +2 (C-vs-py 0-offset), C ranges 516->520
  +4, seal 1578->1584 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-638-q778-
  t10p266 verdict CONFIRM (shape 13/13 + quad/ring 12/12
  + counters 14/14 as sectioned; verdict line reads
  39/39 as-filed; file present, counts verified;
  exact-value corroboration incl 5SIG map, QR double-
  pair, QT tails, single-sig, M-tails NEW, ring edges
  + consts re-checked above) + A-330 viewer
  corroboration (all 3 legs CONFIRM, no correction).
  No CONFIRM-P266.md file; A-638 suffices per rule.
  Agrees with cport commit msg (PYID 7804, RGRAM 15608).
- Quiz: no conflicting CLAIM/GATE/FLAG on b374. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r56/ (build374.log,
  pyid374.log, rgram374py/c.log, cmp374.py/.c,
  for374-old/-new.nums, smoke374.log, tables374.log,
  tabaudit266.py, edges266.py, edges374.log,
  numstat374.txt, add/delnorm374.txt, banddiff374.txt,
  cdiff374.txt, pydiff374.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
