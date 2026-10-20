# VERIFY-d52f218d b319 T10P211 pins 90165..90512 (1248 tiers): PASS

viewer-r37, first-hand, detached tree NVME tmp/encode-viewer/r37/
tree-d52f218d @d52f218d (base d47266c1 = b318 C tip), seat build
build319/ rgramc, env CT_CACHE_DIR + CT_REAL defaults (NVME
ct-cache, miss=real tool), fast batteries.

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2802040 B, sha256 rgramc 0d73a51c / aae d6e27c97
  (aae == r36/r39 cites, stable; aae sha1-8 7d8dd3a2 == GATE).
- RGRAMC-PYID 6186/6186 covered=6186/6186 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM py 12372/12372 PASS 0 FAIL RGRAM-GREEN rc=0.
- RGRAM C 12372/12372 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary).
- C-py PASS-set cmp-identical (12372/12372, diff 0).
- PINS-RGRAM cell set-eq 12372/12372 (cmp-identical).
  PINS N-set == for-list 6186/6186.
- PINS 12374 rows = 2 hdr + 12372 (+52 vs base 12322).
  For-list +26 exactly: 90165 90166 90167 90174 90182 90183
  90184 90185 90188 90192 90193 90208 90209 90224 90225 90239
  90240 90241 90256 90257 90300 90367 90368 90495 90496 90512.
  0 removed (== GATE verbatim).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 90165..90512 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P211 C-vs-py mechanical, ALL EXACT: S0/S1
  168/168-hex-char singletons (sigs f0070000 / e96d0f00 ==
  GATE); AM 16/16, PT 2/2, CM 8/8, M 16/16, X42 4/4, M42
  16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16; AC 75/75, PC
  78/78, CC 70/70, QC 65/65, RC 67/67 (py-hex vs C-decimal
  normalized); C _N decls 75/78/70/65/67 match actual rows
  (== GATE). Const sigs b0-3 first-hand: A e96dff00, P
  e96d0f00, C e96d0700, Q e96d6300, T e96de307 (== GATE).
  b4/b5 in no const table (all 5). Absence inventory:
  _T10P211* symbols == known set exactly, py 17 / C 22
  (+5 _N), no B/F/H/TC either side (== GATE).
  Code-consts vs A-281 incl 76/71/65/67: quad + T exact;
  A/C -1 each = b5-const-via-lencode bookkeeping (b5
  const c0 both, first-hand; == GATE); byte-coverage 84/84
  all 5 groups re-proven first-hand (A 2+7+75, P 2+4+78,
  C 2+12+70, Q 2+17+65, R 2+15+67; 0 overlap anywhere;
  b4/b5 in no const set — == GATE exact).
- Dispatch by eye both impls, 7 blocks in order: P2110
  n==90165 (PB0 f0070000 REPEAT P210) / P2111 n==90166
  (fat PB1 e96d0f00); A 90167-90182 PBA16 off=n-90167,
  mtab 7B b36-38,76-79, raw lencode; P 90183-90184 PAIR
  off=n-90183, b80-83=PT[off] + PC consts; C 90185-90192
  PBC8 off=n-90185, mtab 12B b32,33,37-42,80-83; Q
  90193-90256 QUAD64 single-sig off=n-90193 m=off&15
  q=off>>4, shared M6 b34,43,76-79 M[m] + b42 row-xor
  X42[q]^==M42[m] X=[00,02,03,07] + R6 b36-41 QR[q] (4/4
  distinct, unpaired) + tails b80-83 QT[q]
  a14d25f5/5907bd9e/23a5c1c0/df267dea; R 90257-90512
  off=n-90257 c=off&15 r=off>>4 T-ring ROLE-SWAP
  TRANSPOSED+TAILS-SWAPPED (21st), b4=(0x23+2off)&FF (C:
  35 literal ==) b5=0xC1+(off>=111)+(off>=239) (C: 193
  literal ==), M8 b48-51,72-75 by COL c, R7
  b34,42,43,76-79 by ROW r; all paylen 84 (== GATE
  every value). C blocks carry T58612/617/622/637/652/
  668/693 py-line mirrors (7/7 exact == GATE). Insert
  position exact both sides: dispatch tail ("N out of
  scope" + return 2 follows).
- Counter edges computed first-hand: A const c0
  (90167 6f/c0 -> 90182 8d/c0, no wrap); P const c0
  (90183 8f/c0 -> 90184 91/c0); C const c0 (90185 93/c0
  -> 90192 a1/c0, no wrap); Q off46->off47 (90239->
  90240) ff/c0->01/c1; R off110->111 (90367->90368)
  ff/c1->01/c2 + off238->239 (90495->90496) ff/c2->01/c3;
  all edge Ns in for-list (== GATE).
- A-471 FINDING re-checked first-hand (REQUIRED item):
  step sides ARE 90239 (off46, ff/c0) -> 90240 (off47,
  01/c1) via l16 formula evaluated both pins; code
  comment "b5-carry @off46" uses source convention (==
  GATE); bytes EXACT, pins PASS (both Ns pinned,
  own-loop oracle-agreeing). No DISSENT (A-471 §4
  explicit).
- py diff pure addition: rgram.py +295/-0 (0 deletions,
  tables + dispatch), test_rgram.sh +1/-1 (for-line
  only), PINS +52/-0 (GATE's "+52/-0" == PINS leg).
- C diff pure-add: numstat 752/0; raw grep 752 add (6
  bare `+`, 0 blank-minus; 752+header self-consistent
  == GATE). Coarse-norm ([0-9]+ -> N, cut-c2, sort -u):
  del-uniq 0 / add-uniq 198 / 0 missing (all == GATE
  exact).
- Wall on band diff added lines (d47266c1..d52f218d,
  1094 non-blank added == GATE; 1100 incl 6 bare-plus):
  vendor/disasm 0, depload 0, CT-shim/shebang 0,
  /usr/bin/aa 0 (== GATE). Files: rgramc.c 752/0,
  rgram.py +295/+0, test_rgram.sh 1/1, PINS +52/+0
  (== GATE).
- Band composition: d52f218d^ = 06c29573 single parent;
  06c29573 = merge d47266c1 + aff70122 (py partial +7
  tiers +52 pins) (== GATE; cport msg PYID 6186 /
  RGRAM 12372 agrees).
- CONFIRM evidence: A-471-q603-t10p211 BACKFILL verdict
  CONFIRM 23/23 = 12/12 shape + 8/8 ring + 3/3 counters
  + finding re-checked above (file present, counts
  verified; == GATE), A-281 corroborates (VPOS 8/13/
  19/17 partition-exact vs code mtab sets, X42 rule,
  tails == QT verbatim, R6 UNPAIRED 4/4, consts 76/71/
  65/67 incl, edges, NO D dips; == GATE), no DISSENT
  (CONVERT-01 rule b). GATE's A-471/A-281 cites (PBA
  b4+M7, full-tail PAIR, PBC8 b4+M12, QUAD64 + X b42xor
  64/64 + tails 4/4, T-ring TRANSPOSED 21st +
  TAILS-SWAPPED, M-tails ALL NEW 0/16, edges, NO D)
  all verbatim in files. No FLAG/CLAIM/GATE conflict
  on b319. Sweep logs: 28 *319* files present.
- Notes (not slips): (1) wall "1094 added lines" =
  non-blank convention (1100 incl 6 bare-plus); value
  correct, bare-plus disclosed in C-diff leg same
  GATE. (2) aae digest sha1-8 cited per sweep-r41
  style; sha256 stability corroborated (d6e27c97 ==
  r36 + r39 cites).

Agrees with GATE-d52f218d (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r37/
(*319* files).

Verdict: PASS. Ready for parent PV + merge.
