# GATE 1ff87cd1 b352 T10P244 pins 101649..101996 (1452 tiers) PASS-functional

Seat sweep2-r50, first-hand, WT tmp/wt-encode-sweep2 @1ff87cd1,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r50.
Band = ee73b218 (py merge w2b@ffdee89d partial, +6 tiers, +62 pins)
+ 1ff87cd1 (C port). Base 74f7ebed (b351 tip, 1446 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build352/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4a323a42 / aae d6e27c97
  (aae identical to b288-b351 builds: aae.c untouched).
- RGRAMC-PYID 7122/7122 covered=7122/7122 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 14244/14244 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14244/14244 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 14244/14244).
- PINS-RGRAM cells set-eq 7122/7122 (diff 0, PINS base-N
  set vs for-list); PINS 14246 rows (2 hdr + 14244 =
  PASS lines). For-list union +31 (101649 101650 101651
  101652 101658 101662 101666 101667 101670 101671 101672
  101673 101676 101677 101687 101688 101693 101703 101704
  101709 101719 101725 101740 101741 101759 101760 101805
  101869 101887 101888 101996), 0 removed, range
  101649..101996 exact. Each for-N yields 2 PASS lines
  (g-zN-closed + g-zN); 31x2 = 62 = 14244-14182.
  The 31 = S0/S1 (2) + A head/mids/tail (5) + C
  head/mids/tail (6) + Q head/mids/tail (10) +
  ring head/edge-pairs/mids/tail (8).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var).
- Tables audit P244 C-vs-py, script-compared, all EXACT:
  S0/S1 1/1, AM 16/16, CM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 76/76, CC 65/65,
  QC 59/59, RC 69/69; C _N decls 76/65/59/69
  match actual (tabc244.py rc=0); QB0/QB9/QB10/
  QB11 32/32 x4, M8/X8 16/16 (tabc244x.py rc=0,
  6-block PBA/C10-2SIG/quad-frag/T88-ring, nothing
  else).
  Code-consts vs A-577 (PBA 77 / C10 66 /
  quad 60 / T88 69 INCL): impl -1 on PBA/C10
  is the standing incl/excl bookkeeping (writer
  dual-accounts, excl 76/65 — A-577 §3 explicitly
  no-finding); impl QC 59 = memo-1 likewise (b5
  const 1a verified by the dispatch lencode check,
  same dual-account; memo prose says quad
  identical but coverage is identical 84/84 —
  no finding); T88 69 identical (b5 counter);
  byte-coverage proven A 76+8, C 65+19,
  Q 59+25, R 69+19 (unions 84/84/84/88
  exact, 0 overlap anywhere; b4/b5 in no const
  set).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=101649 (PB0 sig 44620100 NEW, b4/b5 23/1a ==
  lencode, lenB 84), S1 n=101650 (fat PB1 sig 3d319602
  NEW, b4/b5 25/1a == lencode, lenB 84), A 101651-101666
  PBA16 single-sig (sig de136329 via AC b0-b3, AM 16/16
  distinct 6B, mtab b6,7,76-79, b5 const 1a raw
  lencode), C 101667-101676 C10 2-SIG sandwich (sig
  map exact order: b8a9df02 x4 @101667-70 +
  dcd46f01 x2 @101671-72 + b8a9df02 x4 @101673-76,
  CM 10/10 distinct 17B diverge 10/10, mtab
  b0-3,6-8,10,11,48-51,80-83 sig-bytes-in-tab
  b9 SKIPPED verified first-hand, b5 const 1a),
  Q 101677-101740 QUAD-FRAG triple r1==r2==r3
  (9bfa2d110601fedbf5b9 x3, r0 4dfd1685ee000c5f8a75
  distinct, sig-led b1-3; composite row-led sigs
  d04d/c24d row0 + a09b/859b rows1-3 via b0
  2x2-frag d0/c2/a0/85 11+5 split exact; M5
  b12,76-79 M16 16/16 distinct 5B; QB9/QB10/QB11
  dual-coltabs r0-vs-r123 pos-diff 15/16/16/16;
  R10 lenB 10; tails 4/4 a3d62dc6/7e8e0fb4/
  a88e0fb4/d28e0fb4; M-tails 16/16 NEW vs P243M,
  0/16 vs P243T; b5 const 1a whole-range raw
  lencode), R 101741-101996 T88-ring STANDARD +
  b8xor (sig 02000000, TM8 b9,10,11,19,76-79 by
  COL RM 16/16 distinct, TR8 b13-16,80-83 by ROW
  RQ 16/16 distinct UNPAIRED, tails SPLIT, b8
  row-xor X8 00x11+20x5 vs M8 col-tab staged,
  b84-87 const 3e1eb3cc ring-wide, b4=(0xdb+2off)
  &FF, b5=0x1a+(off>=19)+(off>=147)). C blocks carry
  T67107/112/117/132/149/182 py-line mirrors,
  bounds + byte positions exact, all 6 verified.
  Insert position exact both sides: after T10P243R
  close, at dispatch tail (N-out-of-scope fallthrough
  follows). Matches A-577 geometry (PB0/PB1 NEW,
  PBA16 VPOS 7 b5 const 1a, C10-2SIG sandwich VPOS
  18 b9 skipped b5 const 1a 10/10 diverge, QUAD-FRAG
  VPOS 24 b5 const 1a, T88 VPOS 19, lencode 348/348
  whole-tier, ring edges 101759->101760 + 101887->
  101888, NO D dips) incl exact values (QR triple,
  b0 frag, dual-coltabs, tails 4/4, M-tails NEW,
  ring TM8/TR8 16/16 UNPAIRED, tails SPLIT, b8xor
  X staged, b84-87 3e1eb3cc, consts stand).
- Tail-share figure: QT r1/r2/r3 = 7e8e0fb4/a88e0fb4/
  d28e0fb4, byte0 0x7e/0xa8/0xd2 differ, common suffix
  3B 8e0fb4 — confirms A-577 §2 (TRUE 3B, memo
  re-verified programmatically; descriptive only, cut
  SAFE, no DISSENT; exact tail values CONFIRMED, pins
  PASS).
- Edges via counter formula first-hand: 101759 (off18,
  ff/1a) -> 101760 (off19, 01/1b); 101887 (off146,
  ff/1b) -> 101888 (off147, 01/1c); all four pins
  2 PASS lines each. No DISSENT: cut bytes verify.
- C diff purely additive: numstat 814 add / 0 del; raw
  grep 809 content + 5 blank-only `+` lines (verified
  bare) / 0 del; fine-norm (rgramc.c scope, TNP/_tN/
  _iN/_bN, BSD tools, empty-excluding) del-subset-add
  0 missing (del-uniq 0, add-uniq 505).
- Wall on band diff added lines (scope 74f7ebed..
  1ff87cd1, 1282 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  shebang//usr/bin/aa/nominated 0 hits. Files touched:
  rgramc.c 814/0, rgram.py 405/0 purely additive,
  test_rgram.sh 1/1 (for-line extension), PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 520->522 +2 / ranges 428->432 +4 = +6
  (stated method, plain `if n ==` for BSD grep),
  seal 1446->1452 +6: all agree, no slip (absolute
  seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-577-q636-
  t10p244 verdict CONFIRM (38/38 = 16/16 shape +
  14/14 quad/ring + 8/8 counters; file present,
  counts verified; exact-value corroboration incl
  QR triple, b0 frag, dual-coltabs, tails 4/4,
  M-tails NEW, ring edges + consts re-checked above).
  No CONFIRM-P244.md file; A-577 suffices per rule.
  Agrees with cport commit msg (PYID 7122, RGRAM
  14244).
- Quiz: no conflicting CLAIM/GATE/FLAG on b352. Newest
  PARENT-* is QNUM-11 (w2f Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r50/ (build352.log,
  pyid352.log, rgram352py/c.log, cmp352.py/.c, for352-
  1ff87cd1/74f7ebed, for352-added, pins352.basen,
  smoke352.log, tables352.log, tabc244.py, tabc244x.py,
  bycov244.py, bycov352.log, sig244.py/.log, numstat352,
  added352, add/delnorm352).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
