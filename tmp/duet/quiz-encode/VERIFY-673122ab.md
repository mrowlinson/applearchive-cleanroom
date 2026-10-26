# VERIFY-673122ab b381 T10P273 pins 111741..112088 (1626 tiers) PASS

Seat viewer-r53 (recovery), first-hand, tree-673122ab @673122ab,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r53.
Base 9709b26d (b380, 1620 tiers). Band = a11d1919 (py merge
w2b@49b89c84 partial, +6 tiers, +62 pins) + 673122ab (C port,
1626 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build381/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 0a586acd / aae d6e27c97
  (== GATE both) + sha1 rgramc 8e39fa10 / aae 7d8dd3a2
  (aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8027/8027 covered=8027/8027 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16054/16054 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16054/16054 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16054/16054 sorted).
- PINS 16056 rows (2 hdr + 16054, +62 vs base 15994);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0 (pass + pins). For-list delta vs base +31/-0:
  111741 111742 111743 111744 111745 111748 111753 111758
  111759 111760 111763 111764 111765 111766 111767 111768
  111769 111784 111785 111800 111801 111816 111817 111832
  111833 111871 111872 111976 111999 112000 112088
  (== GATE verbatim; S2 + A6 offs 0,1,2,5,10,15 + C8 offs
  0,1,4,5,6,7,8,9 (offs 2,3 unsampled) + Q8 offs
  0,15/16,31/32,47/48,63 + R7 offs 0,38/39,143,166/167,
  255; 7996->8027); 31x2=62 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit381.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 102 PASS
  0 FAIL. Inventory exactly the 13 both sides (STANDARD
  ring, no RT; no BM/BC, no M19, no M42/X42, no QB/PT/
  FM). S0/S1 168ch sigs f22a0700 NEW f2-variant /
  25bd5c0e (S1-sig REPEAT of P272S1 sig; both NEW
  strings vs P272 f62a0700/25bd5c0e re-read). AM 16x8B
  distinct; AC b0-3 c0935ff8 PLAIN, b0 const c0. CM
  10x13B diverge 10/10; 5SIG heads 5c0e x5 rows 0-4 +
  bc0c/ec0a/3c0b/cc0b/cc0b ORDERED rows 5-9; CC b0,b1
  = 25,bd -> sigs 25bd5c0e x5 / 25bdbc0c / 25bdec0a /
  25bd3c0b / 25bdcc0b x2 == A-661 C10 map. M 16x8B
  distinct. QR r1==r2==r3 LAST3-PAIRED c65dbe71ff5f90
  x3 (last3 ff5f90), r0 c1a44d51e1d77d distinct
  (last3 e1d77d), 2 distinct; b3-led (r0 head c1 vs
  r123 head c6). QT ae2d1859/53bca1aa/1d7423ac/
  427423ac 4/4 distinct; r2/r3 share TRUE 3B 7423ac
  (first bytes 1d/42 differ); all other pairs share 0
  bytes (hexchar-lcs 1 all 5). QC b0-2 = 5d,d2,cb
  (QUAD2s prefix; b3 from QR gives 5dd2cbc1/5dd2cbc6
  row-split). RM 16x7B distinct; RQ 16x8B distinct.
  AC/CC/QC/RC 74/69/63/71 py-vs-C; _N decls 74/69/63/
  71 match actual; sorted-unique. RC b0-3 0d000000;
  RC b84-87 27/7b/fb/46 ring-wide. Missing-sets EXACT:
  AC [4,5,48,49,50,51,76,77,78,79]; CC [2,3,4,5,35,
  46,47,48,49,50,51,80,81,82,83]; QC [3,4,5,6,7,8,9,
  46,47,48,49,50,51,76,77,78,79,80,81,82,83]; RC
  [4,5,6,7,9,10,11,12,13,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U
  {b4,b5} == 84/84/84/88, 0 overlap). Tails SPLIT (RM
  b80-83 col / RQ b76-79 row, 16/16 distinct each, 0
  overlap UNPAIRED; full-row sets disjoint). RQ==M
  HEAD2+TAILS FIRST (bytes 0,1 + tails bytes 4-7
  identical 16/16 same-index + tails set-eq; mid bytes
  2,3 own: no cross-row-const xor/add/sub formula
  0/48 own denominator of (byte,mbyte,op) triples --
  GATE counts 0/1536 per-row candidates, same
  conclusion). Q legs M+R7+T4 only, no frags.
  Section-F leg 1 (table-recon): S1-vs-P272PB1 48/84
  at b4,5,21-24,26-55,72-83 EXACT. M-tails 16/16 ALL
  NEW vs P272T (zero overlap vs BOTH P272RM-tail8 and
  P272RQ-tail8); M-full ALL NEW vs P272RQ; QT ALL NEW
  vs P272QT (d5b4b22a/44398e25/69398e25/43399225
  re-read); RM ALL NEW vs P272RM. Base temp maxes
  _t5753/_b3488/_i3489 (no reuse). Memo INCL PBA 74 /
  C10 70 / quad 64 / T88 71 (A-661 re-read): impl
  74/69/63/71 = memo-1 on C10/quad (b5-const
  excluded), identical PBA/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 111741 / S1 111742 / A 111743-758 / C 111759-768 /
  Q 111769-832 / R 111833-112088): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q) + R counter b4=(179+2off)&FF b5=105+
  (off>=39)+(off>=167) both sides (179/105 = 0xb3/0x69)
  + m=off&15/q=off>>4/c=off&15/r=off>>4 both sides +
  mtab/qtab/ttab byte positions exact (A 8B b48-51,
  76-79; C 13B b2,3,35,46-51,80-83; Q 8/7/4B; R 7/8B)
  + NO frag leg (M+R7+T4 only). T-mirrors T74638/
  74643/74648/74663/74679/74702 each re-read: hits the
  exact py guard line. Temps _t5754-5771 continuous
  (base max _t5753, no reuse) + _b3490/3492/3494/3495/
  3496/3498/3499 (base max _b3488) + _i3491/3493/3497/
  3500 (base max _i3489, no reuse). C guards `if ((n)
  == (111741))` / `(111742)` + 4 ranges exact. Insert
  exact both sides: after T10P272R close, N-out-of-
  scope follows. Writer staged comments already record
  S1 NOT byte-equal 48/84 (py + C mirror). Matches
  A-661/A-337 geometry (values re-checked in audit
  above; NO D dips).
- Edges own-loop ownloop381.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (317 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges381.py: paylens 92 x84 + 256 x88;
  lencode 92/92 (A head ff/68 edge 01/69 tail 1d/69
  b5set {68,69} CARRY first-cell 111743->111744; C
  head 1f/69 tail 31/69 b5set {69} NO carry; Q head
  33/69 tail b1/69 b5set {69} const; S0/S1 fb/68 +
  fd/68 match raw lencode); ring counter 256/256
  (head b3/69; 111871 (off38, ff/69) -> 111872 (off39,
  01/6a); 111999 (off166, ff/6a) -> 112000 (off167,
  01/6b); mid off143 (111976) d1/6a; tail 112088
  (off255) b1/6b); counter==raw-lencode 256/256;
  odd-b4 348/348. Edge pins (carry pair + ring pairs)
  + tail 112088 in for-list + 2 PASS lines each py+C.
  Tail 112088: oracle sha 31ce19e7802c756b... matches
  PINS. No DISSENT: cut bytes verify.
- Section-F re-derived THRICE (secf381.py): leg-1
  table-recon 48/84 positions exact + leg-2 oracle-
  direct 48/84 same positions + leg-3 staged==oracle
  byte-exact both pins (111742 + 111394, hit/hit).
  A-661 section-F CONFIRMED; A-337 leg-1 PB1 byte-
  equal wording refuted (record corrected at source).
- C diff pure-add: numstat 610/0 (rgramc.c) + 237/0
  (rgram.py) + 1/1 (for-line) + 62/0 (PINS) == GATE;
  raw C 605 content + 5 bare-blank / 0 del; raw py 237
  content / 0 del. Fine-norm sweep (keep-empty,
  [0-9]+ -> N, sign/';' strip, python sets): C
  del-uniq 0 add-uniq 173, py del-uniq 0 add-uniq 195,
  0 missing EXACT (== GATE).
- Wall on band diff added lines (scope 9709b26d..
  673122ab, 910 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression//usr/bin/aa/shim 0
  hits, shebang 0 hits. Files: rgramc.c 610/0,
  rgram.py 237/0 purely additive, test_rgram.sh 1/1,
  PINS +62/+0.
- Tiers: merge-msg +6/+62, code 6 blocks, tier-comments
  1526->1532 +6, singletons 578->580 +2 / ranges
  544->548 +4 (stated method, plain `if n ==` /
  `<= n <=` BSD grep), CLOSED T10P prints 1526->1532
  +6, C singletons 573->575 +2 (5-count C-vs-py offset
  pre-existing, unchanged) + C ranges 544->548 +4,
  seal 1620->1626 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-661-q785-
  t10p273 verdict CONFIRM 39/40 + section-F as-filed
  (section heads 12/13 + 12/12 + 13/13 = 37/38;
  +2/+2 = section-F's two verified sub-claims:
  sig-match + 48/84-differ; file re-read; exact-value
  corroboration incl PBA/C10-map sigs, QUAD2s + R7
  last3-pair + QT tails, M-tails NEW, ring split +
  edges + consts re-checked above) + A-337 viewer
  corroboration (all 3 legs CONFIRM, consts 74/70/64/
  71 INCL; leg-1 PB1 byte-equal wording refuted by
  section-F thrice-derivation, record corrected at
  source). Agrees with cport commit msg (PYID 8027,
  RGRAM 16054).
- Quiz: no conflicting CLAIM/GATE/FLAG on b381. Newest
  PARENT-* is QNUM-19 (w2d Q-block refill, read, no
  gate impact) -- GATE cites QNUM-18: 1 immaterial
  staleness. PROSE-01: all hex/counts above copied from
  own run output.
- Own near-miss caught pre-filing (script fixed, code
  never impugned): tabaudit381 first compared S1 vs
  OWN-staged C10 (b380 pattern, 21-25 diffs); b381's
  claim is cross-tier (S1 vs P272PB1) -- fixed to
  cross-tier, 48/84 positions exact.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-18 vs -19).
