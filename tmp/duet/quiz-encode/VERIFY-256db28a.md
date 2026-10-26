# VERIFY-256db28a b390 T10P282 pins 114873..115220 (1680 tiers) PASS

Seat viewer-r55, first-hand, tree-256db28a @256db28a,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r55.
Base 4ef44f6f (b389, 1674 tiers). Band = 3640ef6d (py merge
w2b@db0be62c partial, +6 tiers, +64 pins) + 256db28a (C port,
1680 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build390/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 8a15c93b61b7538b / aae
  d6e27c97ced21673 (== GATE both) + sha1 rgramc
  5badf4c1760ff7cf / aae 7d8dd3a2d118e0db (aae pinned,
  band touches no aae sources per numstat).
- RGRAMC-PYID 8311/8311 covered=8311/8311 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16622/16622 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16622/16622 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16622/16622 sorted).
- PINS 16624 rows (2 hdr + 16622, +64 vs base 16560);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +32/-0:
  114873 114874 114875 114876 114880 114885 114889 114890
  114891 114892 114896 114897 114898 114899 114900 114901
  114916 114917 114932 114933 114943 114944 114948 114949
  114964 114965 115071 115072 115136 115199 115200 115220
  (== GATE verbatim; S0/S1 (2) + A6 offs 0,1,5,10,14,15 +
  C7 offs 0,1,5,6,7,8,9 (offs 2,3,4 = 114893/894/895
  unsampled) + Q10 offs 0,15/16,31/32,42/43,47/48,63
  (edge-pair 42/43 = Q step edge) + R7 offs 0,106/107,
  171,234/235,255; 8279->8311); 32x2=64 rows, range
  114873..115220 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit390.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 135 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT/TT; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8); C==py 13/13. S0/S1 168ch sigs
  9ef00700 NEW / cb3de10f NEW (full-string NEW vs BOTH
  P281 strings; diffs S0 31/65 + S1 60/60 EXACT). AM
  16x16ch distinct; AC 74, b0-3 e0/85/7f/fe (b0 const
  e0), no b4/b5, PBA sig e0857ffe. CM 10x26ch 10/10
  diverge; staged sigs ORDERED 3582e4 x6 + 4dffe7 +
  8d59ea + ad85e1 x2; CC 69, b3 const 0f, no b0/b1/b2
  (full sig b0-2 in tab), no b4/b5; full C10 map
  3582e40f x6 + 4dffe70f + 8d59ea0f + ad85e10f x2
  (ORDERED 6+1+1+2). M 16x14ch distinct. QR r0
  b280ae92788e26 distinct (last3 788e26), r1==r2==r3
  72fabf3a6f842e LAST3-PAIRED (last3 6f842e), 2 distinct.
  QT dd6e42df/e1a9fa40/06aafa40/227a1141 4/4 distinct;
  r1/r2 share last 2B fa40 (first halves e1a9/06aa
  differ); r0/r3 last-2B 42df/1141 do not. QC 64, b0-3
  c09b7fe2 (QUAD1s single-sig x64), b20 const 93, no
  b4/b5. RM 16x18ch distinct; RQ 16x14ch 16/16 distinct;
  RC 70, b0-3 0f/00/00/00, b84-87 63/fa/92/06 ring-wide.
  Sorted-unique + _N decls 74/69/64/70 match actual.
  Missing-sets EXACT: AC [4,5,12,13,14,19,76,77,78,79];
  CC [0,1,2,4,5,11,18,19,20,21,22,80,81,82,83]; QC [4,5,
  12,13,14,18,19,21,22,24,25,26,76,77,78,79,80,81,82,83];
  RC [4,5,18,19,27,28,29,30,34,35,76,77,78,79,80,81,82,
  83]. Coverage unions exact every block (const U tab U
  {b4,b5} == 84/84/84/88, 0 overlap). Q legs M[m] +
  QR[q] + QT[q], no frags. R legs RM[c] + RQ[r] STANDARD.
  M==RQ EXACT 16/16 row-for-row + set-eq + C-side
  identical (GATE-stated INTRA-tier identity, confirmed).
  RM-vs-RQ UNPAIRED (full-row sets disjoint; RM-tail4/
  RQ-tail4 16 distinct each, SPLIT-disjoint). AC-QC
  shared-pos 64 same-val 36 (NOT const-repeat). QT byte-
  LCS all-pairs: (1,2)=2 rest 0 (own code-table LCS, memo
  value exact). P281 refs re-read: S0 5eae0700 / S1
  2557520f (== A-692/A-345 preds); PBA c09417fb; C10-4SIG
  partial-b2,3-tab geometry (CC b0,b1 const 25,57, no b2/
  b3 -- full-b0-2-tab change code-verified); RC b0-3
  0c000000 + b84-87 af7cecbc. P282 preds (A-692/A-345
  Next-P282) x4 corroborated (9ef00700/cb3de10f/e0857ffe/
  6+1+1+2 map == staged). M-tails 16/16 ALL NEW vs P281M-
  tail8 + P281RM-tail8 + P281RQ-tail8 (0 overlap x3).
  AM/CM/M/RM/RQ/QT/QR 0-overlap vs P281 (widths 16v12/
  26v24/14v16/18v16/14v16 EXACT; QR/QT same widths 14ch/
  8ch but 0-overlap). Memo INCL PBA 75 / C10 70 / quad
  64 / T88 70 (A-696 re-read): impl 74/69/64/70 = memo-1
  on PBA/C10 (b5-const excluded), identical quad/T88.
  Base temp maxes _t5923/_b3589/_i3590 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 114873 / S1 114874 / A 114875-890 / C 114891-900 /
  Q 114901-964 / R 114965-220): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (A/C/Q; b5-const/step emerge from raw lencode) +
  R counter b4=(0x2B+2off)&FF b5=0x82+(off>=107)+(off>=
  235) (py hex; C stages decimal 43/130/107/235, re-
  derived from code text both sides) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/qtab/ttab byte
  positions exact (A 8B b12-14,19,76-79; C 13B b0-2,11,
  18-22,80-83; Q 7/7/4B QM7 b24-26,76-79 + R7 b12-14,18,
  19,21,22 (b20 skipped const) + T4 b80-83; R 9B TM9
  b18,19,27,34,35,80-83 by COL + 7B TR7 b28-30,76-79 by
  ROW) + M[m]/QR[q]/QT[q]/RM[c]/RQ[r] compares + NO frag
  leg in Q (py + C region greps). T-mirrors T76863/76868/
  76873/76888/76904/76927 each re-read: hits the exact py
  guard line. C guards `if ((n) == (114873))` / `(114874)`
  + 4 range guards exact. Temps _t5924-5941 continuous
  (base max _t5923) + _b3591/3593/3595/3596/3597/3599/
  3600 (base max _b3589) + _i3592/3594/3598/3601 (base
  max _i3590): added-lines-only refs prove no reuse.
  Insert exact both sides: after T10P281R close (C
  205484), at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-696/A-346 geometry (values re-
  checked in audit above; NO D dips: ownloop tags
  exactly the 6 P282 blocks).
- Edges own-loop ownloop390.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P282R N=115220 off=255.
  edges390.py: paylens 92 x84 + 256 x88; lencode 92/92
  (S0/S1 73/81 + 75/81 == raw lencode 0x8173/0x8175) +
  aform 16/16 (A head 77/81 tail 95/81 b5set {81} NO
  carry) + cform 10/10 (C head 97/81 tail a9/81 b5set
  {81} NO carry) + qform 64/64 (Q head ab/81, step off42/
  43 114943 ff/81 -> 114944 01/82 mid-row2, tail 29/82,
  b5set {81,82}, exactly 1 ff in 64 at o42); ring counter
  256/256 + ringraw 256/256 (head 2b/82; 115071 off106
  ff/82 -> 115072 off107 01/83; mid 115136 off171 81/83;
  115199 off234 ff/83 -> 115200 off235 01/84; tail off255
  29/84; exactly 2 ff in 256 at o106/o234); odd-b4 348/
  348 by formula construction (all 5 formulas odd-base +
  2off, all conformance checks green). Ring edges + tail
  115220 in for-list + 2 PASS lines each py+C. Tail
  115220: oracle sha 46ce2926d6caad19... matches PINS; py
  PASS + C CLOSED T10P282R off=255 agree. No DISSENT:
  cut bytes verify.
- Reconstruction secf390.py (cache path) + secf390b.py
  (DIRECT tool, no cache): staged n114543 from P281 code
  (CC + CM row0 520f769791c36744d037d006 + CTAB b2,3,46-
  51,80-83 + lencode) vs oracle 0 diff; oracle114543-vs-
  P282S1 57/84; DIRECT tool 57/84 with identical agree-
  pos 27 positions (3,8,12,17,28,29,40,52-59,68-79) both
  paths. 0 miss (ownloop pre-warmed). A-696's "own
  P281C10-head n114543 reconstruction 57/84 vs P282S1
  NEW" corroborated twice-derived.
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Own-recipe sweep: C del-uniq 0
  add-uniq 157, py del-uniq 0 add-uniq 175, 0 missing.
  GATE temp-norm recipe replicated: C del-uniq 0
  add-uniq 393 missing 0 == GATE EXACT.
- Wall on band diff added lines (scope 4ef44f6f..
  256db28a, 912 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits (loose-`aa` 15 lines on record, all hex -- GATE
  makes no loose claim this band). Files: rgramc.c 610/0,
  rgram.py 237/0 purely additive, test_rgram.sh 1/1,
  PINS +64/+0.
- Tiers: merge-msg +6/+64 (3640ef6d), code 6 blocks,
  singletons 596->598 +2 / ranges 580->584 +4 (stated
  method, plain `if n ==` / `<= n <=` BSD grep), C `(n)
  == (` 596->598 +2 / range idiom 580->584 +4 (absolute
  agreement, even-band no-offset), CLOSED T10P prints
  1580->1586 +6 py + 1580->1586 +6 C (deltas agree both
  sides), seal 1674->1680 +6 (commit msgs): all agree, no
  slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-696-q794-
  t10p282 verdict CONFIRM, tallies 13/13 + 12/12 + 12/12
  = 37/37 as-filed (file present, read in full; tallies
  memo-internal bookkeeping -- my check-mark recount
  gives 7/5/4, counting unit irreproducible; methodology
  note, NO verdict impact) + exact-value corroboration
  incl PBA/C10-4SIG map, QUAD1s + R7 last3-pair + QT
  tails + LCS(1,2)=2 + b20-93 + b5 step o>=43, M-tails
  NEW, ring STANDARD + TR7 16/16 UNPAIRED + edges +
  consts, P281C10-head n114543 reconstruction 57/84 (all
  re-checked above) + A-346 viewer corroboration (all 3
  legs CONFIRM, consts 75/70/64/70 INCL, values re-
  checked above; "QUAD2s-3P" label quirk vs 1-sig values
  -- immaterial, values agree). No CONFIRM-P282.md file
  (absence verified); A-696 suffices per rule. Agrees
  with cport commit msg (PYID 8311, RGRAM 16622).
- Quiz: no conflicting CLAIM/GATE/FLAG on b390 (own seat
  CLAIM only). Newest PARENT-* is QNUM-21 (w2b block) +
  QNUM-20 (w2f block): pure Q-block grants, read, no gate
  impact -- GATE cites QNUM-19: 1 immaterial staleness x2
  (standing pattern). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-19 vs -21).
