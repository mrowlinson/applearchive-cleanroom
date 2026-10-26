# VERIFY-e3caa64f b386 T10P278 pins 113481..113828 (1656 tiers) PASS

Seat viewer-r54, first-hand, tree-e3caa64f @e3caa64f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r54.
Base a33e4c8f (b385, 1650 tiers). Band = ccdc6b7b (py merge
w2b@ba53806f partial, +6 tiers, +64 pins) + e3caa64f (C port,
1656 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build386/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 1875a2a6 / aae d6e27c97
  (== GATE both) + sha1 rgramc 7fd5d647 / aae 7d8dd3a2
  (aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8185/8185 covered=8185/8185 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16370/16370 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16370/16370 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16370/16370 sorted).
- PINS 16372 rows (2 hdr + 16370, +64 vs base 16308);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0. For-list delta vs base +32/-0:
  113481 113482 113483 113484 113488 113493 113497 113498
  113499 113500 113502 113505 113507 113508 113509 113524
  113525 113535 113536 113540 113541 113556 113557 113572
  113573 113663 113664 113675 113691 113791 113792 113828
  (== GATE verbatim; S2 + A6 + C6 + Q10 + R8; 8153->8185);
  32x2=64 rows, range 113481..113828 exact.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit386.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 111 PASS
  0 FAIL. Inventory exactly the 14 both sides (RT present
  = ROWTAIL TT tab; no BM/BC, no M19, no QB/PT/FM, no
  M42/X42, no R8/X8). S0/S1 168ch sigs b0aa0700 NEW /
  f5f4570f (sig == P277C10sig; full-string NEW vs BOTH
  P277S0/S1). AM 16x16ch distinct; AC b0-3 e09a1ffa HELD
  (== P277PBA re-read), b0 const e0, no b5. CM 10x26ch
  diverge 10/10; CC b0-3 f5f4570f HELD (== P277C10
  re-read) + == PB1 sig intra-tier, no b5. M 16x12ch
  distinct. QR r0 a551220fd42f94 distinct (last3 d42f94),
  r1==r2==r3 333104ef5407a6 LAST3-PAIRED (last3 5407a6),
  2 distinct. QT 18e71aa7/1eef163c/8eae4f3c/b3ae4f3c 4/4
  distinct; r2/r3 share TRUE 3B ae4f3c (first bytes 8e/b3
  differ); r0/r1 do not. QC b47 const 96, no b5 (b5 step
  o>=27 computed). RM 16x16ch distinct; RQ 16x4ch 15/16
  PAIRED (r6==r7 f1d5, tails disambiguate: RT[6]!=RT[7]);
  RT 16x8ch distinct. AC/CC/QC/RC 74/69/65/72 py-vs-C;
  _N decls 74/69/65/72 match actual; sorted-unique. RC
  b0-3 0f000000 NEW; RC b84-87 7f/5f/c2/17 ring-wide NEW.
  Coverage unions exact every block (const U tab U {b4,b5}
  == 84/84/84/88, 0 overlap). Q legs M + R7 + T4, no
  frags. R legs RM[c] + RQ[r] + RT[r] ROW-led (4th rowtail
  T88). M-tails 16/16 ALL NEW vs P277 (zero overlap vs
  BOTH P277RM-tail8 and P277RQ-tail8 re-read). AM/CM
  0-overlap vs P277AM/CM (CM 26ch vs 24ch widths). P277
  sigs re-read b6aa0700/d505540f/e09a1ffa/f5f4570f (==
  A-682/A-341 predicted); P277RC 08000000 + 2783811e.
  A-682/A-341 P278 predictions corroborated x4 (b0aa0700/
  f5f4570f/e09a1ffa/f5f4570f == staged). Memo INCL PBA 75
  / C10 70 / quad 65 / T88 72 (A-683 re-read): impl
  74/69/65/72 = memo-1 on PBA/C10 (b5-const excluded),
  identical quad/T88. Base temp maxes _t5849/_b3544/_i3545
  (no reuse).
- PB1-repeat section re-derived first-hand (secf386.py,
  twice-derived): leg-1 staged-S1 vs own-C10 oracle cells
  47x8 + 46x2 EXACT (113499-506: 47; 113507-508: 46) ==
  GATE, NOT byte-repeat; leg-2 oracle PB1 (n113482) vs
  oracle n113151: 56/84 DIFFER, 28 agree @ b0-3,6-21,
  44-51 EXACT (cache path); leg-2b DIRECT-tool re-run
  (fresh oracle, no cache reads): 56/84 differ, agree
  positions IDENTICAL; leg-3 staged==oracle n113482: 0
  diff (sanity). AC-QC shared-pos 65 / same-val 34 EXACT
  == GATE, NOT const-repeat. A-683 (56/84) CONFIRMED;
  A-342 leg-1 "(byte-equal to n113151 first-hand)" wording
  REFUTED (record corrected at source: 56 differ/28 agree
  per positions above).
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 113481 / S1 113482 / A 113483-498 / C 113499-508 /
  Q 113509-572 / R 113573-828): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C) + Q b5 step o>=27 + R counter b4=
  (0x4b+2off)&FF b5=0x77+(off>=91)+(off>=219) (75/119 =
  0x4b/0x77) + m=off&15/q=off>>4/c=off&15/r=off>>4 both
  sides + mtab/qtab/ttab byte positions exact (A 8B
  b34,35,42,43,76-79; C 13B b34,35,41-47,80-83; Q 6/7/4B
  QM6 b48,49,76-79 + R7 b34,35,42-46 (b47 const 96) + T4
  b80-83; R 8B TM8 b6,7,12,13,76-79 by COL + 2B TR2 b52,
  53 by ROW + 4B TT b80-83 ROW-led by r) + NO frag leg
  in Q. T-mirrors T75913/75918/75923/75938/75954/75977
  each re-read: hits the exact py guard line. Temps
  _t5850-5869 continuous (base max _t5849, no reuse) +
  _b3546/3548/3550/3551/3552/3554/3555/3556 (base max
  _b3544) + _i3547/3549/3553/3557 (base max _i3545, no
  reuse). C guards `if ((n) == (113481))` / `(113482)` +
  4 ranges exact. Insert exact both sides: after T10P277R
  close (py 75911 / C 203041), N-out-of-scope follows (py
  75998 / C 203249). Matches A-683/A-342 geometry (values
  re-checked in audit above; NO D dips).
- Edges own-loop ownloop386.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (312 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges386.py: paylens 92 x84 + 256 x88;
  lencode 92/92 + qform 64/64 (A head 97/76 tail b5/76
  b5set {76} NO carry; C head b7/76 tail c9/76 b5set {76}
  NO carry; Q head cb/76, b4=(0xcb+2off)&FF b5=0x76+
  (off>=27) 64/64, step 113535 (o26, ff/76) -> 113536
  (o27, 01/77) mid-row1 + tail 49/77 (113572); Q b5set
  {76,77}; S0/S1 93/76 + 95/76 match raw lencode); ring
  counter 256/256 (head 4b/77; 113663 (off90, ff/77) ->
  113664 (off91, 01/78); 113791 (off218, ff/78) ->
  113792 (off219, 01/79); mids off102 (113675) 17/78 +
  off118 (113691) 37/78; tail 113828 (off255) 49/79);
  counter==raw-lencode 256/256; odd-b4 348/348. Q-step +
  ring edges + tail 113828 in for-list + 2 PASS lines
  each py+C. Tail 113828: oracle sha 8c1ae02e2f02bdaa...
  matches PINS. No DISSENT: cut bytes verify.
- C diff pure-add: numstat 636/0 (rgramc.c) + 257/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 631 content + 5 bare-blank / 0 del; raw py 257
  content / 0 del. Fine-norm (rgramc.c scope, temp-norm,
  empty-excluding): del-uniq 0 add-uniq 430 missing 0
  EXACT (== GATE; empty-including would be 431 -- b386
  GATE number matches the excluding recipe, unlike b384's
  441).
- Wall on band diff added lines (scope a33e4c8f..
  e3caa64f, 958 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 636/0,
  rgram.py 257/0 purely additive, test_rgram.sh 1/1,
  PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, singletons
  588->590 +2 / ranges 564->568 +4 (stated method, plain
  `if n ==` / `<= n <=` BSD grep), CLOSED T10P prints
  1556->1562 +6, C ranges 564->568 +4 + C CLOSED 1556->
  1562 +6 (deltas agree both sides), seal 1650->1656 +6
  (commit msgs): all agree, no slip (absolute seal
  inherits lane tally; delta verified). Methodology note:
  GATE "C absolute 588->590" reproduces EXACT under its
  stated loose pattern `(n) == (` (includes 5 pre-existing
  inline-ternary hits, verified present in base too);
  strict guard pattern `if ((n) == ` gives 583->585 +2
  (5-count C-vs-py offset persists). Deltas +2 agree
  under both -- NO slip.
- CONFIRM evidence (CONVERT-01 rule b): A-683-q790-
  t10p278 verdict CONFIRM 39/39 as-filed (section heads
  13/13 + 14/14 + 12/12 = 39/39 sums exact; file re-read;
  exact-value corroboration incl PBA/C10 sigs, PB1-vs-
  n113151 56/84 payload diff re-derived first-hand exact,
  QUAD1s + R7 last3-pair + QT tails + b5 step, M-tails
  NEW, ring ROWTAIL + TR2 15/16 + edges + consts re-checked
  above) + A-342 viewer corroboration (2 of 3 legs CONFIRM
  clean; leg-1 PB1 byte-equal wording REFUTED by twice-
  derivation above, record corrected at source; consts
  75/70/65/72 INCL stand). Agrees with cport commit msg
  (PYID 8185, RGRAM 16370).
- Quiz: no conflicting CLAIM/GATE/FLAG on b386. GATE cites
  QNUM-19 (current): no staleness. PROSE-01: all hex/counts
  above copied from own run output.
- Own near-misses caught pre-filing (scripts fixed, code
  never impugned): secf386 first run hit cache-miss on
  unwarmed C cell (added tool-miss path, 4 warmed);
  ownloop386 sed-carried sample-N list (replaced with P278
  Ns pre-run).

Verdict: PASS. No RED. GATE CORRECT on code + prose (0
slips). A-342 leg-1 byte-equal wording refuted first-hand,
corrected in this record.
