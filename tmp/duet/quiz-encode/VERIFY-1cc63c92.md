# VERIFY-1cc63c92 b360 T10P252 pins 104433..104780 (1500 tiers) PASS

Seat viewer-r48, first-hand, detached tree-1cc63c92 @1cc63c92,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r48.
Base 0b7920eb (b359, 1494 tiers). Band = 11bc6a4f (py) + 1cc63c92 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build360/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 879f3338 / aae d6e27c97
  (== GATE; aae.c untouched, sha1 aae 7d8dd3a2 == pinned).
- RGRAMC-PYID 7370/7370 covered=7370/7370 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14740/14740 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 14740/14740 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-identical
  (14740/14740, sorted).
- PINS 14742 rows (2 hdr + 14740, +62 vs base 14680); PINS
  base-N 7370 vs for-list 7370 exact both ways (0/0; tail
  104780 pinned AND in for-list). For-list 7339->7370 +31/-0
  verbatim == GATE's 31: sing 104433 104434; A 6 (104435
  head + 104436 + 104441 + carry pair 104447/104448 + 104450
  tail); C 6 (104451 head + 104454 + 104455 + 104456 +
  104459 + 104460 tail); Q 10 (104461 head + 104469 +
  104476 + 104477 + 104492 + 104493 + 104501 + 104508 +
  104509 + 104524 tail); R 7 (104525 head + edge pairs
  104575/104576 + 104703/104704 + mid 104653 + 104780 tail).
  31x2=62=14740-14678. PINS adds == for-list adds x2.
- SMOKE-GREEN rc=0 (6/6 PASS, NVME workdir, default backend).
- Tables audit P252 C-vs-py, own script tables360.py, 88/88
  ALL-EXACT (12-table A/C10-2SIG/QUAD-2T-no-R+T88, NO BM/BC:
  13 syms, S-pair one family): S0/S1 (80fc0200 NEW @104433
  b4b5 e3/2f / 5d169d05 NEW @104434 b4b5 e5/2f, both NEW
  strings vs P251, len 168 == lencode); AM 16/16 distinct 6B;
  CM 10/10 distinct 17B, sig-map exact order 8cc03106 x4
  @0-3 + 46e01803 x1 @4 + 8cc03106 x5 @5-9 (2 distinct sigs,
  10/10 diverge NO pair); M 16/16 distinct 9B; QR 4/4 PAIRED
  r1==r2 1f2fdb590062 + r0 f969885a06c1 + r3 1f2fdc590062
  1B-off (db-vs-dc, exactly 1 byte); QT 4/4 exact
  f470a4a5/6e2ac0e5/982ac0e5/9951481b (r1/r2 share last-3B
  2ac0e5, 4/4 distinct); M col-15-frag 7d x15 + 69 @c15
  EXACT; AC 76/76, CC 65/65, QC 63/63, RC 70/70; _N decls
  76/65/63/70. Varsets exact: AC 8 (b4/b5+M6 b6,7,76-79),
  CC 19 (b4/b5+M17 b0-3,6-8,10,11,48-51,80-83), QC 21
  (b4/b5+QM9 b0,9-12,76-79+R6 b6,7,48-51+T4 b80-83), RC 18
  (b4/b5+TM8 b8-10,19,76-79+TR8 b13-16,80-83). Coverage
  76+8/65+19/63+21/70+18 exact, 0 overlap, b4/b5 in no
  const set. AC sig dc65d159 NEW (in consts, not mtab); CC
  b9 const-staged (0x00); QC b1-3 091c63 + b0 sig-led in M
  tab; RC sig 06000000 NEW (P251 05000000); RC b84-87
  e0/a4/c3/50. RM/RQ UNPAIRED 0-overlap, tails SPLIT 16/16
  both; M-tails 16/16 NEW vs P251RQ-tails (last-8-hex sets
  disjoint; P251RQ 16x16ch first-hand). No BM/BC/M42/X42/
  M8/X8/QB/M19/XA19/PT/PC/FM/FC/FS/FO/RF; inventory exactly
  13 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  104433, S1 104434, A 104435-450, C 104451-460, Q 104461-524
  m=off&15 q=off>>4, R 104525-780 c=off&15 r=off>>4);
  C T-mirrors 6/6 exact bodies (T69035/69040/69045/69060/
  69077/69101); ordered pay-index sequences C==py per range
  block (A n=9, C n=19, Q n=23, R n=20); ring consts
  0x9b/0x30 + (off>=51)+(off>=179) == py; temps _t5336..5353
  / _i3259..3268 / _b3258..3267 appended (base b359 max
  _t5335/_i3257/_b3256 first-hand via git show, no reuse;
  _i3258 + _b3257 skipped); insert at dispatch tail after
  T10P251R close, N-out-of-scope follows both sides.
- Edges PBA 104447 (ff/2f) -> 104448 (01/30) + ring 104575
  (off50, ff/30) -> 104576 (off51, 01/31) + 104703 (off178,
  ff/31) -> 104704 (off179, 01/32); all six pins + tail
  104780 in for-list + 2 PASS lines each py+C. A b5set
  {2f,30} (single carry), C b5set {30}, Q b5set {30}
  NO carry. A head e7/2f tail 05/30, C head 07/30 tail
  19/30, Q head 1b/30 tail 99/30, R head 9b/30 tail
  99/32. Ring counter == raw lencode 256/256, 0 mismatch.
  Odd-lencode 348/348. Matches A-600 (12/12 + 12/12 + 11/11
  as sectioned; verdict line reads 36/36 as-filed; file
  read, counts verified; exact-value corroboration incl CM
  2-sig map, QR pair + 1B-off, QT tails + 3B-share, M-tails
  NEW, ring edges + consts re-checked above) + A-363 (all 3
  legs CONFIRM). Code-consts vs memo INCL (PBA 76 / C10 66 /
  quad 64 / T88 70): impl 76/70 identical on PBA/T88, 65/63
  = memo-1 on C10/quad (b5 const 30 both, standing incl/excl
  bookkeeping - A-600 S3 explicitly no-finding).
- C diff purely additive: numstat 610/0 rgramc.c, 238/0
  rgram.py, 1/1 test_rgram.sh, 62/0 PINS (== GATE; total
  adds 911). C 605 content + 5 bare-`+` / 0 del (all 5 bare
  in rgramc.c). Fine-norm: del-uniq 0, add-uniq 170 EXACT
  under GATE's stated TNP recipe (lead-ws + trailing-';'
  strip, digits->N, empty-excluding; norm file byte-identical
  to sweep's) - sweep2 TNP family.
- Wall on 911 added lines: vendor/disasm 0, depload 0,
  libcompression/compression_tool/aa/nominated/shim/ct-cache
  0, shebang 0. (62 `ct-lzraven` PINS backend tags,
  provenance column, every band.)
- Tiers: merge-msg +6, code 6 blocks, tier-comments `# T10P`
  1400->1406 +6, singletons `if n == ` 536->538 +2,
  range-guards `<= n <=` 460->464 +4, CLOSED prints
  1400->1406 +6, C singletons 531->533 +2 + C ranges
  460->464 +4 (5-offset pre-existing, unchanged), seal
  1494->1500 +6: all agree
  (GATE literals reproduced exactly).
- CONFIRM evidence (CONVERT-01 rule b): A-600 CONFIRM
  (sections + verdict as above, own 367-cell bed, BAD=0) +
  A-363 corroborates 3/3. No CONFIRM-P252.md file; A-files
  suffice per rule. Agrees with cport msg (py/C 14740,
  PYID 7370).
- Own-loop 348/348 (104433..104780, C+py agree CLOSED each N;
  populate fetched 317, 31 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b360. Newest
  PARENT-* is QNUM-14 (GATE says QNUM-13 - stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing (all
  hex/counts from run output).

Verdict: PASS. Code CORRECT; GATE 2 immaterial prose slips
(QNUM-13 vs -14 staleness; "P251RQ 16 rows 16B-wide" should be
8B-wide under the GATE's own B=bytes convention - P251RQ is 16
rows x 16 hex chars = 8B first-hand, same shape the GATE calls
"RQ 16/16 8B distinct" for P252).
