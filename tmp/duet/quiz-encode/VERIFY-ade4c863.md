# VERIFY-ade4c863 b362 T10P254 pins 105129..105476 (1512 tiers) PASS

Seat viewer-r48, first-hand, detached tree-ade4c863 @ade4c863,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r48.
Base 8627293f (b361, 1506 tiers). Band = 451b04ad (py) + ade4c863 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build362/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 868995bc / aae d6e27c97
  (== GATE; aae.c untouched per numstat).
- RGRAMC-PYID 7432/7432 covered=7432/7432 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14864/14864 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14864/14864 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14864/14864, sorted).
- PINS 14866 rows (2 hdr + 14864, +62 vs base 14804); PINS
  base-N 7432 vs for-list 7432 exact both ways (0/0; tail
  105476 pinned AND in for-list); PASS-names vs PINS-names
  xor 0. For-list 7401->7432 +31/-0 verbatim == GATE's 31:
  sing 105129 105130; A 6 (105131 head + 105132 + 105137 +
  105141 + 105145 + 105146 tail); C 6 (105147 head + 105150
  + 105151 + 105154 + 105155 + 105156 tail); Q 10 (105157
  head + 105159 + 105160 + 105172 + 105173 + 105188 + 105189
  + 105204 + carry pair 105215/105216); R 7 (105221 head +
  edge pairs 105343/105344 + 105471/105472 + mid 105349 +
  105476 tail). 31x2=62=14864-14802. PINS adds == for-list
  adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME workdir, default backend).
- Tables audit P254 C-vs-py, own script tables362.py, 96/96
  ALL-EXACT (14-sym A-PBA/C10-2SIG/QUAD-row-led+T88, NO
  BM/BC/M42/X42/PT/FM): S0/S1 (e4180300 NEW @105129 b4b5
  53/35 / 6d4b3306 ==P253C10a @105130 b4b5 55/35, S0 string
  NEW vs P253, S1 string NEW, S1 sig == P253 CC b0,b1 +
  CM head 3306 code-verified, len 168 == lencode); AM 16/16
  distinct 7B; CM 10/10 distinct 15B, sandwich 3306x4/1303x4/
  3306x2 (full sigs 6d4b3306 x6 / 6d4b1303 x4 via CC b0,1 =
  6d,4b; 10/10 diverge NO pair); M 16/16 distinct 8B; QB47
  32/32 (g0 f2x3+f4x13, g1 f9x3+fa13, 2x2-frag positional
  64/64 EXACT: [0:3]/[3:16] splits exact both groups);
  QR 4/4 PAIRED r2==r3 261a8c74d5b8856f93b4e1 + r0
  669a18d8c5b889d7146914 + r1 261a8c14de588a5f53caf9
  distinct, QR b3 66/26/26/26 (row-led a096b766-r0/
  a096b726-r123 via QC b0-2); QT 4/4 exact b6a8543e/
  e95abd76/ef6138db/196238db (r2/r3 share last-2B 38db
  ONLY, 2nd-B 61/62 1B-off, SR-staged); RM 16/16 6B /
  RQ 16/16 9B UNPAIRED 0-overlap, tails SPLIT 16/16 both
  (RM b80-83 by COL, RQ b76-79 by ROW); same-tier RQ rows
  = 1B head + M row 16/16 (heads f9/fa); AC 75/75, CC
  67/67, QC 58/58, RC 71/71; _N decls 75/67/58/71. Varsets
  exact: AC 9 (b4/b5+M7 b34,42,43,76-79, b42 IN range),
  CC 17 (b4/b5+M15 b2,3,34,35,41-47,80-83), QC 26 (b4/b5+
  QM8 b48-51,76-79+b47+R11 b3,14,15,34,35,41-46+T4 b80-83),
  RC 17 (b4/b5+TM6 b6,7,80-83+TR9 b51-55,76-79). Coverage
  75+9/67+17/58+26/71+17 exact, 0 overlap, b4/b5 in no
  const set. AC sig a096b766 ==P253PBA (code-verified vs
  P253AC b0-3); RC sig 02000000 back-to-02 (P253T 06000000
  re-read); RC b84-87 65/5b/bd/76. M-tails 16/16 NEW vs
  P253T (zero overlap vs BOTH P253RM-tail and P253RQ-tail
  sets; P253 TR8/TM6 shapes re-read). Inventory exactly
  14 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  105129, S1 105130, A 105131-146, C 105147-156, Q 105157-220
  m=off&15 q=off>>4 g=0-iff-q0, R 105221-476 c=off&15
  r=off>>4); C T-mirrors 6/6 exact bodies (T69690/69695/
  69700/69715/69732/69759); C b47 coltab via snprintf %02lx
  of pay[47] vs QB47[g+m] (matches py); ordered pay-index
  sequences C==py per range block (A n=9, C n=17, Q n=27,
  R n=19); ring consts 0x0b/0x36 + (off>=123)+(off>=251)
  == py; temps _t5380..5399 contiguous (base max _t5379) +
  _i3281..3290 / _b3280..3289 (base max _i3279/_b3278
  first-hand via git show, no reuse); insert at dispatch
  tail after T10P253R close, N-out-of-scope follows both
  sides.
- Edges Q-carry 105215 (off58, ff/35) -> 105216 (off59,
  01/36) + ring 105343 (off122, ff/36) -> 105344 (off123,
  01/37) + 105471 (off250, ff/37) -> 105472 (off251, 01/38
  near-tail) + mid 105349 (off128, 0b/37); all edge pins +
  tail 105476 in for-list + 2 PASS lines each py+C. A head
  57/35 tail 75/35 b5set {35}; C head 77/35 tail 89/35
  b5set {35}; Q head 8b/35 tail 09/36 b5set {35,36}; R
  head 0b/36 tail 09/38. Ring counter == raw lencode
  256/256, 0 mismatch. Odd-lencode 348/348. Matches A-604
  (shape 12/12 + quad 12/12 + counters 11/11 as sectioned;
  verdict line reads 36/36 + SR as-filed; file read, counts
  verified; SR ruling 2B 38db + 61/62 1B-off - code stages
  exact QT values + Q comment states 2B 38db, P250/P253
  pattern; exact-value corroboration incl CM 4/4/2 map,
  QB47 frag 64/64, QR pair, QT tails, row-led pair, M-tails
  NEW, ring edges + consts re-checked above) + A-365 (all 3
  legs CONFIRM; its S2 "r2/r3 last-3B" line contradicts its
  own cited values ef6138db/196238db exactly as GATE states
  - SR governs, code stages 2B; memo-side prose only).
  Code-consts vs memo INCL (PBA 76 / C10 68 / quad 58 /
  T88 71): impl 75/67 = memo-1 on PBA/C10 (b5 const 35
  both), 58/71 identical on quad/T88 (A-604 S3 explicitly
  no-finding).
- C diff purely additive: numstat 651/0 rgramc.c, 276/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 990). C 646 content + 5 bare-`+` / 0 del. Fine-norm:
  del-uniq 0, add-uniq 176 EXACT under GATE's stated TNP
  recipe (lead-ws + trailing-`;` strip, digits->N,
  empty-excluding; norm file byte-identical to sweep's) -
  sweep2 TNP family.
- Wall on 990 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1412->1418 +6, singletons `if n == ` 540->542 +2,
  range-guards `<= n <=` 468->472 +4, CLOSED prints
  1412->1418 +6, C singletons 535->537 +2 + C ranges
  468->472 +4 (5-offset pre-existing, unchanged), seal
  1506->1512 +6: all agree (GATE literals reproduced
  exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-604 CONFIRM
  36/36 + SR (own 367-cell bed, BAD=0, tier cut SAFE) +
  A-365 corroborates 3/3. No CONFIRM-P254.md file; A-files
  suffice per rule. Agrees with cport msg (py/C 14864,
  PYID 7432).
- Own-loop 348/348 (105129..105476, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b362. Newest
  PARENT-* is QNUM-14 (GATE says QNUM-13 - stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing (all
  hex/counts from run output).

Verdict: PASS. Code CORRECT; GATE 1 immaterial staleness
(QNUM-13 vs -14).
