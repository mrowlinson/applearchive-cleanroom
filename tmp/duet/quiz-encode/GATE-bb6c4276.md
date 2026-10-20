# GATE bb6c4276 b308 T10P200 pins 86337..86684 (1164 tiers) PASS-functional

Seat sweep2-r39, first-hand, WT tmp/wt-encode-sweep2 @bb6c4276,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r39.
Band = 9b7f0228 (py merge w2b@983bc261 partial, +14 tiers +68 pins)
+ bb6c4276 (C port). Base 49329853 (b307 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build308/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 121de84d / aae d6e27c97
  (aae identical to b288-b306 builds: aae.c untouched).
- RGRAMC-PYID 5894/5894 covered=5894/5894 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11788/11788 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11788/11788 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11788/11788).
- PINS-RGRAM cells set-eq 5894/5894 (diff 0, PINS base-N
  set vs for-list); PINS 11790 rows (2 hdr + 11788 =
  PASS lines). For-list union +34 (86337 86338 86339
  86346 86354 86355 86356 86357 86358 86359 86360
  86361 86362 86363 86364 86365 86372 86380 86381
  86388 86396 86397 86399 86400 86412 86413 86420
  86428 86429 86527 86528 86655 86656 86684),
  0 removed (`; do` stripped before tokenize).
  Each for-N yields 2 PASS lines (g-zN-closed + g-zN).
  The 34 ARE the DET34 set (flips 86400/86528/86656 +
  ring edges 86527/86528 + 86655/86656 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P200 C-vs-py, script-compared, all EXACT:
  S0/S1/S2/S3/S4/S5/S6/S7/S8/S9 1/1, AM 16/16, BM 2/2,
  M 16/16, QR 4/4, QT 4/4, AC 75/75, BC 72/72,
  QC 64/64, RM 16/16, RQ 16/16, RC 69/69; C _N decls
  75/72/64/69 match actual (tabc.py rc=0 full Q-band;
  tabc200.py covers S3-S9/RM/RQ/RC rc=0). Code-consts
  75/72/64/69 match A-436 exactly.
- Dispatch eye-verified both sides, 14 tiers in order:
  S0 n=86337 (PB0 sig 74030000 BREAKS chain), S1
  n=86338 (fat PB1 sig 51de0500), A 86339-86354 PBA16
  (sig 51de6d00 NEW, mtab b32-34,76-79, b5 const, raw
  lencode), B 86355-86356 PBB2 (sig 51de0500 ==PB1,
  mtab b22,23,30,36-38,80-83, b5 const, raw lencode),
  8 SINGLES 86357-86364 sigs in exact order 83260300/
  97bb0300/5f950300/7f7f0300/832e0300/97bb0300/
  7f7f0300/832e0300 (all 84B, 5 distinct, ALL NEW),
  Q 86365-86428 QUAD64 single-sig 51de3500 NEW
  bottom-paired r2==r3 (mtab b36-38,76-79 + sigr7
  b22,23,30-34 / tails b80-83 all-distinct, raw
  lencode, b5-carry @off35: 86399 ff/a2 -> 86400
  01/a3), R 86429-86684 T-ring TRANSPOSED (10th)
  sig 51de9103 NEW (M6 b42,43,76-79 by COL off&15,
  Q7 b36-38,72-75 by ROW off>>4, b4=(0x3b+2off)&FF,
  b5=0xa3+(off>=99)+(off>=227)). C blocks carry
  T55371/376/381/396/412/417/422/427/432/437/442/
  447/452/475 py-line mirrors. Insert position exact
  both sides: after T10P199R close, at dispatch tail
  (N-out-of-scope fallthrough follows). Matches A-436
  geometry (VPOS A b4+M7 / B b4+M10 / Q 20 / R 15,
  sigs, lencode 92/92, M7 row-indep 16/16x4 shared,
  R7 bottom-paired r2==r3, tails 4/4 no-sharing,
  M-tails ALL NEW vs P199T, T-ring edges
  86527->86528 + 86655->86656 ff->01, flips
  {86400,86528,86656}, DET34 34 cells).
- C diff renumber-only + new: numstat 2233 add / 1522 del;
  raw grep 2219 add / 1522 del (14 blank-only `+` lines,
  verified; 0 blank `-`); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1518, add-uniq
  1926). Same pipeline as b304/b306 (b302-validated).
- Wall on band diff added lines (scope 49329853..bb6c4276,
  2565 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c 2233/1522, rgram.py +277/+0
  purely additive, test_rgram.sh 1/1, PINS +68/+0.
- CONFIRM evidence (CONVERT-01 rule b): A-436-q432-t10p200
  verdict CONFIRM (40/40 checks; file present, counts
  verified; A-270 corroborates incl-consts). No
  CONFIRM-P200.md file; A-436 suffices per rule. Agrees
  with cport commit msg (PYID 5894, RGRAM 11788).
- Quiz: no conflicting CLAIM/GATE/FLAG on b308. Newest
  PARENT-* is QNUM-03 (w2b Q-block only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep2/r39/ (build308.log,
  pyid308, rgram308py/c, cmp308.py/.c, for308-49329853/
  bb6c4276, for308-added, pins308.csv/.cells, seteq308,
  smoke308, tables308.log, tables308b.log, tabc.py,
  tabc200.py, cdiff308, cdiff308.del/.add, del/addnorm308,
  cdiff308.miss, banddiff308, added308, numstat308).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
