# VERIFY 3cb4aae3 b336 T10P228 pins 96081..96428 (1353 tiers) PASS

Seat viewer-r42, first-hand, fresh detached worktree tree-3cb4aae3
(HEAD 3cb4aae3, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r42. Base b85ccf4c (b335 tip, r41 VERIFY on file).
CT shim on all batteries (fast tests throughout).

- Build: make -C src/c BUILDDIR=r42/build336/bin, rc=0, 0 warnings.
  aae d6e27c97 / rgramc 68eb1ff2 (== GATE, sha256-8 both).
- RGRAMC-PYID 6630/6630 covered=6630/6630 GREEN rc=0 (own binary).
- RGRAM py 13260 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13260 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13260/13260, diff 0).
- PINS 13262 rows (2 hdr + 13260, +56 vs base 13206 = 28x2).
  Base-N set vs for-list set-eq 6630/6630 (cmp clean).
- For-list union +28, 0 removed (old 6602 -> new 6630):
  96081 96082 96083 96090 96098 96099 96100 96101 96104 96108
  96109 96116 96117 96124 96125 96127 96128 96140 96141 96172
  96173 96255 96256 96300 96301 96383 96384 96428 (== GATE verbatim).
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P228 C-vs-py, own script tables336.py rc=0 ALL-EXACT
  (16-table novel layout, 50/50 checks): S0/S1 len 168/168 eq, sigs
  794b0000/8e638e00, b4b5 a3ee/a5ee == lencode first-hand; AM16 CM8
  M16 PT2 QR4 QT4 RF2 RM16 RQ16 all eq + counts + distinct; AC74
  CC72 PC81 QC63 RC65 all eq; _N decls 74/72/81/63/65 match; QR ==
  A-518 4/4 exact values; QT == A-518 4/4 exact; RF f035/e655 ==
  A-298 flips (b0 f0/e6 + b12 35/55, dispatch byte order); PT 94/b4
  distinct; M b0 half-split 30x8/26x8; RM228-vs-RM227 shared 0/16 +
  QT228-vs-QT227 shared 0/4 (M-tails ALL NEW first-hand); varsets
  exact x5 (AC-10, CC-12, PC-3, QC-21, RC-19, from dispatch byte
  positions); cover84 x5 0-overlap; b4/b5 in no const table x5;
  const sigs AC ee38e608 / CC 25994e00 / PC 4a329d00 / QC b1-3
  93e904 / RC b1-3 32994e (b0-led groups share bytes only); A-b5
  ee x16 + C-b5 ee x8 via lencode formula; Q-carry 96127 ffee ->
  96128 01ef; no BM/X42/M42/FS/FO/FM/FC/TC syms either side; table
  inventory exactly the 16 (syms exact, no extras).
- Dispatch eye-verified both sides, 7 blocks in order at dispatch
  tail after T10P227R close (N-out-of-scope fallthrough follows):
  S0 n=96081 PB0 794b0000 NEW, S1 n=96082 PB1 8e638e00 NEW,
  A 96083-96098 PBA16 ee38e608 (M8 b6-9,76-79, b5 ee raw lencode),
  P 96099-96100 PAIR 4a329d00 (b80 tab only, VPOS {b4,b80}),
  C 96101-96108 PBC8 25994e00 (M10 b6,7,48-51,80-83, b5 ee raw),
  Q 96109-96172 QUADhalf 3093e904/2693e904 (m=off&15 M9
  b0,9-12,76-79, q=off>>4 R6 b6,7,48-51 + tails b80-83, NO b42-xor),
  R 96173-96428 T-ring DUAL f032994e/e632994e (h=off>>7 RF b0,b12,
  c=off&15 M8 b16-19,72-75, r=off>>4 R7 b9-11,76-79,
  b4=(0x5b+2off)&FF b5=0xef+(off>=83)+(off>=211)). C T-mirrors 7/7:
  T62922/62927/62932/62947/62961/62977/63001, py lines + bounds +
  comments exact; C guards exact (2 singletons + 5 ranges);
  R-counter ((91+2*off)&255, (239+(off>=83))+(off>=211)) exact;
  temps _t4874.._t4895 appended (base max _t4873, 96 contiguous
  _t4800.._t4895, no reuse); C byte-index lists match py per block.
- Edges recomputed first-hand from code formulas (all 6 edge pins
  in for-list + 2/2 PASS lines both legs): Q carry 96127 (ff/ee) ->
  96128 (01/ef); ring 96255 (off82, ff/ef) -> 96256 (off83, 01/f0);
  96383 (off210, ff/f0) -> 96384 (off211, 01/f1). (== GATE.)
- C diff pure-add: numstat 733/0 + 276/0 + 1/1 + 56/0 (== GATE);
  raw C 727 add + 6 blank-only `+` (verified bare) / 0 del;
  sh 1/1 = for-list line rewrite (+28/0rem verified above).
  Fine-norm GATE-method (C-only, _t/_i/_b/T numbers): add-uniq 426
  (== GATE exactly), del-uniq 0, miss 0.
- Band added 1066 total lines; GATE states 1060 = non-blank count
  (1066 - 6 blank-only `+`, verified bare). Counting-method note,
  NOT a slip: blanks match no wall pattern; wall run over all 1066.
- Wall on band added lines (1066): vendor/disasm/depload(7)/
  libcompression/CT-cache/CT_REAL/compression_tool/shebang/^+#!
  /usr/bin/aa/nominat 0 hits throughout (13 patterns).
- Tiers (FLAG: +7 verified first-hand): merge-msg +7 (39638d99),
  code 7 blocks, singletons 488->490 +2 (== GATE), range-guards
  360->365 +5 (== GATE), CLOSED prints 1252->1259 +7 (own count),
  seal 1346->1353 +7 (commit msgs): all agree, no slip.
- Band comp: 39638d99 (py merge w2b@e62c259e partial, +7 tiers,
  +56 pins) + 3cb4aae3 (C port). Matches GATE.
- CONFIRM: A-518-q620-t10p228 CONFIRM 30/30 (15/15 shape + 11/11
  quad/ring + 4/4 counters, own bed, read in full). Citation
  "A-518-q620" CORRECT. No CONFIRM-P228.md file; rule-b satisfied.
  A-298 recon: sigs + PBA VPOS 9 + PAIR VPOS {b4,b80} + PBC VPOS 11
  (M10 corr) + QUADhalf VPOS 21 + b5-carry + DUAL VPOS 19 (corr,
  2+8+7+2) + flips @off128 + M/R-by-COL/ROW + tails SPLIT + b80-83
  const + lencode 348/348 + ring formulas/edges + NO D dips: all
  consistent first-hand. A-298 const fixes (PBA 75, PBC 73) vs impl
  AC 74 / CC 72 resolved as GATE states: b5 via lencode formula
  not const pairs (verified: varsets incl b5, 0 overlap, cover84
  x5, A/C b5 const ee first-hand). No DISSENT on P228.
- Own-loop ownloop336.py (cache-path-direct, zero-write): 348/348
  ok, 0 bad, rc=0. (320 non-pin Ns fetched via the tool-identical
  -encode -a lzraven invocation; 28 pins pre-cached.)
- Quiz: no conflicting CLAIM/GATE/FLAG on b336. Newest PARENT-*
  QNUM-12 (w2b Q-block only, read, no gate impact).

Verdict: PASS. GATE CORRECT, 0 slips (prose + code).
Logs: NVME ws tmp/encode-viewer/r42/ (tree-3cb4aae3 detached;
build336.log, pyid336.log, rgram336py/c.log, pass336py/c.txt,
for336-old/new.nums, pins336-base.nums, smoke336.log, tables336.py/
.log, cadd336.txt, added336.txt, del336.txt, numstat336.txt,
addnorm336.txt, delnorm336.txt, caddnorm336.txt, ownloop336.py/.log,
populate336.py/.log, ownloop-work336/, smoke336work/, scratch336py/c/,
pyid336work/).
