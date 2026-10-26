# VERIFY-e62c1418 b382 T10P274 pins 112089..112436 (1632 tiers) PASS

Seat viewer-r53 (recovery), first-hand, tree-e62c1418 @e62c1418,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r53.
Base 673122ab (b381, 1626 tiers). Band = bb610c20 (py merge
w2b@2a31358e partial, +6 tiers, +64 pins) + e62c1418 (C port,
1632 sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build382/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc b52844c8 / aae d6e27c97
  (== GATE both) + sha1 rgramc ce8f9754 / aae 7d8dd3a2
  (aae pinned, band touches no aae sources per numstat).
- RGRAMC-PYID 8059/8059 covered=8059/8059 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME
  workdir, CT_CACHE_DIR set).
- RGRAM py 16118/16118 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR).
- RGRAM C 16118/16118 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal (cmp 0
  diff, 16118/16118 sorted).
- PINS 16120 rows (2 hdr + 16118, +64 vs base 16056);
  PASS-names vs PINS-names xor 0 py+C; base-N vs for-list
  xor 0 (pass + pins). For-list delta vs base +32/-0:
  112089 112090 112091 112092 112096 112101 112105 112106
  112107 112108 112111 112112 112113 112114 112115 112116
  112117 112127 112128 112132 112133 112149 112165 112180
  112181 112190 112191 112255 112256 112383 112384 112436
  (== GATE verbatim; S2 + A6 + C8 + Q8 + R8; 8027->8059);
  32x2=64 rows.
- SMOKE-GREEN rc=0 (6/6, NVME workdir, default backend).
- Tables audit own script tabaudit382.py (parses tree
  sources, C-vs-py + derived): TABAUDIT-GREEN 99 PASS
  0 FAIL. Inventory exactly the 13 both sides (SPLIT-b0
  ring, no RT; no BM/BC, no M19, no M42/X42, no QB/PT/
  FM). S0/S1 168ch sigs b2690700 NEW / 1e65d30e NEW
  (both NEW strings, sigs NEW vs P273 f22a0700/25bd5c0e
  re-read). AM 16x8B distinct; AC b0-3 e09effe0 PLAIN,
  b0 const e0, no b5. CM 10x15B diverge 10/10; 5SIG
  prefixes 2557da0e x5 rows 0-4 + a53dd90e / a5eb6b07 /
  adcd6607 / 7541d50e x2 ORDERED rows 5-9 == A-670 map;
  map heads disjoint from S0/S1 sigs; CC b0-3 all in
  tab (full sig in tab), no b5. M 16x6B distinct. QR
  r1==r2==r3 LAST3-PAIRED e986627793551a x3 (last3
  93551a), r0 5ad7e27b73e712 distinct (last3 73e712),
  2 distinct. QT 30f07a3b/13f4bcdf/38f4bcdf/5df4bcdf
  4/4 distinct; r1/r2/r3 share TRUE 3B f4bcdf (first
  bytes 13/38/5d differ); r0 last3 f07a3b, 0 bytes
  shared vs each of r1/r2/r3 (GATE "(0f07a3b)" reads as
  0-shared + r0-tail-f07a3b, confirmed). QC b0-3
  809907fc (QUAD1s x64); b44 const d1; no b5. RM
  16x10B distinct; RQ 16x6B distinct. AC/CC/QC/RC
  74/67/65/69 py-vs-C; _N decls 74/67/65/69 match
  actual; sorted-unique. RC b0 ABSENT (split); RC b123
  zero; RC b84-87 c2/29/ac/4d ring-wide. Missing-sets
  EXACT: AC [4,5,12,13,14,19,76,77,78,79]; CC [0,1,2,3,
  4,5,11,18,19,20,21,22,23,80,81,82,83]; QC [4,5,13,14,
  18,19,20,21,22,24,25,76,77,78,79,80,81,82,83]; RC [0,
  4,5,11,18,19,27,28,29,34,35,76,77,78,79,80,81,82,83].
  Coverage unions exact every block (const U tab U
  {b4,b5} == 84/84/84, RC + {b0} == 88 via split
  guard, 0 overlap). Tails SPLIT (RM b80-83 col / RQ
  b76-79 row, 16/16 distinct each, 0 overlap UNPAIRED;
  full-row sets disjoint). Q legs M+R7+T4 only, no
  frags. M-tails 16/16 ALL NEW vs P273 (zero overlap
  vs BOTH P273RM-tail8 and P273RQ-tail8); AM/CM
  0-overlap vs P273AM/CM (CM 30ch vs 26ch widths).
  Base temp maxes _t5771/_b3499/_i3500 (no reuse).
  Memo INCL PBA 75 / C10 68 / quad 65 / T88 69 (A-670
  re-read): impl 74/67/65/69 = memo-1 on PBA/C10
  (b5-const excluded), identical quad/T88.
- Dispatch eye-verified both sides, 6 blocks in order
  (S0 112089 / S1 112090 / A 112091-106 / C 112107-116 /
  Q 112117-180 / R 112181-436): bounds + paylens (92
  x84 / 256 x88) + lencode l16=((n<<1)|1)&FFFF both
  sides (S/A/C/Q) + R counter b4=(107+2off)&FF b5=108+
  (off>=75)+(off>=203) both sides (107/108 = 0x6b/0x6c)
  + b0 split guard `0x0E iff col<10 else 0x0F` both
  sides (C: ((c<10)?14:15)) + m=off&15/q=off>>4/
  c=off&15/r=off>>4 both sides + mtab/qtab/ttab byte
  positions exact (A 8B b12-14,19,76-79; C 15B
  b0-3,11,18-23,80-83 b0-3 first; Q 6/7/4B; R 10/6B)
  + NO frag leg (M+R7+T4 only). T-mirrors T74875/
  74880/74885/74900/74917/74940 each re-read: hits the
  exact py guard line. Temps _t5772-5789 continuous
  (base max _t5771, no reuse) + _b3501/3503/3505/3506/
  3507/3509/3510 (base max _b3499) + _i3502/3504/3508/
  3511 (base max _i3500, no reuse). C guards `if ((n)
  == (112089))` / `(112090)` + 4 ranges exact. Insert
  exact both sides: after T10P273R close, N-out-of-
  scope follows. Matches A-670/A-338 geometry (values
  re-checked in audit above; NO D dips).
- Edges own-loop ownloop382.py over ALL 348 tier Ns
  (oracle bytes via tool-identical -encode -a lzraven
  through ct-cache; seat rgramc each): 348/348 CLOSED
  rc=0 (316 miss-warmed). Census R256/Q64/A16/C10/S0/
  S1 exact. edges382.py: paylens 92 x84 + 256 x88;
  lencode 92/92 + qform 64/64 (A head b7/6b tail d5/6b
  b5set {6b} NO carry; C head d7/6b tail e9/6b b5set
  {6b} NO carry; Q head eb/6b tail 69/6c, b4=(0xeb+
  2off)&FF b5=0x6b+(off>=11) 64/64, edge 112127 (o10,
  ff/6b) -> 112128 (o11, 01/6c) mid-row0; S0/S1 b3/6b
  + b5/6b match raw lencode); ring counter 256/256
  (head 6b/6c; 112255 (off74, ff/6c) -> 112256 (off75,
  01/6d); 112383 (off202, ff/6d) -> 112384 (off203,
  01/6e); tail 112436 (off255) 69/6e); b0 oracle
  histogram 0e:160 + 0f:96 EXACT (split-pair 112190
  off9 col9 0e / 112191 off10 col10 0f); counter==
  raw-lencode 256/256; odd-b4 348/348. Q-edge +
  split-pair + ring edges + tail 112436 in for-list +
  2 PASS lines each py+C; tail in PINS. No DISSENT:
  cut bytes verify.
- C diff pure-add: numstat 612/0 (rgramc.c) + 241/0
  (rgram.py) + 1/1 (for-line) + 64/0 (PINS) == GATE;
  raw C 607 content + 5 bare-blank (verified bare, no
  whitespace) / 0 del; raw py 241 content / 0 del.
  Fine-norm (rgramc.c scope, _tN/_iN/_bN temp-norm,
  empty-excluding): del-uniq 0 add-uniq 400 missing 0
  EXACT (== GATE).
- Wall on band diff added lines (scope 673122ab..
  e62c1418, 918 added lines): vendor/disasm 0 hits,
  depload 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang
  0 hits. Files: rgramc.c 612/0, rgram.py 241/0 purely
  additive, test_rgram.sh 1/1, PINS +64/+0.
- Tiers: merge-msg +6/+64, code 6 blocks, tier-comments
  1532->1538 +6, singletons 580->582 +2 / ranges
  548->552 +4 (stated method, plain `if n ==` /
  `<= n <=` BSD grep), CLOSED T10P prints 1532->1538
  +6, C singletons 575->577 +2 + C ranges 548->552 +4,
  seal 1626->1632 +6 (commit msgs): all agree, no slip
  (absolute seal inherits lane tally; delta verified).
- CONFIRM evidence (CONVERT-01 rule b): A-670-q786-
  t10p274 verdict CONFIRM 39/39 + TBD-resolved
  (section heads 12/12 + 14/14 + 13/13 = 39/39 sums
  exact; file re-read; exact-value corroboration incl
  PBA/C10-map sigs, QUAD1s + R7 last3-pair + QT tails,
  M-tails NEW, ring split + edges + consts re-checked
  above) + A-338 viewer corroboration (all 3 legs
  CONFIRM, consts 75/68/65/69 INCL). No DISSENT on
  P274. Agrees with cport commit msg (PYID 8059, RGRAM
  16118).
- Quiz: no conflicting CLAIM/GATE/FLAG on b382. Newest
  PARENT-* is QNUM-19 (w2d Q-block refill, read, no
  gate impact) -- GATE cites QNUM-18: 1 immaterial
  staleness. PROSE-01: all hex/counts above copied from
  own run output.

Verdict: PASS. No RED. GATE CORRECT on code + prose (1
immaterial QNUM staleness, QNUM-18 vs -19).
