# VERIFY-e62ee6cf b341 T10P233 pins 97821..98168 (1386 tiers) PASS

Seat viewer-r43, first-hand, detached tree-e62ee6cf @e62ee6cf,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r43.
Base af633902 (b340, 1379 tiers). Band = 8416b83e (py) + e62ee6cf (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build341/bin, rc=0, 0 warnings. SHA-1 first8
  rgramc 29b2bb66 / aae 7d8dd3a2 (== GATE; aae sha256
  d6e27c97 stable, aae.c untouched in band diff).
- RGRAMC-PYID 6778/6778 covered=6778/6778 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13556/13556 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT_CACHE_DIR shim).
- RGRAM C 13556/13556 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13558 rows (2 hdr + 13556, +66 vs base); PINS cells
  6778; for-list 6778; PINS-for SETEQ 6778/6778.
  For-list 6745->6778 +33/-0 first-hand (see slips: GATE's
  6744->6777 wrong). Added 33: 97821 97822 97823 97830
  97838 97839 97840 97841..97848 97849 97856 97864 97865
  97872 97880 97881 97888 97896 97897 97904 97912 97913
  97919 97920 98047 98048 98168. 33x2=66=13556-13490.
  Split re-tallied: sing 2, A 3 (off0/7/15), P 2, F 8 all,
  Q 12 (off0/7/15/16/23/31/32/39/47/48/55/63), R 5
  (head + 2 edge pairs), tail 98168. PINS adds == for-list
  adds exactly (33 cells incl 98168, excl 97820), 0 removed.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P233 C-vs-py, own script tables341.py, 68/68
  ALL-EXACT: S0/S1 (043b0100/dd1a3f01, b4b5==lencode),
  AM 16/16 distinct 8B, PT 2/2 (9b/bb), FM 8/8 diverge 20B
  (6-sig map 6f02/9f01/bf01/df01/ef01x2/cf01/bf01 in order),
  M 16/16 distinct 6B, QR 4/4 (r1==r2 1e2517d802718a4752,
  r0/r3 exact, b3 row-pairs 1c/1e/1e/1c), QT 4/4 (== A tails
  e72e30b8/196917a6/436917a6/20377b54, r1/r2 share 6917a6),
  RM 16/16 (7B) / RQ 16/16 (6B) UNPAIRED, AC 74/74, PC 81/81,
  FC 62/62, QC 63/63, RC 73/73; _N decls 74/81/62/63/73.
  Varsets exact: AC 10, PC 3, FC 22, QC 21, RC 15 (VPOS
  9/{b4,b80}/21/20/15 + b5-excl). Coverage exact, 0 overlap,
  b4/b5 in no const set. Sig consts AC dd1abf13, PC
  dd1a7f02, FC dd1a+b2,3 tab, QC daadf1+b3 tab, RC 01000000.
  RC b84-87 b8/fe/3a/f5. RQ==M 16/16 element-wise. Ring
  tails SPLIT 16/16 both. M-tails NEW vs P232T (both refs),
  RM NEW vs P232RM, QT NEW vs P232QT. Lencode edges A
  3f/fc->5d/fc, P 5f+61/fc, F 63->71/fc, Q 73->f1/fc, b5 fc
  const 97823..97912 (90/90). Ring edges off6/7 ff/fc->01/fd
  + off134/135 ff/fd->01/fe. Inventory exactly 15 + 5 _N,
  no BM/BC, novel-clean both sides.
- Dispatch eye-verified both sides, 7 blocks in order (S0
  97821, S1 97822, A 97823-38, P 97839-40, F 97841-48, Q
  97849-912 m=off&15 q=off>>4, R 97913-98168); C T-mirrors
  7/7 exact (T64252/257/262/277/291/309/332); guards exact;
  PT via snprintf %02lx pay[80]; counter 243/252 + thresholds
  7/135; temps max _t4995 (base _t4975, no reuse); M7/R6
  byte positions exact; insert at dispatch tail,
  N-out-of-scope follows.
- Edges 97919/97920 + 98047/98048 + tail 98168 PASS 2/2 both
  legs. Matches A-537 (35/35: 17+10+8, file read) + A-303
  (3/3 legs; consts 75/63/64/73 INCL with standing -1 x3
  excl bookkeeping on PBA/FRAG/quad, T88 identical; NO D
  dips).
- C diff purely additive: numstat 724/0 rgramc.c, 271/0
  rgram.py, 1/1 test_rgram.sh, 66/0 PINS (== GATE; total
  1062). C 0 del lines; fine-norm by GATE's stated method
  del-uniq 0, add-uniq 172 (== GATE; own initial 171 was own
  double-strip pipeline slip, corrected, clean rerun counted).
- Wall on 1062 added lines: vendor/disasm 0, depload 0,
  oracle/shebang/nominated 0 real (66 PINS ct-lzraven backend
  tags only).
- Tiers: merge-msg +7, code 7 blocks, tier-tags +7, guards
  singletons 498->500 +2 / ranges 383->388 +5, CLOSED prints
  1803->1810 +7 (plain-grep method == GATE absolute), seal
  1379->1386 +7: all agree.
- CONFIRM evidence (CONVERT-01 rule b): A-537 CONFIRM 35/35
  (counts verified); A-303 corroborates. Agrees with cport
  msg (py/C 13556, PYID 6778).
- Own-loop 348/348 (97821..98168, C+py agree CLOSED each N;
  populate fetched 315, 33 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: no conflicting CLAIM/GATE/FLAG on b341. Newest
  PARENT-* is QNUM-12 (GATE says QNUM-09 — stale, immaterial,
  Q-block grants only). PROSE-01 re-read before filing.

4 GATE PROSE SLIPS (sweep-r46; code PASS throughout):
(S1) for-list "6744->6777 +33/-0: 97820 + 32 tier pins" vs
first-hand 6745->6778 +33/-0: 97820 pre-existing (in base
for-list 1x), 33rd added cell is 98168. (S2) "PINS cells
6778 vs for-list 6777: cells-for={98168} (tail pinned, not
in battery for-list)" vs first-hand for-list 6778 with
trailing "98168; do" present, PINS-for SETEQ 6778/6778,
98168 PASS 2/2 both legs. S1+S2 root cause: `;`-token
pollution in sweep parse (trailing "N; do" dropped on old
line -> 6744 and new line -> 6777) — same bug class as b339
S1+S2. (S3) Q row-grouping "q1 off15/16/23" vs code
q=off>>4 both sides: off15 is q0 (actual q0={0,7,15},
q1={16,23}) — same class as b339 S3. (S4) "16-table" layout
headline (x2) vs GATE's own 15-item enumeration + first-hand
15 content symbols both sides (py syms=15 extra=[], C 15+5
_N extra=[]) — self-contradictory GATE. Recommend parent
check PROSE-01 3rd-slip rule for sweep-r46's round (b339+b341
both sweep-r46).

Verdict: PASS. Code CORRECT; GATE prose 4 slips (flagged).
Logs: NVME ws tmp/encode-viewer/r43/ (*341* set:
build341, pyid341, rgram341py/c, cmp341.py/.c, for341-*,
pins341.basen/-base, smoke341, tables341.py/.log,
banddiff341(-c), added341, numstat341, caddnorm341b,
populate341, ownloop341.py/.log).
