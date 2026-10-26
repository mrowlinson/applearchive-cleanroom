# VERIFY-d080cdaf b410 T10P302 pins 121833..122180 (1800 tiers) PASS

Seat viewer-r60, first-hand, tree410 @d080cdaf,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r60.
Base 676b823c (b409, 1794 tiers). Band = d5fabfc0 (py merge
w2b@50c73988 partial, +6 tiers, +62 pins) + d080cdaf (C port,
1800 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical non-tmp both; 117 = 113 non-tmp + 4 tmp).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build410/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 767417f4d519b2c6 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  965ee435cc58fc41 / aae 7d8dd3a2d118e0db (GATE cites no
  sha1; own values recorded).
- RGRAMC-PYID 8936/8936 covered=8936/8936 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17872/17872 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17872/17872 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 17872/17872).
- PINS 17874 rows (2 hdr + 17872, +62 vs base 17812);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  121833 121834 121835 121836 121842 121843 121849 121850
  121851 121852 121855 121856 121859 121860 121861 121869
  121877 121885 121893 121901 121909 121917 121923 121924
  121925 121983 121984 122053 122111 122112 122180
  (== GATE verbatim; decomposition re-derived: S0/S1 (2) +
  A6 offs 0,1,7,8,14,15 + C6 offs 0,1,4,5,8,9 (b5 step
  o4->o5 straddled: 121855+121856 both pinned) + Q10 offs
  0,8,16,24,32,40,48,56,62,63 (tail pair 121923/121924) +
  R7 offs 0,58/59,128,186/187,255 (both counter edges
  straddled + single mid 122053 -- one fewer ring mid
  than the usual 32, hence +62); 8905->8936); 31x2=62
  rows, range 121833..122180 exact. PINS-new-N ==
  for-added 31/31 (4th set-eq way), PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r59/b408/b409);
  band diffs touch no proto/ sources (numstat proves), NO
  verdict impact.
- Tables audit own script tabaudit410.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 149 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-STEP/QUAD88-4R/RING-SWAPPED; no F/F0/F1, no
  QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  0b913100 NEW / 8031ff44 NEW (S0 36/84 vs P301S0 @ 0-2,
  4,5,11,13-31,52-55,68-75 EXACT + cross-P301S1 34, S1
  55/84 vs P301S1 @ 0-5,11-43,52-55,72-83 EXACT +
  cross-P301S0 59). AM 16x14ch distinct; AC 79, b0-3
  04/00/00/00 (b0 const 04), no b4/b5, PBA sig 04000000
  x16 PLAIN (NEW sig 04). CM 10x24ch 10/10 diverge; CC
  70, b0-3 80/31/ff/44 (C10-STEP x10 SAME-as-PB1-sig),
  no b4/b5 (b5 stepped b7/b8 via lencode edge o4->5);
  rows 0-7 share 16ch d317d510bf740ac0 ch16 per-row
  9/9/b/d/f/1/3/5 EXACT, row0 tail7 6e8cdb7 unique,
  rows 1-4 tail7 865d3b7, rows 5-7 tail7 866d3b7, rows
  8-9 distinct heads 4b14/4b15. M 16x12ch distinct. QR
  4x24ch 4-distinct UNPAIRED; r0 1b0295226fb47428b5a79a30
  distinct; r123 share 8B 733415261f744e3e (lcpre 8) +
  byte8-diverge 0b/30/af; tails b84-87 b5a79a30/0bc7cad2/
  30c7cad2/af86cbd2 4/4 distinct; r12 TRUE 3B c7cad2; r3
  1B d2; full-row lcsuf (1,2)=3 (1,3)=(2,3)=1 (0,*)=0 +
  lcpre r0-vs-rest 0; tails longest-common-substring
  (1,2)=3 (1,3)=(2,3)=1 (0,1)=(0,3)=0 (0,2)=1 (shared
  single byte 0x30: r0 ..9a30 vs r2 30.. -- see LCS
  note). QC 68, b0-3 04000000, no b4/b5, b51 const d1
  (QUAD single-sig x64). RM 16x14ch distinct; RQ 16x12ch
  distinct; RM-vs-RQ UNPAIRED (sets disjoint); RC 73,
  b0-3 48/00/00/00, b8 const 9d (no frag), b84-87 ba/db/
  c4/91 ring-wide NEW. M==RQ 16/16 lists identical
  INTRA-tier (even-band EXACT, SWAPPED ring). Tails
  SWAPPED (RM b76-79 by COL, RQ b80-83 by ROW, 16/16
  distinct each, 0 overlap). Sorted-unique + _N decls
  79/70/68/73 match actual. Missing-sets EXACT: AC
  [4,5,38,46,47,80,81,82,83]; CC [4,5,34,35,41,42,43,44,
  45,46,80,81,82,83]; QC [4,5,38,39,45,46,47,48,49,50,
  52,53,80,81,82,83,84,85,86,87]; RC [4,5,6,7,9,52,53,
  76,77,78,79,80,81,82,83]. Coverage unions exact every
  block (const U tab U {b4,b5} == 88/84/88/88, 0
  overlap). Q legs M[m] + QR[q] both sides, NO F-legs
  either region both sides. R legs RM[c] + RQ[r] both
  sides. AC-QC shared-pos 68, same-val 39, AConly 11,
  QConly 0 (computed first-hand; NOT const-repeat).
  P301 refs re-read: S0 2ab31200 / S1 0b887b25 / PBA
  02000000 / C10-1SIG 0b917125 (CC consts) / QUAD
  02000000 x64. Next-P302 preds (A-768 re-read: PB0
  0b913100 NEW / PB1 8031ff44 NEW / PBA88 04000000 x16
  NEW sig 04 first / C10-1SIG 8031ff44 x10 SAME-as-PB1-
  sig) x4 corroborated (C10 staged as STEP variant of
  the predicted 1SIG pattern -- sig + SAME-as-PB1 hold;
  step is the tier's own finding). PBA NEW vs P301
  (04000000 != 02000000). AM/CM/M/QR/RM/RQ 0-overlap vs
  P301 (widths P302 AM14/CM24/M12/QR24/RM14/RQ12 vs P301
  AM16/CM24/M20/QR22/RM16/RQ16; same-width CM pair
  0-overlap by content; base widths re-read first-hand).
  M-tails 16/16 ALL NEW vs P301 M-tail8 + P301 RM-tail8
  + P301 RQ-tail8 (overlap 0 x3, incl ROW-led per memo);
  RM-tails NEW vs P301 RM tails + RQ-tails NEW vs P301
  RQ tails + cross overlaps 0. Memo INCL PBA88 80 /
  C10 70 / quad88 69 / T88 73 (A-770 re-read): impl
  79/70/68/73 = memo-1 on PBA/quad (b5-const excluded),
  identical C10/T88 -- standing +1 rule coherent,
  +1/+0/+1/+0 (A/Q single-const b5 -> +1, C-STEP +0 per
  P295 precedent, T counter +0). Base temp maxes
  _t6260/_b3792/_i3793 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 121833 / S1 121834 / A 121835-850 / C 121851-860 /
  Q 121861-924 / R 121925-180): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-const/step emerges from raw lencode) +
  R counter b4=(0x8b+2off)&FF b5=0xb8+(off>=59)+
  (off>=187) (py hex; C staged decimal 139/184,
  re-derived from code text both sides: 139==0x8b,
  184==0xb8) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 7B b38,46,
  47,80-83; C 12B b34,35,41-46,80-83; Q QM6 b52,53,
  80-83 + R12 b38,39,45-50,84-87, NO frags; R TM7 b6,7,
  9,76-79 by COL + TR6 b52,53,80-83 by ROW) + C guards
  `if ((n) == (121833))` / `(121834)` + 4 range guards
  exact + C byte-index lists match py per block (A 7B,
  C 12B, Q 6/12B, R 7/6B). T-mirrors T81619/81624/81629/
  81644/81660/81681 each re-read: hits the exact py
  guard line. Temps _t6261-6276 continuous (base max
  _t6260) + _b3794/3796/3798/3799/3801/3802 (base max
  _b3792) + _i3795/3797/3800/3803 (base max _i3793):
  combined 3794-3803 added-only, no reuse. Insert exact
  both sides: after T10P301R close, at dispatch tail
  (N-out-of-scope fallthrough follows). S1 comment
  carries 47/84 sig-eq-NOT-byte-equal discipline
  (corroborated below). Matches A-770 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P302 blocks).
- Edges own-loop ownloop410.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (0 miss-warmed -- cache already warm from prior
  legs). Census R256/Q64/A16/C10/S0/S1 exact. Tail line:
  CLOSED T10P302R N=122180 off=255. edges410.py: paylens
  12x84 + 336x88; lencode 92/92 (S/A/C/Q raw l16; S0/S1
  d3/b7, d5/b7 == raw lencode) + aform 16/16 (A 88B head
  d7/b7 tail f5/b7 b5set {b7} NO step, 0 ff) + cform
  10/10 + cb5step 10/10 (C head f7/b7 tail 09/b8 b5set
  {b7,b8} step o4->o5: 121855 o4 ff/b7 -> 121856 o5
  01/b8, exactly 1 ff in 10 at o4) + qform 64/64 +
  qb5const 64/64 (Q head 0b/b8 tail 89/b8 b5set {b8} NO
  step, 0 ff in 64; quad b4 base 0b step2 == raw-lencode
  64/64); ring counter 256/256 + ringraw 256/256 (head
  8b/b8; 121983 off58 ff/b8 -> 121984 off59 01/b9;
  122111 off186 ff/b9 -> 122112 off187 01/ba; tail
  off255 89/ba; exactly 2 ff in 256 at o58/o186);
  odd-lencode 348/348. Ring edges + tail 122180 in
  for-list + 2 PASS lines each py+C. Tail 122180:
  oracle sha d6eef95cfded4726... matches PINS (rawlen
  104 re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P302R off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf410.py (cache path) + secf410b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (121833 +
  121485 + 121834 + 121486); S0: oracle121833-vs-121485
  36/84, codeS0-vs-P301S0 36/84, positions identical;
  DIRECT tool 36/84 with identical agree-pos 48
  positions. S1: oracle121834-vs-121486 55/84,
  codeS1-vs-P301S1 55/84, positions identical; DIRECT
  55/84 identical agree-pos 29 positions. 0 miss
  (cache warm). Triple-derived both pairs.
  S1-vs-own-C10 secf410c.py: [0] n121851 47/84 sig-eq
  (8031ff44 vs 8031ff44) NOT byte-equal (== memo 47/84
  + py comment 47/84 + GATE reconstruction EXACT);
  counts all10 [47,47,47,47,47,48,48,48,48,48]
  step-aligned NON-uniform (cells 0-4 b7 vs 5-9 b8 --
  the extra diff byte is b5). Byte-diff discipline
  observed throughout, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 232/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 232
  content / 0 del. Temp-norm (stated recipe): C del-uniq
  0 add-uniq 399 missing 0 == GATE EXACT (no variant
  gap). Full-digit norm: C 150/147/149/146 + py 172 x4
  (variant-insensitive) recorded; del-subset-add 0
  missing holds every variant (integrity intact).
  C-tempnorm/py-tempnorm 399/187 recorded.
- Wall on band diff added lines (scope 676b823c..
  d080cdaf, 899 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 232/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (d5fabfc0), code 6 blocks,
  dispatch-exact singletons 626->628 +2 == GATE EXACT,
  range-guards 638->642 +4 == GATE EXACT, CLOSED T10P
  prints 1700->1706 +6 py + 1700->1706 +6 C, C identical
  626->628 +2 / 638->642 +4 (py=C dispatch-exact),
  seal 1794->1800 +6 (commit msgs; offset +94 vs
  CLOSED-T10P: 1800-1706 = 94, stable): all agree, no
  slip.
- CONFIRM evidence (CONVERT-01 rule b): A-770-q894-P302
  verdict PORT, tallies 25/25 + 15/15 + 13/15 = 53/55
  arith-consistent as-filed (the 2 short = §F const-count
  writer arithmetic on PBA/quad, geometry exact -- 6th
  consecutive §F per memo, escalation noted; NO verdict
  impact) + exact-value corroboration incl PB0/PB1 NEW
  sigs + S1 47/84 NOT-byte-equal, PBA88-PLAIN new-sig-04,
  C10-STEP + edge o4->5, QUAD88-4R + R12 rows + 8B-share
  + r12-TRUE-3B + r3-1B + b5 const + M-tails NEW,
  T88-RING-SWAPPED + TM7/TR6 + tails-swapped + b84-87
  badbc491 + edges + consts (all re-checked above).
  LCS sense distinction (memo + code comment "r0 lcs=0"
  vs longest-common-substring (0,2)=1 via 0x30):
  shorthand holds in lcsuf/lcpre senses (all r0 pairs 0
  both senses, verified), imprecise ONLY in substring
  sense -- prose shorthand, tails 4-distinct + TRUE-3B/
  1B stand, tier stands (GATE's LCS-NOTE already
  discloses this exact finding with the same numbers).
  No CONFIRM-P302.md file (absence verified); A-770
  suffices per rule. Agrees with cport commit msg (PYID
  8936, RGRAM 17872).
- Quiz: no conflicting CLAIM/GATE/FLAG on b410 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites no
  QNUM (no staleness). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before
  filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (CM ch16 order EXACT, LCS-NOTE
self-disclosed with corroborated numbers, temp-norm 399
reproduced under the stated recipe). Even-band RQ==M
instance recorded as EXACT (M==RQ lists identical,
SWAPPED ring; no ordinal per even/odd convention; chain
stands at 22nd odd TAILS from b409).
Next-P303 predictions banked (A-770 re-read: PB0 @122181
0b913100 EQ-P302PB0sig + PB1 09172263 NEW @122182 +
PBA88 06000000 x16 @122183-98 NEW sig 06 + C10-4SIG
@122199-208 = 001e5f60 x4 + 401e5f60 x1 + 801e5f60 x4 +
80055f70 x1 FIRST 4SIG listed-order exact).
