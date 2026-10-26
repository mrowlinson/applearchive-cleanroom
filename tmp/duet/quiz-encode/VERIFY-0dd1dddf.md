# VERIFY-0dd1dddf b414 T10P306 pins 123225..123572 (1824 tiers) PASS

Seat viewer-r61, first-hand, tree414 @0dd1dddf,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r61.
Base f539e0c8 (b413, 1818 tiers). Band = efb485e3 (py merge
w2b@c5db4c86 partial, +6 tiers, +62 pins) + 0dd1dddf (C port,
1824 sealed). Trees manifest-identical to tips (git ls-tree
vs find identical both; 117 = 113 non-tmp + 4 tmp).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build414/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc fa194b138d6c051a / aae
  d6e27c97ced21673 (== GATE both; aae pinned, band
  touches no aae sources per numstat) + sha1 rgramc
  35bf145bdedca1aa / aae 7d8dd3a2d118e0db (recorded, no
  GATE claim).
- RGRAMC-PYID 9060/9060 covered=9060/9060 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 18120/18120 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 18120/18120 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (sorted
  cmp equal + raw-order identical, 18120/18120).
- PINS 18122 rows (2 hdr + 18120, +62 vs base 18060);
  PASS-names vs PINS-names xor 0 py+C; py-vs-C xor 0;
  base-N vs for-list xor 0. For-list delta vs base +31/-0:
  123225 123226 123227 123228 123234 123235 123241 123242
  123243 123244 123247 123248 123251 123252 123253 123261
  123263 123264 123269 123277 123285 123293 123301 123316
  123317 123391 123392 123445 123519 123520 123572
  (== GATE decomposition: S0/S1 (2) + A6 offs 0,1,7,8,14,
  15 + C6 offs 0,1,4,5,8,9 + Q10 offs 0,8,10,11,16,24,32,
  40,48,63 (head + mid + b5-step edge-pair 123263/123264
  + 5 mids + tail) + R7 offs 0,74/75,128,202/203,255
  (head + both counter edges straddled + mid 123445 +
  tail); 9029->9060); 31x2=62 rows, range 123225..123572
  exact. PINS-new-N == for-added 31/31 (4th set-eq way),
  PINS removed 0.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- UNITS-GREEN rc=0 (tests/test_units.py). AEAD units
  env-blocked (no `lz4` module, same as r60/r61 b412-
  b413); band diffs touch no proto/ sources (numstat
  proves), NO verdict impact.
- Tables audit own script tabaudit414.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 157 PASS
  0 FAIL. Inventory exactly the 12 both sides (PBA88-
  PLAIN/C10-1SIG/QUAD88-4R/RING-STANDARD; no F/F0/F1,
  no QT/RT/TT, no BM/BC, no M19/X19, no QB/PT/FM, no
  M42/X42/H42/L42); C==py 12/12. S0/S1 168ch sigs
  db1b7900 sig-eq-P305PB0 / 80120ffa NEW (S0 32/84 vs
  P305S0 @ 4,5,32-35,37-48,50,51,56-63,80-83 EXACT,
  FIRST 32-diff + cross-P305S1 67, S1 66/58 vs P305
  heads). AM 16x16ch distinct; AC 78, b0-3 0f/00/00/00
  (b0 const 0f), no b4/b5, PBA sig 0f000000 x16 PLAIN
  (NEW sig 0f). CM 10x24ch 10/10 diverge; CC 70, b0-3
  803b4fc4, no b4/b5 (b5 const c2 via lencode); rows0-8
  share 16ch 721329877813b2ab + tails 0daaa4af/2daaa4af/
  4daaa4af/04311bbb/4c3351c3/6c3351c3/8c3351c3/ac3351c3/
  cc3351c3 EXACT, row9 distinct head f20d0937 tail
  2db3ab3a; C10-1SIG x10 NOT-PB1-sig (S1 sig differs
  own-C10). M 16x16ch distinct. QR 4x22ch 4-distinct
  UNPAIRED; r0 4d5cfce5132a6813f28f3f distinct; r123
  share 14ch 8adb9da333e671 + byte7 ea/2e/53; tails
  b84-87 13f28f3f/ea331391/2e341391/53341391 4/4
  distinct; r23 TRUE 3B 341391; r1 2B 1391; full-row
  lcsuf (2,3)=3 (1,2)=(1,3)=2 r0-pairs 0 + lcpre r123
  7 r0-pairs 0 + lcsubstr r0-pairs 1 (via 0x13 at r0
  bytes 4,7 vs r123 byte 9) r123-pairs 7 -- GATE
  LCS-NOTE corroborated EXACT in all 3 senses: "r0
  lcs=0" holds suffix/prefix, substring gives 1
  (b410-class; prose shorthand only, tails 4-distinct
  + TRUE-3B/2B stand, tier stands). QC 67, b0-3
  0f000000, no b4/b5 (QUAD single-sig x64), b27 const
  ff (memo's varpos exclusion corroborated). RM
  16x18ch distinct; RQ 16x16ch distinct; RM-vs-RQ
  UNPAIRED (sets disjoint); RC 69, b0-3 b0/00/00/00,
  b8 const 79, b84-87 e4/6e/4a/40 ring-wide. M==RQ
  lists identical 16/16 (even-band EXACT, no ordinal;
  3rd running P302/P304/P306). Tails STANDARD-SPLIT
  (RM b80-83 by COL, RQ b76-79 by ROW, 16/16 distinct
  each, 0 overlap). Sorted-unique + _N decls 78/70/67/
  69 match actual. Missing-sets EXACT: AC [4,5,20,21,
  22,23,80-83]; CC [4,5,12,13,14,18-22,80-83]; QC [4,5,
  20-26,28-31,80-87]; RC [4,5,18,19,27,28-31,34,35,
  76-83]. Coverage unions exact every block (const U
  tab U {b4,b5} == 88/84/88/88, 0 overlap). Q legs M[m]
  + QR[q] both sides, NO F-legs either region both
  sides. R legs RM[c] + RQ[r] both sides. AC-QC shared-
  pos 67, same-val 39, AConly 11, QConly 0 (== GATE
  both=67 sameval=39; QUAD-sig-EQ-PBA-sig tier, same
  sig different tables). P305 refs re-read: S0
  db1b7900 / S1 80299f81 / PBA 09000000 / C10-1SIG
  80299f81 / QUAD-2SIG (no b0). Next-P306 preds (A-779
  re-read: PB0 db1b7900 EQ-P305PB0sig / PB1 80120ffa
  NEW / PBA88 0f000000 x16 NEW sig 0f / C10-1SIG
  803b4fc4 x10 NOT-PB1-sig) x4 corroborated. PBA NEW
  vs P305 (0f000000 != 09000000). AM/CM/M/QR/RM/RQ
  0-overlap vs P305 (all widths differ: P306 AM16/CM24/
  M16/QR22/RM18/RQ16 vs P305 AM18/CM22/M14/QR24/RM14/
  RQ14; base widths re-read first-hand). M-tails 16/16
  ALL NEW vs P305 M-tail8 + P305 RM-tail8 + P305 RQ-
  tail8 (overlap 0 x3); RM-tails NEW vs P305 RQ row-led
  tails + RQ-tails NEW vs P305 RM col-led tails + cross
  overlaps 0. Memo INCL PBA88 79 / C10 71 / quad88 67 /
  T88 69 (A-782 re-read): impl 78/70/67/69 = memo-1 on
  PBA/C10 (b5-const excluded), identical quad/T88 (b5
  varies/counter) -- standing +1 rule coherent, +1/+1/
  +0/+0. Base temp maxes _t6324/_b3832/_i3833 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 123225 / S1 123226 / A 123227-242 / C 123243-252 /
  Q 123253-316 / R 123317-572): bounds + paylens
  (12x84 + 336x88) + lencode l16=((n<<1)|1)&FFFF A/C/Q
  both sides (b5-const/step emerges from raw lencode) +
  R counter b4=(0x6b+2off)&FF b5=0xc3+(off>=75)+
  (off>=203) (py hex; C staged decimal 107/195,
  re-derived from code text both sides: 107==0x6b,
  195==0xc3) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/rtab byte positions exact (A 8B b20-23,
  80-83; C 12B b12-14,18-22,80-83; Q QM8 b28-31,80-83 +
  R11 b20-26,84-87, NO frags; R TM9 b18,19,27,34,35,
  80-83 by COL + TR8 b28-31,76-79 by ROW) + C guards
  `if ((n) == (123225))` / `(123226)` + 4 range guards
  exact + C byte-index lists match py per block (A 8B,
  C 12B, Q 8B/11B, R 9B/8B). T-mirrors T82539/82544/
  82549/82564/82580/82601 each re-read: hits the exact
  py guard line. Temps _t6325-6340 continuous (base max
  _t6324) + _b3834/3836/3838/3839/3841/3842 (base max
  _b3832) + _i3835/3837/3840/3843 (base max _i3833):
  added-only, no reuse. Insert exact both sides: P305R
  block precedes, at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-782 geometry (values
  re-checked in audit above; NO D dips: ownloop tags
  exactly the 6 P306 blocks).
- Edges own-loop ownloop414.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (303 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. Tail line: CLOSED T10P306R N=123572
  off=255. edges414.py: paylens 12x84 + 336x88;
  lencode 92/92 (S/A/C/Q raw l16; S0/S1 b3/c2, b5/c2
  == raw lencode) + aform 16/16 (A head b7/c2 tail
  d5/c2 b5set {c2} NO step, 0 ff) + cform 10/10 (C
  head d7/c2 tail e9/c2 b5set {c2} NO step, 0 ff) +
  qform 64/64 + qb5step 64/64 (Q head eb/c2, edge
  o10->o11 123263->123264 ff/c2->01/c3, tail 69/c3,
  b5set {c2,c3}, exactly 1 ff in 64 at o10; quad b4
  base 0xeb step2 == raw-lencode 64/64); ring counter
  256/256 + ringraw 256/256 (head 6b/c3; 123391 off74
  ff/c3 -> 123392 off75 01/c4; mid off128 6b/c4 at
  123445; 123519 off202 ff/c4 -> 123520 off203 01/c5;
  tail off255 69/c5; exactly 2 ff in 256 at o74/o202);
  ff total x3 (123263 Q-step + 2 ring). odd-lencode
  92+256=348/348. Ring edges + tail 123572 in for-list
  + 2 PASS lines each py+C. Tail 123572: oracle sha
  8a6b34bb9bcb3bd6... matches PINS (rawlen 104
  re-checked: paylen 88 + 12 + 4); py+C CLOSED
  T10P306R off=255 agree. No DISSENT: cut bytes verify.
- PB-diff secf414.py (cache path) + secf414b.py (DIRECT
  tool, no cache): staged-vs-oracle 0/0/0/0 (123225 +
  122877 + 123226 + 122878); S0: oracle123225-vs-122877
  32/84, codeS0-vs-P305S0 32/84, positions identical;
  DIRECT tool 32/84 with identical agree-pos 52
  positions. S1: oracle123226-vs-122878 58/84,
  codeS1-vs-P305S1 58/84, positions identical; DIRECT
  58/84 identical agree-pos 26 positions. 0 miss
  (ownloop pre-warmed). Triple-derived both pairs.
  S1-vs-own-C10 secf414c.py: 28/84 UNIFORM all 10 C10
  cells ([0] n123243 sig 80120ffa vs 803b4fc4 differs,
  NOT byte-equal -- viewer-measured, GATE claims only
  sig-differs, no conflict). Byte-diff discipline
  observed throughout, nothing to refute.
- C diff pure-add: numstat 604/0 (rgramc.c) + 230/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 599 content + 5 bare-blank / 0 del == GATE;
  raw py 230 content / 0 del. C-tempnorm del-uniq 0
  add-uniq 389 missing 0 == GATE EXACT (recipe stated
  explicitly: rgramc.c scope, _tN/_iN/_bN temp-norm,
  BSD tools, empty-excluding -- no variant gap,
  b408/b410/b412 family). Full-digit norm recorded (no
  GATE claim): C 149/146/148/145 + py 173 x4, del-uniq
  0 missing 0 every variant (integrity intact).
  py-tempnorm 190 recorded.
- Wall on band diff added lines (scope f539e0c8..
  0dd1dddf, 897 added lines == GATE): vendor/disasm 0
  hits, depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0
  hits. Files: rgramc.c 604/0, rgram.py 230/0 purely
  additive, test_rgram.sh 1/1, PINS +62/+0.
- Tiers: merge-msg +6/+62 (efb485e3), code 6 blocks,
  dispatch-exact (4-space) singletons 634->636 +2 /
  ranges 654->658 +4 py + C identical == GATE EXACT,
  CLOSED T10P prints 1724->1730 +6 py + C == GATE
  EXACT, seal 1818->1824 +6 (commit msgs; offset +94
  vs CLOSED-T10P: 1824-1730 = 94, stable): all agree,
  no slip.
- CONFIRM evidence (CONVERT-01 rule b): A-782-q898-P306
  verdict CONFIRM, tallies 25/25 + 15/15 + 14/14 =
  54/54 arith-consistent as-filed + exact-value
  corroboration incl PB0 sig-eq + 32/84 NOT-byte-equal
  FIRST-32, PB1 NEW, PBA88-PLAIN sig-0f M8, C10-1SIG
  NOT-PB1-sig M12, QUAD88-4R + R11 rows + share-14ch +
  r23-TRUE-3B + r1-2B + b5-step o10->11 + M-tails NEW,
  T88-RING-STANDARD + TM9/TR8 + SPLIT tails + b84-87
  e46e4a40 + edges + consts 6b/c3/75/203 + lencode
  348/348 + VPOS 9/13/21/19 (all re-checked above; QC
  b27 == 0xff corroborated, memo's varpos exclusion
  stands). LCS-NOTE (GATE self-disclosed, corroborated
  EXACT all 3 senses -- b410-class, prose shorthand
  only, tier stands). Sheet-vs-tables const-count note:
  Q-898 sheet FIXED-rule 79/71/67/69 memo-exact (3rd
  straight fully clean w2b sheet per memo), committed
  tables 78/70/67/69 still deduct const-b5 in PBA/C10
  -- 9th consecutive tables-lag band (geometry exact,
  PORT verdict stands). No viewer P306 geometry answer
  on file at gate time (memo-only recon; this VERIFY
  is the viewer record). No CONFIRM-P306.md file
  (absence verified); A-782 suffices per rule. Agrees
  with cport commit msg (PYID 9060, RGRAM 18120).
- Quiz: no conflicting CLAIM/GATE/FLAG on b414 (own seat
  CLAIM only; NO-FLAG greps first-hand). GATE cites no
  QNUM (no staleness). PROSE-01: all hex/counts above
  copied from own run output; GATE re-read before filing.

Verdict: PASS. No RED. GATE CORRECT on code + behavior
legs; 1 prose-level note ("r123 share-14B": the shared
prefix 8adb9da333e671 is 14 hex chars = 7 bytes (lcpre 7
first-hand); "B" reads bytes everywhere else in the
round, so the token should be 7B or 14ch -- value itself
corroborated EXACT, unit label loose; code GREEN; 2nd
instance after b412, same sweep2-r66 family token).
Even-band RQ==M instance corroborated as EXACT (M==RQ
lists identical 16/16, no ordinal per even/odd
convention; 3rd running P302/P304/P306; even/odd
convention holds). Next-P307 predictions banked (A-782
re-read: PB0 ab687400 NEW @123573 + PB1 803b4f44 NEW
@123574 + PBA88 05000000 x16 @123575-90 + C10-1SIG
803b4f84 x10 @123591-600 NOT-PB1-sig).
