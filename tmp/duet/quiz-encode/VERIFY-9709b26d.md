# VERIFY-9709b26d b380 T10P272 pins 111393..111740 (1620 tiers) PASS

Seat viewer-r53, first-hand, detached tree-9709b26d @9709b26d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r53.
Base b9db70db (b379, 1614 tiers). Band = 4e302e0a (py merge
w2b@9b4ce56f partial, +6 tiers, +62 pins) + 9709b26d (C port,
1620 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build380/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 810ac304 / aae d6e27c97
  (== GATE both) + sha1 rgramc 877f9bf3 / aae 7d8dd3a2
  (aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 7996/7996 covered=7996/7996 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15992/15992 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15992/15992 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15992/15992 sorted).
- PINS 15994 rows (2 hdr + 15992, +62 vs base 15932);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0 (pass + pins). For-list delta vs base +31/-0:
  111393 111394 111395 111396 111400 111405 111409 111410
  111411 111412 111414 111417 111419 111420 111421 111428
  111435 111436 111437 111452 111453 111468 111469 111484
  111485 111487 111488 111615 111616 111628 111740
  (== GATE verbatim; S2 + A6 offs 0,1,5,10,14,15 + C6
  offs 0,1,3,6,8,9 (offs 2,4,5,7 unsampled) + Q10 offs
  0,7,14,15,16,31,32,47,48,63 + R7 offs 0,2,3,130,131,
  143,255; 7965->7996); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit380.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 102 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT; no BM/BC, no M19, no M42/X42, no QB/PT/
  FM). S0/S1 168ch sigs f62a0700 NEW f62a-family /
  25bd5c0e NEW (both NEW strings, sigs NEW vs P271
  76270700/fcec550e re-read). AM 16x7B distinct; AC b0-3
  c0935ff8 PLAIN (AC has b0; P271 PBA split-sig, no
  single b0-3). CM 10x12B diverge 10/10 (rows 0-4 share
  head 3709a57e75ec; rows 5,6,7 pairwise lcp 0; rows 8,9
  lcp 16 head-only, rows differ). CC b0-3 25bd5c0e ==
  S1 sig (intra-tier sig-repeat). M 16x7B distinct. QR
  r1==r2==r3 LAST3-PAIRED 3f8f317eb5563d x3 (last3
  b5563d), r0 87c77df9550a1a distinct (last3 550a1a), 2
  distinct. QT d5b4b22a/44398e25/69398e25/43399225 4/4
  distinct; r1/r2 share TRUE 3B 398e25 (first bytes 44/
  69 differ); r3 43399225 suffix-shares 1B-only (25).
  RM/RQ 16x7B distinct. AC/CC/QC/RC 75/70/64/72 py-vs-C
  normalized; _N decls 75/70/64/72 match actual;
  sorted-unique. AC/CC/QC no b5. QC b0-3 c0935ff8 ==
  PBA sig; QC b44 const ca. RC b0-3 0a000000 NEW (P271
  0e000000 re-read); RC b84-87 b874e2de ring-wide.
  Missing-sets EXACT: AC [4,5,21,22,31,76-79]; CC
  [4,5,22,23,30-35,80-83]; QC [4,5,22,23,30-34,36-38,
  76-83]; RC [4,5,39-42,46,47,76-83]. Coverage unions
  exact every block (const U tab U {b4,b5} == 84/84/84/
  88, 0 overlap). Tails SPLIT (RM b80-83 col / RQ b76-79
  row, 16/16 distinct each, 0 overlap UNPAIRED; full-row
  sets disjoint). Q legs M+R7+T4 only, no frags.
  S1-vs-staged-C10 re-derived THRICE (table-recon +
  oracle-direct + staged==oracle byte-exact 10/10, 4
  miss-warmed): 47/84 x8 + 46/84 x2 (111419/111420,
  extra agree byte b83) -- GATE "48 ALL 10" is a
  PROSE-01 count slip, conclusion (sig-repeat, not
  byte-repeat) stands. M-tails 16/16 ALL NEW vs P271
  (zero overlap vs BOTH P271RM-tail8 and P271RQ-tail8;
  M-full also NEW vs both); QT/RM/RQ ALL NEW vs P271
  (P271QT d45a1a47/81d84934/a6d84934/cbd84934 re-read).
  Base temp maxes _t5735/_b3477/_i3478 (no reuse).
  Memo INCL PBA 76 / C10 71 / quad 65 / T88 72 (A-660
  re-read): impl 75/70/64/72 = memo-1 on PBA/C10/quad,
  identical T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 111393 / S1 111394 / A 111395-410 / C 111411-420 /
  Q 111421-484 / R 111485-740): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q) + R counter b4=(251+2off)&FF b5=102+
  (off>=3)+(off>=131) both sides (251/102 = 0xfb/0x66)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/qtab/ttab byte positions exact (A 7B b21,22,31,
  76-79; C 12B b22,23,30-35,80-83; Q 7/7/4B; R 7/7B) +
  NO frag leg (M+R7+T4 only). T-mirrors T74401/74406/
  74411/74426/74442/74465 each re-read: hits the exact
  py guard line. Temps _t5736-5753 continuous (base max
  _t5735, no reuse) + _b3479/3481/3483/3484/3485/3487/
  3488 (base max _b3477) + _i3480/3482/3486/3489 (base
  max _i3478, no reuse). C guards `if ((n) == (111393))`
  / `(111394)` + 4 ranges exact. Insert exact both
  sides: after T10P271R close, N-out-of-scope follows.
  Matches A-660/A-336 geometry (values re-checked in
  audit above; NO D dips).
- Edges own-loop ownloop380.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0. Census R256/Q64/A16/C10/S0/S1 exact. (Re-run 0
  miss; first-run miss count not captured -- own logging
  miss, code unaffected.) edges380.py: paylens 92 x84 +
  256 x88; lencode 92/92 (A head 47/66 tail 65/66 b5set
  {66}; C head 67/66 tail 79/66 b5set {66}; Q head 7b/
  66 tail f9/66 b5set {66} NO carry; S0/S1 43/66 +
  45/66 match raw lencode); ring counter 256/256 (head
  fb/66; 111487 (off2, ff/66) -> 111488 (off3, 01/67);
  111615 (off130, ff/67) -> 111616 (off131, 01/68); mid
  off143 (111628) 19/68; tail 111740 (off255) f9/68).
  Edge pins + tail 111740 in for-list + 2 PASS lines
  each py+C. Odd-lencode 348/348. No DISSENT: cut bytes
  verify.
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE; raw
  C 605 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 237 content / 0 del.
  Fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm,
  empty-excluding): del-uniq 0 add-uniq 389 missing 0
  EXACT (== GATE).
- Wall on band diff added lines (scope b9db70db..
  9709b26d, 910 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 610/0,
  rgram.py 237/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, singletons
  576->578 +2 / ranges 540->544 +4 (stated method, plain
  `if n ==` / `<= n <=` BSD grep), CLOSED T10P prints
  1520->1526 +6, C singletons 571->573 +2 (5-count C-vs-
  py offset pre-existing, unchanged) + C ranges 540->544
  +4, C CLOSED 1520->1526 +6, seal 1614->1620 +6 (commit
  msgs): all agree, no slip (absolute seal inherits lane
  tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-660-q784-
  t10p272 verdict CONFIRM 37/37 (13+12+12 sums exact;
  file re-read; exact-value corroboration incl PBA/C10
  sigs, QUAD1s + R7 last3-pair + QT tails, M-tails NEW,
  ring edges + consts re-checked above) + A-336 viewer
  corroboration (all 3 legs CONFIRM, consts 76/71/65/72
  INCL). No CONFIRM-P272.md file; A-660 suffices per
  rule. Agrees with cport commit msg (PYID 7996, RGRAM
  15992).
- Quiz: no conflicting CLAIM/GATE/FLAG on b380. Newest
  PARENT-* is QNUM-18 (== GATE cite, current, no
  staleness). PROSE-01: all hex/counts above copied from
  own run output.
- Own near-miss caught pre-filing (script fixed, code
  never impugned): cmp380.py copy-over carried stale
  379 PASS data; caught before use, regenerated from
  fresh logs (C-py cmp-equal 15992/15992).

Verdict: PASS. No RED. GATE CORRECT on code, 1 immaterial
prose slip (S1-staged count "48 ALL 10" vs thrice-derived
47x8+46x2 -- conclusion unaffected).
