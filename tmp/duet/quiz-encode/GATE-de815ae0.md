# GATE de815ae0 b302 T10P194 pins 84249..84596 (1105 tiers) PASS-functional

Seat sweep2-r37, first-hand, WT tmp/wt-encode-sweep2 @de815ae0,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r37.
Band = 32965b6e (py merge w2b@54c436f9 partial, +7 tiers +54 pins)
+ de815ae0 (C port). Base 55308f7c (b301 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build302/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 99d0585b / aae d6e27c97
  (aae identical to b288-b300 builds: aae.c untouched).
- RGRAMC-PYID 5712/5712 covered=5712/5712 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11424/11424 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11424/11424 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11424/11424).
- PINS-RGRAM cells set-eq 5712/5712 (diff 0, PINS base-N
  set vs for-list); PINS 11426 rows (2 hdr + 11424 =
  PASS lines). For-list union +27 (84249 84250 84251
  84258 84266 84267 84268 84272 84276 84277 84284
  84292 84293 84300 84308 84309 84316 84324 84325
  84332 84340 84341 84351 84352 84479 84480 84596),
  0 removed (`; do` stripped before tokenize). Each for-N
  yields 2 PASS lines (g-zN-closed + g-zN).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P194 C-vs-py, script-compared, all EXACT:
  S0/S1/S2 1/1, AM 16/16, BM 9/9, AC 74/74, BC 71/71,
  OM 16/16, OR 4/4, OT 4/4, OC 61/61, RM 16/16,
  RQ 16/16, RC 65/65; C _N decls 74/71/61/65 match
  actual. M/QR/QT/QC absent BOTH sides (no Q tier in
  P194: 7 tiers = PB0+PB1+PBA16+SING+PBB9+4xOWN16+
  T-ring per A-416; tabc.py QC_N probe N/A, rc=1 on
  that probe only; tabc194.py covers O/R tables rc=0).
- Dispatch eye-verified both sides, 7 tiers in order:
  S0 n=84249 (PB0 sig 48030000 NEW), S1 n=84250
  (fat PB1 sig 20900600 NEW), A 84251-84266 PBA16
  (sig 0a026900 NEW, mtab b20-23,76-79, b5 const 92,
  raw lencode), S2 n=84267 (SING sig 6fcd0700 NEW),
  B 84268-84276 PBB9 (sig 10480300 NEW, 11B mtab
  b20-26,80-83, b5 const 92, raw lencode), O
  84277-84340 4xOWN16 own-sig rows (2db13500/
  0f193500/6f8d3400/a59b3600, SHARED mtab
  b20-22,26-28,76-79 + row-tuple r7 b0-2,18,19,24,
  25/tails b80-83, raw lencode), R 84341-84596
  T-ring TRANSPOSED sig 6f8d4803 (M8 b32-35,76-79
  by COL off&15, Q9 b24-28,72-75 by ROW off>>4,
  b4=(0xeb+2off)&FF, b5=0x92+(off>=11)+(off>=139)).
  C blocks carry T53655/660/665/680/685/701/725
  py-line mirrors. Insert position exact both sides:
  after T10P193R close, at dispatch tail (N-out-of-
  scope fallthrough follows). Matches A-416 geometry
  (NO quad; VPOS A [4,20-23,76-79] / B b4+M11
  b20-26,80-83 / O [4,20,21,22,26,27,28,76-79] /
  R 19, sigs, lencode 92/92, const-diffs 9/11/11B,
  M-tails 64/64, T-ring edges 84351->84352 +
  84479->84480 ff->01, DET27 27 cells).
- C diff renumber-only + new: numstat 2089 add / 1469 del;
  raw grep 2082 add / 1469 del (7 blank-only `+` lines,
  verified); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1466, add-uniq
  1848).
- Wall on band diff added lines (scope 55308f7c..de815ae0,
  2379 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py (+242/+0 purely
  additive), test_rgram.sh (for-line 1/1), PINS (+54/+0).
- CONFIRM evidence (CONVERT-01 rule b): A-416-q425-t10p194
  verdict CONFIRM (58/58 checks; file present, counts
  verified; A-264 corroborates). No CONFIRM-P194.md
  file; A-416 suffices per rule. Agrees with cport
  commit msg (PYID 5712, RGRAM 11424).
- Quiz: no conflicting CLAIM/GATE/FLAG on b302. No new
  PARENT-* (newest PROSE-01, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r37/ (build302.log,
  build302.sha, pyid302, rgram302py/c, cmp302.py/.c,
  for302-old/new, pins302.csv/.cells, seteq302, smoke302,
  tables302.log, tables302b.log, tabc.py, tabc194.py,
  cdiff302, cdiff302.del/.add, del/addnorm302,
  cdiff302.miss, banddiff302, added302).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
