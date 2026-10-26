# VERIFY bcc7d15a b339 T10P231 pins 97125..97472 (1372 tiers) PASS

Seat viewer-r42, first-hand, fresh detached worktree tree-bcc7d15a
(HEAD bcc7d15a, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r42. Base 69174c03 (b338 tip, own VERIFY filed
this round). CT shim on all batteries (fast tests throughout).

- Build: make -C src/c BUILDDIR=r42/build339/bin, rc=0, 0 warnings.
  aae sha1-8 7d8dd3a2 (== GATE) / sha256-8 d6e27c97 (first-hand);
  rgramc sha1-8 04b3c29c (== GATE) / sha256-8 066e1ac6 (first-hand).
- RGRAMC-PYID 6712/6712 covered=6712/6712 GREEN rc=0 (own binary).
- RGRAM py 13424 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13424 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13424/13424, diff 0).
- PINS 13426 rows (2 hdr + 13424, +54/-0 rows = +27/-0 cells).
  PINS adds exactly the 27 added cells (26 tier pins + 97472 tail,
  no 97124 — pre-existing). Base-N set vs for-list set-eq
  6712/6712 (comm both ways empty).
- For-list union 6685->6712 +27, 0 removed (no dups either side):
  97125 97126 97127 97134 97142 97143 97147 97151 97152 97153
  97160 97168 97169 97176 97184 97185 97192 97200 97201 97208
  97216 97217 97279 97280 97407 97408 97472.
  (GATE's "6684->6711" + "97124 added" + "97472 not in battery
  for-list" are PROSE SLIPS S1/S2 — see bottom. Code: 13424 =
  2x6712, all cells battery-covered incl 97472 with 2/2 PASS
  lines both legs.)
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P231 C-vs-py, own script tables339.py rc=0 ALL-EXACT
  (15-table mixed-size layout): S0/S1 len 168/168 eq, sigs
  329d0000/f1053b01, b4b5 cbf6/cdf6 == lencode first-hand; AM16
  BM10 M16 M19-16 XA19-4 QR4 QT4 RM16 RQ16 all eq + counts (AM/BM/
  M/QT/RM/RQ distinct; M19 2-valued {35,b5}; XA19 3-distinct;
  QR 3-distinct r1==r2); AC75 BC71 QC63 RC70 all eq; _N decls
  75/71/63/70 match; QR r1==r2 b2fc01da137e x2, r0/r3 distinct
  (df3c65fa69d5/01bc573a353a); XA19 00,09,09,f5 (== A-529
  A=[0,9,9,-11]); row-add 6 distinct over 64 cells
  {2a,35,3e,aa,b5,be}; QT == A-529/A-301 4/4 exact, r1/r2 share
  af3d; M col0 15-sig order EXACT (== A column order incl dd3d x2
  cols 3-4); RM-tail16 + RQ-tail16 (SPLIT first-hand, w7/w9);
  RM231-vs-RM230 shared 0/16 + vs-RQ230 0/16 + QT231-vs-QT230 0/4
  (M-tails ALL NEW first-hand); varsets exact x4 (AC-9, BC-13,
  QC-21, RC-18 over 0..87, from dispatch byte positions); cover
  75+9=84 / 71+13=84 / 63+21=84 / 70+18=88, 0 overlap; b4/b5 in
  no const table x4; const sigs AC 2d5eb013 / BC e0053b01 / RC
  01000000 / QC b3=0x1e (b0-2 in m-tab); RC b84-87 d6/38/64/3c;
  A-b5 f6 x16 + B-carry 97151 fff6 -> 97152 01f7 + Q-b5 f7 x64
  via lencode formula; no PT/PC/CM/CC/M31/M42/X42/FS/FO/FM/FC/RF
  syms either side; table inventory exactly the 15 (syms exact,
  no extras).
- Dispatch eye-verified both sides, 6 blocks in order at dispatch
  tail after T10P230R close (N-out-of-scope fallthrough follows):
  S0 n=97125 PB0 329d0000 NEW, S1 n=97126 PB1 f1053b01 NEW,
  A 97127-97142 PBA16 2d5eb013 (M7 b9-11,76-79, b5 f6 raw),
  B 97143-97152 PBB10 single-sig e0053b01 (M11 b13-19,80-83,
  b5-carry f6->f7 @97151->97152, 10/10 diverge, NO pair/C8),
  Q 97153-97216 QUADms 15-sig (m=off&15 M8 b0-2,11,76-79,
  b19 row-add (pay[19]-XA19[q])&FF==M19[m] ADD staged, q=off>>4
  R6 b13-18 + tails b80-83, b5 f7 raw),
  R 97217-97472 T88-ring STANDARD 01000000 paylen 88 (c=off&15 M7
  b29-31,80-83, r=off>>4 R9 b16-19,23,76-79, b84-87 const,
  b4=(0x83+2off)&FF b5=0xf7+(off>=63)+(off>=191)). C T-mirrors
  6/6: T63726/63731/63736/63751/63767/63792, py lines + bounds +
  comments exact; C guards exact (2 singletons + 4 ranges);
  b19add via snprintf %02lx (pay[19]-hexval(XA19[q]))&FF exact py
  mirror; C R-counter ((131+2*off)&255, (247+(off>=63))+
  (off>=191)) exact; temps _t4936.._t4955 appended (base max
  _t4935, 56 contiguous _t4900.._t4955, no reuse); C byte-index
  lists match py per block.
- Edges recomputed first-hand from code formulas (all 6 edge pins
  in for-list + 2/2 PASS lines both legs): A head 97127 (cf/f6)
  -> tail 97142 (ed/f6, b5 const); B 97151 (ff/f6) -> 97152
  (01/f7); Q head 97153 (03/f7) -> tail 97216 (81/f7, b5 const);
  ring 97279 (off62, ff/f7) -> 97280 (off63, 01/f8); 97407
  (off190, ff/f8) -> 97408 (off191, 01/f9). (== GATE.)
- C diff: numstat 642/1 + 261/1 + 1/1 + 54/0 (== GATE). The 3 del
  lines identified first-hand: C paylen-guard allow-list 1-line
  rewrite (44..84 -> 44..88), py guard same 1-line rewrite (+88
  with "T10P231+ T88 rings" comment), for-line 1-line rewrite
  (+27/0rem verified above). No other dels: all other 642 C +
  261 py lines pure-add. Norm GATE-method (C-only, [0-9]+->N,
  cut-c2, ;-strip): add-uniq 184 (== GATE exactly), del-uniq 1,
  miss 1 = old paylen-guard line (== GATE exactly).
- Band added 958 lines (== GATE; blanks-IN: 642 incl 5 blank-only
  `+` verified bare + 261 + 1 + 54; cf b337 same convention).
- Wall on band added lines (958): vendor/disasm/depload(8 incl
  System.load)/libcompression/CT-cache/CT_REAL/shim//usr/bin/aa/
  compression_tool/shebang/^+#!/nominat 0 hits throughout
  (14 patterns).
- Tiers (+6 verified first-hand): merge-msg +6 (d8dcb7f9), code 6
  blocks, tier-tags 1272->1278 +6 (== GATE; own py+C CLOSED-T10P
  counts agree), singletons 494->496 +2 (== GATE), range-guards
  374->378 +4 (== GATE), CLOSED prints 1790->1796 +6 (== GATE;
  bare-CLOSED literal, reproduced in both files), seal 1366->1372
  +6 (commit msgs): all agree, no slip.
- Band comp: d8dcb7f9 (py merge w2b@df48700e partial, +6 tiers,
  +54 pins) + bcc7d15a (C port). Matches GATE.
- CONFIRM: A-529-q623-t10p231 CONFIRM 35/35 (15/15 shape + 12/12
  quad/ring + 8/8 counters, own bed, read in full; XOR-tie flag
  adopts ADD per precedent, cut SAFE, states no DISSENT).
  Citation "A-529-q623" CORRECT. No CONFIRM-P231.md file; rule-b
  satisfied. A-301 recon: mixed-size 92x84+256x88 + sigs + PBA
  VPOS 8 + PBB VPOS 13 + carry + QUADms 15-sig + VPOS 20 + row-add
  ADD/XOR both-fit (genuinely undecidable, staged ADD stands) +
  R6 r1==r2 + tails + M-tails NEW + T88 M7/R9 + SPLIT + b84-87
  const + lencode 348/348 incl 88B + ring formulas/edges + consts
  76/71/64/70 + NO D dips: all consistent first-hand. Impl AC 75
  / QC 63 (memo-1 on b5-const zones) resolved: b5 via lencode
  formula (verified: varsets incl b5, 0 overlap, cover, A-b5 f6
  + Q-b5 f7 first-hand); BC 71 + RC 70 identical (b5-varying).
  No DISSENT on P231.
- Own-loop ownloop339.py (cache-path-direct, zero-write): 348/348
  ok, 0 bad, rc=0. (321 non-pin Ns fetched via the tool-identical
  -encode -a lzraven invocation; 27 pins pre-cached.)
- Quiz: no conflicting CLAIM/GATE/FLAG/DISSENT on b339. Newest
  PARENT-* still QNUM-12 (read, no gate impact).

Verdict: PASS. Code CORRECT; 3 GATE PROSE SLIPS (prose wrong,
code PASS — PROSE-01 category):
S1: for-list stated "6684->6711 +27/-0: 97124 + 26 tier pins" —
  correct first-hand: 6685->6712 +27/-0, all 27 added cells
  >=97125 (97124 pre-existing in old for-list, not added; 27th
  added cell is the 97472 tail). Related: "R 5" undercounts R
  pins (6 incl 97472 tail). Same root cause as S2.
S2: "PINS cells 6712 vs for-list 6711, cells-for = {97472} (tail
  pinned, not in battery for-list)" — wrong: for-list 6712
  unique, PINS base-N set-eq for-list 6712/6712, 97472 present in
  for-line (trailing "97472; do") with 2/2 PASS lines both legs.
  Root cause S1+S2: `;`-token pollution in sweep's for-list parse
  (trailing "<N>; do" token dropped; same bug class caught in my
  own b336 parse pre-count and fixed with sed strip).
S3: Q row-grouping "q0 off0/7, q1 off15/16/23, q2 off31/32/39, q3
  off47/48/55/63" — wrong vs code q=off>>4 (verified both sides):
  actual q0: off0/7/15; q1: off16/23/31; q2: off32/39/47; q3:
  off48/55/63 (3 pins/row; pin list itself correct, only the
  row-grouping parenthetical misaligned at boundaries).
Recommend parent check PROSE-01 3rd-slip rule for sweep-r46's round.
Logs: NVME ws tmp/encode-viewer/r42/ (tree-bcc7d15a detached;
build339.log, pyid339.log, rgram339py/c.log, pass339py/c.txt,
for339-old/new.raw/.nums, pins339-base.nums, pins339-old/new.srt,
pins339-added.txt, smoke339.log, tables339.py/.log, cadd339.txt,
cdel339.txt, caddnorm339.txt, cdelnorm339.txt, added339.txt,
numstat339.txt, ownloop339.py/.log, populate339.py/.log,
ownloop-work339/, smoke339work/, scratch339py/c/, pyid339work/).
