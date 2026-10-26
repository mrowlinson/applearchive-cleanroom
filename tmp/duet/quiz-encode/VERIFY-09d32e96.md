# VERIFY-09d32e96 b342 T10P234 pins 98169..98516 (1392 tiers) PASS

Seat viewer-r43, first-hand, detached tree-09d32e96 @09d32e96,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r43.
Base e62ee6cf (b341, 1386 tiers). Band = 7a541611 (py) + 09d32e96 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build342/bin, rc=0, 0 warnings. sha256 rgramc
  62f59d9f / aae d6e27c97 (== GATE; aae.c untouched).
- RGRAMC-PYID 6812/6812 covered=6812/6812 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13624/13624 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13624/13624 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13626 rows (2 hdr + 13624); base-N set vs for-list
  set-eq 6812/6812. For-list 6778->6812 +34/-0; added 34 ==
  GATE verbatim (98169 98170 98171 98175 98176 98180 98186
  98187 98189 98190 98191 98192 98193 98194 98195 98196
  98197 98204 98212 98213 98220 98228 98229 98236 98244
  98245 98252 98260 98261 98303 98304 98431 98432 98516).
  34x2=68=13624-13556. Split re-tallied: S0/S1 2, A 5
  (head/mids/carry-pair/tail), F 9 of 10 (98188 unpinned),
  Q 12, ring 6 (head/edge-pairs/tail).
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P234 C-vs-py, own script tables342.py, 54/54
  ALL-EXACT (own QR-1Bdiff check over-strict first run,
  fixed, clean rerun counted): S0/S1 (8c470100/ee8c4701,
  b4b5 f3fe/f5fe == lencode), AM 16/16 distinct 9B (b0-2
  13 distinct), FM 10/10 distinct 13B (7-sig map order
  cd898b x3/ddfc8f/958d8c/653582/25b385/3dd589/857683/
  958d8c), M 16/16 distinct 7B, QR 4/4 (r0==r3 b49bc46f3243a3
  OUTER-PAIRED, r1/r2 exactly-1B-diff byte-2 e8/f8:
  99ade8707209ab/99adf8707209ab), QT 4/4 (== A tails
  2e189304/f98d105d/311be64a/55426037), RM/RQ 16/16
  UNPAIRED, AC 73/73, FC 69/69, QC 64/64, RC 71/71; _N
  decls 73/69/64/71. Varsets exact: AC 11 (b4,b5+M9
  b0-2,11,19,76-79), FC 15, QC 20 (T4=b80-83), RC 17
  (b4,b5,b6step+M7+R7). Coverage 73+11/69+15/64+20/71+17
  exact, 0 overlap, b4/b5 in no const set. Sig consts:
  AC b0-2 in tab, FC b0-2 in tab + b3==02, QC 40806734,
  RC 02000000. RC b84-87 a0/a4/60/37. M-tails NEW vs P233M;
  QT overlap 0/4 vs P233T; ring tails SPLIT 16/16 both.
  A-carry 98175=fffe 98176=01ff; F/Q b5 ff const 98187..
  98260 (74/74). Ring edges off42/43 ff/ff/66->01/00/67 +
  off170/171 ff/00->01/01 (WRAP verified). No PT/PC/CM/CC/
  BM/BC; inventory exactly 13 + 4 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 6 blocks in order (S0
  98169, S1 98170, A 98171-86, F 98187-96, Q 98197-98260,
  R 98261-98516); C T-mirrors 6/6 exact (T64505/510/515/
  530/546/569); ring formulas both sides (171/255/102 =
  0xab/0xff/0x66, thresholds 43/171, b5 &FF wrap, b6 step);
  M7/R7 byte positions exact; insert after T10P233R close
  at dispatch tail, N-out-of-scope follows.
- Edges 98303/98304 + 98431/98432 + carry pair 98175/98176
  PASS 2/2 both legs. Matches A-540 (35/35 = 16+11+8, file
  read, counts verified) + A-304 (outer-pair exact, tails
  exact, M-tails NEW, b6 256/256 claim consistent with
  formula+GREEN, b84-87 exact, consts 73/70/65/71 INCL with
  standing -1 x2 excl on FRAG/quad, NO D dips).
- C diff purely additive: numstat 612/0 rgramc.c, 239/0
  rgram.py, 1/1 test_rgram.sh, 68/0 PINS (== GATE; total
  920). C raw 607 content + 5 blank-only / 0 del; fine-norm
  del-uniq 0, add-uniq 397 (== GATE).
- Wall on 920 added lines: vendor/disasm 0, depload 0,
  oracle/shebang/nominated 0 real (68 PINS ct-lzraven backend
  tags only).
- Tiers: merge-msg +6, code 6 blocks, guards singletons
  500->502 +2 / ranges 388->392 +4 = +6 (stated `if n ==`
  method), seal 1386->1392 +6: all agree.
- CONFIRM evidence (CONVERT-01 rule b): A-540 CONFIRM 35/35;
  A-304 corroborates. Agrees with cport msg (PYID 6812,
  RGRAM 13624).
- Own-loop 348/348 (98169..98516, C+py agree CLOSED each N;
  populate fetched 314, 34 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b342. Newest
  PARENT-* is QNUM-12 (GATE says QNUM-09 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

Verdict: PASS. Code CORRECT; GATE CORRECT, 0 slips.
Logs: NVME ws tmp/encode-viewer/r43/ (*342* set:
build342, pyid342, rgram342py/c, cmp342.py/.c, for342-*,
pins342.basen, smoke342, tables342.py/.log, banddiff342(-c),
added342, numstat342, caddnorm342, populate342,
ownloop342.py/.log).
