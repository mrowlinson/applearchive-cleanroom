# VERIFY-c9b64be1 b415 T10P307 pins 123573..123920 (1830 tiers) PASS

Seat viewer-r61, first-hand, tree415 @c9b64be1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r61.
Base 0dd1dddf (b414, 1824 tiers). Band = a694751f (py merge
w2b@dae68b44 partial, +6 tiers, +62 pins) + c9b64be1 (C port,
1830 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117 = 113 non-tmp + 4 tmp).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build415/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ce7b736ca026fe4c / aae
  d6e27c97ced21673 + sha1 rgramc d345b89faebb3dbc / aae
  7d8dd3a2d118e0db (aae == GATE both; rgramc DIFFERS from
  GATE-claimed 0abce382/8f4c2da1 -- see prose note: BOTH
  real binaries agree (sweep's own r65/build415/rgramc ==
  seat binary, sha256-equal), source blob-verified
  (tree rgramc.c sha256 916863bc == git blob); the gated
  artifact is identical to the verified artifact; code
  GREEN, all behavior legs below run first-hand against
  the seat binary).
- RGRAMC-PYID 9091/9091 covered=9091/9091 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 18182/18182 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 18182/18182 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 18182/18182; GATE
  claims sorted only, raw corroborated too).
- PINS 18184 rows (2 hdr + 18182, +62 vs base 18122);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  123573 123574 123575 123576 123582 123583 123589 123590
  123591 123592 123595 123596 123599 123600 123601 123609
  123617 123625 123633 123641 123647 123648 123649 123664
  123665 123775 123776 123793 123903 123904 123920
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 123593/123594/
  123597/123598 unsampled, absence verified) + Q10 offs
  0,8,16,24,32,40,46,47,48,63 (head + 5 mids + b5-step
  edge-pair 123647/123648 + off48 123649 + tail 123664)
  + R7 offs 0,110/111,128,238/239,255 (head + both
  counter edges straddled + mid 123793 + tail);
  9060->9091); 31x2=62 rows, range 123573..123920 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60/r61 b412-
  b414); band diffs touch no proto/ sources (numstat
  proves), NO verdict impact.
- Tables audit own script tabaudit415.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 154 PASS
  0 FAIL. Inventory exactly the 13 both sides (PBA88-
  PLAIN/C10-1SIG/QUAD88-4R-FRAG/RING-STANDARD + F; no
  F0/F1, no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM,
  no M42/X42/H42/L42); C==py 13/13. S0/S1 168ch sigs
  ab687400 NEW / 803b4f44 NEW NOT-PB1-sig (S0 30/84 vs
  P306S0 @ 0-2,4-10,13-19,24,64-75 EXACT + cross-P306S1
  32, S1 49/84 vs P306S1 @ 1-5,12-39,52-55,68-75,80-83
  EXACT + cross-P306S0 64). AM 16x16ch distinct; AC 78,
  b0-3 05/00/00/00 (b0 const 05), no b4/b5, PBA sig
  05000000 x16 PLAIN (NEW sig 05). CM 10x22ch 10/10
  diverge; CC 71, b0-3 803b4f84, no b4/b5 (b5 const c5
  via lencode); C10-1SIG x10 NOT-PB1-sig (S1 803b4f44
  differs). M 16x12ch distinct. F 16x2ch 2-distinct
  {10,90}, sequence 90 10 90 10 90 90 10 90 90 10 90
  90 10 10 90 10 EXACT == memo. QR 4x20ch 4-distinct
  UNPAIRED; r0 5c5c471c92184c3c8f8d distinct; r123
  share 12ch 42dc42e872fd; tails b84-87 4c3c8f8d/
  63696b0a/88696b0a/ad696b0a 4/4 distinct; r123 ALL
  TRUE 3B 696b0a; full-row lcsuf r123 pairs 3,
  r0-vs-rest 0 + lcpre r123 6, r0-vs-rest 0 +
  lcsubstr r0-vs-rest 0 (r0 lcs=0 holds ALL senses --
  no LCS subtlety this tier). QC 69, b0-3 09000000,
  no b4/b5 (QUAD single-sig x64). RM 16x20ch distinct;
  RQ 16x14ch distinct; RM-vs-RQ UNPAIRED (sets
  disjoint); RC 69, b0-3 93/00/00/00, b84-87 1f/f2/0e/
  c5 ring-wide. M-ne-RQ lists; SHIFT all cells (M 6B
  vs RQ 7B: agree (0,0),(1,2),(2,3),(3,4),(4,5),(5,6)
  16/16; ALL off-pattern cells 0/16 -- zero off-pattern
  incidentals HOLDS exactly; M[1:6]==RQ[2:7] all16;
  RQ[1] isolated maxagree 0/16 2-distinct 18/98 x7/x9,
  RQ[0] 2-distinct 78/f8 x4/x12, RQ[2] 13-distinct).
  Tails STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by
  ROW, 16/16 distinct each, 0 overlap). Sorted-unique +
  _N decls 78/71/69/69 match actual. Missing-sets EXACT:
  AC [4,5,40-43,80-83]; CC [4,5,36-42,80-83]; QC [4,5,
  38,40-47,80-87]; RC [4,5,38,46,47,50-55,76-83].
  Coverage unions exact every block (const U tab U
  {b4,b5} == 88/84/88/88, 0 overlap). Q legs M[m] +
  QR[q] + FRAG F[m] both sides. R legs RM[c] + RQ[r]
  both sides, NO F-legs. AC-QC shared-pos 69, same-val
  25, AConly 9, QConly 0 (computed first-hand). P306
  refs re-read: S0 db1b7900 / S1 80120ffa / PBA
  0f000000 / C10-1SIG 803b4fc4 / QUAD 0f000000 x64.
  Next-P307 preds (A-782 re-read: PB0 ab687400 NEW /
  PB1 803b4f44 NEW / PBA88 05000000 x16 / C10-1SIG
  803b4f84 x10 NOT-PB1-sig) x4 corroborated. PBA NEW
  vs P306 (05000000 != 0f000000). AM/CM/M/QR/RM/RQ
  0-overlap vs P306 (widths P307 AM16/CM22/M12/QR20/
  RM20/RQ14 vs P306 AM16/CM24/M16/QR22/RM18/RQ16;
  same-width AM pair 0-overlap by content; base widths
  re-read first-hand). M-tails 16/16 ALL NEW vs P306
  RM-tail8 + RM-tails NEW vs P306 RM + RQ-tails NEW vs
  P306 RQ + cross overlaps 0 (P306T widths RM 9B/RQ 8B
  re-read). Memo INCL PBA88 79 / C10 72 / quad88 69 /
  T88 69 (A-787 re-read): impl 78/71/69/69 = memo-1 on
  PBA/C10 (b5-const excluded), identical quad/T88 (b5
  varies/counter) -- standing +1 rule coherent, +1/+1/
  +0/+0. Base temp maxes _t6340/_b3842/_i3843 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 123573 / S1 123574 / A 123575-590 / C 123591-600 /
  Q 123601-664 / R 123665-920): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-const/step emerges from raw lencode) +
  FRAG b46 coltab+ADD3 BOTH sides (py: q==0 ftab
  ("%02x" % pay[46]) vs F[m], else fadd3 pay[46] ==
  (F[m]+3)&FF; C: snprintf-hex vs F[m], else pay[46] ==
  (hexval(F[m])+3)&FF; ADD constant 3 derived from code
  text both sides -- FIRST ADD3) + R counter b4=(0x23+
  2off)&FF b5=0xc6+(off>=111)+(off>=239) (py hex; C
  staged decimal 35/198, re-derived from code text both
  sides: 35==0x23, 198==0xc6) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A 8B b40-43,80-83; C 11B b36-42,
  80-83; Q QM6 b38,47,80-83 + R10 b40-45,84-87; R TM10
  b50-55,80-83 by COL + TR7 b38,46,47,76-79 by ROW) +
  C guards `if ((n) == (123573))` / `(123574)` + 4
  range guards exact + C byte-index lists match py per
  block (A 8B, C 11B, Q 6B/10B, R 10B/7B). T-mirrors
  T82787/82792/82797/82812/82828/82854 each re-read:
  hits the exact py guard line. Temps _t6341-6358
  continuous-18 (base max _t6340; FRAG legs take 2
  extra) + _b3844/3846/3848/3849/3851/3852 (base max
  _b3842) + _i3845/3847/3850/3853 (base max _i3843):
  added-only, no reuse. Insert exact both sides: P306R
  block precedes, at dispatch tail (N-out-of-scope
  fallthrough follows; 2 scope hits py + 2 scope hits
  C). Matches A-787 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P307 blocks).
- Edges own-loop ownloop415.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P307R N=123920
  off=255. edges415.py: paylens 12x84 + 336x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 6b/c5, 6d/c5
  == raw lencode) + aform 16/16 (A head 6f/c5 tail
  8d/c5 b5set {c5} NO step, 0 ff) + cform 10/10 (C
  head 8f/c5 tail a1/c5 b5set {c5} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head a3/c5, edge
  o46->o47 123647->123648 ff/c5->01/c6, off48 03/c6,
  tail 21/c6, b5set {c5,c6}, exactly 1 ff in 64 at
  o46; quad b4 base 0xa3 step2 == raw-lencode 64/64);
  ring counter 256/256 + ringraw 256/256 (head 23/c6;
  123775 off110 ff/c6 -> 123776 off111 01/c7; mid
  off128 23/c7 at 123793; 123903 off238 ff/c7 ->
  123904 off239 01/c8; tail off255 21/c8; exactly 2
  ff in 256 at o110/o238); ff total x3 (123647 Q-step
  + 2 ring). odd-lencode 92+256=348/348. Ring edges +
  tail 123920 in for-list + 2 PASS lines each py+C.
  Tail 123920: oracle sha d48ee749c97cc315... matches
  PINS (rawlen 104 re-checked: paylen 88 + 12 + 4);
  py+C CLOSED T10P307R off=255 agree. No DISSENT: cut
  bytes verify.
- FRAG oracle leg frag415.py (staged F vs oracle
  pay[46] over all 64 Q Ns): F-C==py; ftab 16/16
  (q==0) + fadd3 48/48 (q>0) rc=0; oracle r0!=r123
  48/48. FIRST ADD3 corroborated against oracle.
- PB-diff secf415.py (cache path) + secf415b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (123573 +
  123225 + 123574 + 123226); S0: oracle123573-vs-123225
  30/84, codeS0-vs-P306S0 30/84, positions identical;
  DIRECT tool 30/84 with identical agree-pos 54
  positions. S1: oracle123574-vs-123226 49/84,
  codeS1-vs-P306S1 49/84, positions identical; DIRECT
  49/84 identical agree-pos 35 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs.
  S1-vs-own-C10 secf415c.py: 27/84 TRUE-UNIFORM all 10
  ([0] n123591 27/84 @ b3,4,14,15,22,23,30,32-43,76-83
  == GATE EXACT; counts [27]x10 AND positions identical
  all 10 -- verified beyond GATE's cell0; sig 803b4f44
  vs 803b4f84 differs, NOT byte-equal). Byte-diff
  discipline observed throughout, nothing to refute.
- C diff pure-add: numstat 634/0 (rgramc.c) + 254/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 629 content + 5 bare-blank / 0 del (see prose
  note: GATE writes "634 content"); raw py 254 content
  / 0 del. Full-digit norm ([0-9]+ -> N): C del-uniq 0
  add-uniq 156 missing 0 under the recipe AS STATED
  (diff-sign strip + trailing-';' strip, NO whitespace
  handling stated); GATE's 151 reproduces iff leading-
  whitespace-stripped AND empty-excluded (strip+
  dropempty 151, strip-only 152, dropempty-only 155 --
  recipe variant gap, same class as b405/b407/b409/b411/
  b413; see prose note); py del-uniq 0 add-uniq 176
  missing 0 == GATE EXACT (variant-insensitive: 176
  all four variants). del-subset-add 0 missing holds
  every variant (integrity intact). C-tempnorm 458 /
  py-tempnorm 216 recorded (no GATE claim).
- Wall on band diff added lines (scope 0dd1dddf..
  c9b64be1, 951 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 634/0, rgram.py 254/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (a694751f), code 6 blocks,
  tier-comments `# T10P` 1730->1736 +6 == GATE stated-
  method EXACT, singletons `if n == ` 646->648 +2 ==
  GATE EXACT, range-guards `<= n <=` 680->684 +4 ==
  GATE EXACT, CLOSED T10P prints 1730->1736 +6 py +
  1730->1736 +6 C == GATE EXACT, C singleton
  `if ((n) == (` 641->643 +2 == GATE EXACT (5-count
  C-vs-py offset pre-existing, unchanged: 646-641 =
  648-643 = 5), C ranges 680->684 +4 == GATE EXACT,
  seal 1824->1830 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1830-1736 = 94, stable b401-b415): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-787-q899-P307
  verdict CONFIRM, tallies 27/27 + 17/17 + 14/14 =
  58/58 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 NEW diff-own-C10,
  PBA88-PLAIN sig-05 M8, C10-1SIG NOT-PB1 M11,
  QUAD88-4R-FRAG + R10 rows + 6B-share + r123-TRUE-3B
  + F-seq + ADD3 + M-tails NEW, T88-RING-STANDARD +
  TM10/TR7 16/16 UNPAIRED + SPLIT tails + b84-87
  1ff20ec5 + edges + consts 23/c6/111/239 + lencode
  348/348 + VPOS 9/12/19/19 (all re-checked above;
  "4th FRAG shape" ordinal + priors list beyond
  first-hand window -- corroborated only that THIS
  band is single-F +ADD3, not disputed). Sheet-vs-
  tables const-count note: Q-899 sheet rule 79/72/69/
  69 memo-exact (4th straight fully clean w2b sheet
  per memo; w2b-r25 round cap 8/8), committed tables
  78/71/69/69 still deduct const-b5 in PBA/C10 -- 10th
  consecutive tables-lag band (geometry exact, PORT
  verdict stands). No viewer P307 geometry answer on
  file at gate time (memo-only recon; this VERIFY is
  the viewer record). No CONFIRM-P307.md file (absence
  verified); A-787 suffices per rule. Agrees with cport
  commit msg (PYID 9091, RGRAM 18182).
- Quiz: no conflicting CLAIM/GATE/FLAG on b415 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-22 newest -- TRUE at filing time (GATE 14:09,
  QNUM-23 14:51 postdates it): NO staleness. PROSE-01:
  all hex/counts above copied from own run output;
  GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 4 prose-level notes (build rgramc hashes
8f4c2da1/0abce382 UNGROUNDED: both real binaries agree
on d345b89f/ce7b736c from blob-verified source, and the
claimed values appear NOWHERE except the GATE file
itself -- no battery-output provenance, PROSE-01
copy-from-output violation; code GREEN since gated
artifact == verified artifact; "raw C 634 content + 5
blank-only" reads 634+5=639 vs numstat 634 -- first-hand
is 629 content + 5 bare-blank = 634 (2nd instance after
b413, same sweep-r65 token); norm-151 recipe variant
gap: stated recipe yields 156, strip+dropempty yields
the claimed 151 -- integrity holds every variant, same
class as b405/b407/b409/b411/b413; "third TRUE-uniform
case after P299 + P303": P306 in this round is 28/84
count-AND-position uniform (verified first-hand beyond
GATE's cell0, positions-identical all 10) and r60's
filed P300 record is 56/84 uniform -- P307 is FIFTH on
record (4th excluding unverified P299), so the ordinal
holds only under a narrower scope the GATE doesn't
state). 25th odd-band RQ==M instance corroborated as
SHIFT (shift-6 identity + RQ[1]-isolated + heads-own
distinctness 2/2/13; NEW variant joining neither prior
group; memo-silent on the relation; even/odd convention
holds: b414 even EXACT takes no ordinal). Next-P308
SHAPE NOVELTY banked (A-787 re-read: PB1 + C10-region
88B-pay @123922/123939-48, 12x84B pattern breaks; shape
TBD P308 census r26; P308 pins start @123921).
