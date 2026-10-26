# VERIFY ee8f0330 b337 T10P229 pins 96429..96776 (1360 tiers) PASS

Seat viewer-r42, first-hand, fresh detached worktree tree-ee8f0330
(HEAD ee8f0330, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r42. Base 3cb4aae3 (b336 tip, own VERIFY filed
this round). CT shim on all batteries (fast tests throughout).

- Build: make -C src/c BUILDDIR=r42/build337/bin, rc=0, 0 warnings.
  aae sha1-8 7d8dd3a2 (== GATE) / sha256-8 d6e27c97 (first-hand);
  rgramc sha1-8 37aa9f09 (== GATE) / sha256-8 af1cc1dd (first-hand).
- RGRAMC-PYID 6659/6659 covered=6659/6659 GREEN rc=0 (own binary).
- RGRAM py 13318 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13318 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13318/13318, diff 0).
- PINS 13320 rows (2 hdr + 13318, +58 vs base 13262 = 29x2).
  Base-N set vs for-list set-eq 6659/6659 (cmp clean).
- For-list union +29, 0 removed (old 6630 -> new 6659):
  96429 96430 96431 96438 96446 96447 96448 96449 96452 96456
  96457 96464 96472 96473 96480 96488 96489 96496 96504 96505
  96511 96512 96520 96521 96639 96640 96767 96768 96776
  (== GATE verbatim).
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P229 C-vs-py, own script tables337.py rc=0 ALL-EXACT
  (17-table PAIR/C8 layout): S0/S1 len 168/168 eq, sigs 994e0000/
  e6969900, b4b5 5bf1/5df1 == lencode first-hand; AM16 PT2 CM8 M16
  M31-16 XA4 QR4 QT4 RM16 RQ16 all eq + counts (M distinct, M31
  16/16 distinct, QR 3-distinct r0==r2, XA 2-distinct 00/01);
  AC76 PC79 CC69 QC63 RC66 all eq; _N decls 76/79/69/63/66 match;
  QR r0==r2 fabc851eb404f9 + r1/r3 distinct (== A-521/GATE);
  QT == A-521 4/4 exact; QT r0/r2 common suffix eaa6 2B (byte1 8f
  vs 90) = A-521 §F correction CONFIRMED first-hand (over A-299
  3B note); PT 5c640f/ed0d10 distinct (== GATE values); XA
  00,01,00,00 (== A-521 A-vector); row-add 32 distinct over 64
  cells; RM229-vs-RM228 shared 0/16 + QT229-vs-QT228 shared 0/4
  (M-tails ALL NEW first-hand); varsets exact x5 (AC-8, PC-5,
  CC-15, QC-21, RC-18, from dispatch byte positions); cover84 x5
  0-overlap; b4/b5 in no const table x5; const sigs b0-3 AC
  e696d109 / PC 32f79900 / CC 32f74900 / QC 32f7c107 / RC e096d758;
  PC b83 = 0x60 (96) in-table; head-b5 f1 x83 (96429..96511) + f2
  x9 (96512..96520) via lencode formula; Q-carry 96511 fff1 ->
  96512 01f2; no BM/BC/FM/FS/FO/FC/X42/M42/TC syms either side;
  table inventory exactly the 17 (syms exact, no extras).
- Dispatch eye-verified both sides, 7 blocks in order at dispatch
  tail after T10P228R close (N-out-of-scope fallthrough follows):
  S0 n=96429 PB0 994e0000 NEW, S1 n=96430 PB1 e6969900 NEW,
  A 96431-96446 PBA16 e696d109 (M6 b24,25,76-79, b5 f1 raw),
  P 96447-96448 PAIR-3T 32f79900 (b80-82 tab, b83=0x60 const),
  C 96449-96456 PBC8 32f74900 (M13 b20,21,25-31,80-83, b5 f1 raw),
  Q 96457-96520 single-sig quad 32f7c107 (m=off&15 M7
  b21-23,76-79, b31 row-add (pay[31]-XA[q])&FF==M31[m], q=off>>4
  R7 b24-30 + tails b80-83, b5-carry @96511->96512),
  R 96521-96776 T-ring STANDARD e096d758 (c=off&15 M8
  b32,33,38,39,72-75, r=off>>4 R8 b21-23,31,76-79,
  b4=(0x13+2off)&FF b5=0xf2+(off>=119)+(off>=247)). C T-mirrors
  7/7: T63215/63220/63225/63240/63254/63270/63295, py lines +
  bounds + comments exact; C guards exact (2 singletons +
  5 ranges); b31add via snprintf %02lx (pay[31]-hexval(XA[q]))&FF
  exact py mirror; C R-counter ((19+2*off)&255,
  (242+(off>=119))+(off>=247)) exact; temps _t4896.._t4917
  appended (base max _t4895, no reuse); C byte-index lists match
  py per block.
- Edges recomputed first-hand from code formulas (all 6 edge pins
  in for-list + 2/2 PASS lines both legs): Q carry 96511 (ff/f1)
  -> 96512 (01/f2); ring 96639 (off118, ff/f2) -> 96640 (off119,
  01/f3); 96767 (off246, ff/f3) -> 96768 (off247, 01/f4). (== GATE.)
- C diff pure-add: numstat 752/0 + 291/0 + 1/1 + 58/0 (== GATE);
  raw C 746 add + 6 blank-only `+` (verified bare) = 752 / 0 del;
  sh 1/1 = for-list line rewrite (+29/0rem verified above).
  Norm GATE-method (C-only, [0-9]+->N, cut-c2, ;-strip): add-uniq
  194 (== GATE exactly), del-uniq 0, miss 0.
- Band added 1102 lines (== GATE; blanks-IN convention: 746+6+291
  +1+58; cf b336 GATE's blanks-excluded 1060 — both self-consistent,
  conventions noted here).
- Wall on band added lines (1102): vendor/disasm/depload(8 incl
  System.load)/libcompression/CT-cache/CT_REAL/compression_tool/
  shebang/^+#!/usr/bin/aa/nominat 0 hits throughout (15 patterns).
- Tiers (+7 verified first-hand): merge-msg +7 (6c4c75bd), code 7
  blocks, singletons 490->492 +2 (== GATE), range-guards 365->370
  +5 (== GATE), CLOSED prints 1259->1266 +7 (own literal count;
  GATE tier-tags 1257->1264 +7, delta agrees), seal 1353->1360 +7
  (commit msgs): all agree, no slip.
- Band comp: 6c4c75bd (py merge w2b@0461e11b partial, +7 tiers,
  +58 pins) + ee8f0330 (C port). Matches GATE.
- CONFIRM: A-521-q621-t10p229 CONFIRM 33/34 + finding (15/15 shape
  + 10/11 quad/ring + 8/8 counters, own bed, read in full; §F
  tail-share 2B descriptive, cut SAFE, states no DISSENT).
  Citation "A-521-q621" CORRECT. No CONFIRM-P229.md file; rule-b
  satisfied. A-299 recon: sigs + PBA VPOS 7 + PAIR-3T VPOS
  {b4,b80-82} + b83 0x60 (prose-convention fix agreed) + PBC VPOS
  14 + QUAD VPOS 21 + row-add 32 + R7 r0==r2 + tails + STANDARD
  M8/R8 + SPLIT + b80-83 const + lencode 348/348 + ring formulas/
  edges + consts 77/70 (fixes vs Q-prose 76/69) + NO D dips: all
  consistent first-hand. A-299 const fixes vs impl AC 76 / CC 69
  resolved: b5 via lencode formula not const pairs (verified:
  varsets incl b5, 0 overlap, cover84 x5, A/C b5 const f1
  first-hand). QT r0/r2 share taken as A-521's corrected 2B eaa6
  as GATE states (verified first-hand above). No DISSENT on P229.
- Own-loop ownloop337.py (cache-path-direct, zero-write): 348/348
  ok, 0 bad, rc=0. (319 non-pin Ns fetched via the tool-identical
  -encode -a lzraven invocation; 29 pins pre-cached.)
- Quiz: no conflicting CLAIM/GATE/FLAG on b337. Newest PARENT-*
  still QNUM-12 (read, no gate impact).

Verdict: PASS. GATE CORRECT, 0 slips (prose + code).
Logs: NVME ws tmp/encode-viewer/r42/ (tree-ee8f0330 detached;
build337.log, pyid337.log, rgram337py/c.log, pass337py/c.txt,
for337-old/new.nums, pins337-base.nums, smoke337.log, tables337.py/
.log, cadd337.txt, added337.txt, numstat337.txt, ownloop337.py/.log,
populate337.py/.log, ownloop-work337/, smoke337work/, scratch337py/c/,
pyid337work/).
