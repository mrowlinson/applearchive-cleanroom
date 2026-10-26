# VERIFY-608c167f b431 T10P323 pins 129141..129488 (1926 tiers) PASS

Seat viewer-r65, first-hand, tree @608c167f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r65.
Base b6af2b17 (b430 tip, 1920 tiers sealed; this seat's
VERIFY-b6af2b17 PASS-filed same round, base-use only,
respected). Band = 1ec8fc82 (py merge w2b@8c471df4
partial, +6 tiers, +66 pins) + 608c167f (C port, 1926
sealed). Trees manifest-identical to tips (git ls-tree
vs git ls-files cmp clean, 117/117 both; WT detached
at band, will return to lanes/encode-viewer at round
end).

Banked Next-P323 shape (r65 from A-831 FWD-check +
A-832) CONSUMED FIRST and corroborated below:
PB0 b7ce7001 pay84 NEW-sig (differs vs P322 heads
77435801/02000000) @129141 / PB1 02000000 pay88
sig-eq-P322PB1 (50/88 diff) @129142 / PBA88 2d000000
x16 @129143-158 / C10-region 02000000 pay88 x10
@129159-168 -- all exact.

- Build: make -C src/c BUILDDIR=build431 aae rgramc
  (absolute NVME path, -O2 -Wall -Wextra -std=c11),
  rc=0, 0 warnings. sha256 rgramc 49e3de23867e711a
  79e336fea3403b19548d3c603daf3c5ab0b21bcf8f732036 /
  sha1 0760f18dd1ad00890d65f802bfcd408b41bff35a
  (== GATE both; aae sha256 d6e27c97 pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 9596/9596 covered=9596/9596 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary
  exported before the run, CT_CACHE_DIR set, NVME
  workdir).
- RGRAM py 19192/19192 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 19192/19192 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (sorted cmp equal + raw-order identical, 19192/19192;
  cmp431.py; GATE claims sorted only, raw corroborated
  too).
- PINS 19194 rows (2 hdr + 19192, +66 vs base 19128;
  +66 = 33 for-Ns x2, A carries 8 this tier);
  PASS-names vs PINS-names xor 0 py+C; PINS-baseN vs
  for-list xor 0 (4-way set-eq, seteq431.py). For-list
  union delta vs base +33/-0 (9563->9596):
  129141 129142 129143 129144 129149 129150 129151
  129152 129157 129158 129159 129160 129163 129164
  129167 129168 129169 129176 129185 129192 129201
  129208 129217 129224 129231 129232 129233 129279
  129280 129350 129407 129408 129488
  (== GATE sampled list EXACT). Decomposition first-hand
  from the added set: 2 sing (129141/42) + A head-pair
  43/44 + mids 49/50 + step-edge pair 51/52 (offs 8/9,
  b5 STEP f0->f1 NEW 8-pin shape, first-hand) + mids
  57 + tail 58 (8: offs 0,1,6,7,8,9,14,15) + C head
  59/60 + mids 63/64 + 67 + tail 68 (6: offs 0,1,4,5,
  8,9; offs 2,3,6,7 = 61/62/65/66 unsampled, absence
  verified) + Q head 69/off0 + off7 76 + mids 85/92/
  01/08/17/24 + tail pair 31/32 (10: offs 0,7,16,23,
  32,39,48,55,62,63; const-b5 NO step; per-row pairs
  (m0,m7) x4 rows + q3 tail pair (m14,m15) sampling,
  first-hand) + R head 33/edge-pairs 79/80 + 07/08/
  mid 50/tail 88 (7: offs 0,46/47,117,174/175,255;
  1-mid shape, both counter edges pair-covered,
  first-hand). 33x2=66 rows, range 129141..129488
  exact. PINS-new-N == for-added 33/33, PINS removed 0.
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle
  backend, NVME workdir).
- UNITS-GREEN rc=0 (22/22 PASS, 0 FAIL,
  tests/test_units.py, no oracle).
- Tables audit own script tabaudit431.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 159 PASS
  0 FAIL after 2 seat-script fixes (aliased triple-list
  init `fr0=fr2=fr3=[]` caught by run; FRAG-r01 count
  32-not-16 + TAILS4-head scope corrected first-hand).
  Inventory exactly the 13 both sides, C==py (S0/S1/AM/
  AC/CM/CC/M/QR/QC/RM/RQ/RC/F; bare F tab, no FT46, no
  F0/F1, no QT (R10 carries b84-87 in QR), no RT/TT,
  no BM/BC, no M19/X19, no M42/X42/H42/L42, no
  QB/PT/FM).
  S0 168ch sig b7ce7001 NEW (28/84 payload diff vs
  P322S0 @ b0-2,4-10,13,15-19,24,56-60,62,63,80-83
  first-hand, NOT byte-equal; differs vs P322 heads
  77435801/02000000) / S1 176ch sig 02000000 sig-eq-
  P322PB1 (50/88 payload diff vs P322S1 @
  b4,5,8-11,16-43,60-71,84-87, NOT byte-equal; [24]x10
  vs own C10 assembled, NOT byte-equal; sig SAME-as-
  own-C10; differs vs own PB0), staged as full-payload
  singletons.
  AM 16/16 16ch (8B) distinct, CM 10/10 8ch (4B)
  distinct, M 16/16 14ch (7B) distinct, QR 4/4 20ch
  (10B) distinct, F 16/16 2ch (1B) distinct {42,c2},
  RM 16/16 12ch (6B) distinct, RQ 16/16 16ch (8B)
  distinct UNPAIRED, no QT + no RT (STANDARD tails) +
  FRAG-b46 (dual-ADD, below).
  AC 78, b0-3 2d000000 (b0 const 2d), no b4/b5.
  C10-1SIG-88-TAIL sig 02000000 x10 SAME-as-PB1 (sig
  in CC b0-3 consts; CM 10/10 diverge 8ch first-hand;
  CC has no b4/b5, b5 const f1 full block via lencode).
  S1-vs-own-C10 staged per-cell (M4 b84-87, b4/b5
  lencode, each cell own assembly) [24]x10
  TRUE-UNIFORM count+position (cell0 24 @
  4,5,26,27,34,36-40,42-47,72-75,84-87 EXACT; positions
  identical all 10 staged AND oracle; sig 02000000
  both, NOT byte-equal -- 18th TRUE-uniform case on
  record, 17th excluding unverified P299; beyond-GATE
  values corroborated by oracle leg below).
  QUAD88-1SIG-4R-FRAG 1-sig 2d000000 x64 SAME-sig-as-
  PBA (QC b0 const 2d, b0 NOT in tab; b5 const f1 full
  64, NO step; b4 base 0x23 step2 64/64 range 23..a1
  NO edge; QM7 b38,39,47,80-83 7B distinct + R10
  b40-45,84-87 rows 4/4 NO pairing pairwise-disjoint:
  r0/r1 share 6B prefix e85db57812a1, differ b84 90/
  b0 (NOT 7B -- A-833 erratum CONFIRMED first-hand:
  writer label numeral fix, no byte impact); r2/r3
  fully distinct;
  tails b84-87 4/4 distinct 90f22506/b0f22506/
  9fa9c7d2/5e771e5d, r01 TRUE-3B f22506, r2/r3-lcs0
  vs all, r0r1-lcs3, all other pairs lcs0;
  FRAG b46 dual-ADD FIRST-of-class verified triple
  first-hand: tab16 ordered (c2,c2,c2,42,c2,42,c2,
  42,c2,42,42,42,c2,42,c2,c2; 2 distinct {42,c2},
  c2x9/42x7) + oracle pay46 over all 64 Q Ns: q<=1
  rows == F[m] 32/32, q==2 rows == F[m]+0xef 16/16
  (set {31,b1}), q==3 rows == F[m]+0xe6 16/16 (set
  {28,a8}); C legs _T10P323F[m] + hexval + 239/230
  (&255) exact; memo "all 48 cells" = F-tab16 + r2 +
  r3 (r01 uses the same tab, 32 cells covered);
  M-tails 16/16 ALL NEW vs P322T (zero overlap vs P322M
  AND vs P322RM-tail8 AND vs P322RQ-tail8).
  Ring STANDARD: sig ad030000 x256; TM6 b52,53,80-83
  by COL RM 16/16 + TR8 b40,41,46,47,76-79 by ROW RQ
  16/16 UNPAIRED (tails SPLIT b80-83 col / b76-79 row);
  b0 const ad b1 const 03; b84-87 3e2dd21b ring-wide
  NEW.
  M==RQ TAILS4-ONLY: M 7B vs RQ 8B agree (3,4),(4,5),
  (5,6),(6,7) 16/16 each; last-4 tails agree, 3 head
  M-byte rows isolated maxagree 0,0,0; tails-adjacent
  singles (4,0),(4,6),(5,1),(5,5) = 1 recorded as
  noise; tabs differ. 33rd odd-band RQ==M instance
  (viewer chain b421-28th FULL7/b423-29th TAILS4-ONLY/
  b425-30th TAILS4-ONLY/b427-31st FULL6/b429-32nd
  FULL7/b431-33rd TAILS4-ONLY sequential); 4th
  TAILS4-ONLY degree instance (after P309 + P315 +
  P317, all re-verified vs records).
  Memo-silent on the relation.
  Sorted-unique + _N decls 78/82/68/72 match actual.
  Missing-sets EXACT: AC-10 [4,5,40-43,80-83] =
  b4,b5+M8 / CC-6 [4,5,84-87] = b4,b5+M4 /
  QC-20 [4,5,38-47,80-87] = b4,b5+QM7+R10+F1 (b0 const
  2d, NOT missing) / RC-16 [4,5,40,41,46,47,52,53,
  76-83] = b4,b5+TM8+TR8. VPOS 10/5/19/16 == A-833
  EXACT (PBA b4,b5+M8 (b5 STEP counted) / C10 b4+M4 /
  quad b4+QM7+R10+F1 (b5-const excluded) / T
  b4,b5+TM8+TR8). Coverage unions exact every block
  (const U tab U {b4,b5} == 88 x4, 0 overlap); each
  missing == region pay-index set (A/C/Q/R region text
  re-derived first-hand, tab == region-idx minus {b4,b5}
  EXACT all 4).
  Q legs M[m] + QR[q] + F[m]-scalar/ADD both sides, NO
  F-row leg in Q; R legs RM[c] + RQ[r] both sides, NO
  F anywhere in R (STANDARD RM-col / RQ-row verified
  in region text both sides). RM 16/16 distinct + RQ
  16/16 distinct, sets disjoint.
  P322 refs re-read: S0 77435801 / S1 02000000 /
  PBA 29000000 / C10 02000000 / QUAD 1SIG 29.
  PBA sig 2d NEW vs P322 29 (2d000000 != 29000000);
  QUAD 1SIG 2d SAME-sig-as-PBA vs P322 1SIG 29 (rows
  NEW, single-sig structure continues; R10 replaces
  R11 class). AM/CM/M/QR/RM/RQ 0-overlap vs P322; F
  NEW this tier (no T10P322F in base). Memo INCL PBA
  78 / C10 83 / quad 69 / T88 72 (A-833 re-read): impl
  78/82/68/72 = b5 STEP counted on PBA (varies), b5
  const deducted on C10/quad (b5 covered by lencode),
  T b5 varies deducted -- deduct-b5-only-when-b5vary
  rule holds; geometry exact, PORT verdict stands;
  memo-exact on T88 (b5 varies, no deduction). 26th
  consecutive tables-lag band (b431 pattern +0/+1/+1/+0:
  C10/quad lag; PBA exact this tier; running b412-b430
  per GATE + r64/r65 records).
  Base temp maxes _t6616/_b4003/_i4004 (no reuse:
  band adds _t6617-6634 continuous-18 + _b4005/07/09/
  10/12/13 + _i4006/08/11/14, all above base maxes).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 129141 / S1 129142 / A 129143-158 / C 129159-168 /
  Q 129169-232 / R 129233-488): bounds + paylens
  (1x84 + 347x88) + lencode l16 A/C both sides (A b5
  STEP f0->f1 @off9: 129151 ff/f0 -> 129152 01/f1;
  C/Q b5 const f1 emerges from raw lencode, NO step,
  NO edge; Q range 23..a1) + R explicit counter
  (b4=(0xa3+2off)&FF b5=0xf1+(off>=47)+(off>=175); py
  hex 0xa3/0xf1; C staged literals 163/241,
  re-derived: 163==0xa3, 241==0xf1; Q uses raw
  lencode, no counter literals) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/rtab byte
  positions exact (A M8 b40-43,80-83 + b5 STEP; C M4
  b84-87; Q QM7 b38,39,47,80-83 + R10 b40-45,84-87 +
  F1 b46; R TM6 b52,53,80-83 by COL + TR8 b40,41,46,
  47,76-79 by ROW, tails SPLIT) + C guards
  `if ((n) == (129141))` / `(129142)` + 4 range
  guards exact + counter literals exact + C byte-index
  lists match py per block. C blocks carry T86744/
  86749/86754/86769/86784/86813 py-line mirrors
  (T86744/T86749 spot-verified verbatim against py
  lines 86744/86749); bounds + byte positions exact
  (A 8B, C 4B, Q 7B/10B/1B, R 6B/8B STANDARD-split).
  Insert exact both sides: after T10P322R close
  (py CLOSED-then-guard; C block follows P322R close),
  at dispatch tail (N-out-of-scope
  fallthrough follows; 2 scope hits py + 2 scope hits
  C). Matches A-833 geometry (values re-checked in
  audit above; NO D dips: ownloop tags exactly the 6
  P323 blocks).
- Edges own-loop ownloop431.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (246 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P323R N=129488
  off=255. edges431.py: paylens 1x84 + 347x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 eb/f0, ed/f0
  == raw lencode) + aform 16/16 (A head ef/f0 tail
  0d/f1 edge off8->9 b5set {f0,f1} STEP @9, exactly
  1 ff in 16) + cform 10/10 (C head 0f/f1 tail 21/f1
  b5set {f1} NO step, 0 ff) + qform 64/64 + qb5const
  64/64 (Q head 23/f1 tail a1/f1 b5set {f1} NO step,
  NO edge, range 23..a1, 0 ff in 64) + ring counter
  256/256 + ringraw 256/256 (head a3/f1; 129279
  off46 ff/f1 -> 129280 off47 01/f2; mid off117 8d/f2
  at 129350 re-verified direct; 129407 off174 ff/f2
  -> 129408 off175 01/f3; tail off255 a1/f3; exactly
  2 ff in 256); ff total x3 (1 A + 2 R); ff-in-Q 0.
  odd-lencode 92+256=348/348. Ring edges + tail
  129488 in for-list + 2 PASS lines each py+C. Tail
  129488: oracle rav sha 89bbb415fed8cc19 == PINS
  (== GATE prefix EXACT; rawlen 104 re-checked:
  paylen 88 + 12 + 4); py+C CLOSED T10P323R off=255
  agree. No DISSENT: cut bytes verify.
- PB-diff secf431.py (cache path, 0 miss) + secf431b.py
  (DIRECT tool, no cache): staged-vs-oracle 0/0/0/0
  (129141 + 128793 + 129142 + 128794); S0: oracle129141-
  vs-128793 28/84, codeS0-vs-P322S0 28/84, positions
  identical (agree-pos 56 positions listed); DIRECT
  tool 28/84 agree. S1: oracle129142-vs-128794 50/88,
  codeS1-vs-P322S1 50/88, positions identical; DIRECT
  50/88 agree. Triple-derived both pairs (same novel
  shape both tiers: 84/84/84/84 + 88/88/88/88).
  S1-vs-own-C10 secf431c.py (oracle C10 cells n129159-
  168): [24]x10 TRUE-UNIFORM counts AND positions
  identical all 10 (cell0 pos 4,5,26,27,34,36-40,
  42-47,72-75,84-87 == staged EXACT; sig 02000000
  both, NOT byte-equal). Byte-diff discipline observed
  throughout.
- C diff pure-add: numstat 644/0 (rgramc.c) + 257/0
  (rgram.py) + 1/1 (for-line) + PINS +66/+0 (clean
  append, 33 Ns x2) == GATE; raw C 644 total = 639
  content + 5 bare-blank / 0 del (verified bare `+`
  lines; GATE writes "644 content + 5 blank" which
  sums 649 vs numstat 644 -- mild overcount-by-5,
  same token as b429 GATE, late catch noted in
  HANDOFF); full-digit norm ([0-9]+ -> N): C
  del-uniq 0 add-uniq 179/173/178/172 across the 4
  strip/dropempty variants (172 = strip+dropempty, as
  cited), missing 0 every variant; py del-uniq 0
  add-uniq 193/192/193/192 (192 as cited), missing 0
  (integrity intact, variant-robust); C-tempnorm 420
  / py-tempnorm 209 recorded. Band-level sole del =
  old for-line churn (1/1).
- Wall on band diff added lines (scope b6af2b17..
  608c167f, 968 added lines == GATE): vendor 0 hits,
  disasm 0 hits, depload 0 hits, libcompression/
  compression_tool//usr/bin/aa 0 hits, shebang 0 hits.
  Files: rgramc.c 644/0, rgram.py 257/0 purely
  additive, test_rgram.sh 1/1 (for-line), PINS +66/+0.
- Tiers: merge-msg +6/+66 (1ec8fc82), code 6 blocks,
  tier-comments `# T10P` 1826->1832 +6, singletons
  `if n == ` 678->680 +2 / range-guards `<= n <=`
  744->748 +4 = +6 py; C guards: singleton
  `if ((n) == (` 673->675 +2 / range 744->748 +4
  (5-count C-vs-py singleton offset pre-existing,
  unchanged: 680-675 = 678-673 = 5), CLOSED T10P
  prints 1826->1832 +6 py + 1826->1832 +6 C (seal
  1920->1926 +6; offset +94 vs CLOSED-T10P: 1926-1832
  = 94, stable b401-b431). All agree (stated literal
  methods first-hand; no method-mix this band).
  Deliberate structural add: py elif 46->48 (+2 =
  the FRAG q-branch `elif q == 2:` + `elif pay[46]...
  0xE6...` in T10P323Q region, verified located);
  C else-if 0->0 (C uses separate ifs).
- CONFIRM evidence (CONVERT-01 rule b): A-833-q915
  memo CONFIRM 66/66 CLEAN (own bed r3-P323 129141..
  129520 BAD=0 + own r3-P322, verifier v219.py 66/66
  PASS, novelties FIRST dual-ADD frag + PBA-STEP-
  M8classic; w2b-r27 [8/8 CAP hit]; file present,
  counts verified; exact-value corroboration incl PB0
  NEW-sig b7ce7001, PB1 sig-eq-P322PB1 50/88 SAME-
  as-C10 24/88, PBA88-STEP-M8classic sig-2d M8 b5-
  STEP, C10-1SIG-88-TAIL SAME-as-PB1-sig M4,
  QUAD88-1SIG-4R-FRAG SAME-sig-as-PBA + R10 rows +
  r01-share-6B (NOT 7B, erratum confirmed) + r01-
  TRUE-3B + r2r3-lcs0 + QM7 + F-tab + dual-ADD sets +
  NO frags (row-pairing) + b5-const + M-tails NEW,
  T88-RING-STANDARD + TM6/TR8 + tails-split + b84-87
  3e2dd21b + edges + consts; plus sheet-vs-tables
  const-count note: Q-915 sheet 78/83/69/72
  memo-exact, committed tables 78/82/68/72 --
  deduct-b5-only-when-b5vary rule (A b5 STEP counted,
  C10/quad b5 const deducted), geometry exact, PORT
  verdict stands; 26th consecutive tables-lag band).
  Agrees with cport commit msg (PYID 9596, RGRAM
  19192). No viewer P323 geometry answer on file at
  gate time (memo-only recon; this VERIFY is the
  viewer record).
- Quiz: no conflicting CLAIM/GATE/FLAG on b431 (own seat
  CLAIM only; exactly 1 GATE-608c167f; zero FLAG hits
  on b431/608c167f/T10P323/129141; even bases b430
  respected; b432 = sweep2 turf untouched). PROSE-01:
  all hex/counts above copied from own run output; GATE
  re-read in FULL before filing (zero slips on values;
  2 mild prose notes below).
- RQ==M chain: b431 odd TAILS4-ONLY (M 7B vs RQ 8B
  agree (3,4),(4,5),(5,6),(6,7) 16/16; head M-byte
  rows 0-2 maxagree 0,0,0; tabs differ).
  33rd odd-band instance (viewer chain b421-28th FULL7/
  b423-29th TAILS4-ONLY/b425-30th TAILS4-ONLY/b427-31st
  FULL6/b429-32nd FULL7/b431-33rd TAILS4-ONLY
  sequential); 4th TAILS4-ONLY degree instance (after
  P309 + P315 + P317). Running odd pattern continues.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 mild prose-level notes (raw-C content overcount
by 5: "644 content + 5 blank" sums 649 vs numstat 644;
first-hand 644 total = 639 content + 5 bare-blank --
same token as b429 GATE "607 content + 5 blank" vs
first-hand 602+5=607, late catch carried in HANDOFF;
RQ==M/TRUE-uniform ordinal-scope: GATE odd-scope "8th"
(P299+P303+P307+P311+P315+P317+P319+P323) vs viewer
full-scope 18th (17th excl P299) -- both correct under
stated scope, recurring token; code GREEN since gated
artifact == verified artifact). Next-P324 SHAPE banked
(A-833, for r66: PB0 b7ce3001 pay84 NEW 32/84 @129489
/ PB1 pay88 41/88 @129490 / PBA88 29000000 x16
@129491-506 / C10 02000000 x10 @129507-516).
