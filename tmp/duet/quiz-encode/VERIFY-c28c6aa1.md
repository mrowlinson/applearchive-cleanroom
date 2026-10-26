# VERIFY-c28c6aa1 b394 T10P286 pins 116265..116612 (1704 tiers) PASS

Seat viewer-r56, first-hand, tree-c28c6aa1 @c28c6aa1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r56.
Base 9cac7b4f (b393, 1698 tiers). Band = b959a4a1 (py merge
w2b@21de6053 partial, +6 tiers, +62 pins) + c28c6aa1 (C port,
1704 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build394/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1be7f560a2fadb4b / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  982a172241f3960d / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8437/8437 covered=8437/8437 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16874/16874 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16874/16874 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 16874/16874).
- PINS 16876 rows (2 hdr + 16874, +62 vs base 16814);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  116265 116266 116267 116268 116274 116275 116281 116282
  116283 116284 116287 116288 116291 116292 116293 116308
  116309 116317 116325 116333 116341 116351 116352 116356
  116357 116479 116480 116485 116607 116608 116612
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,4,5,8,9 + Q10 offs 0,15,16,24,32,40,48,
  58,59,63 + R7 offs 0,122,123,128,250,251,255;
  8406->8437); 31x2=62 rows, range 116265..116612 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit394.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 125 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/1SIG/QUAD88-4R/SWAPPED ring; no QT/RT/TT; no
  BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/L42);
  C==py 12/12. S0/S1 168ch sigs 1df80a00 NEW / cd23fd15
  (sig-eq P285C10, payload NEW: full-string NEW vs BOTH
  P285 strings; S0-vs-P285S0 30/84 exact-pos +
  cross-P285S1 34, S1-vs-P285S1 46/84 exact-pos +
  cross-P285S0 57). AM 16x14ch distinct; AC 79, b0-3
  01/00/00/00 (b0 const 01), no b4/b5, PBA sig 01000000
  x16 PLAIN. CM 10x26ch 10/10 diverge; CC 69, b0-3
  cd236d10 full-sig in consts, no b4/b5 (C10-1SIG x10).
  M 16x18ch distinct. QR 4x22ch 4-distinct UNPAIRED; r0
  8549271f5406c3bd851512 distinct; r123 share 7B
  fb421acf3422d6, differ at byte 7 (4e/73/98); tails
  b84-87 bd851512/4ec1d406/73c1d406/98c1d406 4/4
  distinct; r123 TRUE 3B c1d406; byte-LCS (0,*)=0,
  (1,2)=(1,3)=(2,3)=3. QC 66, b0-3 01000000, no b4/b5.
  AC-QC shared-pos 66 same-val 39 (NOT const-repeat;
  QC positions subset of AC positions). RM 16x16ch
  distinct; RQ 16x18ch distinct; RC 69, b0-3 10/00/00/
  00, b84-87 b0/d5/78/7a ring-wide. M==RQ 16/16
  identical row-for-row INTRA-tier. RM-vs-RQ UNPAIRED
  (sets disjoint; tail4 sets disjoint). Sorted-unique +
  _N decls 79/69/66/69 match actual. Missing-sets EXACT:
  AC [4,5,38,46,47,80,81,82,83]; CC [4,5,34,35,41,42,43,
  44,45,46,47,80,81,82,83]; QC [4,5,38,39,46,47,48,49,
  50,51,52,53,54,55,80,81,82,83,84,85,86,87]; RC [4,5,6,
  7,12,13,51,52,53,54,55,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U {b4,
  b5} == 88/84/88/88, 0 overlap). A m-tab = 7 positions
  (code stages M7 geometry; staged "M6" label is the
  A-710/A-350-noted label nit, geometry stands). Q legs
  M[m] + QR[q], no frags. R legs RM[c] + RQ[r] SWAPPED.
  P285 refs re-read: S0 19f80a00 / S1 ddbef415 / PBA
  01000000 / C10 cd23fd15 (== P285 preds EXACT). P286
  preds (A-709/A-349 Next-P286: 1df80a00/cd23fd15/
  01000000/cd236d10) x4 corroborated staged. PBA REPEAT
  vs P285 (01000000 == 01000000; novelty = AM rows
  0-overlap + M7 b38,46,47,80-83 vs P285 M9). C10 NEW
  vs P285 (cd236d10 vs cd23fd15; M13 b34,35,41-47,80-83
  vs P285 M12). QR 0-overlap vs P285QR (same width
  22ch). M-tails 16/16 ALL NEW vs P285M-tail8 +
  P285RM-tail8 + P285RQ-tail8 (0 overlap x3). AM/CM/M/
  RM/RQ 0-overlap vs P285 (widths differ M 18ch vs 16ch,
  AM 14ch vs 18ch, CM 26ch vs 24ch, RM 16ch vs 14ch, RQ
  18ch vs 14ch). Memo INCL PBA88 80 / C10 70 / quad88
  66 / T88 69 (A-710 re-read): impl 79/69/66/69 =
  memo-1 on PBA/C10 (b5-const excluded), identical
  quad/T88. Base temp maxes _t5995/_b3631/_i3632 (no
  reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 116265 / S1 116266 / A 116267-282 / C 116283-292 /
  Q 116293-356 / R 116357-612): bounds + paylens (12x84
  + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q both
  sides (b5-const/step emerge from raw lencode; Q equiv
  counter b4=(0x8b+2off)&FF verified 64/64 in edges) +
  R counter b4=(0x0b+2off)&FF b5=0x8d+(off>=123)+
  (off>=251) (py hex; C stages decimal 11/141/123/251,
  re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 7B b38,46,47,80-83; C 13B
  b34,35,41-47,80-83; Q QM9 b51-55,80-83 + R11 b38,39,
  46-50,84-87; R TM8 b6,7,12,13,76-79 by COL + TR9
  b51-55,80-83 by ROW) + NO frag leg in Q. T-mirrors
  T77821/77826/77831/77846/77862/77883 each re-read:
  hits the exact py guard line. C guards `if ((n) ==
  (116265))` / `(116266)` + 4 range guards exact. C
  byte-index lists match py per block (A 7B, C 13B, Q
  9B/11B, R 8/9B). Temps _t5996-6011 continuous (base
  max _t5995) + _b3633/3635/3637/3638/3640/3641 (base
  max _b3631) + _i3634/3636/3639/3642 (base max _i3632):
  added-lines-only refs (base tree zero refs to new
  temps) prove no reuse. Insert exact both sides: after
  T10P285R close, at dispatch tail (N-out-of-scope
  fallthrough follows; C 2 scope hits, py 2 scope
  hits). Matches A-710/A-350 geometry (values re-checked
  in audit above; NO D dips: ownloop tags exactly the 6
  P286 blocks). Py S1 comment T77826 cites "57/84
  payload diff first-hand, NOT byte-equal" (code-side
  corroboration of secf below).
- Edges own-loop ownloop394.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P286R N=116612 off=255.
  edges394.py: paylens 12x84 + 336x88; lencode 92/92
  (S/A/C/Q raw l16; S0/S1 53/8c, 55/8c == raw lencode
  0x8C53/0x8C55) + aform 16/16 (A 88B head 57/8c tail
  75/8c b5set {8c} NO step, 0 ff) + cform 10/10 (C head
  77/8c tail 89/8c b5set {8c} NO step, 0 ff) + qform
  64/64 (Q head 8b/8c tail 09/8d b5set {8c,8d} step
  o58->59: 116351 o58 ff/8c -> 116352 o59 01/8d Q-row3,
  exactly 1 ff in 64); ring counter 256/256 + ringraw
  256/256 (head 0b/8d; 116479 off122 ff/8d -> 116480
  off123 01/8e; 116607 off250 ff/8e -> 116608 off251
  01/8f; tail off255 09/8f; exactly 2 ff in 256 at
  o122/o250); odd-lencode 348/348. Ring edges + tail
  116612 in for-list + 2 PASS lines each py+C. Tail
  116612: oracle sha 395816e2e918a172... matches PINS.
  No DISSENT: cut bytes verify.
- PB-diff secf394.py (cache path) + secf394b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (116265 +
  115917 + 116266 + 115918); S0: oracle116265-vs-115917
  30/84, codeS0-vs-P285S0 30/84, positions identical;
  DIRECT tool 30/84 with identical agree-pos 54
  positions. S1: oracle 46/84, code 46/84, positions
  identical; DIRECT 46/84 identical agree-pos 38
  positions. PB1-vs-P285C10-head: oracle116266-vs-115935
  57/84 DIFFER, DIRECT tool 57/84 with identical
  agree-pos 27 positions ([0-3,6-20,44-51]); sigs both
  cd23fd15 (sig-eq only). 0 miss (ownloop pre-warmed).
  A-350 leg-1 "(byte-equal to n115935 first-hand)"
  wording REFUTED first-hand, twice-derived (cache path
  + direct-tool path, identical agree positions): 57/84
  differ. A-710 (57/84 NOT byte-equal) + GATE + py S1
  comment CONFIRMED. Record corrected here (r54/A-342
  precedent: correction lives in the VERIFY record; 4th
  memo wording refutation: A-342/A-345/A-347/A-350).
  A-350 legs 2-3 + consts stand. A-350 "r123 share 11B-
  prefix fb421acf3422" loose wording: true shared run
  is 7B fb421acf3422d6 (A-710 correction corroborated
  first-hand; rows differ at byte 7).
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Normalized: C tempnorm del-uniq 0
  add-uniq 403 missing 0 == GATE EXACT; py tempnorm
  del-uniq 0 add-uniq 185 missing 0; r55-recipe C
  add-uniq 150 / py 167, 0 missing.
- Wall on band diff added lines (scope 9cac7b4f..
  c28c6aa1, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (b959a4a1), code 6 blocks,
  tier-comments `# T10P` 1604->1610 +6, singletons
  plain-method 604->606 +2 (= GATE dispatch-guard
  594->596 + 10 inline non-guards both sides) / ranges
  596->600 +4, CLOSED T10P prints 1604->1610 +6 py +
  1604->1610 +6 C, C singleton `if ((n) == (` 599->601
  +2 / C ranges 596->600 +4, seal 1698->1704 +6 (commit
  msgs): all agree, no slip. 5-count C-vs-py singleton
  offset pre-existing + unchanged (gap 5 at base AND
  new under GATEPAT).
- CONFIRM evidence (CONVERT-01 rule b): A-710-q798-
  t10p286 verdict CONFIRM, tallies 14/14 + 12/12 + 12/12
  = 38/38 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 18 total vs 38, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0 NEW + PB1 sig-eq + 57/84 diff,
  PBA88-PLAIN, C10-1SIG, QUAD88-4R + R11 rows + 7B-share
  + TRUE-3B + b5 step + edge + M-tails NEW, ring SWAPPED
  + TR9 16/16 UNPAIRED + edges + consts (all re-checked
  above) + own P285C10-head n115935 reconstruction
  57/84 vs P286S1 payload-NEW (reproduced first-hand,
  twice-derived) + A-350 viewer corroboration (legs 2-3
  CONFIRM, consts 80/70/66/69 INCL; leg-1 byte-equal
  wording REFUTED per secf above, sig-eq value
  CONFIRMS). No CONFIRM-P286.md file (absence verified);
  A-710 suffices per rule. Agrees with cport commit msg
  (PYID 8437, RGRAM 16874).
- Quiz: no conflicting CLAIM/GATE/FLAG on b394 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites no QNUM (quiz line claims poll
  only): no staleness to note. PROSE-01: all hex/counts
  above copied from own run output; GATE re-read before
  filing.

Verdict: PASS. No RED. GATE CORRECT on code + prose.
Next-P287 predictions banked for r56+ (A-710/A-350: PB0
85620b00 / PB1 4c0ac516 / PBA88 01000000 x16 / C10
86148a2d).
FLAG for parent/memo (code PASS): A-350 leg-1 byte-equal
wording refuted + corrected above (4th memo wording
refutation this project: A-342/A-345/A-347/A-350 --
pattern: viewer-r8 leg-1 "byte-equal" claims vs memo-r3
measured diffs; suggest memo-side byte-diff discipline).
