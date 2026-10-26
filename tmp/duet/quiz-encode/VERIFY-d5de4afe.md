# VERIFY-d5de4afe b399 T10P291 pins 118005..118352 (1734 tiers) PASS

Seat viewer-r57, first-hand, tree-d5de4afe @d5de4afe,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r57.
Base b5516b9b (b398, 1728 tiers). Band = 7c7363ba (py merge
w2b@8b76d52e partial, +6 tiers, +62 pins) + d5de4afe (C port,
1734 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build399/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc 4a8f214c5b03a937 / aae
  7d8dd3a2d118e0db + sha256 rgramc e020d4752bbbee0c / aae
  d6e27c97ced21673 (== GATE all 4; aae pinned, band
  touches no aae sources per numstat).
- RGRAMC-PYID 8593/8593 covered=8593/8593 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17186/17186 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17186/17186 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17186/17186).
- PINS 17188 rows (2 hdr + 17186, +62 vs base 17126);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  118005 118006 118007 118008 118015 118016 118021 118022
  118023 118024 118027 118030 118031 118032 118033 118041
  118048 118049 118057 118065 118073 118081 118089 118096
  118097 118143 118144 118225 118271 118272 118352
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,8,9,14,15
  (b5 step edge o8->o9 straddled: 118015+118016 both
  pinned) + C6 offs 0,1,4,7,8,9 (offs 2,3,5,6 = 118025/
  118026/118028/118029 unsampled) + Q10 offs 0,8,15,16,
  24,32,40,48,56,63 (b5 const, NO step) + R7 offs 0,46/
  47,128,174/175,255 (both counter edges straddled);
  8562->8593); 31x2=62 rows, range 118005..118352 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit399.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 136 PASS
  0 FAIL. Inventory exactly the 14 both sides (PBA88-
  STEP/C10-2SIG/QUAD88-2SIG-FRAG/STANDARD ring + F0/F1
  rowpair-tabs; no QT/RT/TT; no BM/BC, no M19/XA19, no
  QB/PT/FM, no M42/X42/H42/L42); C==py 14/14. S0/S1
  168ch sigs 5f6f1300 sig-eq-P290PB0 / 2b81c726 NEW
  (S0-vs-P290S0 30/84 @ b4-10,13-15,17,18,20-25,64-75
  EXACT, sig-eq only, NOT byte-equal; S0 cross-P290S1
  36; S1-vs-P290S1 48/84 @ b0-2,4,5,13-39,52-55,68-75,
  80-83 EXACT + cross-P290S0 62; S1 full-string NEW vs
  BOTH P290 strings). AM 16x16ch distinct; AC 78, b0-3
  02/00/00/00 (b0 const 02), no b4/b5, PBA sig 02000000
  x16 STEP. CM 10x32ch 10/10 diverge; CM-b2-3 sequence
  c726 x8 + 6713 x2 ORDERED (rows 0-7/8-9); CC 66,
  b0-1 2b/81 const, b2-3 in tab (partial sig), no b4/
  b5; C10-2SIG 2b81c726 x8 + 2b816713 x2 ORDERED. M
  16x8ch distinct. QR 4x24ch 4-distinct UNPAIRED; r0
  01175bddb0b0112d322dd5e9 distinct; r1/r2 share 8B
  022f0cdf49ad1296 (NOTE: memos quote 6B 022f0cdf49ad;
  first-hand 8B is the fuller value -- immaterial
  memo-prefix truncation, code unanimous); r3 head
  022f0ddf distinct from r1/r2; tails b84-87 322dd5e9/
  553f379a/7a3f379a/12f6cff1 4/4 distinct; r1r2 TRUE 3B
  3f379a; tail-lcsuf (1,2)=3, all other pairs 0 (r0+r3
  lcs=0). F0/F1 16x8ch 16-distinct each; FRAG rows
  differ 16/16 + per-pos differ 16/16 x4 (clean
  r0-vs-r123 split all 4 positions). QC 66, b0 in tab
  (sig-led R12), b1-3 00/00/00, no b4/b5. RM 16x18ch
  distinct; RQ 16x16ch distinct; RC 69, b0-3 23/00/00/
  00, b84-87 15/37/fc/9a ring-wide; b51-skipped const
  dc verified in table. RQ==M TAILS (M 4B b80-83 vs RQ
  8B: RQ[4:8]==M[0:4] 16/16; head 4x4 agree noise <=1
  with incidental (3,3)=1 -- TAILS degree, joins P255/
  P263/P267/P285 group; 17th odd-band RQ==M instance).
  RM-vs-RQ UNPAIRED (sets disjoint). Tails STANDARD-
  SPLIT (RM b80-83 by COL, RQ b76-79 by ROW, 16/16
  distinct each, 0 overlap). Sorted-unique + _N decls
  78/66/66/69 match actual. Missing-sets EXACT: AC [4,
  5,40,41,42,43,80,81,82,83]; CC [2,3,4,5,34,35,36,37,
  38,39,40,41,42,43,80,81,82,83]; QC [0,4,5,19,38,39,
  40,41,42,43,44,45,46,47,80,81,82,83,84,85,86,87];
  RC [4,5,38,39,46,47,50,52,53,54,55,76,77,78,79,80,
  81,82,83]. Coverage unions exact every block (const
  U tab U {b4,b5} == 88/84/88/88, 0 overlap). Q legs
  M[m] + QR[q] + F0/F1 ftab. R legs RM[c] + RQ[r]
  STANDARD. P290 refs re-read: S0 5f6f1300 / S1
  ccbede26 / PBA 02000000 (== P290 preds EXACT). P291
  preds (A-729 Next-P291: 5f6f1300-sig-eq/2b81c726/
  02000000-STEP/2SIG-8+2-ORDERED) x4 corroborated
  staged (A-354 window agrees except its PB0 byte-equal
  line, refuted below). PBA sig REPEAT vs P290
  (02000000 == 02000000; STEP is the novelty). QR
  0-overlap vs P290QR. M-tails 16/16 ALL NEW vs P290
  RM-tail8 (overlap 0); RM-tails ALL NEW vs P290
  RM-tail8 (overlap 0); RQ-tails ALL NEW vs P290
  RM-tail8 + P290 RQ-tail8 (overlap 0 x2). Memo INCL
  PBA88 78 / C10 67 / quad88 67 / T88 69 (A-730
  re-read): impl 78/66/66/69 = identical on PBA/T88,
  memo-1 on C10/quad (b5-const excluded; A-STEP +0
  mirrors the Q-step +0 rule). Base temp maxes _t6075/
  _b3681/_i3682 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 118005 / S1 118006 / A 118007-022 / C 118023-032 /
  Q 118033-096 / R 118097-352): bounds + paylens (12x84
  + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q both
  sides (b5-step/consts emerge from raw lencode) + A b5
  step 0x99+(o>=9) edge o8->o9 + Q b5 const 0x9a full
  block (equiv counter b4=(0x23+2off)&FF 64/64) + R
  counter b4=(0xa3+2off)&FF b5=0x9a+(off>=47)+(off>=
  175) (py hex; C stages decimal 163/154/47/175,
  re-derived from code text both sides) + FRAG ftab
  (q==0)?F0:F1 both sides + m=off&15/q=off>>4/c=off&
  15/r=off>>4 both sides + mtab/rtab byte positions
  exact (A 8B b40-43,80-83; C 16B b2,3,34-43,80-83; Q
  QM4 b80-83 + R12 b0,19,40-45,84-87 + FRAG b38,39,46,
  47; R TM9 b50,52-55,80-83 by COL + TR8 b38,39,46,47,
  76-79 by ROW) + rowpair-tabs F0(r0)/F1(r123). T-
  mirrors T79009/79014/79019/79034/79051/79076 each
  re-read: hits the exact py guard line. C guards
  `if ((n) == (118005))` / `(118006)` + 4 range guards
  exact. C byte-index lists match py per block (A 8B,
  C 16B, Q 4B/12B/4B, R 9/8B). Temps _t6076-6094
  continuous (base max _t6075) + _b3683/3685/3687/3688/
  3689/3691/3692 (base max _b3681) + _i3684/3686/3690/
  3693 (base max _i3682): added-lines-only refs (base
  tree zero refs to new temps) prove no reuse. Insert
  exact both sides: after T10P290R close, at dispatch
  tail (N-out-of-scope fallthrough follows; C 2 scope
  hits, py 2 scope hits). Matches A-730/A-355 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P291 blocks).
- Edges own-loop ownloop399.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P291R N=118352 off=
  255. edges399.py: paylens 12x84 + 336x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 eb/99, ed/99 == raw
  lencode) + aform 16/16 + ab5step 16/16 (A 88B head
  ef/99 tail 0d/9a b5set {99,9a} step o8->o9: 118015
  o8 ff/99 -> 118016 o9 01/9a, exactly 1 ff in 16 at
  o8) + cform 10/10 (C head 0f/9a tail 21/9a b5set
  {9a} NO step, 0 ff) + qform 64/64 + qb5const 64/64
  (Q head 23/9a tail a1/9a b5set {9a} NO step, 0 ff in
  64; quad b4 formula == raw-lencode 64/64); ring
  counter 256/256 + ringraw 256/256 (head a3/9a;
  118143 off46 ff/9a -> 118144 off47 01/9b; mid off128
  a3/9b; 118271 off174 ff/9b -> 118272 off175 01/9c;
  tail off255 a1/9c; exactly 2 ff in 256 at o46/o174);
  odd-lencode 348/348. Ring edges + tail 118352 in
  for-list + 2 PASS lines each py+C. Tail 118352:
  oracle sha 5d5480eb5ca05125... matches PINS; py+C
  CLOSED T10P291R off=255 agree. No DISSENT: cut bytes
  verify.
- PB-diff secf399.py (cache path) + secf399b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (118005 +
  117657 + 118006 + 117658); S0: oracle118005-vs-117657
  30/84, codeS0-vs-P290S0 30/84, positions identical;
  DIRECT tool 30/84 with identical agree-pos 54
  positions. S1: oracle 48/84, code 48/84, positions
  identical; DIRECT 48/84 identical agree-pos 36
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. A-355 leg-1 "(byte-equal first-hand)"
  REFUTED (30/84 differ, twice-derived cache+direct
  identical positions, sig-eq 5f6f1300 only),
  corrected in record; A-730's 30/84 figure + NOT-
  byte-equal call VINDICATED (5th wording refutation:
  A-342/A-345/A-347/A-350/A-355 -- this one viewer-
  side, pattern now bilateral; byte-diff discipline
  stands).
- C diff pure-add: numstat 656/0 (rgramc.c) + 269/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 651 content + 5 bare-blank / 0 del; raw py 269
  content / 0 del. Normalized ([0-9]+ -> N recipe):
  py del-uniq 0 add-uniq 200 missing 0 == GATE EXACT.
  C add-uniq: stated recipe gives 189 first-hand (python
  + BSD shell, twice-derived, same inputs: sweep's
  cdiff399 +line set cmp-equal mine 656/656); lstrip +
  drop-empty reconstruction gives 185 == GATE EXACT
  (python + BSD shell, twice-derived; py is 200 under
  EVERY variant, so one lstrip+drop-empty script yields
  exactly GATE's 185/200 pair). del-uniq 0 +
  del-subset-add 0 missing hold under EVERY variant
  (integrity property intact). Recipe-description
  imprecision only (GATE prose omits the lstrip +
  empty-drop steps); numbers are genuine script
  outputs. Code unaffected. Same sweep-r61 one-liner
  as b397 (147 there) -- standing note, suggest sweep
  publish the one-liner (one line, no re-GATE needed).
- Wall on band diff added lines (scope b5516b9b..
  d5de4afe, 988 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 656/0, rgram.py 269/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (7c7363ba), code 6 blocks,
  tier-comments `# T10P` 1634->1640 +6, singletons
  614->616 +2 / ranges 616->620 +4, CLOSED T10P prints
  1634->1640 +6 py + 1634->1640 +6 C, C singleton
  `if ((n) == (` 609->611 +2 / C ranges 616->620 +4,
  seal 1728->1734 +6 (commit msgs): all agree, no slip.
  5-count py-vs-C singleton offset pre-existing +
  unchanged (gap 5 at base AND new).
- CONFIRM evidence (CONVERT-01 rule b): A-730-q883-
  t10p291 verdict CONFIRM, tallies 15/15 + 15/15 + 14/14
  = 44/44 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 19 total vs 44, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0 sig-eq + 30/84 NOT-byte-equal,
  PB1 NEW, PBA88-STEP + b5 step + edge, C10-2SIG
  ORDERED 8+2, QUAD88-2SIG-FRAG + R12 rows + tails +
  TRUE-3B + FRAG split + M-tails NEW, T88 STANDARD +
  TM9/TR8 16/16 UNPAIRED + SPLIT tails + b51-skipped dc
  + b84-87 const + ring edges + thresholds (all
  re-checked above) + A-355 viewer corroboration
  (CONFIRM all legs EXCEPT leg-1 byte-equal line,
  refuted 30/84 above; consts 78/67/67/69 INCL stand).
  No CONFIRM-P291.md file (absence verified); A-730
  suffices per rule. Agrees with cport commit msg
  (PYID 8593, RGRAM 17186).
- Quiz: no conflicting CLAIM/GATE/FLAG on b399 (own seat
  CLAIM only). Newest PARENT-QNUM-22 (w2e Q-block grant,
  read, no gate impact) -- GATE cites QNUM-20: 1
  immaterial staleness (standing pattern). PROSE-01: all
  hex/counts above copied from own run output; GATE
  re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 2 immaterial GATE prose notes (QNUM-20 vs -22
staleness; norm recipe prose omits lstrip + empty-drop
steps -- 185/200 verified genuine via reconstruction,
integrity intact) + 1 memo-side note (A-355 byte-equal
refuted, A-730 vindicated -- code/record already
correct, no band impact).
Next-P292 predictions banked for r58 (A-730/A-355: PB0
@118353 436f1300 NEW / PB1 2b81e720 NEW / PBA88 02000000
x16 / C10-2SIG 08075220 x7 @118371-77 + 84032910 x3
@118378-80 ORDERED 7+3 window-resolved).
