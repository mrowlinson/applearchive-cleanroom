# VERIFY-af633902 b340 T10P232 pins 97473..97820 (1379 tiers) PASS

Seat viewer-r43, first-hand, detached tree-af633902 @af633902,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r43.
Base bcc7d15a (b339, 1372 tiers). Band = 4de2cb3c (py) + af633902 (C).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build340/bin, rc=0, 0 warnings. sha256 rgramc
  dd964bb9 / aae d6e27c97 (== GATE; aae.c untouched in band diff).
- RGRAMC-PYID 6745/6745 covered=6745/6745 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, NVME workdir).
- RGRAM py 13490/13490 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, NVME workdir, CT shim).
- RGRAM C 13490/13490 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set diff 0 lines.
- PINS 13492 rows (2 hdr + 13490); base-N set vs for-list
  set-eq 6745/6745 (own `;`-token parse bug caught pre-count,
  fixed, clean rerun counted). For-list 6712->6745 +33/0rem;
  added 33 == GATE verbatim (97473 97474 97475 97478 97482
  97483 97486 97490 97491 97492 97493 97496 97500 97501
  97508 97516 97517 97524 97532 97533 97535 97536 97540
  97548 97549 97556 97564 97565 97663 97664 97791 97792
  97820). 33x2=66=13490-13424. Split 2+6+2+3+14+6 by range
  re-tallied first-hand: S0/S1 2, A 6 (all in 97475..490),
  PAIR 2, C 3, Q 14 (all in 97501..564), ring 6.
- SMOKE-GREEN rc=0 (6/6 PASS, default backend).
- Tables audit P232 C-vs-py, own script tables340.py, 61/61
  ALL-EXACT: S0/S1 1/1 (sigs 053b0100/dd1a3f01, b4b5==lencode
  97473/97474), AM 16/16 distinct 10B (df14 x8 + 2f16 x8),
  PT 2/2 (a9/c9), CM 8/8 distinct 12B, M 16/16 distinct,
  QR 4/4 (r1==r2 21578e7f54512a07, r0/r3
  e9768af8347c0507/13195ef814dbe306), QT 4/4 (== A tails
  aeef66e5/acab63db/d6ab63db/d3703d27, r1/r2 share ab63db
  max-suffix 3B), RM/RQ 16/16 UNPAIRED, AC 72/72, PC 81/81,
  CC 70/70, QC 62/62, RC 69/69; _N decls 72/81/70/62/69.
  Varsets exact: AC 12 (2,3,4,5,21,22,23,31,76-79), PC 3
  (4,5,80), CC 14, QC 22 (T4=b80-83), RC 19 over 0..87.
  Coverage unions 72+12/81+3/70+14/62+22/69+19 exact, 0
  overlap, b4/b5 in no const set. Sig consts AC dd1a, PC
  dd1a7f02, CC dd1a3f01, QC dd1abf13, RC 01000000. RC b84-87
  c8/34/3c/ae. M-tails 16/16 NEW vs P231M; QT overlap 0/4
  vs P231T; ring tails SPLIT 16/16 both. b5 f9 const over
  97475..97500; carry 97535=fff9 97536=01fa. Inventory
  exactly 15 + 5 _N, novel-clean both sides.
- Dispatch eye-verified both sides, 7 blocks in order (S0
  97473, S1 97474, A 97475-90, P 97491-92, C 97493-97500,
  Q 97501-564, R 97565-97820); C T-mirrors 7/7 exact
  (T63982/987/992/008/022/038/061); ring formula both sides
  (0x3b/59, 0xfa/250, thresholds 99/227, off&15 col, off>>4
  row); M9/R8 byte positions exact both sides; insert after
  T10P231R close at dispatch tail, N-out-of-scope follows.
- Edges via formula first-hand: off98 ff/fa -> off99 01/fb
  (97663->97664); off226 ff/fb -> off227 01/fc (97791->
  97792); all four + carry pair 97535/97536 PASS 2/2 both
  legs. Matches A-532 §2-3 + A-302 (R8 paired exact, tails
  exact, M-tails NEW, ring STANDARD, consts 73/71/62/69
  INCL with standing -1 x2 excl bookkeeping, NO D dips).
- C diff purely additive: numstat 724/0 rgramc.c, 269/0
  rgram.py, 1/1 test_rgram.sh (for-line), 66/0 PINS (==
  GATE; total 1060). C raw 718 content + 6 blank-only / 0
  del; fine-norm del-uniq 0, add-uniq 426 (== GATE).
- Wall on 1060 added lines: vendor/disasm 0, depload 0,
  libcompression/CT-shim/shebang/aa/nominated 0 real (66
  PINS `ct-lzraven` backend provenance tags on new rows
  only; generator test_rgram_fast.py per FASTBAT-01).
- Tiers: merge-msg +7, code 7 blocks, guards singletons
  496->498 +2 / ranges 378->383 +5 = +7 (stated `if n ==`
  method), seal 1372->1379 +7 in band msgs: 4/4 agree.
  FLAG b340-+7 CONFIRMED first-hand.
- CONFIRM evidence (CONVERT-01 rule b): A-532 CONFIRM 34/34
  (16+10+8, file read, counts verified); A-302 corroborates.
  Agrees with cport msg (PYID 6745, RGRAM 13490).
- Own-loop 348/348 (97473..97820, C+py agree CLOSED each N;
  populate fetched 315, 33 pins pre-cached; tool-identical
  -encode -a lzraven).
- Quiz: newest PARENT-* is QNUM-12 (w2b block 1120-1159),
  not QNUM-09 as GATE states — STALE NOTE, immaterial:
  QNUM-10/11/12 are writer Q-block grants, no gate impact.
  Not counted as PROSE-01 impl slip. No conflicting
  CLAIM/GATE/FLAG on b340. PROSE-01 re-read before filing.

Verdict: PASS. Code CORRECT; GATE CORRECT (0 impl slips).
Logs: NVME ws tmp/encode-viewer/r43/ (build340, pyid340,
rgram340py/c, cmp340.py/.c, for340-*, pins340.basen,
smoke340, tables340.py/.log, banddiff340(-c), added340,
numstat340, caddnorm340, populate340, ownloop340.py/.log).
