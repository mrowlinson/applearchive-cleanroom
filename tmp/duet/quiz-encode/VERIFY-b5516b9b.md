# VERIFY-b5516b9b b398 T10P290 pins 117657..118004 (1728 tiers) PASS

Seat viewer-r57, first-hand, tree-b5516b9b @b5516b9b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r57.
Base 7e4dcf66 (b397, 1722 tiers). Band = aecb8331 (py merge
w2b@d0220e2e partial, +6 tiers, +62 pins) + b5516b9b (C port,
1728 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build398/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 6c3c3aa3a7dfd249 / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  14abf4e5bcd631a8 / aae 7d8dd3a2d118e0db.
- RGRAMC-PYID 8562/8562 covered=8562/8562 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 17124/17124 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 17124/17124 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp 0 diff, 17124/17124).
- PINS 17126 rows (2 hdr + 17124, +62 vs base 17064);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +31/-0:
  117657 117658 117659 117660 117666 117667 117673 117674
  117675 117676 117681 117682 117683 117684 117685 117692
  117700 117701 117709 117717 117725 117733 117740 117748
  117749 117759 117760 117877 117887 117888 118004
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,7,8,14,15 +
  C6 offs 0,1,6,7,8,9 (offs 2,3,4,5 = 117677/117678/
  117679/117680 unsampled) + Q10 offs 0,7,15,16,24,32,
  40,48,55,63 (b5 const, NO step) + R7 offs 0,10/11,128,
  138/139,255 (both counter edges straddled); 8531->8562);
  31x2=62 rows, range 117657..118004 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit398.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 141 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-3SIG/QUAD88-4R/STANDARD ring; no QT/RT/TT;
  no BM/BC, no M19/XA19, no QB/PT/FM, no M42/X42/H42/
  L42); C==py 12/12. S0/S1 168ch sigs 5f6f1300 NEW /
  ccbede26 NEW (full-string NEW vs BOTH P289 strings;
  S0-vs-P289S0 31/84 @ b0-2,4,5,30,31,38-42,44-50,56-63,
  80-83 EXACT + cross-P289S1 65, S1-vs-P289S1 62/84
  EXACT, agree-pos exactly b11,12,28,29,40,42,52-55,68-
  79 + cross-P289S0 61). AM 16x18ch distinct; AC 77,
  b0-3 02/00/00/00 (b0 const 02), no b4/b5, PBA sig
  02000000 x16 PLAIN. CM 10x26ch 10/10 diverge; CM-b0-2
  sequence 1b19db x7 + bb9cdb x1 + 8bf4d6 x2 ORDERED
  (rows 0-6/7/8-9); CC 69, b0-2 in tab (3 sig bytes),
  b3 const 26, no b4/b5; C10-3SIG 1b19db26 x7 +
  bb9cdb26 x1 + 8bf4d626 x2 ORDERED. M 16x14ch distinct.
  QR 4x24ch 4-distinct UNPAIRED; r0 f272eec66e934b3b
  93fc9b25 distinct; r123 share 8B 328fc02e7833d143,
  byte8 eb/c9/ee; tails b84-87 93fc9b25/eb2b0327/
  c9af0327/eeaf0327 4/4 distinct; r23 TRUE 3B af0327;
  r1 shares 2B 0327 (not the 3B); tail-LCS (0,*)=0,
  (1,2)=(1,3)=2, (2,3)=3 AND tail-lcsuf identical
  0/2/2/3 (both computed first-hand, agree). QC 67,
  b0-3 02000000, no b4/b5; b27-skipped const 55 verified
  in table. RM 16x18ch distinct; RQ 16x14ch distinct;
  RC 70, b0-3 24/00/00/00 NEW, b84-87 fc/aa/79/e0
  ring-wide NEW. M==RQ EXACT 16/16 (lists identical).
  RM-vs-RQ UNPAIRED (sets disjoint). Tails STANDARD-
  SPLIT (RM b80-83 by COL, RQ b76-79 by ROW, 16/16
  distinct each, 0 overlap). Sorted-unique + _N decls
  77/69/67/70 match actual. Missing-sets EXACT: AC [4,
  5,16,17,18,19,23,80,81,82,83]; CC [0,1,2,4,5,11,18,
  19,20,21,22,80,81,82,83]; QC [4,5,16,17,18,22,23,24,
  25,26,28,29,30,80,81,82,83,84,85,86,87]; RC [4,5,18,
  19,27,28,29,30,34,35,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U {b4,
  b5} == 88/84/88/88, 0 overlap). Q legs M[m] + QR[q],
  no frags. R legs RM[c] + RQ[r] STANDARD. AC-QC
  shared-pos 66, same-val 38, AConly 11, QConly 1 (==
  GATE, computed first-hand; NOT const-repeat). P289
  refs re-read: S0 0fc51600 / S1 3bf3f420 / PBA
  02000000 / QUAD 01000000 (== P289 preds EXACT). P290
  preds (A-728/A-353 Next-P290: 5f6f1300/ccbede26/
  02000000/3SIG-7+1+2-ORDERED) x4 corroborated staged.
  PBA REPEAT vs P289 (02000000 == 02000000; novelty =
  AM rows 0-overlap + M9 b16-19,23,80-83 vs P289 M7
  b52-54,80-83 code-verified). QUAD sig NEW vs P289
  (02000000 vs 01000000). QR 0-overlap vs P289QR (R12
  24ch vs P289 R10 20ch). AM/CM/M/QR/RM/RQ 0-overlap
  vs P289 (widths differ M 14ch vs 12ch, AM 18ch vs
  14ch, CM 26ch vs 24ch, QR 24ch vs 20ch, RQ 14ch vs
  12ch; RM same width 18ch but 0-overlap; base widths
  re-read first-hand). M-tails 16/16 ALL NEW vs P289
  M-tail8 + P289 RM-tail8 + P289 RQ-tail8 (overlap 0
  x3). Memo INCL PBA88 78 / C10 70 / quad88 68 / T88
  70 (A-729 re-read): impl 77/69/67/70 = memo-1 on
  PBA/C10/quad (b5-const excluded), identical T88.
  Base temp maxes _t6059/_b3671/_i3672 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 117657 / S1 117658 / A 117659-674 / C 117675-684 /
  Q 117685-748 / R 117749-118004): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-consts emerge from raw lencode) + Q b5
  const 0x97 full block (equiv counter b4=(0x6b+2off)
  &FF 64/64) + R counter b4=(0xeb+2off)&FF b5=0x97+
  (off>=11)+(off>=139) (py hex; C stages decimal 235/
  151/11/139, re-derived from code text both sides) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/rtab byte positions exact (A 9B b16-19,23,80-83;
  C 13B b0-2,11,18-22,80-83; Q QM7 b28-30,80-83 + R12
  b16-18,22-26,84-87; R TM9 b18,19,27,34,35,80-83 by
  COL + TR7 b28-30,76-79 by ROW) + NO frag leg in Q.
  T-mirrors T78745/78750/78755/78770/78786/78807 each
  re-read: hits the exact py guard line. C guards
  `if ((n) == (117657))` / `(117658)` + 4 range guards
  exact. C byte-index lists match py per block (A 9B,
  C 13B, Q 7B/12B, R 9/7B). Temps _t6060-6075
  continuous (base max _t6059) + _b3673/3675/3677/3678/
  3680/3681 (base max _b3671) + _i3674/3676/3679/3682
  (base max _i3672): added-lines-only refs (base tree
  zero refs to new temps) prove no reuse. Insert exact
  both sides: after T10P289R close, at dispatch tail
  (N-out-of-scope fallthrough follows; C 2 scope hits,
  py 2 scope hits). Matches A-729/A-354 geometry
  (values re-checked in audit above; NO D dips: ownloop
  tags exactly the 6 P290 blocks).
- Edges own-loop ownloop398.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P290R N=118004 off=
  255. edges398.py: paylens 12x84 + 336x88; lencode
  92/92 (S/A/C/Q raw l16; S0/S1 33/97, 35/97 == raw
  lencode) + aform 16/16 (A 88B head 37/97 tail 55/97
  b5set {97} NO step, 0 ff) + cform 10/10 (C head 57/
  97 tail 69/97 b5set {97} NO step, 0 ff) + qform 64/64
  + qb5const 64/64 (Q head 6b/97 tail e9/97 b5set {97}
  NO step, 0 ff in 64; quad b4 formula == raw-lencode
  64/64); ring counter 256/256 + ringraw 256/256 (head
  eb/97; 117759 off10 ff/97 -> 117760 off11 01/98; mid
  off128 eb/98; 117887 off138 ff/98 -> 117888 off139
  01/99; tail off255 e9/99; exactly 2 ff in 256 at
  o10/o138); odd-lencode 348/348. Ring edges + tail
  118004 in for-list + 2 PASS lines each py+C. Tail
  118004: oracle sha 28ac09d19a6c88e4... matches PINS;
  py+C CLOSED T10P290R off=255 agree. No DISSENT: cut
  bytes verify.
- PB-diff secf398.py (cache path) + secf398b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (117657 +
  117309 + 117658 + 117310); S0: oracle117657-vs-117309
  31/84, codeS0-vs-P289S0 31/84, positions identical;
  DIRECT tool 31/84 with identical agree-pos 53
  positions. S1: oracle 62/84, code 62/84, positions
  identical; DIRECT 62/84 identical agree-pos 22
  positions (b11,12,28,29,40,42,52-55,68-79 ==
  tabaudit). 0 miss (ownloop pre-warmed). Twice-derived
  both pairs. P289C10-head n117327 vs S1: 55/84 differ,
  sigs differ (3bf3f420 vs ccbede26 -- matches GATE
  note: P290S1 NEW standalone, matches no P290 sig).
  No byte-equal wording in A-729/A-354 this band (both
  stage NEW sigs, consistent with 31/62 diffs) --
  byte-diff discipline observed, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del; raw py 230
  content / 0 del. Fine-norm (temp-norm, empty-
  excluding): del-uniq 0 add-uniq 387 missing 0 ==
  GATE EXACT (first-hand, no reconstruction needed;
  this GATE states the temp-norm recipe explicitly).
  del-subset-add 0 missing holds (integrity intact).
- Wall on band diff added lines (scope 7e4dcf66..
  b5516b9b, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (aecb8331), code 6 blocks,
  tier-comments `# T10P` 1628->1634 +6, py top-level
  singletons (^4sp `if n == `) 602->604 +2 == GATE
  stated-method EXACT, py T10P range guards 590->594
  +4 == GATE EXACT, CLOSED T10P prints 1628->1634 +6
  py + 1628->1634 +6 C, C singleton `if ((n) == (`
  607->609 +2 == GATE EXACT / C ranges 612->616 +4 ==
  GATE EXACT, seal 1722->1728 +6 (commit msgs): all
  agree, no slip. C-vs-py-GATE +5 offset pre-existing
  + unchanged (nested guards counted in C total both
  trees).
- CONFIRM evidence (CONVERT-01 rule b): A-729-q882-
  t10p290 verdict CONFIRM, tallies 14/14 + 11/11 + 12/12
  = 37/37 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 16 total vs 37, counting unit irreproducible;
  methodology note, NO verdict impact) + exact-value
  corroboration incl PB0/PB1 NEW, PBA88-PLAIN + b5
  const, C10-3SIG ORDERED 7+1+2 map, QUAD88-4R + R12
  rows + 8B-share + r23-TRUE-3B + r1-2B + b5 const +
  M-tails NEW, ring STANDARD + TR7 16/16 UNPAIRED +
  edges + consts (all re-checked above) + A-354 viewer
  corroboration (CONFIRM all legs, consts 78/70/68/70
  INCL). No CONFIRM-P290.md file (absence verified);
  A-729 suffices per rule. Agrees with cport commit msg
  (PYID 8562, RGRAM 17124).
- Quiz: no conflicting CLAIM/GATE/FLAG on b398 (own seat
  CLAIM only). Newest PARENT-QNUM-22 (w2e Q-block grant,
  read, no gate impact) -- GATE cites no QNUM (no
  staleness). PROSE-01: all hex/counts above copied from
  own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 0 prose slips (norm recipe stated explicitly this
band, temp-norm 387 reproduced EXACT with no variant
gap; py-tier recipe reproduced EXACT via top-level-
guard reading).
Next-P291 predictions banked for r58 (A-729/A-354: PB0
@118005 5f6f1300 sig-REPEAT (30/84 payload diff vs
n117657 settled, never assumed) / PB1 2b81c726 NEW /
PBA88-STEP 02000000 x16 / C10-2SIG 2b81c726 x8 @118023-
30 + 2b816713 x2 @118031-32 ORDERED 8+2 window-resolved).
