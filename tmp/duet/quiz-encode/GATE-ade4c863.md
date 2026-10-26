# GATE ade4c863 b362 T10P254 pins 105129..105476 (1512 tiers) PASS-functional

Seat sweep2-r53, first-hand, trees /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r53/w362 @ade4c863.
Band = 451b04ad (py merge w2b@b9794825 partial, +6 tiers, +62 pins)
+ ade4c863 (C port). Base 8627293f (b361 tip, 1506 tiers sealed).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build362/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 868995bc / aae d6e27c97
  (aae d6e27c97 = b288-b354 pinned value + r52/r53 builds;
  band touches no aae sources per numstat).
- RGRAMC-PYID 7432/7432 covered=7432/7432 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir,
  CT_CACHE_DIR set).
- RGRAM py 14864/14864 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 14864/14864 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (cmp 0 diff, 14864/14864).
- PINS-RGRAM cells set-eq 7432/7432 (xor 0, PINS base-N
  set vs for-list; PASS-names vs PINS-names xor 0);
  PINS 14866 rows (2 hdr + 14864 = PASS lines, +62 vs base
  14804). For-list union +31 (105129 105130 105131 105132
  105137 105141 105145 105146 105147 105150 105151 105154
  105155 105156 105157 105159 105160 105172 105173 105188
  105189 105204 105215 105216 105221 105343 105344 105349
  105471 105472 105476), 0 removed, range 105129..105476
  exact. Each for-N yields 2 PASS lines (g-zN-closed +
  g-zN); 31x2 = 62 = 14864-14802.
  The 31 = S0/S1 (2) + A head/mids/tail (6) + C
  head/mids/tail (6) + Q head/frag-pairs/mids/carry-pair
  (10) + ring head/edge-pairs/mid/tail (7).
- SMOKE-GREEN rc=0 (6/6: aar-encode/decode/bytes +
  aea-encrypt/decrypt/bytes PASS, default oracle backend,
  no BACKEND var, NVME workdir).
- Tables audit P254 C-vs-py, script-compared, TABAUDIT-GREEN
  78 PASS 0 FAIL (tabaudit254.py rc=0): S0/S1 168ch
  EXACT sigs e4180300 NEW / 6d4b3306 ==P253C10a (S0 string
  NEW vs P253; S1 == P253 CC b0,b1 + CM head, code-verified),
  AM 16/16 7B distinct, CM 10/10 15B distinct, M 16/16 8B
  distinct, QB47 32/32 1B, QR 4/4 11B, QT 4/4 4B, RM 16/16
  6B distinct, RQ 16/16 9B distinct, AC 75/75, CC 67/67,
  QC 58/58, RC 71/71; C _N decls 75/67/58/71 match actual;
  byte-coverage unions exact every block (84/84/84/88,
  0 overlap, b4/b5 in no const set).
  CM sig-map exact order: 6d4b3306 x4 @105147-50 +
  6d4b1303 x4 @105151-54 + 6d4b3306 x2 @105155-56 (CC
  b0,b1 6d,4b const + CM b2,b3 in tab; 2 distinct sigs,
  10/10 diverge NO pair).
  QB47 dual-coltab EXACT: r0 f2 x3 + f4 x13, r123 f9 x3
  + fa x13 (g=0/16 by q==0, P244-style 2x2-frag staging
  per A-604 invitation).
  QR r2==r3 PAIRED 261a8c74d5b8856f93b4e1 x2, r0
  669a18d8c5b889d7146914 + r1 261a8c14de588a5f53caf9
  distinct; row-led a096b766 (r0) / a096b726 (r123) via
  QC b0-2 + QR b3 EXACT.
  QT values b6a8543e/e95abd76/ef6138db/196238db (4/4
  distinct; r2/r3 share last 2B 38db + 2nd-B 61/62 1B-off
  = A-604 SR 2B staging, code comment agrees).
  AC b0-3 a096b766 ==P253PBA (code-verified vs P253AC
  b0-3); b42 in M-range (NOT in consts).
  RC b0-3 02000000 back-to-02 (P253T sig 06000000 re-read
  first-hand); RC b84-87 655bbd76 ring-wide.
  RM/RQ UNPAIRED, tails SPLIT (RM b80-83 by COL 16/16,
  RQ b76-79 by ROW 16/16; TR9 widest R yet: 9).
  Same-tier RQ rows = 1B head + M row 16/16 (byte positions
  differ: TR9 b51-55 vs QM8 b48-51 - staging, NOT a finding
  per precedent).
  Code-consts vs A-604 INCL (PBA 76 / C10 68 / quad 58 /
  T88 71): impl 75/67 = memo-1 on PBA/C10 (b5 const 35
  both, standing incl/excl bookkeeping - A-604 S3
  explicitly no-finding), 58/71 identical on quad/T88 (b5
  carry / counter vary). M-tails 16/16 ALL NEW vs P253T
  (zero overlap vs BOTH P253RM-tail and P253RQ-tail sets;
  P253 TR8 b25-27,35,80-83 / TM6 b40,41,76-79 order
  re-read first-hand).
- Dispatch eye-verified both sides, 6 blocks in order:
  S0 n=105129 (PB0 sig e4180300 NEW, lenB 84), S1
  n=105130 (fat PB1 sig 6d4b3306 ==P253C10a, lenB 84),
  A 105131-105146 PBA16 (sig a096b766 ==P253PBA via AC
  b0-b3, AM 16/16 distinct 7B, mtab b34,42,43,76-79 b42
  IN range, b5 const 35 raw lencode),
  C 105147-105156 C10-2SIG sandwich (sig map exact order
  above, CM 10/10 distinct 15B diverge 10/10, mtab
  b2,3,34,35,41-47,80-83 sig-b2,b3-in-tab, b5 const 35),
  Q 105157-105220 QUADms row-led (a096b766-r0/a096b726
  -r123, QM8 b48-51,76-79 M 16/16 distinct 8B + b47
  dual-coltab above + R11 b3,14,15,34,35,41-46 pair
  above + QT tails above, b5-carry 35->36 @105215->
  105216 raw lencode),
  R 105221-105476 T88-ring STANDARD (sig 02000000
  back-to-02, TM6 b6,7,80-83 by COL RM 16/16 distinct,
  TR9 b51-55,76-79 by ROW RQ 16/16 distinct UNPAIRED,
  tails SPLIT b80-83 col / b76-79 row, b84-87 const
  655bbd76 ring-wide, b4=(0x0b+2off)&FF,
  b5=0x36+(off>=123)+(off>=251)). C blocks carry
  T69690/69695/69700/69715/69732/69759 py-line mirrors
  (each re-read: hits the exact py guard line), bounds
  + byte positions exact (A 7B, C 15B, Q 8/1/11/4B, R
  6/9B), b47 via snprintf %02lx vs QB47[g+m] (matches py),
  counter 11/54 + (off>=123)+(off>=251), temps _t5380-5399
  (base max _t5379, no reuse) + _b3280-3289/_i3281-3290
  (base max _b3278/_i3279, no reuse), all 6 verified.
  Insert position exact both sides: after T10P253R close,
  at dispatch tail (N-out-of-scope fallthrough follows).
  Matches A-604/A-365 geometry (PB0 NEW / PB1 ==P253C10a,
  PBA16 VPOS 8 b42-IN b5 const 35, C10-2SIG VPOS 16 b5
  const 35 10/10 diverge NO pair, QUAD VPOS 26 row-led +
  2x2-frag dual-coltab + R11 pair + QT 2B-share + M-tails
  NEW, T88 VPOS 17 STANDARD SPLIT + b84-87 655bbd76,
  lencode 348/348 whole-tier, Q-carry 105215->105216,
  ring edges 105343->105344 + 105471->105472 near-tail,
  NO D dips) incl exact values (CM 4/4/2 map, QB47 frag,
  QR pair, QT tails + 2B-share, ring TM6/TR9 16/16
  UNPAIRED, tails SPLIT, consts stand).
- Edges via counter formula first-hand: Q-carry 105215
  (ff/35) -> 105216 (01/36); ring 105343 (off122, ff/36)
  -> 105344 (off123, 01/37); 105471 (off250, ff/37) ->
  105472 (off251, 01/38); all six pins + tail 105476 in
  for-list + 2 PASS lines each py+C. A b5set {35}, C
  b5set {35}, Q b5set {35,36} (single carry). A head
  57/35 tail 75/35, C head 77/35 tail 89/35, Q head
  8b/35 tail 09/36, R head 0b/36 tail 09/38. Ring counter
  == raw lencode 256/256, 0 mismatch. Odd-lencode 348/348.
  No DISSENT: cut bytes verify.
- C diff purely additive: numstat 651 add / 0 del
  (rgramc.c) + 276/0 (rgram.py) + 1/1 (for-line) +
  62/0 (PINS); raw C grep 646 content + 5 blank-only
  `+` lines (verified bare) / 0 del; fine-norm
  (rgramc.c scope, TNP/_tN/_iN/_bN, BSD tools,
  empty-excluding) del-subset-add 0 missing (del-uniq
  0, add-uniq 176).
- Wall on band diff added lines (scope 8627293f..
  ade4c863, 990 added lines): vendor/disasm 0 hits,
  depload (dylib/CDLL/dlopen/ctypes/LoadLibrary/
  System.load) 0 hits, libcompression/compression_tool/
  /usr/bin/aa/nominated/shim/ct-cache 0 hits, shebang 0 hits.
  Files touched: rgramc.c 651/0, rgram.py 276/0 purely
  additive, test_rgram.sh 1/1 (for-line extension),
  PINS +62/+0.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards
  singletons 540->542 +2 / ranges 468->472 +4 = +6
  (stated method, plain `if n ==` / `<= n <=` for BSD
  grep), CLOSED T10P prints 1412->1418 +6, C singletons
  535->537 +2 (C-vs-py 5-offset pre-existing, unchanged),
  C ranges 468->472 +4, seal 1506->1512 +6: all agree,
  no slip (absolute seal inherits lane tally; delta
  verified).
- CONFIRM evidence (CONVERT-01 rule b): A-604-q766-
  t10p254 verdict CONFIRM (shape 12/12 + quad/ring 12/12
  + counters 11/11 as sectioned + SR ruling; verdict line
  reads 36/36 + SR as-filed; file present, counts
  verified; exact-value corroboration incl CM 4/4/2 map,
  QB47 frag, QR pair, QT tails + 2B-share, row-led pair,
  M-tails NEW, ring edges + consts re-checked above) +
  A-365 viewer corroboration (all 3 legs CONFIRM; its S2
  "r2/r3 last-3B" line contradicts its own cited values
  ef6138db/196238db - 61 vs 62 in 3rd-last byte - while
  A-604 SR rules 2B + 1B-off from the same values; SR
  governs, code stages 2B; memo-side prose only, no code
  impact, no DISSENT). No CONFIRM-P254.md file; A-604
  suffices per rule. Agrees with cport commit msg (PYID
  7432, RGRAM 14864).
- Quiz: no conflicting CLAIM/GATE/FLAG on b362. Newest
  PARENT-* is QNUM-13 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing (all hex/
  counts copied from run output above).
- Logs: NVME ws tmp/encode-sweep2/r53/ (build362.log,
  pyid362.log, rgram362py/c.log, cmp362.py/.c,
  for362-old/-new.nums, pins362.basen, smoke362.log,
  tables362.log, tabaudit254.py, edges254.py,
  edges362.log, numstat362.txt, added362.txt,
  add/delnorm362.txt, banddiff362.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
