# GATE 13c46dc8 b312 T10P204 pins 87729..88076 (1196 tiers) PASS-functional

Seat sweep2-r40, first-hand, WT tmp/wt-encode-sweep2 @13c46dc8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r40.
Band = 4b8ca051 (py merge w2b@706ed5a4 partial, +8 tiers +52 pins)
+ 13c46dc8 (C port). Base bf0ee03b (b311 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build312/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc b894500c / aae d6e27c97
  (aae identical to b288-b310 builds: aae.c untouched).
- RGRAMC-PYID 6004/6004 covered=6004/6004 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 12008/12008 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, ct-cache).
- RGRAM C 12008/12008 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, NVME workdir); C-py PASS-set cmp-equal
  (diff 0 lines, 12008/12008).
- PINS-RGRAM cells set-eq 6004/6004 (diff 0, PINS base-N
  set vs for-list); PINS 12010 rows (2 hdr + 12008 =
  PASS lines). For-list union +26 (87729 87730 87731
  87738 87746 87747 87748 87749 87750 87753 87756
  87757 87772 87773 87788 87789 87804 87807 87808
  87820 87821 87935 87936 88063 88064 88076),
  0 removed (`; do` stripped before tokenize). Each for-N
  yields 2 PASS lines (g-zN-closed + g-zN). The 26 ARE
  the DET26 set (ring edges 87935/87936 + 88063/88064,
  quad b5-carry @87808 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P204 C-vs-py, script-compared, all EXACT:
  S0/S1/S2 1/1, AM 16/16, BM 9/9, M 16/16, QR 4/4,
  QT 4/4, RM 16/16, RQ 16/16, AC 76/76, BC 72/72,
  QC 65/65, RC 68/68; C _N decls 76/72/65/68 match
  actual (tabc204.py rc=0). Code-consts vs A-274
  (PBA 77 / PBB 73 / quad 65 / T 68): quad+T exact;
  A/B -1 each is bookkeeping (b5 checked via lencode
  formula, not const pairs); byte-coverage proven
  84/84 both tiers (lencode + mtab + consts, 0 overlap).
- Dispatch eye-verified both sides, 8 tiers in order:
  S0 n=87729 (PB0 sig 3c070000 NEW chain), S1 n=87730
  (fat PB1 sig 95020d00), A 87731-87746 PBA16 (sig
  5629d000 NEW, mtab b6,7,76-79, b5 const, raw lencode),
  B 87747-87748 PBB pre-gap 2x (sig ab290f00 joint,
  mtab b6,7,48-51,80-83, b5 const, raw lencode),
  S2 n=87749 (SING gap sig de940700 NEW), B2 87750-87756
  PBB post-gap 7x (sig ab290f00 joint, off+2, same mtab),
  Q 87757-87820 QUAD64 4x16 (sig 3e9af200, M7 b9-11,76-79
  shared + R6 b6,7,48-51/tails b80-83, b5-carry @off51),
  R 87821-88076 T-ring TRANSPOSED (14th) + TAILS-SWAPPED
  (5th) sig 1ea3290f NEW (M7 b16-18,72-75 by COL off&15,
  Q7 b9-11,76-79 by ROW off>>4, b4=(0x1b+2off)&FF,
  b5=0xae+(off>=115)+(off>=243)). C blocks carry
  T56469/474/479/494/510/515/531/554 py-line mirrors,
  all 8 verified exact. Insert position exact both sides:
  after T10P203R close, at dispatch tail (N-out-of-scope
  fallthrough follows). Matches A-454 geometry (PB0/PB1
  sigs, PBA16, PBB split 2+7 + SING gap, QUAD64 b5 carry
  off51, ring TRANSPOSED+TAILS-SWAPPED, lencode 92/92,
  ring edges 87935->87936 ff/ae->01/af + 88063->88064
  ff/af->01/b0) and A-274 (VPOS A 7 / B 11 / quad 19 /
  ring 16, M-tails ALL NEW vs P203T).
- C diff renumber-only + new: numstat 2219 add / 1561 del;
  raw grep 2219 add / 1561 del (8 blank-only `+` lines,
  verified bare; 0 blank `-`); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1557, add-uniq
  1931). Same pipeline as b304-b310 (b302-validated).
- Wall on band diff added lines (scope bf0ee03b..13c46dc8,
  2530 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c 2219/1561, rgram.py +258/+0
  purely additive, test_rgram.sh 1/1, PINS +52/+0.
- CONFIRM evidence (CONVERT-01 rule b): A-454-q436-t10p204
  verdict CONFIRM (28/28 = 13 shape + 9 quad/ring +
  6 counters; file present, counts verified; A-274
  corroborates incl-consts with -1 bookkeeping resolved).
  No CONFIRM-P204.md file; A-454 suffices per rule. Agrees
  with cport commit msg (PYID 6004, RGRAM 12008).
- Quiz: no conflicting CLAIM/GATE/FLAG on b312. Newest
  PARENT-* is QNUM-04 (w2f Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r40/ (build312.log,
  pyid312, rgram312py/c, cmp312.py/.c, for312-bf0ee03b/
  13c46dc8, for312-added, pins312.csv/.cells/.basen, seteq312,
  smoke312, tables312.log, tabc204.py, cdiff312,
  cdiff312.del/.add, del/addnorm312, cdiff312.miss,
  banddiff312, added312, numstat312).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
