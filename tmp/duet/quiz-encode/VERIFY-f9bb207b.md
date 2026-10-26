# VERIFY-f9bb207b b356 T10P248 pins 103041..103388 (1476 tiers) PASS

Seat viewer-r47, first-hand, detached tree-f9bb207b @f9bb207b,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r47.
Base 4b8d0444 (b355, 1470 tiers). Band = 129832ad (py) + f9bb207b (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build356/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 4438b124 / aae d6e27c97
  (== GATE both; aae.c untouched, pinned value holds).
- RGRAMC-PYID 7246/7246 covered=7246/7246 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14492/14492 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14492/14492 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14492/14492, sorted).
- PINS 14494 rows (2 hdr + 14492, +62 vs base 14432); PINS
  base-N 7246 vs for-list 7246 exact both ways (0/0; tail
  103388 pinned AND in for-list). For-list 7215->7246 +31/-0
  verbatim == GATE's 31: sing 103041 103042; A 6 (103043
  head + 103044 + 103050 + 103054 + 103057 + 103058 tail);
  C 6 (103059 head + 103062 + 103063 + 103065 + 103067 +
  103068 tail); Q 10 (103069 head + 103077 + 103085 + 103093
  + 103101 + 103109 + 103117 + 103125 + 103131 + 103132
  tail); R 7 (103133 head + edge pairs 103167/103168 +
  103295/103296 + mid 103261 + 103388 tail). 31x2=62=
  14492-14430. PINS adds == for-list adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME TMPDIR, default backend).
- Tables audit P248 C-vs-py, own script tables356.py, 79/79
  ALL-EXACT (12-table A/C10-2SIG/QUAD-2T-no-R+T88, NO QR):
  S0/S1 (1ce10200 NEW @103041 b4b5 03/25 / c503ce05 NEW
  @103042 b4b5 05/25, len 168 == lencode, P247 bcdf0200/
  dd39c205); AM 16/16 distinct 8B (b21-head {03,83});
  CM 10/10 distinct 14B diverge (2-sig map order EXACT:
  ce05 x4 @103059-62 + ee02 x6 @103063-68, full sigs via
  CC b0,b1 c5,03); M 16/16 distinct 7B; QT 4/4 exact 6936/
  9336/30ea/5aea (r0/r1 2nd-B 36, r2/r3 2nd-B ea); RQ==M
  same-index full-string 16/16 + set-eq (P245-style
  staged-identical); M-tails 16/16 NEW vs P247M (0 shared);
  RM 16/16 (8B) / RQ 16/16 (7B) UNPAIRED 0-overlap, tails
  SPLIT 16/16 both; AC 74/74, CC 68/68, QC 73/73, RC 71/71;
  _N decls 74/68/73/71. Varsets exact: AC 10 (b4/b5+M8
  b21-23,31,76-79), CC 16 (b4/b5+M14 b2,3,22,23,30-35,
  80-83), QC 11 (b4/b5+QM7 b36-38,76-79+T2 b80,81), RC 17
  (b4/b5+TM8 b19,39,46,47,80-83+TR7 b40-42,76-79).
  Coverage 74+10/68+16/73+11/71+17 exact, 0 overlap, b4/b5
  in no const set. AC sig 809a1f4a; QC sig 809a1f2a
  (PBA-adjacent); RC sig 02000000 (==P247T); CC b12 const
  0x00; QC b82,83 const 36,64 quad-wide; RC b84-87 fd/74/
  65/1e. A/C/Q b5 const 25 whole-range (A 0725..2525, C
  2725..3925, Q 3b25..b925, no carry); ring head bb/25,
  edges off34/35 + off162/163 exact; counter==lencode
  256/256. No BM/BC/M42/X42/M8/X8/QB/M19/XA19/PT/PC/FM/FC/
  FS/FO/RF/QR; inventory exactly 12 + 4 _N, novel-clean
  both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  103041, S1 103042, A 103043-58, C 103059-68, Q 103069-132
  m=off&15 q=off>>4, R 103133-388 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T68066/68071/68076/68091/
  68108/68127); ordered pay-index sequences C==py per range
  block (A n=10, C n=16, Q n=11, R n=17); ring consts
  0xbb/0x25 + (off>=35)+(off>=163) == py; temps _t5264..5279
  / _i3216..3224 / _b3215..3223 appended (base b355 max
  _t5263/_i3214/_b3213 first-hand via git show, no reuse;
  _i3215 skipped, _t max + _i/_b maxes == GATE); insert at
  dispatch tail after T10P247R close, N-out-of-scope follows
  both sides.
- Edges head 103041 + 103167/103168 + 103295/103296 PASS 2/2
  cells both legs. Odd-lencode whole-tier via own-loop
  348/348. Matches A-596 (34/34 = 11/11 shape + 14/14
  quad/ring + 9/9 counters, file read, counts verified) +
  A-318 (3/3 legs CONFIRM). Code-consts vs memo INCL (PBA
  75 / C10 69 / quad 74 / T88 71): impl 74/68/73 = memo-1
  on PBA/C10/quad, T88 71 identical (A-596 §3 explicitly
  no-finding).
- C diff purely additive: numstat 596/0 rgramc.c, 230/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 889). C 591 content + 5 bare-`+` / 0 del (all 5 bare
  in rgramc.c). Fine-norm TNP (temp-number-only,
  empty-excluding): del-uniq 0, add-uniq 402 EXACT == GATE.
- Wall on 889 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, singletons `if n == `
  528->530 +2, range-guards `<= n <=` 444->448 +4, CLOSED
  T10P prints 1376->1382 +6, C singletons 523->525 +2
  (C-vs-py 5-offset pre-existing, unchanged), seal
  1470->1476 +6: all agree (GATE literals reproduced
  exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-596 CONFIRM 34/34
  (backfill, own 364-cell bed, BAD=0) + A-318 corroborates
  3/3. No CONFIRM-P248.md file; A-files suffice per rule.
  Agrees with cport msg (py/C 14492, PYID 7246).
- Own-loop 348/348 (103041..103388, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b356. Newest
  PARENT-* is QNUM-13 (== GATE, no staleness). PROSE-01
  re-read before filing (all hex/counts from run output).

Verdict: PASS. GATE CORRECT, 0 slips.
