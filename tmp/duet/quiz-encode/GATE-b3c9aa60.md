# GATE b3c9aa60 b296 T10P188 pins 82161..82252 (1056 tiers) PASS-functional

Seat sweep2-r36, first-hand, WT tmp/wt-encode-sweep2 @b3c9aa60,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r36.
Band = d78fdd55 (py merge w2b@1f6da9e7 partial, +6 tiers +32 pins)
+ b3c9aa60 (C port). Base e4676a40 (b295 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build296/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ba28f0f3 / aae d6e27c97
  (aae identical to b288-b294 builds: aae.c untouched).
- RGRAMC-PYID 5582/5582 covered=5582/5582 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11164/11164 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11164/11164 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11164/11164).
- PINS-RGRAM cells set-eq 5582/5582 (diff 0, PINS base-N
  set vs for-list); PINS 11166 rows (2 hdr + 11164 =
  PASS lines). For-list union +16 (82161 82162 82163
  82175 82176 82179 82180 82184 82188 82189 82204
  82205 82221 82237 82251 82252), 0 removed
  (`; do` stripped before tokenize). Each for-N yields
  2 PASS lines (g-zN-closed + g-zN).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P188 C-vs-py, all 11 EXACT (script-compared):
  S0/S1/S2 singletons 1/1 each, AM 16/16, AC 74/74,
  BM 9/9, BC 71/71, M 16/16, QR 4/4, QT 4/4, QC 65/65.
  C _N decls 74/71/65 match actual.
- Dispatch eye-verified both sides, 6 tiers in order:
  S0 n=82161 (sig f6020000 REPEAT x3 P186/P187), S1
  n=82162 (fat PB1, sig 3b070500 == P187 PB1 sig), A
  82163-82178 (sig b7735000 NEW, mtab b6-9/76-79, b5
  step @82176 raw lencode), S2 n=82179 (SING own sig
  e83d0600 NEW), B 82180-82188 MID9 (per-N sigs b0-var,
  b1-3 const 1e0300, 11B mtab b0,6-11,80-83, raw
  lencode), Q 82189-82252 multi-sig quad rows2==3
  (rows0,2,3 e9ef3100 / row1 eaef3100), M 6B
  b13,15,76-79, sigR 7B b0,6-11, T 4B b80-83 (raw
  lencode). C blocks carry T52301/306/311/326/331/347
  py-line mirrors. Insert position exact both sides:
  after T10R185 close, before T10R186 (n<=82508,
  base 82253). Matches A-402 geometry (VPOS A
  [4,5,6-9,76-79] / B [0,4,6-11,80-83], sigs,
  lencode 92/92, flip [82176]).
- C diff renumber-only + new: raw grep 1517 del / 1978
  add (numstat identical, no blank-only lines);
  normalized (_t/_i/_b/T numbers) del-subset-add
  0 missing (del-uniq 1478, add-uniq 1767).
- Wall on band diff added lines (scope e4676a40..b3c9aa60,
  2184 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c, rgram.py (+173/+0 purely
  additive), test_rgram.sh (for-line 1/1), PINS (+32/+0).
- CONFIRM evidence (CONVERT-01 rule b): A-402-q393p188
  verdict CONFIRM (26/26 checks; file present, counts
  verified). No CONFIRM-P188.md file; A-402 suffices
  per rule. Agrees with cport commit msg (PYID 5582,
  RGRAM 11164).
- Quiz: no conflicting CLAIM/GATE/FLAG on b296. No new
  PARENT-* (newest PROSE-01, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r36/ (build296.log,
  build296.sha, pyid296, rgram296py/c, cmp296.py/.c,
  for296-old/new, pins296.csv/.cells/.uniq, pass296.cells,
  seteq296, smoke296, tables296.log, tabc.py, cdiff296,
  cdiff296.del/.add, del/addnorm296, cdiff296.miss,
  banddiff296, added296).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
