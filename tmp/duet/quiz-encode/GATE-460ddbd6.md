# GATE 460ddbd6 b290 T10P182 pins 80073..80164 (1020 tiers) PASS-functional

Seat sweep2-r34, first-hand, WT tmp/wt-encode-sweep2 @460ddbd6,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r34.
Band = 30e7818e (py merge w2b@a34684aa partial, +6 tiers +32 pins)
+ 460ddbd6 (C port). Base e300bc17 (b289 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build290/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc 684bb707 / aae d6e27c97
  (aae identical to b288 build: aae.c untouched).
- RGRAMC-PYID 5486/5486 covered=5486/5486 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10972/10972 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10972/10972 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10972/10972).
- PINS-RGRAM cells set-eq 5486/5486 (diff 0, PINS base-N
  set vs for-list); PINS 10974 rows (2 hdr + 10972 =
  PASS lines). For-list union +16 (80073 80074 80075
  80082 80090 80091 80092 80096 80100 80101 80117
  80127 80128 80133 80149 80164), 0 removed
  (`; do` stripped before tokenize).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P182 C-vs-py, all 11 EXACT (script-compared):
  S0/S1/S2 singletons 1/1 each, AM 16/16, AC 74/74,
  BM 9/9, BC 70/70, M 16/16, QR 4/4, QT 4/4, QC 62/62.
- Dispatch eye-verified both sides, 6 tiers in order:
  S0 n=80073 (sig ce020000 NEW), S1 n=80074 (274f0400),
  A 80075-80090 (sig 274f4c00 NEW, mtab 8B
  b34/b35/b42/b43/b76-79, raw lencode b4/b5),
  S2 n=80091 (sig-echoes-PB1), B 80092-80100
  (sig bf5b0200 OWN-SIG, mtab 12B b34/b35/b41-46/
  b80-83, raw lencode), Q 80101-80164 (single-sig
  quad rows0==2, M 8B b48-51/b76-79, R 8B
  b34/b35/b41-46, T 4B b80-83, raw lencode incl
  b5 step @80128). Insert position exact both sides:
  after T10R179 close, before T10R180 (n<=80420,
  base 80165). Matches A-388 geometry (VPOS, sigs,
  lencode 92/92, flip [80128]).
- C diff renumber-only + new: raw 1628 del / 2089 add;
  normalized (_t/_i/_b/T numbers) del-subset-add 0 missing
  (del-uniq 1495, add-uniq 1779).
- Wall on band diff added lines (scope e300bc17..460ddbd6,
  2295 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py (+173/+0), test_rgram.sh
  (for-line 1/1), PINS (+32/+0). Py side purely additive.
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-P182.md
  PASS 28/28 + A-388-q379p182 verdict CONFIRM 28/28
  (file present, counts verified). Agrees with cport
  commit msg (PYID 5486, RGRAM 10972).
- Quiz: no conflicting CLAIM/GATE/FLAG on b290. No new
  PARENT-* (newest QNUM-02, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r34/ (build290.log,
  build290.sha, pyid290, rgram290py/c, cmp290.py/.c,
  cmp290, for290-old/new, pins290.cells, seteq290,
  smoke290, tables290.log, dispatch290.c, cdiff290,
  del/addnorm290, cdiff290.miss, banddiff290, added290,
  wall290, depload290).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
