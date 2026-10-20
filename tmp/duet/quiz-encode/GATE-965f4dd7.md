# GATE 965f4dd7 b288 T10R189 LAST R n<=83552 (1008 tiers) PASS-functional

Seat sweep2-r34, first-hand, WT tmp/wt-encode-sweep2 @965f4dd7,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r34.
Band = da37154a (py merge w2@9f51c59e partial, +2 tiers +24 pins)
+ 965f4dd7 (C port). Base 85522530 (b287 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build288/bin/{aae,rgramc} (BUILDDIR= override;
  Makefile default OUTDIR is shared NVME build/aae), rc=0,
  0 warnings. sha256 rgramc 3099b88d / aae d6e27c97.
- RGRAMC-PYID 5454/5454 covered=5454/5454 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 10908/10908 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 10908/10908 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 10908/10908).
- PINS-RGRAM cells set-eq 5454/5454 (diff 0, PINS base-N
  set vs for-list); PINS 10910 rows (2 hdr + 10908 =
  PASS lines). For-list union +12 (83297 83298 83327
  83328 83361 83425 83455 83456 83489 83537 83551
  83552), 0 removed (`; do` stripped before tokenize).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit R189 C-vs-py: M 16/16, Q 16/16, C 67/67 EXACT
  (script-compared). b45 const line verified by eye
  ({45,60}=0x3c both sides).
- Dispatch eye-verified both sides: ceiling 83552, base 83297,
  paylen 84, b4 0xc3+2off, b5 0x8a+(off>=31)+(off>=159),
  M-tab 8B b11/b19/b26/b27/b76-79 (CLASSIC m->b76-79,
  heads drifted per A-417), Q-tab 7B
  b20/b21/b22/b72-75 (R189Q own-copy, matches A-417).
- C diff renumber-only + new: raw 1378 del / 1537 add
  (1536 non-blank + 1 blank);
  normalized (_t/_i/_b/T numbers) del-subset-add 0 missing
  (del-uniq 1375, add-uniq 1523 non-blank).
- Wall on band diff added lines (scope 85522530..965f4dd7,
  1632 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py (+70/+0), test_rgram.sh
  (for-line 1/1), PINS (+24/+0). Py side purely additive.
- CONFIRM evidence (CONVERT-01 rule a+b): CONFIRM-R189.md
  PASS 16/16 + A-417-q401 CONFIRM 16/16 + 16/16 (file
  present, counts verified). Agrees with cport commit msg
  (PYID 5454, RGRAM 10908).
- Quiz: no conflicting CLAIM/GATE/FLAG on b288. (GATE-965f4dd.md
  is a stale writer2-R35 object sharing 7 hex chars, different
  full sha; this file uses 8 chars.) No new PARENT-*
  (newest QNUM-02, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r34/ (build288.log,
  build288-seat.log, build288.sha, pyid288, rgram288py/c,
  cmp288.py/.c, cmp288, for288-old/new, pins288.cells,
  seteq288, smoke288, tables288.c/.log, dispatch288.c,
  cdiff288, del/addnorm288, cdiff288.miss, banddiff288,
  added288, wall288, depload288).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
