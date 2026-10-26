# VERIFY b85ccf4c b335 T10P227 pins 95733..96080 (1346 tiers) PASS

Seat viewer-r41, first-hand, fresh detached worktree tree-b85ccf4c
(HEAD b85ccf4c, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r41. Base 45854a24 (b334 tip, own VERIFY filed
this round). CT shim on all batteries (fast tests throughout).

- Build: make BUILDDIR=r41/build335/bin, rc=0, 0 warnings. aae
  sha1-8 7d8dd3a2 (== GATE); rgramc sha1-8 08a003c4 (== GATE) /
  sha256-8 dc61aa95 (first-hand).
- RGRAMC-PYID 6602/6602 covered=6602/6602 GREEN rc=0 (own binary).
- RGRAM py 13204 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13204 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13204/13204, diff 0).
- PINS 13206 rows (2 hdr + 13204, +52 vs base 13154).
  Base-N set vs for-list set-eq 6602/6602 (diff -q clean).
- For-list union +26, 0 removed (old 6576 -> new 6602):
  95733 95734 95735 95743 95744 95750 95751 95753 95754 95760
  95761 95771 95772 95777 95788 95793 95804 95809 95820 95824
  95825 95871 95872 95999 96000 96080 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P227 C-vs-py, own script tables335.py rc=0 ALL-EXACT
  (15-table classic-B layout): S0/S1 len 168/168 eq, sigs
  bf250000/8e634e00, b4b5 ebeb/edeb == lencode first-hand;
  AM16 BM10 M16 X42-4 M42-16 QR4 QT4 RM16 RQ16 all eq; AC76
  BC64 QC63 RC65 all eq; _N decls 76/64/63/65 match; b0-3:
  AC 8e63b604, BC 8e63??00 + QC 8e63??04 (b2 sig byte in tab
  both), RC a0990745; varsets exact x4 (AC-8, BC-20, QC-21,
  RC-19); cover84 x4 0-overlap; b4/b5 in no const table x4;
  head-b5 eb x11 (95733..95743) + ec x81 (95744..95824) via
  lencode formula first-hand; BM 10/10 distinct w=18, order
  96x3+4ex7 exact; M 16/16, sig-led col b2 ee x11 (rows 0-10)
  / f6 x5 (rows 11-15); X42 00,03,05,04; M42 16 rows exact;
  lows set 7 {1c,3c,5c,7c,9c,bc,dc}; row-xor 16/16 cols
  all-4-distinct; col-0 9c,9f,99,98; QR UNPAIRED 4/4
  cb5bae95f046/9b5a58ebb025/dddb554c10a8/46de61cff06d; QT
  verbatim 4b696cac/f3c5f3b1/bd589836/5c9fa7af 4/4 distinct;
  RM/RQ 16/16 UNPAIRED distinct; RM227-vs-RM226 shared 0/16
  + QT227-vs-QT226 shared 0/4 (M-tails ALL NEW first-hand);
  no PT/PC/CM/CC/FS/FO/FM/FC/H/TC syms either side; table
  inventory exactly the 15 (syms exact, no extras).
- Dispatch eye-verified both sides, 6 blocks in order at dispatch
  tail after T10P226R close (N-out-of-scope fallthrough follows):
  S0 n=95733 PB0 bf250000 REPEAT ==P226PB0, S1 n=95734 PB1
  8e634e00 NEW, A 95735-95750 PBA16 8e63b604 NEW (m-tab 6B
  b36,37,76-79, b5-carry raw lencode), B 95751-95760 PBB10
  2-sig (m-tab 18B b2,23,32-43,80-83, sig byte in tab),
  Q 95761-95824 QUADmotif 2-sig ee04/f604 (m=off&15 M8
  b2,34,35,43,76-79, b42 row-xor X=[00,03,05,04] vs M42[m],
  q=off>>4 R6 b36-41 UNPAIRED + tails b80-83, b5 const ec),
  R 95825-96080 T-ring a0990745 ==P226T STANDARD (c=off&15 M8
  b48-51,76-79, r=off>>4 R9 b14,34,35,42,43,72-75, b4=
  (0xa3+2off)&FF b5=0xec+(off>=47)+(off>=175)); A/B/Q raw
  lencode. C T-mirrors 6/6: T62661/62666/62671/62686/62703/
  62728, py lines + bounds + comments exact; C guards exact
  (2 singletons + 4 ranges); b42xor via snprintf %02lx
  pay[42]^hexval(X42[q]) vs M42[m] (exact py mirror); C
  R-counter ((163+2*off)&255, (236+(off>=47))+(off>=175))
  exact; temps _t4854.._t4873 appended (base max _t4853, no
  reuse); C byte-index lists match py per block.
- Edges recomputed first-hand from code formulas (all 6 edge
  pins in for-list + PASS): A carry 95743 (off8, ff/eb) ->
  95744 (off9, 01/ec); ring 95871 (off46, ff/ec) -> 95872
  (off47, 01/ed); 95999 (off174, ff/ed) -> 96000 (off175,
  01/ee). (== GATE.)
- C diff pure-add: numstat 636/0 + 262/0 + 1/1 + 52/0 (== GATE);
  raw C 636 add / 0 del (637 incl +++ header); band added 951
  (== GATE). Norm ([0-9]+->N, cut-c2-strip variants agree):
  add-uniq 184, del-uniq 0, miss 0 (== GATE exactly).
  sh 1/1 = for-list line rewrite (+26/0rem verified above).
- Wall on band added lines (951): vendor/disasm/depload(7)/
  libcompression/CT-cache/CT_REAL/compression_tool/shebang/^+#!
  /usr/bin/aa/nominat 0 hits throughout (13 patterns).
- Tiers: merge-msg +6, code 6 blocks, singletons 486->488 +2
  (== GATE), range-guards 356->360 +4 (== GATE), tier-tags +6
  (own 1113->1119; GATE stated-method 1244->1250; delta +6
  agrees), CLOSED prints +6 (own 1494->1500; GATE stated-method
  1246->1252; delta +6 agrees), seal 1340->1346 +6 (commit
  msgs; GATE tiers leg omits the seal line — verified here):
  all agree, no slip.
- Band comp: 9af40a73 (py merge w2b@953bd5e5 partial, +6 tiers,
  +52 pins) + b85ccf4c (C port). Matches GATE.
- CONFIRM: A-508-q619-t10p227 CONFIRM 31/31 (15/15 shape + 12/12
  quad/ring + 4/4 counters, own bed, read in full). Citation
  "A-508-q619" CORRECT. No CONFIRM-P227.md file; rule-b
  satisfied. A-297 recon: sigs + PBB10 2-sig map + QUADmotif
  2-sig/VPOS + M8/ee-f6 + row-xor 64/64 + col-0 + R6 UNPAIRED
  vals + tails + M-tails 16/16 NEW (both refs) + T-ring
  STANDARD + lencode 348/348 + ring formulas/edges + consts
  76/65/64/65 (in-table + b5-const B/Q) + NO D dips: all
  consistent first-hand. A-297's 2 Q-prose fixes verified
  present in file; GATE uses corrected versions (4e==PB1,
  VPOS 20 ex-b5) as claimed. No DISSENT on P227 (only
  P923/P924/P926, other turf).
- Own-loop ownloop335b.py (cache-path-direct, zero-write):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen.)
- Quiz: no conflicting CLAIM/GATE/FLAG on b335. Newest PARENT-*
  QNUM-12 (writer Q-blocks only, read, no gate impact).

Verdict: PASS. GATE CORRECT, 0 slips (prose + code).
Logs: NVME ws tmp/encode-viewer/r41/ (tree-b85ccf4c detached;
build335.log, pyid335.log, rgram335py/c.log, pass335py/c.txt,
for335-old/new.nums, pins335-base.nums, smoke335.log, tables335.py/
.log, cadd335.txt, added335.txt, numstat335.txt, ownloop335b.py/
.log, populate335.py/.log, ownloop-work335/, smoke335work/,
scratch335py/c/, pyid335work/).
