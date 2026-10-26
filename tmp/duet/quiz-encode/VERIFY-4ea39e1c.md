# VERIFY-4ea39e1c b392 T10P284 pins 115569..115916 (1692 tiers) PASS

Seat viewer-r56, first-hand, tree-4ea39e1c @4ea39e1c,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r56.
Base 2d5cbe97 (b391, 1686 tiers). Band = dc9bff5b (py merge
w2b@c6a35346 partial, +6 tiers, +62 pins) + 4ea39e1c (C port,
1692 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build392/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 06b3de142bd3a869 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  6319d23c3fa0fd7f / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8375/8375 covered=8375/8375 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16750/16750 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16750/16750 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 16750/16750).
- PINS 16752 rows (2 hdr + 16750, +62 vs base 16690);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  115569 115570 115571 115572 115582 115583 115584 115586
  115587 115588 115591 115592 115595 115596 115597 115604
  115612 115613 115621 115629 115637 115645 115652 115660
  115661 115711 115712 115789 115839 115840 115916
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,11,12,13,15 +
  C6 offs 0,1,4,5,8,9 + Q10 offs 0,7,15,16,24,32,40,48,55,
  63 + R7 offs 0,50,51,128,178,179,255; 8344->8375);
  31x2=62 rows, range 115569..115916 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit392.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 130 PASS
  0 FAIL. Inventory exactly the 12 both sides (PLAIN/1SIG/
  QUAD88-4R/STANDARD ring, no QT/RT/TT; no BM/BC, no M19,
  no QB/PT/FM, no M42/X42, no R8/X8, no H42/L42); C==py
  12/12. S0/S1 168ch sigs 99f00700 NEW / 4513630f NEW
  (full-string NEW vs BOTH P283 strings; S0-vs-P283S0
  31/84 exact-pos + cross-P283S1 36, S1-vs-P283S1 54/84
  exact-pos + cross-P283S0 73). AM 16x18ch distinct; AC
  73, b0-3 5d/34/31/f6 (b0 const 5d), no b4/b5, PBA sig
  5d3431f6 x16 STEP. CM 10x22ch 10/10 diverge; CC 71,
  b0-3 c432f015 full-sig in consts, no b4/b5 (C10-1SIG
  x10). M 16x14ch distinct. QR 4x20ch 4-distinct
  UNPAIRED; r0 1b36beda5c674aa60eca distinct; r123 share
  6B 534c7bdbb26d; tails b84-87 4aa60eca/e4e03671/
  e7843771/0c853771 4/4 distinct; r123 share 1B 71, r2r3
  share 2B 3771, r1 last-2B 3671 differs; byte-LCS
  (0,*)=0, (1,2)=1, (1,3)=1, (2,3)=2. QC 69, b0-3
  01000000, no b4/b5. AC-QC shared-pos 62 same-val 7
  (NOT const-repeat). RM 16x16ch distinct; RQ 16x14ch
  distinct; RC 71, b0-3 14/00/00/00, b84-87 30/9f/7e/aa
  ring-wide. M==RQ 16/16 identical row-for-row INTRA-tier.
  RM-vs-RQ UNPAIRED (full-row sets disjoint; tail4 sets
  16-distinct each, SPLIT-disjoint). Sorted-unique + _N
  decls 73/71/69/71 match actual. Missing-sets EXACT: AC
  [4,5,6,7,8,9,10,76,77,78,79]; CC [4,5,6,7,8,48,49,50,
  51,80,81,82,83]; QC [4,5,6,7,13,14,15,52,53,54,55,80,
  81,82,83,84,85,86,87]; RC [4,5,8,9,10,13,14,15,19,76,
  77,78,79,80,81,82,83]. Coverage unions exact every
  block (const U tab U {b4,b5} == 84/84/88/88, 0
  overlap). Q legs M[m] + QR[q], no frags, no nibsplit.
  R legs RM[c] + RQ[r] STANDARD. P283 refs re-read: S0
  9ef00700 / S1 4513e30f / PBA c09b7fe2 / C10-map
  4513e30f x6 + 4513f307 x4 (== A-699/A-347 preds EXACT).
  P284 preds (r55: 99f00700/4513630f/5d3431f6/c432f015)
  x4 corroborated staged. PBA NEW vs P283; C10 NEW vs
  P283 map; QR 0-overlap vs P283QR; M-tails 16/16 ALL
  NEW vs P283M-tail8 + P283RM-tail8 + P283RQ-tail8 (0
  overlap x3). AM/CM/M/QR/RM/RQ 0-overlap vs P283
  (widths differ M 14ch vs 12ch, RM 16ch vs 12ch; RQ
  same width 14ch but 0-overlap). Memo INCL PBA 73 /
  C10 72 / quad88 70 / T88 71 (A-705 re-read): impl
  73/71/69/71 = memo identical on PBA/T88, memo-1 on
  C10/quad (b5-const excluded). Base temp maxes
  _t5963/_b3611/_i3612 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 115569 / S1 115570 / A 115571-586 / C 115587-596 /
  Q 115597-660 / R 115661-916): bounds + paylens (28x84
  + 320x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q both
  sides (A/C/Q; b5-step/consts emerge from raw lencode)
  + R counter b4=(0x9b+2off)&FF b5=0x87+(off>=51)+
  (off>=179) (py hex; C stages decimal 155/135/51/179,
  re-derived from code text both sides) + m=off&15/
  q=off>>4/c=off&15/r=off>>4 both sides + mtab/rtab
  byte positions exact (A 9B b6-10,76-79; C 11B b6-8,
  48-51,80-83; Q QM7 b13-15,80-83 + R10 b6,7,52-55,
  84-87; R TM8 b8,9,10,19,80-83 by COL + TR7 b13,14,15,
  76-79 by ROW) + NO frag leg in Q. T-mirrors T77361/
  77366/77371/77386/77402/77423 each re-read: hits the
  exact py guard line. C guards `if ((n) == (115569))` /
  `(115570)` + 4 range guards exact. Temps _t5964-5979
  continuous (base max _t5963) + _b3613/3615/3617/3618/
  3620/3621 (base max _b3611) + _i3614/3616/3619/3622
  (base max _i3612): added-lines-only refs (base tree
  zero refs to new temps) prove no reuse. Insert exact
  both sides: after T10P283R close, at dispatch tail
  (N-out-of-scope fallthrough follows; C 2 scope hits,
  py 2 scope hits). Matches A-705/A-348 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P284 blocks).
- Edges own-loop ownloop392.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P284R N=115916 off=255.
  edges392.py: paylens 28x84 + 320x88; lencode 92/92
  (S/A/C raw l16; S0/S1 e3/86, e5/86 == raw lencode
  0x86E3/0x86E5) + aform 16/16 (A head e7/86 tail 05/87
  b5set {86,87} step o12->13: 115583 o12 ff/86 ->
  115584 o13 01/87, exactly 1 ff in 16) + cform 10/10
  (C head 07/87 tail 19/87 b5set {87} NO step, 0 ff) +
  qform 64/64 (Q head 1b/87 tail 99/87 b5set {87} NO
  step, 0 ff); ring counter 256/256 + ringraw 256/256
  (head 9b/87; 115711 off50 ff/87 -> 115712 off51
  01/88; 115839 off178 ff/88 -> 115840 off179 01/89;
  tail off255 99/89; exactly 2 ff in 256 at o50/o178);
  odd-lencode 348/348. Ring edges + tail 115916 in
  for-list + 2 PASS lines each py+C. Tail 115916:
  oracle sha fbd6e8032c287455... matches PINS. No
  DISSENT: cut bytes verify.
- PB-diff secf392.py (cache path) + secf392b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (115569 +
  115221 + 115570 + 115222); S0: oracle115569-vs-115221
  31/84, codeS0-vs-P283S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1: oracle 54/84, code 54/84, positions
  identical; DIRECT 54/84 identical agree-pos 30
  positions. 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. No byte-equal wording in A-705/A-348 this
  band (both stage NEW sigs, consistent with 31/54
  diffs) -- byte-diff discipline observed, nothing to
  refute.
- C diff pure-add: numstat 600/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 595 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Normalized: C tempnorm del-uniq 0
  add-uniq 415 missing 0 == GATE EXACT; py tempnorm
  del-uniq 0 add-uniq 191 missing 0; r55-recipe C
  add-uniq 150 / py 172, 0 missing.
- Wall on band diff added lines (scope 2d5cbe97..
  4ea39e1c, 893 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 600/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (dc9bff5b), code 6 blocks,
  tier-comments `# T10P` 1592->1598 +6, singletons
  plain-method 600->602 +2 / ranges 588->592 +4,
  CLOSED T10P prints 1592->1598 +6 py + 1592->1598 +6 C,
  C singleton `if ((n) == (` 595->597 +2 (GATE pattern
  REPRODUCED EXACT) / C ranges 588->592 +4, seal 1686->
  1692 +6 (commit msgs): all agree, no slip. 5-count
  C-vs-py singleton offset pre-existing + unchanged
  (gap 5 at base AND new under GATEPAT).
- CONFIRM evidence (CONVERT-01 rule b): A-705-q796-
  t10p284 verdict CONFIRM, tallies 14/14 + 12/12 + 12/12
  = 38/38 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 17 total vs 38, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PBA-STEP + b5 step + edge,
  C10-1SIG, QUAD88-4R + QR rows + tails + LCS + M-tails
  NEW, ring STANDARD + TR7 16/16 UNPAIRED + edges +
  consts (all re-checked above) + own P283C10-head
  n115239 reconstruction 49/84 vs P284S1 NEW
  (reproduced first-hand) + A-348 viewer corroboration
  (CONFIRM all legs, consts 73/72/70/71 INCL). No
  CONFIRM-P284.md file (absence verified); A-705
  suffices per rule. Agrees with cport commit msg
  (PYID 8375, RGRAM 16750).
- Quiz: no conflicting CLAIM/GATE/FLAG on b392 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-19 vs -21).
Next-P285 predictions banked for r56+ (A-705/A-348: PB0
19f80a00 / PB1 ddbef415 / PBA88 01000000 x16 / C10
cd23fd15).
