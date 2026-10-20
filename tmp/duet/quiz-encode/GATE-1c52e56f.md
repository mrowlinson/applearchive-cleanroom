# GATE 1c52e56f b329 T10P221 pins 93645..93992 (348 pins) PASS-functional

Seat sweep-r43, first-hand, WT tmp/wt-encode-sweep @1c52e56f,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r43.
Band = 053c7aa8 (py merge w2b@fe907444 partial, +6 tiers
+52 pins) + 1c52e56f (C port). Base 655f5077 (b328 C tip,
EVEN, diff-base only).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile
  (BUILDDIR seat-private), build329/{aae,rgramc}, rc=0,
  0 warnings. aae sha 7d8dd3a2 (shasum SHA-1 first8;
  stable r39-r43).
- RGRAMC-PYID 6446/6446 covered=6446/6446 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 12892/12892 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 12892/12892 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (12892/12892).
- PINS-RGRAM cells set-eq 12892/12892 (cmp-equal).
  PINS base-N vs for-list 6446/6446 exact.
- PINS 12894 rows (2 hdr + 12892, +52 vs base 12842). py diff
  +52/-0 (pure P221 addition). For-list union +26 (93645
  93646 93647 93654 93662 93663 93667 93672 93673 93681
  93688 93689 93695 93696 93704 93705 93720 93721 93729
  93736 93737 93823 93824 93951 93952 93992), 0 removed.
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P221 C-vs-py, 13-table, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs 16120000 / 3a072300);
  AM 16/16, BM 10/10, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16 EXACT;
  AC 74/74, BC 69/69, QC 61/61,
  RC 62/62 EXACT (py-hex vs C-decimal
  normalized);
  C _N decls 74/69/61/62 match actual;
  no _T10P221PT/PC/CM/CC/FM/FC/FS/FO/H/TC* symbols either
  side (novel A/B/Q/T geometry — classic single-sig B,
  NO PAIR/C8/FRAG, grep-verified inventory).
  Excl-b4/b5 accounting in-table (no b4/b5 entry in
  any of the 4 const tables) = memo code 75/70/61/62
  exact (A/B/Q/T); memo also verified incl from own
  bed (+b5-where-const: A +1 const-db, B +1 const-db
  first-hand, Q +0 carry, T +0) — resolved in-table
  per sweep2-r37 P192 precedent, NOT a FAIL. Q 61 =
  memo 61 (b5-carry in-table, 93695->93696 edge);
  T 62: 84-62=22=VPOS (b4,b5+M9+R11 partition
  first-hand from RC table, A-291 partition
  exact).
  VPOS partitions first-hand EXACT all 4 (AC-10 /
  BC-15 / QC-23 / RC-22 missing-sets).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + 4 tiers): P2210 n==93645 / P2211 n==93646
  singleton-const (offs 0/1);
  P221A 93647..93662 off=n-93647;
  P221B 93663..93672 off=n-93663;
  P221Q 93673..93736 off=n-93673 m=off&15 q=off>>4;
  P221R(T-ring) 93737..93992 off=n-93737 c=off&15
  r=off>>4;
  all paylen 84; A/B/Q raw lencode
  l16=((n<<1)|1)&0xFFFF pay4=l16&0xFF pay5=l16>>8;
  T shared full-ring counter b4=(0x53+2off)&FF
  b5=0xdc+(off>=87)+(off>=215); mtab bytes A:b24-27,
  76-79 (8B), B:b20,21,25-31,80-83 (13B),
  Q:M b32-37,76-79 (10B) + QR b24-30 (7B)
  + QT b80-83, T:RM b32,33,37-39,72-75 (9B) by COL +
  RQ b14,15,21-23,31,36,76-79 (11B) by ROW;
  const sigs A:3a074302 B:3a822100
  Q:3a824102 T:a083873c both sides
  (const-table b0-3).
  C blocks carry T61143/148/153/168/184/208 py-line
  mirrors (exact); C byte-index lists match py per
  block; insert position exact (dispatch
  tail, N out-of-scope follows).
  Counter edges computed first-hand (never trusted
  from comments): A/B b5 const db across;
  Q b5-carry db->dc @93695 ff/db -> 93696 01/dc;
  T off86 ff/dc -> off87 01/dd (93823->93824) +
  off214 ff/dd -> off215 01/de (93951->93952).
  Matches A-494/A-291 geometry (PBA VPOS b4+M8,
  PBB10 single-sig VPOS 14 b4+M13 EXACT, NO
  PAIR/C8/FRAG, QUAD64 M10 shared 16/16 x3 +
  R7 r1==r2==r3 TRIPLE-PAIRED 0efc035f14b58e
  2/4 distinct (r0 1b3cc472f458bb) + tails 4/4
  distinct r2/r3 share b64ea3 (64b64ea3/93b64ea3),
  T-ring ROLE-SWAP4 M9 by COL + R11 by ROW
  UNPAIRED 16/16 distinct, M-tails ALL NEW 0/16,
  NO D dips).
- C diff pure-add: raw 0 del / 606 add (incl 5
  blank-plus, 0 blank-minus); normalized ([0-9]+ -> N,
  cut-c2 strip, sort -u) del-subset-add 0 missing
  (del-uniq 0, add-uniq 173).
- Wall on band diff added lines (scope 655f5077..1c52e56f,
  897 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)
  0 hits, CT-shim/shebang 0 hits, /usr/bin/aa 0 hits.
  Files touched: rgramc.c, rgram.py, test_rgram.sh
  (for-line), PINS.
- CONFIRM evidence (CONVERT-01 rule b): A-494-q613
  T10P221 predictive reproduces 28/28 (shape 14/14 +
  quad+Tring 10/10 + counters 4/4 CONFIRM) + A-291
  corroborates same tier (shape + quad/triple + tails
  + T-ring + edges CONFIRM, incl consts 75/70/61/62,
  NO D dips). Agrees with cport commit msg (py/C
  12892, PYID 6446).
- Quiz: no conflicting CLAIM/GATE/FLAG on b329/1c52e56f.
  b328 EVEN = sweep2 turf (GATE-655f5077 filed by
  sweep2-r44), used as diff-base only, NOT gated.
- Logs: NVME ws tmp/encode-sweep/r43/ (*329* files:
  build329.log, pyid329, rgram329py/c, pass329py/c,
  cells329-battery, pins328base/pins329-cells/-nums,
  for329-old/-new.nums, smoke329.log, tables329.log,
  tabaudit329.py, sigcheck329.py/.log, cdiff329.txt/-del-norm/
  -add-norm/-missing, banddiff329.txt, added329.txt).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
