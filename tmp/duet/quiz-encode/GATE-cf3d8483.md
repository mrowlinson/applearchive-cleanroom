# GATE cf3d8483 b298 T10P190 pins 82857..82948 (1068 tiers) PASS-functional

Seat sweep2-r36, first-hand, WT tmp/wt-encode-sweep2 @cf3d8483,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r36.
Band = c58e23a6 (py merge w2b@c34ee645 partial, +6 tiers +32 pins)
+ cf3d8483 (C port). Base c557266f (b297 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build298/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 9b5ae83e / aae d6e27c97
  (aae identical to b288-b296 builds: aae.c untouched).
- RGRAMC-PYID 5614/5614 covered=5614/5614 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11228/11228 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11228/11228 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11228/11228).
- PINS-RGRAM cells set-eq 5614/5614 (diff 0, PINS base-N
  set vs for-list); PINS 11230 rows (2 hdr + 11228 =
  PASS lines). For-list union +16 (82857 82858 82859
  82866 82875 82876 82880 82884 82885 82900 82901
  82917 82933 82943 82944 82948), 0 removed
  (`; do` stripped before tokenize). Each for-N yields
  2 PASS lines (g-zN-closed + g-zN).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P190 C-vs-py, all 11 EXACT (script-compared):
  S0/S1/S2 singletons 1/1 each, AM 16/16, AC 74/74,
  BM 9/9, BC 70/70, M 16/16, QR 4/4, QT 4/4, QC 63/63.
  C _N decls 74/70/63 match actual.
- Dispatch eye-verified both sides, 6 tiers in order:
  S0 n=82857 (sig 1e030000 REPEAT P189), S1 n=82858
  (fat PB1, sig 614e0700 == P189 SING sig), A
  82859-82874 (sig 614e7300 NEW, mtab b34,35,42,43,
  76-79, b5 const 87, raw lencode), S2 n=82875
  (SING echoes PB1 614e0700), B 82876-82884 PBB9
  (sig 37070300 NEW, 12B mtab b34,35,41-46,80-83,
  b5 const 87, raw lencode), Q 82885-82948
  single-sig quad 614e3300 rows0==2, M 7B
  b48-50,76-79, sigR 8B b34,35,41-46, T 4B b80-83
  (raw lencode). C blocks carry T52686/691/696/711/
  716/732 py-line mirrors. Insert position exact both
  sides: after T10R187 close, before T10R188 (n<=83204,
  base 82949). Matches A-407 geometry (VPOS A
  [4,34,35,42,43,76-79] / B [4,34,35,41-46,80-83],
  sigs, lencode 92/92, flip [82944] Q3-internal,
  b5 tier-set {0x87,0x88}).
- C diff renumber-only + new: raw grep 1481 del / 1942
  add (numstat identical, no blank-only lines);
  normalized (_t/_i/_b/T numbers) del-subset-add
  0 missing (del-uniq 1469, add-uniq 1763).
- Wall on band diff added lines (scope c557266f..cf3d8483,
  2148 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py (+173/+0 purely
  additive), test_rgram.sh (for-line 1/1), PINS (+32/+0).
- CONFIRM evidence (CONVERT-01 rule b): A-407-q421p190
  verdict CONFIRM (32/32 checks; file present, counts
  verified). No CONFIRM-P190.md file; A-407 suffices
  per rule. Agrees with cport commit msg (PYID 5614,
  RGRAM 11228).
- Quiz: no conflicting CLAIM/GATE/FLAG on b298. No new
  PARENT-* (newest PROSE-01, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r36/ (build298.log,
  build298.sha, pyid298, rgram298py/c, cmp298.py/.c,
  for298-old/new, pins298.csv/.cells/.uniq, pass298.cells,
  seteq298, smoke298, tables298.log, tabc.py, cdiff298,
  cdiff298.del/.add, del/addnorm298, cdiff298.miss,
  banddiff298, added298).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
