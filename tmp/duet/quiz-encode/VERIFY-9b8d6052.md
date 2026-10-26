# VERIFY-9b8d6052 b378 T10P270 pins 110697..111044 (1608 tiers) PASS

Seat viewer-r52, first-hand, detached tree-9b8d6052 @9b8d6052,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r52.
Base 376bc6a9 (b377, 1602 tiers). Band = 304b0414 (py merge
w2b@fb6379f9 partial, +6 tiers, +66 pins) + 9b8d6052 (C port,
1608 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build378/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 8da910c6 / aae d6e27c97
  (== GATE both; aae pinned, band touches no aae sources
  per numstat) + sha1 rgramc 5157a625 / aae 7d8dd3a2.
- RGRAMC-PYID 7932/7932 covered=7932/7932 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 15864/15864 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 15864/15864 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 15864/15864 sorted).
- PINS 15866 rows (2 hdr + 15864, +66 vs base 15800);
  PASS-names vs PINS-names cmp-equal 15864/15864 py+C;
  base-N vs for-list cmp-equal 7932/7932. For-list delta
  vs base +33/-0: 110697 110698 110699 110700 110704
  110709 110713 110714 110715 110716 110718 110719 110720
  110721 110723 110724 110725 110732 110739 110740 110741
  110756 110757 110772 110773 110788 110789 110847 110848
  110932 110975 110976 111044 (2 sing + A6 offs 0,1,5,
  10,14,15 + C8 offs 0,1,3,4,5,6,8,9 + Q10 offs 0,7,
  14,15,16,31,32,47,48,63 + R7 offs 0,58,59,143,186,187,
  255 == GATE decomposition; 7899->7932); 33x2=66 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit378.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 96 PASS 0
  FAIL (1 script-side slice fix pre-pass, code never
  impugned). Inventory exactly the 14 both sides (RT
  present; no BM/BC, no M19, no M42/X42, no QB/PT/FM).
  S0/S1 168ch sigs a6930300 NEW / a5322507 SIG-REPEAT
  (both NEW strings, full-string ne vs P269 pair; S1 sig
  == P269CC b0-b3 a5322507 re-read). AM 16x7B / CM 10x
  12B / M 16x9B / QR 4x6B / QT 4x4B / RM 16x7B / RQ 16x
  5B / RT 16x4B all C==py. AM/CM/M/RM/RQ/RT all 16/16
  or 10/10 distinct. CM rows 0-4 share head 49c1c1386f14
  (carry staged via lencode). PBA sig 208c277e REPEAT
  (P269 PBA 208c277e re-read; AM rows 0-overlap novel
  implied by M-tails NEW + staging); b0 const 20; AC no
  b5. C10-CARRY a532450e x10 via CC b0-b3; CM 10/10
  diverge; CC no b5. QUAD1s single-sig 208c27fe x64 via
  QC b0-b3; NO frags (M+R6+T4 legs only, eye-verified);
  R6 LAST3-PAIRED r1==r2==r3 7b9e0c9f6478 x3 (r0
  3b8d37cfc067 distinct; 2 distinct); tails row-shared
  4/4 distinct ea14f78d/4e664444/73664444/98664444,
  r1/r2/r3 share TRUE 3B 664444 (first bytes 4e/73/98
  differ); b44 const 54 (b44-skipped); QC no b5. Ring
  ROWTAIL (2nd): RM b6,7,12,76-79 16/16 by COL, RQ
  b51-55 16/16 by ROW UNPAIRED (full-row sets disjoint),
  RT b80-83 ROW-led 16/16 by r; RC b0-3 0f000000 NEW
  (P269 07000000 re-read); RC b84-87 bd664444 ring-wide
  NEW (P269 had 1b2a6322 re-read; shares 664444 with
  quad r123 tails). Same-tier M[m]==RQ[m]+RT[m] 16/16
  full-row (staging). AC/CC/QC/RC 75/70/63/70 py-vs-C
  normalized; _N decls 75/70/63/70 match actual;
  sorted-unique. Missing-sets EXACT: AC-9
  [4,5,34,42,43,76-79]; CC-14 [4,5,34,35,41-46,80-83];
  QC-21 [4,5,34,35,42,43,45-51,76-83]; RC-18
  [4,5,6,7,12,51-55,76-83]. Coverage unions exact every
  block (const U tab U {b4,b5} == 84/84/84/88, 0
  overlap). M-tails 16/16 ALL NEW vs P269T (overlap 0
  vs P269 RM-tail8 + RT sets; P269 RM 14ch / RT 8ch
  rows re-read). Memo INCL PBA 76 / C10 70 / quad 64 /
  T88 70 (A-654 re-read): impl 75/70/63/70 = memo-1 on
  PBA/quad (standing), identical C10/T88.
- Section-F own scripts secf270.py (table reconstruction
  from P269CM+P269CC+lencode) + secf270b.py (oracle bytes
  direct) + secf270c.py (recon==oracle cross-check +
  agree positions): P270S1 sig a5322507 == P269C10 sig
  re-read; payload diffs vs the 10 staged P269 C10
  cells (110367..376): 55/84 x8 (110367-110374) +
  54/84 x2 (110375, 110376); recon==oracle byte-exact
  all 10; the extra agree byte on 110375/110376 is b24.
  Finding stands (sig-repeat staged, NOT byte-repeat;
  memo "54-55 diffs each" EXACT). GATE prose-count
  error: GATE claims "55/84 from ALL 10" — 110375 and
  110376 are 54/84, thrice-derived (two independent
  methods + cross-check). PROSE-01-class slip, code
  unaffected (see Verdict).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 110697 / S1 110698 / A 110699-714 / C 110715-724 /
  Q 110725-788 / R 110789-111044): bounds + paylens (92
  x84 / 256 x88) + lencode both sides (C carry + Q b5
  const emerge from raw lencode) + R counter
  b4=(139+2off)&FF b5=97+(off>=59)+(off>=187) both
  sides (C 139/97 = 0x8b/0x61) + mtab/qtab/ttab byte
  positions exact (A 7B b34,42,43,76-79; C 12B
  b34,35,41-46,80-83; Q 9/6/4B; R 7/5/4B) +
  m=off&15/q=off>>4/c=off&15/r=off>>4 both sides.
  T-mirrors T73921/73926/73931/73946/73962/73986 each
  re-read: hits the exact py guard line. Temps
  _t5698-5717 (base max _t5697, no reuse) + _b3456/3458/
  3460/3461/3462/3464/3465/3466 (base max _b3454) +
  _i3457/3459/3463/3467 (base max _i3455, no reuse). C
  guards `if ((n) == (110697))` / `(110698)` + 4 ranges
  exact. Insert exact both sides: after T10P269R close,
  N-out-of-scope follows. Matches A-654/A-334 geometry
  (values re-checked in audit above; NO D dips).
- Edges own-loop ownloop378.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache, 315 miss-warmed; seat rgramc each):
  348/348 CLOSED. Census R256/Q64/A16/C10/S0/S1 exact.
  edges378.py: paylens 92 x84 + 256 x88; lencode 92/92
  (A head d7/60 tail f5/60 b5set {60} NO carry; C head
  f7/60 tail 09/61, carry edge 110719 (o4, ff/60) ->
  110720 (o5, 01/61), C-form b4=(0xf7+2off)&FF
  b5=0x60+(off>=5) 10/10; Q head 0b/61 tail 89/61
  b5set {61} NO carry); ring counter 256/256 (head
  8b/61; 110847 (off58, ff/61) -> 110848 (off59,
  01/62); 110975 (off186, ff/62) -> 110976 (off187,
  01/63); mid off143 (110932) a9/62; tail 111044
  (off255) 89/63). S0/S1 d3/60 + d5/60 match raw
  lencode. Edge pins + tail 111044 in for-list + 2 PASS
  lines each py+C. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 636/0 (rgramc.c) + 259/0
  (rgram.py) + 1/1 (for-line) + 66/0 (PINS) == GATE; raw
  C 631 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 259 content / 0 del.
  Fine-norm temp-norm-only (_tN/_iN/_bN, empty-
  excluding): C del-uniq 0 add-uniq 433 EXACT (== GATE),
  py del-uniq 0 add-uniq 225. Sweep2 family.
- Wall on band diff added lines (scope 376bc6a9..
  9b8d6052, 962 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 636/0, rgram.py 259/0 purely
  additive, test_rgram.sh 1/1, PINS +66/+0.
- Tiers: merge-msg +6/+66, code 6 blocks, dispatch-guards
  singletons 572->574 +2 / ranges 532->536 +4 = +6,
  CLOSED T10P prints 1508->1514 +6, C singletons
  567->569 +2 / ranges 532->536 +4 (deltas agree both
  sides), seal 1602->1608 +6: all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-654-q782-
  t10p270 verdict CONFIRM (40/41 + section-F as-filed:
  shape 13/14 + quad/ring 13/13 + counters 14/14;
  file re-read; exact-value corroboration incl PBA/C10
  sigs, QUAD1s + R6 last3-pair + QT tails, M-tails NEW,
  ring edges + consts, section-F re-checked above) +
  A-334 viewer corroboration (all 3 legs CONFIRM; its
  PB1 byte-equal claim superseded by memo section-F,
  corroborated first-hand above). No CONFIRM-P270.md
  file; A-654 suffices per rule. Agrees with cport
  commit msg (PYID 7932, RGRAM 15864).
- Quiz: no conflicting CLAIM/GATE/FLAG on b378. Newest
  PARENT-* is QNUM-18 (grants, read, no gate impact);
  GATE cites QNUM-13 (grants-only staleness, immaterial,
  standing pattern). PROSE-01: all hex/counts above
  copied from own run output.
- Own near-miss caught pre-filing (script fixed, code
  never impugned): tabaudit378 CM-head slice compared
  14 chars against a 12-char literal; fixed to [:12],
  96/96.

Verdict: PASS. No RED. GATE CORRECT on code; 2 prose
slips, both immaterial to the verdict: (1) QNUM-13 vs
-18 staleness (standing pattern); (2) PROSE-01-class
count error — section-F "55/84 from ALL 10 staged
cells" is wrong for 110375/110376 (54/84 first-hand,
thrice-derived; memo's "54-55 diffs each" is exact).
The section-F conclusion (sig-repeat, not byte-repeat)
is unaffected.
