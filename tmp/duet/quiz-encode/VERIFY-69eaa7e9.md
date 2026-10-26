# VERIFY-69eaa7e9 b387 T10P279 pins 113829..114176 (1662 tiers) PASS

Seat viewer-r54, first-hand, tree-69eaa7e9 @69eaa7e9,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r54.
Base e3caa64f (b386, 1656 tiers). Band = bff93d36 (py merge
w2b@3e774788 partial, +6 tiers, +66 pins) + 69eaa7e9 (C port,
1662 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build387/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha1 rgramc f785d34b / aae 7d8dd3a2
  + sha256 rgramc 7d76c33d / aae d6e27c97 (== GATE all 4;
  aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8218/8218 covered=8218/8218 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16436/16436 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16436/16436 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16436/16436 sorted).
- PINS 16438 rows (2 hdr + 16436, +66 vs base 16372);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +33/-0:
  113829 113830 113831 113832 113841 113842 113843 113844
  113845 113846 113847 113848 113850 113853 113855 113856
  113857 113864 113872 113873 113888 113889 113904 113905
  113919 113920 113921 113985 114047 114048 114112 114175
  114176
  (== GATE verbatim; S2 + A8 offs 0,1,10,11,12,13,14,15
  (SPLIT-dense: x12 tail pair + full x4 part) + C6 offs
  0,1,3,6,8,9 (offs 2,4,5,7 unsampled) + Q10 offs 0,7,
  15/16,31/32,47/48,62/63 + R7 offs 0,64,126/127,191,
  254/255; 8185->8218); 33x2=66 rows, range 113829..
  114176 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit387.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 113 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT/TT; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8). S0/S1 168ch sigs b8aa0700 NEW /
  74b05c0f NEW (both NEW strings: 32/84 + 75/84 differ vs
  P278; S0 diff @ b0,4,5,30-32,34-41,44-49,56-59,76-83
  EXACT). AM 16x16ch distinct; AM b0 ORDERED c6 x12 (offs
  0-11) + c8 x4 (offs 12-15); AC b1-3 05/cb/f5 -> sigs
  c605cbf5 x12 @113831-42 + c805cbf5 x4 @113843-46
  (no AC b0 const -- split covered by mtab). CM 10x22ch
  diverge 10/10 1SIG (rows 0-5 share 7B head ecbc91fba167
  87 + distinct 4B tails 56aa120f/76aa120f/b34f130f/
  37c9801d/76c9801d/96c9801d; rows 6-9 all-distinct); CC
  b0-3 5eb05c0f 1SIG x10. M 16x14ch distinct. QR r0
  a09b0ff6f9d44c distinct (last3 f9d44c), r1==r2==r3
  00928ff4c51894 LAST3-PAIRED (last3 c51894), 2 distinct;
  sig-led (r0 head a09b0ff6 = row0 sig, r123 head 00928ff4
  = rows1-3 sig). QT 9aa19575/7f90f0d4/a490f0d4/c990f0d4
  4/4 distinct; r1/r2/r3 share last 3B 90f0d4 (first bytes
  7f/a4/c9 differ); r0 last-2B 9575 distinct. RM 16x16ch
  distinct; RQ 16x12ch 16/16 UNPAIRED distinct. AC/CC/QC/
  RC 74/71/64/72 py-vs-C; _N decls 74/71/64/72 match
  actual; sorted-unique. RC b0-3 0f000000; RC b84-87 75/
  da/a8/0b ring-wide. Missing-sets EXACT: AC [0,4,5,9,10,
  11,76,77,78,79]; CC [4,5,13,14,15,16,17,18,19,80,81,82,
  83]; QC [0,1,2,3,4,5,12,13,16,17,18,19,76,77,78,79,80,
  81,82,83]; RC [4,5,20,21,28,29,30,31,76,77,78,79,80,81,
  82,83]. Coverage unions exact every block (const U tab U
  {b4,b5} == 84/84/84/88, 0 overlap; AC tab incl split-b0).
  Q legs M + R7 + T4, no frags. R legs RM[c] + RQ[r]
  STANDARD. RQ==M HEAD1+SHIFT FIRST (M 7B vs RQ 6B: byte1
  identical 16/16 + RQ[2:6]==M[3:7] 16/16, same-index agree
  vector [0,16,0,0,0,0] EXACT; RQ[0] own 16 distinct 6c/73/
  04/15/64/94/be/4f/52/70/9c/c0/02/12/88/e3, no cross-row-
  const xor/add/sub formula over any M byte -- GATE counts
  0/5376 per-row candidates, same conclusion; methodology
  note, 11th RQ==M instance). Tails SPLIT (RM b80-83 col /
  RQ b76-79 row, 16/16 distinct each, 0 overlap UNPAIRED;
  full-row sets disjoint). M-tails 16/16 ALL NEW vs P278T
  col-0; QT 4/4 ALL NEW vs P278QT; RM ALL NEW vs P278RM.
  P278 sigs re-read b0aa0700/f5f4570f/e09a1ffa/f5f4570f
  (== A-683/A-342 predicted; PB1 == P277C10sig as
  predicted). A-683/A-342 P279 predictions corroborated x4
  (b8aa0700/74b05c0f/c605cbf5+c805cbf5/5eb05c0f == staged).
  Memo INCL PBA 75 / C10 72 / quad 64 / T88 72 (A-690
  re-read): impl 74/71/64/72 = memo-1 on PBA/C10 (b5-const
  excluded), identical quad/T88. Base temp maxes _t5869/
  _b3556/_i3557 (no reuse).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 113829 / S1 113830 / A 113831-846 / C 113847-856 /
  Q 113857-920 / R 113921-176): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C; b5-consts emerge from raw lencode) + Q
  raw lencode with b5 step off>=63 LAST-CELL + R counter
  b4=(0x03+2off)&FF b5=0x7a+(off>=127)+(off>=255) (3/122
  = 0x03/0x7a, C stages decimal) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/qtab/ttab byte
  positions exact (A 8B b0,9-11,76-79 covers split; C 11B
  b13-19,80-83; Q 7/7/4B QM7 b12,13,19,76-79 + sig-led R7
  b0-3,16-18 + T4 b80-83; R 8B TM8 b28-31,80-83 by COL +
  6B TR6 b20,21,76-79 by ROW) + NO frag leg in Q.
  T-mirrors T76152/76157/76162/76177/76193/76216 each
  re-read: hits the exact py guard line. Temps _t5870-5887
  continuous (base max _t5869, no reuse) + _b3558/3560/
  3562/3563/3564/3566/3567 (base max _b3556) + _i3559/
  3561/3565/3568 (base max _i3557, no reuse). C guards
  `if ((n) == (113829))` / `(113830)` + 4 ranges exact.
  Insert exact both sides: after T10P278R close (py 76150
  / C 203658), N-out-of-scope follows (py 76235 / C
  203859; C has 2 scope hits, rfind-used). Matches A-690/
  A-343 geometry (values re-checked in audit above; NO D
  dips).
- Edges own-loop ownloop387.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (315 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges387.py: paylens 92 x84 + 256 x88;
  lencode 92/92 + qform 64/64 (A head 4f/79 tail 6d/79
  b5set {79} NO carry; C head 6f/79 tail 81/79 b5set {79}
  NO carry; Q head 83/79, b4=(0x83+2off)&FF b5=0x79+
  (off>=63) 64/64, step 113919 (o62, ff/79) -> 113920
  (o63, 01/7a) LAST-CELL + tail 01/7a (113920); Q b5set
  {79,7a}; S0/S1 4b/79 + 4d/79 match raw lencode); ring
  counter 256/256 (head 03/7a; off64 (113985) 83/7a;
  114047 (off126, ff/7a) -> 114048 (off127, 01/7b); mid
  off191 (114112) 81/7b; LAST 114175 (off254, ff/7b) ->
  114176 (off255, 01/7c)); counter==raw-lencode 256/256;
  odd-b4 348/348. Q-step + ring edges + tail 114176 in
  for-list + 2 PASS lines each py+C. Tail 114176: oracle
  sha 12d03ff936fda249... matches PINS. No DISSENT: cut
  bytes verify.
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 66/0 (PINS) == GATE;
  raw C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Fine-norm sweep (keep-empty, [0-9]+
  -> N, sign/';' strip, python sets): C del-uniq 0
  add-uniq 171, py del-uniq 0 add-uniq 192, 0 missing
  EXACT (== GATE).
- Wall on band diff added lines (scope e3caa64f..
  69eaa7e9, 914 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 610/0,
  rgram.py 237/0 purely additive, test_rgram.sh 1/1,
  PINS +66/+0.
- Tiers: merge-msg +6/+66, code 6 blocks, tier-comments
  1562->1568 +6, singletons 590->592 +2 / ranges
  568->572 +4 (stated method, plain `if n ==` /
  `<= n <=` BSD grep), CLOSED T10P prints 1562->1568
  +6, C singletons 585->587 +2 (5-count C-vs-py offset
  pre-existing, unchanged) + C ranges 568->572 +4,
  seal 1656->1662 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-690-q791-
  t10p279 verdict CONFIRM 37/37 as-filed (section heads
  12/12 + 13/13 + 12/12 = 37/37 sums exact; file re-read;
  exact-value corroboration incl PBA-SPLIT/C10 sigs,
  QUAD2s row-split + sig-led R7 last3-pair + QT tails,
  M-tails NEW, ring STANDARD + UNPAIRED TR6 + edges +
  consts re-checked above) + A-343 viewer corroboration
  (all 3 legs CONFIRM, consts 75/72/64/72 INCL). Agrees
  with cport commit msg (PYID 8218, RGRAM 16436).
- Quiz: no conflicting CLAIM/GATE/FLAG on b387. Newest
  PARENT-* is QNUM-19 (w2d Q-block refill, read, no
  gate impact) -- GATE cites QNUM-18: 1 immaterial
  staleness (standing pattern). PROSE-01: all hex/counts
  above copied from own run output.
- Own near-miss caught on re-read (fixed same-turn,
  code never impugned): Wall bullet first typed rgram.py
  257/0 (b386 carryover) vs correct 237/0 per numstat.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-18 vs -19).
