# VERIFY-5f75b749 b347 T10P239 pins 99909..100256 (1422 tiers) PASS

Seat viewer-r44, first-hand, detached tree-5f75b749 @5f75b749,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r44.
Base b74c603f (b346, 1416 tiers). Band = e58ca8e2 (py) + 5f75b749 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build347/bin, rc=0, 0 warnings. SHA-1 first8
  rgramc 8bacad39 / aae 7d8dd3a2 (== GATE; aae.c untouched).
- RGRAMC-PYID 6967/6967 covered=6967/6967 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13934/13934 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13934/13934 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13936 rows (2 hdr + 13934, +62 vs base); PINS cells
  6967 vs for-list 6967 exact match both ways (sorted, diff 0;
  numeric-token parse, no `;` pollution; tail 100256 pinned AND
  in for-list). For-list 6936->6967 +31/-0 verbatim == GATE's
  31: sing 99909 99910; A 6 (99911 head + 99915 off4 + 99919
  split9-tail + 99920 split7-head + 99923 off12 + 99926 tail);
  C 5 (99927/99929/99930/99933/99936 = off0,2,3,6,9; off1,4,5,
  7,8 = 99928/99931/99932/99934/99935 confirmed unsampled); Q
  12 (row starts 99937/99953/99969/99985 + row ends 99952/
  99968/99984/100000 + 99960/99976/99992 + carry pair 99967/
  99968); R 6 (100001 + 100095/100096 + 100223/100224 +
  100256). 31x2=62=13934-13872. PINS adds == for-list adds.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P239 C-vs-py, own script tables347.py, 65/65
  ALL-EXACT (15-table + b19 leg): S0/S1 (9f540100 NEW /
  417faa02 NEW, len 168, b4b5 8b0c/8d0c == lencode), AM 16/16
  distinct 10B SPLIT triples c9d644 x9 + ea9645 x7 const,
  CM 10/10 distinct 15B 2-sig map 5e7faa02 x3 + af3f5501 x7
  exact order (full 4B heads), M 16/16 distinct 6B sig-led
  b0 15 distinct (d1 doubled, exact multiset), M19 16/16
  45x6/c5x10, XA19 00/09/09/09 (ADD staged), QR 4/4 r2==r3
  ee7ce21a7a80 x2 + r0 7f3c403a8b1d + r1 ed7ce21a7a80 1B-off
  (verified 1 hex-char diff), QT 4/4 exact de328733/c3741d50/
  b1ea2893/dbea2893 + r2/r3 TRUE-3B ea2893, RM 16/16 (7B) /
  RQ 16/16 (7B) UNPAIRED, AC 72/72, CC 67/67, QC 65/65, RC
  72/72; _N decls 72/67/65/72. Varsets exact: AC 12, CC 17,
  QC 19, RC 16 (A-560 VPOS + b5-excl on A/C). Coverage
  72+12/67+17/65+19/72+16 exact, 0 overlap, b4/b5 in no
  const set. b0-3: AC 0:TAB + f5/a7/2a, CC all TAB, QC 0:TAB
  + ad/f6/14 (sig-led ??adf614), RC 01000000. RC b84-87
  a2/3b/39/be. RQ==M 0/16 (no staged equality, as stated).
  M-tails NEW vs P238T; RM NEW vs P238RM; QT 4/4 NEW vs
  P238QT. Ring tails SPLIT 16/16 both. A/C b5 const 0c,
  Q carry ff0c->010d @99967->99968 + b5set {0c,0d}; ring
  edges off94/95 + off222/223 (0x43/0x0d base). No M42/X42/
  BM/BC/PT/PC/FM/FC; inventory exactly 15 + 4 _N,
  novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  99909, S1 99910, A 99911-26, C 99927-36, Q 99937-100000
  m=off&15 q=off>>4, R 100001-256 c=off&15 r=off>>4); C
  T-mirrors 6/6 exact (T65735/740/745/761/778/803); guards
  exact; b19 ADD leg both sides ((pay[19]-XA19[q])&FF ==
  M19[m]; C via snprintf %02lx + hexval; XOR-tie noted in
  code comment per A-560/A-309 verdict); ring consts
  67/95/223 (67=0x43); ring byte lists M7 b29-31,80-83 /
  R7 b16,17,23,76-79 match; temps _t5088.._t5107 appended
  (base max _t5087, no reuse); insert after T10P238R close
  at dispatch tail, N-out-of-scope follows both sides.
- Edges 100095/100096 + 100223/100224 + Q carry 99967/99968
  + head 99909 + tail 100256 PASS 2/2 both legs. Odd-lencode
  whole-tier via own-loop 348/348. Matches A-560 (40/40 =
  18/18 shape + 14/14 quad/ring + 8/8 counters, file read,
  counts verified) + A-309 (3/3 legs; SPLIT9/7 exact, C10
  map exact, QUADms triple/tails exact, b19 ADD/XOR tie
  flagged with ADD staged by P231 precedent, ring SPLIT
  explicit, consts 73/68/65/72 INCL with standing -1 x2
  excl on PBA/C10, NO D dips).
- C diff purely additive: numstat 640/0 rgramc.c, 261/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  964). C 640 add / 0 del; fine-norm: del-uniq 0, missing 0
  (== GATE); add-uniq 181 under the stated method vs GATE's
  178 — see note S1 (178 reproduces iff lines are also
  whitespace-stripped: 4 bare-`}` indent variants merge).
- Wall on 964 added lines: vendor/disasm 0, depload 0,
  libcompression/aa/shim/shebang/nominated 0.
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10`
  1581->1587 +6, singletons `if n == ` 510->512 +2,
  range-guards `<= n <=` 408->412 +4, CLOSED prints
  `print("CLOSED` 1839->1845 +6, seal 1416->1422 +6: all
  agree (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-560 CONFIRM
  40/40; A-309 corroborates. Agrees with cport msg (py/C
  13934, PYID 6967).
- Own-loop 348/348 (99909..100256, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: FLAG-937c347-hold read, SUPERSEDED per PARENT-032/033
  (band5-era, name collision on "347" — GATE's note correct).
  No conflicting CLAIM/GATE/FLAG on b347. Newest PARENT-* is
  QNUM-12 (GATE says QNUM-10 — stale, immaterial, Q-block
  grants only). PROSE-01 re-read before filing.

1 GATE METHOD NOTE (sweep-r48; code PASS): (S1) fine-norm
"add-uniq 178" vs 181 under the method as stated ([0-9]+ ->
N, sign/';' strip, python sets); 178 reproduces exactly iff
lines are additionally whitespace-stripped (4 bare-`}`
indent variants 12/8/4/0-space merge to 1). So the count is
right under their actual pipeline but the method string
under-specifies it (cf b345 same method string reproduced
158 exactly WITHOUT strip — the two seats' pipelines differ
despite identical strings). Del-uniq 0 + missing 0 agree;
purely-additive verdict unaffected.

Verdict: PASS. Code CORRECT; GATE 1 method note (flagged).
Logs: NVME ws tmp/encode-viewer/r44/ (*347* set:
build347, pyid347, rgram347py/c, cmp347.py/.c, for347-*,
pins347.basen, smoke347, tables347.py/.log, banddiff347(-c),
added347, numstat347, populate347, ownloop347.py/.log).
