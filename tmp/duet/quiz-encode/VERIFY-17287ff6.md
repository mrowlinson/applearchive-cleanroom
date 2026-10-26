# VERIFY-17287ff6 b405 T10P297 pins 120093..120440 (1770 tiers) PASS

Seat viewer-r59, first-hand, tree-17287ff6 @17287ff6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r59.
Base b8ca9f9b (b404, 1764 tiers). Band = 823f4d45 (py merge
w2b@7e38535a partial, +6 tiers, +62 pins) + 17287ff6 (C port,
1770 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; base re-archived clean after b404
__pycache__ byproduct taint).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build405/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 16b677d12e53abcb / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  e0f33ba3c426eb51 / aae 7d8dd3a2d118e0db (== GATE both).
- RGRAMC-PYID 8779/8779 covered=8779/8779 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17558/17558 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17558/17558 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17558/17558).
- PINS 17560 rows (2 hdr + 17558, +62 vs base 17498);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  120093 120094 120095 120096 120102 120103 120109 120110
  120111 120112 120115 120118 120119 120120 120121 120128
  120136 120137 120145 120153 120161 120169 120176 120184
  120185 120191 120192 120313 120319 120320 120440
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,7,8,9 (offs 2,3,5,6 = 120113/120114/
  120116/120117 unsampled) + Q10 offs 0,7,15/16,24,32,40,
  48,55,63 (b5 const, NO step) + R7 offs 0,6/7,128,134/
  135,255 (both counter edges straddled); 8748->8779);
  31x2=62 rows, range 120093..120440 exact. PINS-new-N ==
  for-added 31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit405.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 141 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-3SIG/QUAD88-4R/STANDARD ring; no F0/F1, no
  QT/RT/TT; no BM/BC, no M19/XA19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  66501000 NEW / 7b802f23 NEW (S0 32/84 vs P296S0 @
  0,4,5,11,18-27,29,32,34-37,52-55,72-79 EXACT +
  cross-P296S1 55, S1 49/84 vs P296S1 @ 2-5,21-24,
  26-51,53-55,72-83 EXACT + cross-P296S0 72). AM
  16x14ch distinct; AC 79, b0-3 02/00/00/00 (b0 const
  02), no b4/b5, PBA sig 02000000 x16 PLAIN. CM 10x26ch
  10/10 diverge; heads 2f23 x8 + 8f1d + cf1c ORDERED
  8+1+1; CC 69, b0,b1 7b,80 const, b2,3 in tab
  (partial sig), no b4/b5 (C10-3SIG 7b802f23 x8 +
  7b808f1d + 7b80cf1c, b5 const aa via lencode). M
  16x14ch distinct. QR 4x24ch 4-distinct UNPAIRED; r0
  d8f34ef5f1a04ff097eaadda distinct; r12 share 8B
  e67394c411df5fd3 (lcpre 8); r123 lcpre 4B e67394c4;
  r03 lcpre 0; r3 e67394c451df5fd384ecbe72; tails
  b84-87 97eaadda/1f70534f/cc2a3761/84ecbe72 4/4
  distinct; full-row lcsuf 0 ALL pairs + tail-lcsuf 0
  ALL pairs (computed first-hand, FIRST). QC 67, b0-3
  01000000, no b4/b5. RM 16x16ch distinct; RQ 16x14ch
  distinct; RC 71, b0-3 1e/00/00/00, b84-87 be/38/e6/
  5b ring-wide. M==RQ EXACT 16/16 (lists identical);
  agree-matrix diag 16/16 x7/7, off-diag max 3 at
  exactly (9,12)+(12,9), dist {0:72,1:124,2:42,3:2}
  (FULL7 degree corroborated; see prose note on GATE's
  "only"). RM-vs-RQ UNPAIRED (sets disjoint). Tails
  STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by ROW,
  16/16 distinct each, 0 overlap). Sorted-unique + _N
  decls 79/69/67/71 match actual. Missing-sets EXACT: AC
  [4,5,52,53,54,80,81,82,83]; CC [2,3,4,5,35,46,47,48,
  49,50,51,80,81,82,83]; QC [4,5,6,7,11,12,39,50,51,52,
  53,54,55,80,81,82,83,84,85,86,87]; RC [4,5,6,7,9,10,
  11,12,20,76,77,78,79,80,81,82,83]. Coverage unions
  exact every block (const U tab U {b4,b5} == 88/84/88/
  88, 0 overlap). Q legs M[m] + QR[q], no frags. R legs
  RM[c] + RQ[r] STANDARD. AC-QC shared-pos 67, same-val
  44, AConly 12, QConly 0 (computed first-hand; NOT
  const-repeat). P296 refs re-read: S0 63501000 / S1
  7b80af20 / PBA 02000000 / C10-1SIG 7b80af20 (==
  A-749/A-360 Next-P296 preds EXACT x4). P297 preds
  (A-749/A-360 Next-P297: 66501000 NEW / 7b802f23 NEW /
  02000000 x16 / C10-3SIG 8+1+1 ORDERED) x4 corroborated.
  PBA REPEAT vs P296 (02000000 == 02000000). QUAD sig
  01000000 x64 (back to 01 after P296 02). QR/AM/CM/M/
  RM/RQ 0-overlap vs P296 (widths differ AM 14ch vs 20ch,
  CM 26ch vs 24ch, M 14ch vs 16ch, QR 24ch vs 22ch, RQ
  14ch vs 16ch; RM 16ch same width, 0-overlap by content;
  base widths re-read first-hand). M-tails 16/16 ALL NEW
  vs P296 M-tail8 + P296 RM-tail8 + P296 RQ-tail8
  (overlap 0 x3); RM-tails NEW vs P296 RM tails + RQ-
  tails NEW vs P296 RQ tails + cross overlaps 0. Memo
  INCL PBA88 80 / C10 70 / quad88 68 / T88 71 (A-752/
  A-361 re-read): impl 79/69/67/71 = memo-1 on PBA/C10/
  quad (b5-const excluded), identical T88 -- standing +1
  rule coherent (A/C/Q single-const b5 -> +1, T counter
  -> +0; Q-const +1 per P295 precedent, C-const +1 now
  on 3SIG). Base temp maxes _t6176/_b3742/_i3743
  (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 120093 / S1 120094 / A 120095-110 / C 120111-120 /
  Q 120121-184 / R 120185-440): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + R
  counter b4=(0xf3+2off)&FF b5=0xaa+(off>=7)+(off>=135)
  (py hex; C staged decimal 243/170, re-derived from
  code text both sides) + m=off&15/q=off>>4/c=off&15/
  r=off>>4 both sides + mtab/rtab byte positions exact
  (A 7B b52-54,80-83; C 13B b2,3,35,46-51,80-83 M13; Q
  QM7 b6,7,12,80-83 + R12 b11,39,50-55,84-87; R TM8
  b9,10,11,20,80-83 by COL + TR7 b6,7,12,76-79 by ROW)
  + NO frag leg in Q. T-mirrors T80418/80423/80428/
  80443/80459/80480 each re-read: hits the exact py guard
  line. C guards `if ((n) == (120093))` / `(120094)` +
  4 range guards exact. C byte-index lists match py per
  block (A 7B, C 13B, Q 7B/12B, R 8B/7B). Temps
  _t6177-6192 continuous (base max _t6176) + _b3744/
  3746/3748/3749/3751/3752 (base max _b3742) + _i3745/
  3747/3750/3753 (base max _i3743): base-tree zero refs
  to new temps prove no reuse. Insert exact both sides:
  after T10P296R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Code comments M13 both sides
  confirm memo label over A-361 "M12" slip. Q comment
  "r1/r2 share 6B-prefix" both sides is memo-partial
  phrasing (first-hand lcpre 8; technically true,
  imprecise) -- comment-only, code GREEN. Matches
  A-752/A-361 geometry (values re-checked in audit
  above; NO D dips: ownloop tags exactly the 6 P297
  blocks).
- Edges own-loop ownloop405.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P297R N=120440 off=255.
  edges405.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 3b/aa, 3d/aa == raw lencode) +
  aform 16/16 (A 88B head 3f/aa tail 5d/aa b5set {aa} NO
  step, 0 ff) + cform 10/10 (C head 5f/aa tail 71/aa
  b5set {aa} NO step, 0 ff) + qform 64/64 + qb5const 64/
  64 (Q head 73/aa tail f1/aa b5set {aa} NO step, 0 ff;
  quad b4 base 73 step2 == raw-lencode 64/64); ring
  counter 256/256 + ringraw 256/256 (head f3/aa; 120191
  off6 ff/aa -> 120192 off7 01/ab; mid off128 f3/ab at
  120313; 120319 off134 ff/ab -> 120320 off135 01/ac;
  tail off255 f1/ac; exactly 2 ff in 256 at o6/o134);
  odd-lencode 348/348. Ring edges + tail 120440 in
  for-list + 2 PASS lines each py+C. Tail 120440:
  oracle sha b09ff02a661bdb8b... matches PINS (rawlen
  104 re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P297R off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf405.py (cache path) + secf405b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (120093 +
  119745 + 120094 + 119746); S0: oracle120093-vs-119745
  32/84, codeS0-vs-P296S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle120094-vs-119746 49/84,
  codeS1-vs-P296S1 49/84, positions identical; DIRECT
  49/84 identical agree-pos 35 positions. 0 miss
  (ownloop pre-warmed). Twice-derived both pairs. Both
  NEW strings, no byte-equal wording anywhere this band
  -- byte-diff discipline observed, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 231/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 231
  content / 0 del. Full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 148 missing 0 under the recipe AS
  STATED; GATE's 144 reproduces iff leading-whitespace-
  stripped AND empty-excluded (strip+dropempty 144,
  strip-only 145, dropempty-only 147 -- recipe variant
  gap, see prose note); py del-uniq 0 add-uniq 167
  missing 0 == GATE EXACT (variant-insensitive: 167 all
  four variants). del-subset-add 0 missing holds every
  variant (integrity intact). C-tempnorm 396 / py-
  tempnorm 190 recorded (no GATE claim).
- Wall on band diff added lines (scope b8ca9f9b..
  17287ff6, 898 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 231/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (823f4d45), code 6 blocks,
  tier-comments `# T10P` 1670->1676 +6 == GATE stated-
  method EXACT, singletons `if n == ` 626->628 +2 ==
  GATE EXACT, range-guards `<= n <=` 640->644 +4 ==
  GATE EXACT, CLOSED T10P prints 1670->1676 +6 py +
  1670->1676 +6 C, C singleton `if ((n) == (` 621->623
  +2 == GATE EXACT (5-count C-vs-py offset pre-existing,
  unchanged), C ranges 640->644 +4 == GATE EXACT, seal
  1764->1770 +6 (commit msgs; offset +94 vs CLOSED-T10P:
  1770-1676 = 94): all agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-752-q889-P297
  verdict PORT (tallies 24/24 + 12/12 + 11/14 = 47/50
  arith-consistent as-filed; the 3 non-confirm = §F
  const-count writer arithmetic, geometry exact -- memo-
  internal methodology note, NO verdict impact) + exact-
  value corroboration incl PB0/PB1 NEW, PBA88-PLAIN,
  C10-3SIG 8+1+1 ORDERED, QUAD88-4R + R12 rows + M-tails
  NEW, ring STANDARD + TM8/TR7 16/16 UNPAIRED + edges +
  consts (all re-checked above) + A-361 viewer
  corroboration (CONFIRM all legs, consts 80/70/68/71
  INCL; "M12" label slip + "share 6B" partiality already
  flagged in GATE recon, code M13 + first-hand 8B
  confirm). No CONFIRM-P297.md file (absence verified);
  A-752 suffices per rule. Agrees with cport commit msg
  (PYID 8779, RGRAM 17558).
- Quiz: no conflicting CLAIM/GATE/FLAG on b405 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-21 newest; QNUM-22 + QNUM-23 both read FULL
  first-hand (pure w2e/w2b Q-block grants, no gate
  impact) -- standing-pattern staleness, immaterial.
  PROSE-01: all hex/counts above copied from own run
  output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes (norm-144 recipe variant gap:
stated recipe yields 148, strip+dropempty yields the
claimed 144 -- integrity holds every variant;
agree-matrix "only" = max-only, 166 off-diag pairs
agree 1-2B -- FULL7 diag corroborated EXACT; QNUM-21
staleness -- immaterial standing pattern). 20th odd-band
RQ==M instance corroborated as FULL7 NEW (tab equality
head-same + tails-cross value-equal).
Next-P298 predictions banked (A-752/A-361: PB0 @120441
36721e00 NEW + PB1 d46ce43c NEW @120442 + PBA88 03000000
x16 @120443-58 + C10 cb56e43c x8 + 0b2cfa3c + 2b8be43c
@120459-68 ORDERED 8/1/1).
