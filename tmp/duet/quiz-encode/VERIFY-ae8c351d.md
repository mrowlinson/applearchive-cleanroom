# VERIFY ae8c351d b330 T10P222 pins 93993..94340 (1316 tiers) PASS

Seat viewer-r40, first-hand, fresh detached worktree tree-ae8c351d
(HEAD ae8c351d), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r40. Base 1c52e56f (b329 tip). CT shim on all
batteries.

- Build: make BUILDDIR=r40/build330, rc=0, 0 warnings. aae 56448B
  sha256 d6e27c97; rgramc 2921768B sha256 16229ff1 (both == GATE).
- RGRAMC-PYID 6472/6472 covered=6472/6472 GREEN rc=0 (own binary).
- RGRAM py 12944 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 12944 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (12944/12944).
- PINS 12946 rows (2 hdr + 12944). N-set 6472. For-list union +26,
  0 removed:
  93993 93994 93995 94002 94010 94011 94015 94020 94021 94029
  94036 94037 94045 94052 94053 94068 94069 94079 94080 94084
  94085 94207 94208 94335 94336 94340 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6).
- Tables audit P222 C-vs-py, own script tables330.py rc=0 ALL-EXACT
  (0 false): S0/S1 len 168/168 eq, sigs 17120000/3a822100 b4b5
  53de/55de; AM16 BM10 M16 QR4 QT4 RM16 RQ16 all eq; AC74 BC70
  QC61 RC67 all eq; _N decls 74/70/61/67 match; sigs 3a820102/
  3a822100/3a824102/ae231824; S1==PBB-sig confirmed; varsets exact
  (A 10: 4,5+8; B 14: 4,5+12; Q 23: 4,5+9+8+4; R 17: 4,5+6+9);
  cover84 x4 0-overlap; QR r2==r3 PAIRED 2e7b899abfd3e438 x2 3/4
  distinct; QT verbatim 09bb7378/d1f01af7/b6f9d055/472ce255 r2/r3
  share last-1B 55; widths AM8/BM12/M9/QR8/RM6/RQ9; BM12==QR8+tails
  POSITIONAL set-exact (B mtab indices = QR indices + tail indices,
  script-extracted from dispatch); QM-heads==TR-heads 16/16
  (b47-51 5B heads, matches A-499 "stronger than 5/5"); RM222-vs-
  RM221 shared 0/16 (M-tails ALL NEW first-hand); no extra P222
  syms py/c. NOTE: first script version checked BM value
  decomposition (False) — wrong reading; A-292/GATE claim is
  positional, confirmed True. Script fixed, code CORRECT.
- Dispatch eye-verified both sides, 6 blocks (2 sing + 4) at
  dispatch tail after T10P221R close (N-out-of-scope follows):
  S0 n=93993 PB0 17120000, S1 n=93994 PB1 3a822100, A 93995-94010
  PBA16 3a820102, B 94011-94020 PBB10 3a822100, Q 94021-94084 QUAD
  3a824102 (m=off&15, q=off>>4), R 94085-94340 T-ring ae231824
  (STANDARD, c=off&15, r=off>>4). C T-mirrors 6/6:
  T61382/387/392/407/423/446, bounds + comments exact.
- Edges recomputed first-hand: A/B b5 const de; Q-carry 94079
  (off58 ff/de) -> 94080 (off59 01/df); ring 94207 (off122 ff/df)
  -> 94208 (off123 01/e0); 94335 (off250 ff/e0) -> 94336 (off251
  01/e1); singletons 53/de + 55/de == lencode. All pins PASS.
- C diff: raw 601 + 5 blank-only = 606 add / 0 del. Fine-norm
  (sweep2-r43 sed pipe) add-uniq 371 del-uniq 0 miss 0 (== GATE).
  Coarse INCL 416 / EXCL 415, del 0, miss 0 both.
- Numstat 606/0 + 237/0 + 1/1 + 52/0 (== GATE). sh 1/1 = for-list
  tail append of the 26 new Ns after 93992, purely additive.
- Wall on band added lines (896): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa/nominated 0 hits.
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards 780->786 +6,
  seal 1310->1316 +6: all agree.
- Band comp: da8f64ae (py merge w2b@0c767190 partial, +6 tiers,
  +52 pins) + ae8c351d (C port). Matches GATE.
- CONFIRM: A-499-q614-t10p222 CONFIRM 28/28 (14+10+4, own bed,
  read in full). A-292 recon: consts 75/71/61/67 (in-table
  74/70/61/67 + b5-where-const A/B) resolved; VPOS A9/B13/Q23/
  T17 consistent with varsets; PBB==quad-R POSITIONAL set-exact
  confirmed; paired/tails verbatim match; M-tails "0/4" framing
  recomputed first-hand: RM sets share 0/16. No DISSENT: cut
  bytes verify.
- Own-loop zero-write variant ownloop330b.py (cache-path-direct):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen.)

Verdict: PASS. GATE CORRECT, 0 slips (6th clean round running).
Logs: NVME ws tmp/encode-viewer/r40/ (*330* files: build330.log,
pyid330.log, rgram330py/c.log, pass330py/c.txt, for330-old/
new.nums, pins330-base.csv, smoke330.log, tables330.py/.log,
cdiff330.txt, add/delnorm330.txt, banddiff330.txt, added330.txt,
numstat330.txt, rgram-base330.py, ownloop330b.py/.log,
populate330.py).
