# VERIFY 6be444ff b331 T10P223 pins 94341..94688 (1322 tiers) PASS

Seat viewer-r40, first-hand, fresh detached worktree tree-6be444ff
(HEAD 6be444ff), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r40. Base ae8c351d (b330 tip). CT shim on all
batteries.

- Build: make BUILDDIR=r40/build331, rc=0, 0 warnings. aae 56448B
  sha1-8 7d8dd3a2 (== GATE) sha256 d6e27c97; rgramc 2938648B
  sha1-8 f78eeb25 (== GATE) sha256 9a3072ec (first-hand).
- RGRAMC-PYID 6498/6498 covered=6498/6498 GREEN rc=0 (own binary).
- RGRAM py 12996 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 12996 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (12996/12996).
- PINS 12998 rows (2 hdr + 12996, +52 vs base 12946). N-set 6498.
  For-list union +26, 0 removed:
  94341 94342 94343 94344 94351 94358 94359 94363 94368 94369
  94377 94384 94385 94393 94400 94401 94416 94417 94425 94432
  94433 94463 94464 94591 94592 94688 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6).
- Tables audit P223 C-vs-py, own script tables331.py rc=0 ALL-EXACT
  (0 false): S0/S1 len 168/168 eq, sigs 17120000/5c1f1200 b4b5
  0be1/0de1; AM16 BM10 M16 QR4 QT4 RM16 RQ16 all eq; AC73 BC71
  QC64 RC65 all eq; _N decls 73/71/64/65 match; split-sig A:
  AC b1-3=f42101 b0-variant, AM0 1ea08657957a2f9bd3 (b0=1e
  b12=95), rest b0=00 b12=b5; sigs B 813e2400 / Q 1de84302 / T
  20827f28; varsets exact (A 11: 0,4,5+8; B 13: 4,5+11; Q 20:
  4,5+7+7+4; R 19: 4,5+9+8); cover84 x4 0-overlap; QR r2==r3
  PAIRED e6fc877a5b8d9c x2 3/4 distinct (r0 11fc431add39a7, r1
  cc7c22fa9282a3); QT verbatim 7f7a1c5f/5dfc677c/d8397426/
  073a7426 r2/r3 share 7426; widths AM9/BM11/M7/QR7/RM9/RQ8;
  BM==QR+QT POSITIONAL set-exact; RM223-vs-RM222 shared 0/16 +
  QT223-vs-QT222 shared 0/4 (M-tails ALL NEW first-hand); no
  PT/PC/CM/CC/FM/FC/FS/FO/H/TC syms either side; no extra P223
  syms py/c.
- Dispatch eye-verified both sides, 6 blocks (2 sing + 4) at
  dispatch tail after T10P222R close (N-out-of-scope follows):
  S0 n=94341 PB0 17120000 REPEAT, S1 n=94342 PB1 5c1f1200 NEW,
  A 94343-94358 PBA split-sig (m-tab b0,9-12,76-79 covers split),
  B 94359-94368 PBB10 813e2400, Q 94369-94432 QUAD 1de84302
  (m=off&15, q=off>>4), R 94433-94688 T-ring 20827f28
  (STANDARD, c=off&15, r=off>>4). C T-mirrors 6/6:
  T61618/623/628/643/659/682, bounds + comments exact.
- Head b5 const e1 verified first-hand over all 92 head cells
  94341..94432 (0 bad; n=94341 0b/e1, n=94432 c1/e1, no carry).
  Ring edges recomputed: 94463 (off30 ff/e1) -> 94464 (off31
  01/e2); 94591 (off158 ff/e2) -> 94592 (off159 01/e3). All
  edge pins PASS.
- C diff: raw 601 + 5 blank-only = 606 add / 0 del. GATE norm
  ([0-9]+ -> N) reproduced: add-uniq 175 del-uniq 0 miss 0
  (== GATE). Own fine pipe (sweep2-r43 seds): add-uniq 405,
  del 0, miss 0.
- Numstat 606/0 + 236/0 + 1/1 + 52/0 (== GATE). sh 1/1 = for-list
  tail append of the 26 new Ns after 94340, purely additive.
- Wall on band added lines (895): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa/nominated 0 hits.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards 786->792 +6,
  seal 1316->1322 +6: all agree.
- Band comp: c9fcc2fb (py merge w2b@f8d57674 partial, +6 tiers,
  +52 pins) + 6be444ff (C port). Matches GATE.
- CONFIRM: A-501-q615-t10p223 CONFIRM 30/30 (16+10+4, own bed,
  read in full). A-293 recon: consts 74/72/65/65 (in-table
  73/71/64/65 + b5-where-const A/B/Q) resolved; VPOS A10/B12/
  Q19/T19 consistent with varsets; split-sig + paired/tails
  verbatim match; M-tails "0/4" framing recomputed first-hand:
  RM sets share 0/16. No DISSENT: cut bytes verify.
- Own-loop zero-write variant ownloop331b.py (cache-path-direct):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen.)

PROSE FLAG 1 (sweep seat, code PASS): GATE line 113 cites
"A-501-q617" — actual file is A-501-q615 (Q-615, T10P223);
q617 is A-503 (T10P225, other turf). Counts 30/30 verified
correct against the real A-501. PROSE-01: 1st slip this round,
below 3-slip bar; no NOTE/PROD.

Verdict: PASS. GATE CORRECT except 1 prose slip (ends 6-round
clean streak on a citation typo; code 0 slips).
Logs: NVME ws tmp/encode-viewer/r40/ (*331* files: build331.log,
pyid331.log, rgram331py/c.log, pass331py/c.txt, for331-old/
new.nums, pins331-base.csv, smoke331.log, tables331.py/.log,
cdiff331.txt, add/delnorm331-GATE.txt, banddiff331.txt,
added331.txt, numstat331.txt, rgram-base331.py, ownloop331b.py/
.log, populate331.py).
