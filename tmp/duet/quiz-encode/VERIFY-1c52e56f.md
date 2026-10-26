# VERIFY 1c52e56f b329 T10P221 pins 93645..93992 (1310 tiers) PASS

Seat viewer-r40, first-hand, fresh detached worktree tree-1c52e56f
(HEAD 1c52e56f), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r40. Base 655f5077 (b328 tip). CT shim on all
batteries.

- Build: make BUILDDIR=r40/build329, rc=0, 0 warnings. aae 56448B
  sha1-8 7d8dd3a2 (== GATE) sha256 d6e27c97 (stable); rgramc
  2921432B sha256 05892d24 (first-hand, GATE omits).
- RGRAMC-PYID 6446/6446 covered=6446/6446 GREEN rc=0 (own binary).
- RGRAM py 12892 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 12892 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (12892/12892).
- PINS 12894 rows (2 hdr + 12892, +52 vs base 12842). N-set 6446.
  For-list union +26, 0 removed:
  93645 93646 93647 93654 93662 93663 93667 93672 93673 93681
  93688 93689 93695 93696 93704 93705 93720 93721 93729 93736
  93737 93823 93824 93951 93952 93992 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6).
- Tables audit P221 C-vs-py, own script tables329.py rc=0 ALL-EXACT
  (0 false): S0/S1 len 168/168 eq, sigs 16120000/3a072300 b4b5
  9bdb/9ddb; AM16 BM10 M16 QR4 QT4 RM16 RQ16 all eq; AC74 BC69
  QC61 RC62 all eq; _N decls 74/69/61/62 match; sigs 3a074302/
  3a822100/3a824102/a083873c; varsets exact (A 10: 4,5+8; B 15:
  4,5+13; Q 23: 4,5+10+7+4; R 22: 4,5+9+11); cover84 x4
  0-overlap; QR r1==r2==r3 TRIPLE 0efc035f14b58e x3 2/4 distinct
  (r0 1b3cc472f458bb); QT verbatim 9dcf57e2/d0b943a3/64b64ea3/
  93b64ea3 r2/r3 share b64ea3; widths AM8/BM13/M10/QR7/RM9/RQ11;
  RM221-vs-RM220 shared 0/16 (M-tails ALL NEW first-hand); no
  PT/PC/CM/CC/FM/FC/FS/FO/H/TC syms either side; no extra P221
  syms py/c.
- Dispatch eye-verified both sides, 6 blocks (2 sing + 4) at
  dispatch tail after T10P220R close (N-out-of-scope follows):
  S0 n=93645 PB0 16120000, S1 n=93646 PB1 3a072300, A 93647-93662
  PBA16 3a074302, B 93663-93672 PBB10 3a822100, Q 93673-93736 QUAD
  3a824102 (m=off&15, q=off>>4), R 93737-93992 T-ring a083873c
  (ROLE-SWAP4, c=off&15, r=off>>4). C T-mirrors 6/6:
  T61143/148/153/168/184/208, bounds + comments exact.
- Edges recomputed first-hand: A/B b5 const db across (93647
  9f/db, 93662 bd/db, 93663 bf/db, 93672 d1/db); Q-carry 93695
  (ff/db) -> 93696 (01/dc); ring 93823 (off86 ff/dc) -> 93824
  (off87 01/dd); 93951 (off214 ff/dd) -> 93952 (off215 01/de).
  All pins PASS.
- C diff: raw 601 + 5 blank-only = 606 add / 0 del. GATE norm
  ([0-9]+ -> N) reproduced: add-uniq 173 del-uniq 0 miss 0
  (== GATE). Own fine pipe (sweep2-r43 seds): add-uniq 406,
  del 0, miss 0.
- Numstat 606/0 + 238/0 + 1/1 + 52/0 (py 238 first-hand, GATE
  omits). sh 1/1 = for-list tail append (same pattern as b328).
- Wall on band added lines (897): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa/nominated 0 hits.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards 774->780 +6,
  seal 1304->1310 +6: all agree.
- Band comp: 053c7aa8 (py merge w2b@fe907444 partial, +6 tiers,
  +52 pins) + 1c52e56f (C port). Matches GATE.
- CONFIRM: A-494-q613-t10p221 CONFIRM 28/28 (14+10+4, own bed,
  read in full). A-291 recon: consts 75/70/61/62 (in-table
  74/69/61/62 + b5-where-const A/B) resolved; VPOS A9/B14/Q23/
  T22 consistent with varsets; triple + tails verbatim match;
  M-tails "0/4" framing recomputed first-hand: RM sets share
  0/16. No DISSENT: cut bytes verify.
- Own-loop zero-write variant ownloop329b.py (cache-path-direct):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen.)

Verdict: PASS. GATE CORRECT, 0 slips (6th clean round running).
Logs: NVME ws tmp/encode-viewer/r40/ (*329* files: build329.log,
pyid329.log, rgram329py/c.log, pass329py/c.txt, for329-old/
new.nums, pins329-base.csv, smoke329.log, tables329.py/.log,
cdiff329.txt, add/delnorm329-GATE.txt, banddiff329.txt,
added329.txt, numstat329.txt, rgram-base329.py, ownloop329b.py/
.log, populate329.py).
