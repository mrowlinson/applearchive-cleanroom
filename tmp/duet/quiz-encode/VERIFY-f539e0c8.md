# VERIFY-f539e0c8 b413 T10P305 pins 122877..123224 (1818 tiers) PASS

Seat viewer-r61, first-hand, tree413 @f539e0c8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r61.
Base 05055220 (b412, 1812 tiers). Band = e53a773d (py merge
w2b@c942f03b partial, +6 tiers, +62 pins) + f539e0c8 (C port,
1818 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117 = 113 non-tmp + 4 tmp).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build413/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ad486bdfb869b6fc / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  3b8cd518b9cabdfb / aae 7d8dd3a2d118e0db (== GATE both).
- RGRAMC-PYID 9029/9029 covered=9029/9029 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 18058/18058 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 18058/18058 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 18058/18058).
- PINS 18060 rows (2 hdr + 18058, +62 vs base 17998);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0 (4-way set-eq). For-list
  delta vs base +31/-0:
  122877 122878 122879 122880 122886 122887 122893 122894
  122895 122896 122899 122900 122903 122904 122905 122913
  122921 122929 122937 122945 122953 122961 122967 122968
  122969 123007 123008 123097 123135 123136 123224
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,5,8,9 (offs 2,3,6,7 = 122897/122898/
  122901/122902 unsampled, absence verified) + Q10 offs
  0,8,16,24,32,40,48,56,62,63 (head + 7 mids + tail pair
  122967/122968) + R7 offs 0,38/39,128,166/167,255 (head
  + both counter edges straddled + mid 123097 + tail);
  8998->9029); 31x2=62 rows, range 122877..123224 exact.
  PINS-new-N == for-added 31/31, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60/r61 b412);
  band diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit413.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 150 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  STEP/C10-1SIG/QUAD88-2SIG/RING-STANDARD; no F/F0/F1,
  no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  db1b7900 NEW / 80299f81 NEW ==own-C10-sig (S0 38/84 vs
  P304S0 @ 0-2,4,5,11,19-39,52-55,72,74-79 EXACT +
  cross-P304S1 55, S1 62/84 vs P304S1 @ 0-5,11-19,21-55,
  72-83 EXACT + cross-P304S0 78). AM 16x18ch distinct;
  AC 77, b0-3 09/00/00/00 (b0 const 09), no b4/b5, PBA
  sig 09000000 x16 STEP (NEW sig 09). CM 10x22ch 10/10
  diverge; CC 71, b0-3 80299f81, no b4/b5 (b5 const c0
  via lencode); C10-1SIG x10 SAME-as-PB1-sig (S1 sig-eq
  own C10). M 16x14ch distinct. QR 4x24ch 4-distinct
  UNPAIRED; r0 04fa935ef1e90fd86435c2fa [b0=04]
  distinct; r123 share 16ch 0808120e51f14f82 [b0=08];
  tails b84-87 6435c2fa/eeaf4f2a/13b04f2a/d4ed1b48 4/4
  distinct; r1r2 pair-only 2B 4f2a; full-row lcsuf
  r1r2=2 else 0 + lcpre r123 8, r0-pairs 0 (r0 lcs=0
  vs all AND r3 lcs=0 vs all suffix-sense; r3 shares
  the 8B prefix). QC 67, NO b0 (2SIG b0 row-led in R
  tab), no b4/b5 (QUAD 2SIG row0 04000000 x16 +
  rows1-3 08000000 x48). RM 16x14ch distinct; RQ
  16x14ch distinct; RM-vs-RQ UNPAIRED (sets disjoint);
  RC 72, b0-3 84/00/00/00, b84-87 c3/72/80/2f ring-wide.
  M-ne-RQ lists; DIAG6 all cells (M 7B vs RQ 7B:
  agree (0,0),(1,1),(3,3),(4,4),(5,5),(6,6) 16/16;
  ALL off-pattern cells 0/16 -- zero off-pattern
  incidentals HOLDS exactly; RQ[2] isolated maxagree
  0/16 2-distinct f4/f5 x7/x9, RQ[0] 15-distinct (49
  x2), RQ[1] 5-distinct (b7/b8/b6 x4, b5 x3, b9 x1)).
  Tails STANDARD-SPLIT (RM b80-83 by COL, RQ b76-79 by
  ROW, 16/16 distinct each, 0 overlap). Sorted-unique +
  _N decls 77/71/67/72 match actual. Missing-sets EXACT:
  AC [4,5,51-55,80-83]; CC [4,5,15,46-51,80-83]; QC [0,
  4,5,6,7,12,19,50-55,80-87]; RC [4,5,6,7,9,13,14,15,
  76-83]. Coverage unions exact every block (const U
  tab U {b4,b5} == 88/84/88/88, 0 overlap). Q legs M[m]
  + QR[q] both sides, NO F-legs either region both
  sides. R legs RM[c] + RQ[r] both sides. AC-QC shared-
  pos 67, same-val 43, AConly 10, QConly 0 (computed
  first-hand; QC const positions subset of AC -- FIRST
  QConly-0). P304 refs re-read: S0 0b913100 / S1
  db1b7929 / PBA 02000000 / C10-1SIG 80299f41 / QUAD
  05000000 x64. Next-P305 preds (A-777 re-read: PB0
  db1b7900 NEW / PB1 80299f81 NEW sig-eq-own-C10 /
  PBA88 09000000 x16 NEW sig 09 / C10-1SIG 80299f81 x10
  SAME-as-PB1-sig) x4 corroborated. PBA NEW vs P304
  (09000000 != 02000000). AM/CM/M/QR/RM/RQ 0-overlap vs
  P304 (widths P305 AM18/CM22/M14/QR24/RM14/RQ14 vs P304
  AM16/CM26/M14/QR22/RM14/RQ14; same-width M/RM/RQ
  pairs 0-overlap by content; base widths re-read
  first-hand). M-tails 16/16 ALL NEW vs P304 RM-tail8 +
  RM-tails NEW vs P304 RM + RQ-tails NEW vs P304 RQ +
  cross overlaps 0. Memo INCL PBA88 77 / C10 72 /
  quad88 68 / T88 72 (A-779 re-read): impl 77/71/67/72
  = memo-exact on PBA/T88, memo-1 on C10/quad (b5-const
  excluded) -- standing +1 rule coherent, +0/+1/+1/+0
  (P305 A b5-step +0 like Q-step P303, C/Q single-const
  b5 -> +1, T counter +0). Base temp maxes _t6308/
  _b3822/_i3823 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 122877 / S1 122878 / A 122879-894 / C 122895-904 /
  Q 122905-968 / R 122969-123224): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-step/const emerges from raw lencode) +
  R counter b4=(0xb3+2off)&FF b5=0xc0+(off>=39)+
  (off>=167) (py hex; C staged decimal 179/192,
  re-derived from code text both sides: 179==0xb3,
  192==0xc0) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 9B b51-55,
  80-83; C 11B b15,46-51,80-83; Q QM7 b6,7,12,80-83 +
  R12 b0,19,50-55,84-87, NO frags; R TM7 b13,14,15,
  80-83 by COL + TR7 b6,7,9,76-79 by ROW) + C guards
  `if ((n) == (122877))` / `(122878)` + 4 range guards
  exact + C byte-index lists match py per block (A 9B,
  C 11B, Q 7B/12B, R 7B/7B). T-mirrors T82309/82314/
  82319/82334/82350/82371 each re-read: hits the exact
  py guard line. Temps _t6309-6324 continuous (base max
  _t6308) + _b3824/3826/3828/3829/3831/3832 (base max
  _b3822) + _i3825/3827/3830/3833 (base max _i3823):
  added-only, no reuse. Insert exact both sides: P304R
  block precedes, at dispatch tail (N-out-of-scope
  fallthrough follows; 2 scope hits py + 2 scope hits
  C). Matches A-779 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P305 blocks).
- Edges own-loop ownloop413.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (0 miss, cache warm). Census R256/Q64/A16/C10/
  S0/S1 exact. Tail line: CLOSED T10P305R N=123224
  off=255. edges413.py: paylens 12x84 + 336x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 fb/bf, fd/bf
  == raw lencode) + astep 16/16 (A head ff/bf, edge
  o0->o1 122879->122880 ff/bf->01/c0, tail 1d/c0,
  b5set {bf,c0} step o0->o1 earliest PBA step) +
  cform 10/10 (C head 1f/c0 tail 31/c0 b5set {c0} NO
  step, 0 ff) + qform 64/64 + qb5flat 64/64 (Q head
  33/c0 tail b1/c0 b5set {c0} NO step, 0 ff in 64;
  quad b4 base 0x33 step2 == raw-lencode 64/64); ring
  counter 256/256 + ringraw 256/256 (head b3/c0;
  123007 off38 ff/c0 -> 123008 off39 01/c1; mid
  off128 b3/c1 at 123097; 123135 off166 ff/c1 ->
  123136 off167 01/c2; tail off255 b1/c2; exactly 2
  ff in 256 at o38/o166); ff total x3 (122879 A-step
  + 2 ring). odd-lencode 92+256=348/348. Ring edges +
  tail 123224 in for-list + 2 PASS lines each py+C.
  Tail 123224: oracle sha ccac87af1ba01cb4... matches
  PINS (rawlen 104 re-checked: paylen 88 + 12 + 4);
  py+C CLOSED T10P305R off=255 agree. No DISSENT: cut
  bytes verify.
- PB-diff secf413.py (cache path) + secf413b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (122877 +
  122529 + 122878 + 122530); S0: oracle122877-vs-122529
  38/84, codeS0-vs-P304S0 38/84, positions identical;
  DIRECT tool 38/84 with identical agree-pos 46
  positions. S1: oracle122878-vs-122530 62/84,
  codeS1-vs-P304S1 62/84, positions identical; DIRECT
  62/84 identical agree-pos 22 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs.
  S1-vs-own-C10 secf413c.py: [22x7,21,21,23]
  NON-uniform == GATE EXACT ([0] n122895 22/84 @ b4,5,
  34,35,42-51,56-59,80-83 == GATE EXACT; sig 80299f81
  vs 80299f81 sig-eq, NOT byte-equal). Byte-diff
  discipline observed throughout, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del (see prose
  note: GATE writes "604 content"); raw py 230 content
  / 0 del. Full-digit norm ([0-9]+ -> N): C del-uniq 0
  add-uniq 165 missing 0 under the recipe AS STATED
  (diff-sign strip + trailing-';' strip, NO whitespace
  handling stated); GATE's 161 reproduces iff leading-
  whitespace-stripped AND empty-excluded (strip+
  dropempty 161, strip-only 162, dropempty-only 164 --
  recipe variant gap, same class as b405/b407/b409/
  b411; see prose note); py del-uniq 0 add-uniq 179
  missing 0 == GATE EXACT (variant-insensitive: 179
  all four variants). del-subset-add 0 missing holds
  every variant (integrity intact). C-tempnorm 410 /
  py-tempnorm 202 recorded (no GATE claim).
- Wall on band diff added lines (scope 05055220..
  f539e0c8, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (e53a773d), code 6 blocks,
  tier-comments `# T10P` 1718->1724 +6 == GATE stated-
  method EXACT, singletons `if n == ` 642->644 +2 ==
  GATE EXACT, range-guards `<= n <=` 672->676 +4 ==
  GATE EXACT, CLOSED T10P prints 1718->1724 +6 py +
  1718->1724 +6 C == GATE EXACT, C singleton
  `if ((n) == (` 637->639 +2 == GATE EXACT (5-count
  C-vs-py offset pre-existing, unchanged: 642-637 =
  644-639 = 5), C ranges 672->676 +4 == GATE EXACT,
  seal 1812->1818 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1818-1724 = 94, stable b401-b413): all
  agree, no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-779-q897-P305
  verdict CONFIRM, tallies 27/27 + 16/16 + 15/15 =
  58/58 arith-consistent as-filed + exact-value
  corroboration incl PB0 NEW + PB1 NEW sig-eq-own-C10
  22/84, PBA88-STEP sig-09 M9 + step o0->o1,
  C10-1SIG SAME-as-PB1 M11, QUAD88-2SIG + R12 rows +
  8B-share + r1r2-pair-2B + r0+r3-isolated + M-tails
  NEW, T88-RING-STANDARD + TM7/TR7 16/16 UNPAIRED +
  SPLIT tails + b84-87 c372802f + edges + consts
  b3/c0/39/167 + lencode 348/348 + VPOS 11/12/20/16
  (all re-checked above). Sheet-vs-tables const-count
  note: Q-897 sheet rule 77/72/68/72 memo-exact (2nd
  straight fully clean w2b sheet per memo), committed
  tables 77/71/67/72 still deduct const-b5 in C/Q --
  8th consecutive tables-lag band (geometry exact,
  PORT verdict stands). No viewer P305 geometry answer
  on file at gate time (memo-only recon; this VERIFY
  is the viewer record). No CONFIRM-P305.md file
  (absence verified); A-779 suffices per rule. Agrees
  with cport commit msg (PYID 9029, RGRAM 18058).
- Quiz: no conflicting CLAIM/GATE/FLAG on b413 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites
  QNUM-22 newest -- TRUE at filing time (GATE 14:03,
  QNUM-23 14:51 + QNUM-24 16:04 both postdate it): NO
  staleness. PROSE-01: all hex/counts above copied from
  own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 3 prose-level notes (norm-161 recipe variant gap:
stated recipe yields 165, strip+dropempty yields the
claimed 161 -- integrity holds every variant, same class
as b405/b407/b409/b411; "raw C 604 content + 5
blank-only" reads 604+5=609 vs numstat 604 -- first-hand
is 599 content + 5 bare-blank = 604, the "604 content"
token is wrong (contrast b412 GATE's correct "599
content + 5 bare-blank"); PB1-vs-C10 22/84 attribution:
value CORRECT first-hand (cell0 == GATE EXACT), but
A-777 predicted sig-eq + "byte-diff TBD P305 census" --
the 22/84 count is census-measured (memo A-779 +
GATE), and the "== A-777 predicted next EXACT"
parenthetical overstates (same looseness as b409/b411)).
24th odd-band RQ==M instance corroborated as DIAG6
(diag-6 identity + RQ[2]-isolated + heads-own
distinctness 15/5 (+2-distinct f4/f5 at RQ2); NEW
variant joining neither prior group; memo-silent on the
relation; even/odd convention holds: b412 even EXACT
takes no ordinal). Next-P306 predictions banked (A-779
re-read: PB0 db1b7900 EQ-P305PB0sig @123225 + PB1
80120ffa NEW @123226 + PBA88 0f000000 x16 @123227-42
NEW sig 0f + C10-1SIG 803b4fc4 x10 @123243-52
NOT-PB1-sig).
