# VERIFY-b8ca9f9b b404 T10P296 pins 119745..120092 (1764 tiers) PASS

Seat viewer-r59, first-hand, tree-b8ca9f9b @b8ca9f9b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r59.
Base d525fb04 (b403, 1758 tiers). Band = d6f51bc4 (py merge
w2b@40052c13 partial, +6 tiers, +62 pins) + b8ca9f9b (C port,
1764 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build404/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 28043d02b041eda3 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  8a299931650ff42f / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8748/8748 covered=8748/8748 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17496/17496 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17496/17496 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17496/17496).
- PINS 17498 rows (2 hdr + 17496, +62 vs base 17436);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  119745 119746 119747 119748 119754 119755 119761 119762
  119763 119764 119767 119768 119771 119772 119773 119788
  119789 119797 119805 119807 119808 119821 119829 119836
  119837 119935 119936 119965 120063 120064 120092
  (== GATE verbatim; S0/S1 (2) + A6 119747/119748/119754/
  119755/119761/119762 + C6 119763/119764/119767/119768/
  119771/119772 + Q10 119773/119788/119789/119797/119805/
  119807/119808/119821/119829/119836 (b5 step o34->o35
  straddled: 119807+119808 both pinned) + R7 119837/
  119935/119936/119965/120063/120064/120092 (both counter
  edges straddled + mid 119965); 8717->8748); 31x2=62 rows,
  range 119745..120092 exact. PINS-new-N == for-added
  31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS: tests/test_aead_units.py NOT runnable here (import
  lz4 ModuleNotFoundError, no repo venv, no pip lz4).
  Band touches no proto/ sources per numstat; environment
  block, NO verdict impact.
- Tables audit own script tabaudit404.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 135 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG/QUAD88-4R/STANDARD ring; no F0/F1, no
  QT/RT/TT; no BM/BC, no M19/XA19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  63501000 SIG-EQ-P295PB0 / 7b80af20 NEW-own-C10 (S0
  31/84 vs P295S0 @ 4-11,13-18,44-47,50,60-71 EXACT +
  cross-P295S1 72, S1-vs-P295S0 68 + vs-P295S1 75).
  AM 16x20ch distinct; AC 76, b0-3 02/00/00/00 (b0 const
  02), no b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x24ch
  10/10 diverge; rows 0-7 share 16ch 1be355f8f58e6f07
  byte8 8-diverge (da/fa/1a/3a/5a/7a/9a/ba), rows 8-9
  share 16ch 737f4df955e51906 byte8 fb/ef; CC 70, b0-3
  7b80af20 const, no b4/b5 (C10-1SIG SAME-as-PB1-sig,
  b5 const a7 via lencode). M 16x16ch distinct. QR 4x22ch
  4-distinct UNPAIRED; r0 bfbd937e55ff42057437ba
  distinct; r123 share 7B 6757b37f75526e, byte7 a5/ca/ef;
  tails b84-87 057437ba/a56fbb3a/ca6fbb3a/ef6fbb3a 4/4
  distinct; r123 TRUE 3B 6fbb3a; byte-LCS (0,*)=0,
  (1,2)=(1,3)=(2,3)=3 (computed first-hand). QC 67,
  b0-3 02000000, no b4/b5, b39 const 6e. RM 16x16ch
  distinct; RQ 16x16ch distinct; RC 70, b0-3 26/00/00/00,
  b84-87 2f/7c/f3/16 ring-wide. M==RQ EXACT 16/16 (lists
  identical). RM-vs-RQ UNPAIRED (sets disjoint). Tails
  STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by ROW,
  16/16 distinct each, 0 overlap). Sorted-unique + _N
  decls 76/70/67/70 match actual. Missing-sets EXACT: AC
  [4,5,18,19,25,26,27,35,80,81,82,83]; CC [4,5,22,23,30,
  31,32,33,34,35,80,81,82,83]; QC [4,5,26,27,34,35,36,37,
  38,40,41,42,43,80,81,82,83,84,85,86,87]; RC [4,5,30,39,
  40,41,42,43,46,47,76,77,78,79,80,81,82,83]. Coverage
  unions exact every block (const U tab U {b4,b5} ==
  88/84/88/88, 0 overlap). Q legs M[m] + QR[q], no frags.
  R legs RM[c] + RQ[r] STANDARD. AC-QC shared-pos 64,
  same-val 31, AConly 12, QConly 3 (== GATE, computed
  first-hand; NOT const-repeat). P295 refs re-read: S0
  63501000 / S1 f2c7a020 / PBA 02000000 / C10-STEP
  86c7a020 / RC 20000000+21e74240 (== A-741/A-358
  Next-P295 preds EXACT x4 + RC consts). P296 preds
  (A-748/A-359 Next-P296: 63501000 sig-eq 31/84 /
  7b80af20 NEW / 02000000 x16 / C10-1SIG 7b80af20 x10)
  x4 corroborated. PBA REPEAT vs P295 (02000000 ==
  02000000). QUAD sig 02000000 x64 (REPEAT). QR/AM/CM/M/
  RM/RQ 0-overlap vs P295 (widths differ AM 20ch vs 14ch,
  CM 24ch vs 22ch, RM 16ch vs 12ch; M/RQ 16ch + QR 22ch
  same width, 0-overlap by content; base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P295 M-tail8 +
  P295 RM-tail8 + P295 RQ-tail8 (overlap 0 x3). Memo INCL
  PBA88 77 / C10 71 / quad88 67 / T88 70 (A-749 re-read):
  impl 76/70/67/70 = memo-1 on PBA/C10 (b5-const excluded),
  identical quad/T88. Base temp maxes _t6160/_b3732/
  _i3733 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 119745 / S1 119746 / A 119747-762 / C 119763-772 /
  Q 119773-836 / R 119837-120092): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + R
  counter b4=(0x3b+2off)&FF b5=0xa8+(off>=99)+(off>=227)
  (py hex; C staged decimal 59/168, re-derived from
  code text both sides) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 10B b18,19,25-27,35,80-83; C 12B b22,23,30-35,80-83;
  Q QM8 b40-43,80-83 + R11 b26,27,34-38,84-87; R TM8
  b30,39,46,47,80-83 by COL + TR8 b40-43,76-79 by ROW)
  + NO frag leg in Q. T-mirrors T80186/80191/80196/
  80212/80228/80249 each re-read: hits the exact py guard
  line. C guards `if ((n) == (119745))` / `(119746)` +
  4 range guards exact. C byte-index lists match py per
  block (A 10B, C 12B, Q 8B/11B, R 8/8B). Temps
  _t6161-6176 continuous (base max _t6160) + _b3734/
  3736/3738/3739/3741/3742 (base max _b3732) + _i3735/
  3737/3740/3743 (base max _i3733): base-tree zero refs
  to new temps prove no reuse. Insert exact both sides:
  after T10P295R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Code comments carry 31/84 +
  46/84 NOT-byte-equal discipline; Q r0-lcs=0 comment
  TRUE (LCS(0,*)=0 first-hand, no b402-style staleness).
  Matches A-749/A-360 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P296 blocks).
- Edges own-loop ownloop404.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P296R N=120092 off=255.
  edges404.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 83/a7, 85/a7 == raw lencode) +
  aform 16/16 (A 88B head 87/a7 tail a5/a7 b5set {a7} NO
  step, 0 ff) + cform 10/10 (C head a7/a7 tail b9/a7
  b5set {a7} NO step, 0 ff) + qform 64/64 + qb5step 64/
  64 (Q head bb/a7 tail 39/a8 b5set {a7,a8} step o34->o35:
  119807 o34 ff/a7 -> 119808 o35 01/a8, exactly 1 ff in
  64 at o34; quad b4 base bb step2 == raw-lencode 64/64);
  ring counter 256/256 + ringraw 256/256 (head 3b/a8;
  119935 off98 ff/a8 -> 119936 off99 01/a9; mid off226
  ff/a9 at 120063 -> 120064 off227 01/aa; tail off255
  39/aa; exactly 2 ff in 256 at o98/o226; Q tail 39/a8
  vs R tail 39/aa differ in b5 -- labeled apart);
  odd-lencode 348/348. Ring edges + tail 120092 in
  for-list + 2 PASS lines each py+C. Tail 120092:
  oracle sha abf1b6b6cf670a76... matches PINS; py+C
  CLOSED T10P296R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf404.py (cache path) + secf404b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (119745 +
  119397 + 119746 + 119398); S0: oracle119745-vs-119397
  31/84, codeS0-vs-P295S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1-vs-own-C10-head secf404c.py: cache
  46/84 + DIRECT 46/84, positions identical, cache==
  direct payload (sig 7b80af20 vs 7b80af20 sig-eq, NOT
  byte-equal). 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. A-749 + w2b NOTE correction of A-360 stale
  byte-equal prose VINDICATED (9th standing-rule hit);
  byte-diff discipline observed throughout.
- C diff pure-add: numstat 604/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 231
  content / 0 del. Fine-norm: C-tempnorm (temp-norm,
  empty-excluding) del-uniq 0 add-uniq 402 missing 0 ==
  GATE EXACT (this GATE states the temp-norm recipe
  explicitly); full-digit norm C 149 / py 167 recorded.
  del-subset-add 0 missing holds (integrity intact).
- Wall on band diff added lines (scope d525fb04..
  b8ca9f9b, 898 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (d6f51bc4), code 6 blocks,
  py top-level singletons (^4sp `if n == `) 614->616 +2
  == GATE stated-method EXACT, py T10P range guards
  614->618 +4 == GATE EXACT, CLOSED T10P prints 1664->
  1670 +6 py + 1664->1670 +6 C, C top-level singleton
  `if ((n) == (` 614->616 +2 == GATE EXACT / C top-level
  ranges `if ((N) <= (n)` 614->618 +4 == GATE EXACT
  (broad-C nested 8-space extras 5 singletons + 22 ranges
  outside dispatch scope, standing bookkeeping), seal
  1758->1764 +6 (commit msgs): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-749-q888-
  t10p296 verdict CONFIRM, tallies 14/14 + 11/11 + 14/14
  = 39/39 arith-consistent as-filed (file present, read in
  full; self-correction note: first batch 38/39 with
  check-text FAIL on quad-b8487-4distinct, isolated
  re-check + full re-run clean 39/39 -- memo-internal
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0 sig-eq + 31/84 + PB1 NEW +
  46/84, PBA88-PLAIN, C10-1SIG, QUAD88-4R + R11 rows +
  7B-share + r123-TRUE-3B + r0-lcs0 + b5 step + edge +
  M-tails NEW, ring STANDARD + TM8/TR8 16/16 UNPAIRED +
  edges + consts (all re-checked above) + A-360 viewer
  corroboration (CONFIRM all legs, consts 77/71/67/70
  INCL; S0 byte-equal prose STALE per w2b correction,
  geometry unaffected). No CONFIRM-P296.md file (absence
  verified via quiz poll); A-749 suffices per rule. Agrees
  with cport commit msg (PYID 8748, RGRAM 17496).
- Quiz: no conflicting CLAIM/GATE/FLAG on b404 (own seat
  CLAIM only; NO-FLAG greps first-hand). Newest
  PARENT-QNUM-23 (w2b Q-block 1600-1639 grant, read, no
  gate impact) -- GATE cites no QNUM (no staleness).
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (norm recipe stated explicitly this
band, temp-norm 402 reproduced EXACT with no variant
gap; tier recipes reproduced EXACT via dispatch-guard
reading).
Next-P297 predictions banked (A-749/A-360: PB0 @120093
66501000 NEW + PB1 7b802f23 NEW @120094 + PBA88 02000000
x16 @120095-110 + C10-3SIG 7b802f23 x8 @120111-18 +
7b808f1d @120119 + 7b80cf1c @120120 ORDERED 8/1/1).
