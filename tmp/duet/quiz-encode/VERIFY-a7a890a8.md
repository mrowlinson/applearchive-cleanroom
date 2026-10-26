# VERIFY-a7a890a8 b490 T10P382 pins 149673..150020 (348 pins) PASS

Seat encode-viewer r84, first-hand. Band = 1e3ca791 (py merge
w2b@a068b673 P382, +6 tiers +58 pins, RGRAM-GREEN 22702/22702
+ SMOKE-GREEN first-hand) + a7a890a8 (C port). Base b396d725
(b489 tip, 2274 tiers sealed). Banked Next-P382 consumed FIRST
+ corroborated EXACT at boot (NOTE-viewer-r84-hb1:
Q-1130/A-965 heads read, Q+A agree; scoped sig-share vs lane
code a068b673 + pin endpoints in T10P3820/1/A/C/Q/R comments).
b487-b489 NOT re-verified (bases only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r84/
(fresh detached worktrees tree-490BASE @ b396d725 +
tree-490BAND @ a7a890a8; seat build dir build490/; no branch
switch; cport lane worktree untouched; no push).

Method note: 6 battery scripts pre-written during poll-wait from
banked Q-1130/A-965 + lane PY commit a068b673 (git show, no
checkout) + ct-cache oracle, py_compile 6/6 PASS. BANDSHA/seal/
numstat/RCN-BAND/for29 FILLs filled at landing from first-hand
port msg + numstat + battery run. Two script bugs fixed to match
verified code facts (never to force GREEN): edges T-head b1-const
index (oracle e0/47 exactly right); supplement sed-eats-line on
shared-line FILLs. One wall-check refinement with recorded cause:
2 bare-'aea' substring hits both inside quoted oracle hex blob
607dff2aea3b7147 (PY+C identical); identifier-form regex 0 —
wall holds. CLOSED382-6 adapted pre-run (first-hand grep: 6 new
region lines, NO old-tier homonym — differs from b488/b489
pattern, recorded not assumed).

## FAST (seat-built binaries, BUILDDIR=r84/build490, NVME workdirs)
- Build: make -C tree-490BAND/src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11351/11351 covered=11351/11351 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary). Single-writer
  seat run: fully GREEN.
- RGRAM py 22702/22702 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22644+58 = 11351x2.
- CMP490 GREEN: py 22702 PASS; C PYID 11351/11351 + GREEN.
- SETEQ490 GREEN: py 22702 == PINS 22702 (xor 0);
  PINS-N == for 11351 (xor 0); base PINS 22644 == forbase
  11322 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 149673..150020 exact, all in-band.
  for-added 29 = [149673, 149674, 149675, 149676, 149682,
  149683, 149689, 149690, 149691, 149692, 149695, 149696,
  149699, 149700, 149701, 149716, 149717, 149733, 149759,
  149760, 149764, 149765, 149887, 149888, 149951, 150015,
  150016, 150017, 150020]
  (S0/S1 + A head/mid/tail pairs + C head/mid/tail pairs + Q
  head/mid-pair/mid/edge-pair/tail + T head/edge-pair/mid/
  edge-triple/tail).
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 (tests/test_units.py).

## TABAUDIT (tabaudit490.py 104 PASS 0 FAIL)
- S0 5f522927 (len168) NEW-sig 31/84 vs P381PB0, positions
  [0,1,2,4,5,13-17,19-21,24-29,56-63,80-83], b0b1b2-IN.
  S1 48000000 (len176) NEW-sig 48/88 vs P381PB1, positions
  [0,4,5,19-47,64-71,80-87], b0-IN b1b2b3-same. Both C-eq-py.
  S1 DIFFERS-sig-from-own-C10 (48 vs 45; 41x10 DIVERGE).
- C10 staged == oracle 10/10, 10/10 DIVERGE, sig 45000000.
- M tables AM16x7/CM10x5/M16x8/QR4x2/RM16x8/RQ16x8, all distinct,
  all C-eq-py; M-EQ-RQ lists (overlap 16, positional 16:
  RQ==M PRESENT, even band); M-tails/RM-tails 16/16 ALL NEW
  vs P381T RM and RQ.
  0-overlap vs P381 all six (widths 7v7/5v5/8v7/2v4/8v7/8v6).
- Const tables AC79/CC81/QC76/RC70 == census 79/81/76/70;
  missing AC-[0,1,4,5,10,11,16,80-83]/CC-[4,5,45,84-87]/
  QC-[4,5,52-55,80-85]/RC-[4-9,52-55,76-83];
  AC0-3 7e040000 (AC0-1 present); AC84-87 e3/6d/98/27;
  CC0-3 45000000; CC84-87 absent;
  QC0-3 7e040000; QC84,85 absent / QC86,87 88/00;
  RC0-1 e0/47; RC84-87 3e/f2/88/00.
- R2 tails rows bef18800/def18800/fef18800/1ef28800;
  suffix=tshare=subseq=(3,3,2,3,2,2);
  QM8shared 48; Tring 3ef28800 both ends + ring-wide 256;
  Qb8083 row0 9935979f; Tb8083 split.
- Guards: py sing 786->788 +2, ranges 958->962 +4, elif
  50/50; C sing 791->793 +2, ranges 980->984 +4,
  else-if 0/0. RC_N band 70 / base 73 (70->73? NO: 73->70;
  band 70 == RC count, cutter-regen CONFIRMED by this run,
  1-hit each). CLOSED-T10P 2180->2186 +6
  (CLOSED382 = 6 new region lines, no homonym).

## EDGES (edges490.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 57+2off, b5 const 91 NO step, b0 const 7e);
  C 10/10 (b4 77+2off, b5 const 91, b0 const 45);
  Q 64/64 (b4 8b+2off, b5 91+(off>=59) STEP edge 149759->
  149760, b0 const 7e);
  R 256/256 (b4 0b+2off, b5 92+(off>=123)+(off>=251),
  b0 const e0, b1 const 47, b84-87 3ef28800 256/256).
  ff exactly [149759, 149887, 150015]. Edge pairs
  ff/91->01/92 (149759->149760) + ff/92->01/93
  (149887->149888) + ff/93->01/94 (150015->150016).
  Heads/tails spot values all exact (S0 53/91, S1 55/91,
  A0 57/91, A-tail 75/91, C0 77/91, C-tail 89/91, Q0 8b/91,
  Q-tail 09/92, T-head 0b/92, T-tail 09/94). Tail rav sha
  == PINS g-z150020 (full sha recorded in edges490.log),
  rawlen 104.

## SUPPLEMENT (supplement490.py 30 PASS 0 FAIL)
- R2 full-tail triples (3,3,2,3,2,2) all three metrics.
- AC84-87 e36d9827; CC84-87 absent; QC84,85 absent +
  QC86,87 8800; RC84-87 3ef28800.
- Oracle b0: P381 PBA f0x16, P382 PBA 7ex16 (7e NEW);
  P381 C10 4fx10, P382 C10 45x10 (45 NEW-sig, DIFFSIG).
- Guards re-verified (same deltas as TABAUDIT).
- numstat b396d725..a7a890a8: rgramc.c 608/0, rgram.py
  231/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673... pinned-stable, seat-built).
- for-added 29-set stable (== seteq list above).
- Wall: identifier-form `aea` 0 on added lines (2 bare-hex
  blob hits recorded, oracle data, PY+C identical).
- Seal 2280 (+6 vs b489 2274, port msg) vs CLOSED-T10P 2186
  (+6): offset +94 stable (base 2274-2180).
- rgramc sha256 7f7f7c8345618ae87b944c96af2873144a03a9
  ea4152bf0403381185f77ce55d (recorded, never transcribed).

## GATE reconciliation (GATE-a7a890a8 read first-hand)
Values-agree on EVERY checkable metric, no slip:
for-added 29 set IDENTICAL; S0/S1 sigs+diffs (31/84,
48/88, S1-vs-C10 41x10, DIFFSIG); M-EQ-RQ 16/16 same-order;
R2 rows + (3,3,2,3,2,2) all three metrics; missing sets EXACT;
consts 79/81/76/70; M/RM-tails NEW 16/16 both; 0-overlaps +
widths; guards (786/788, 958/962, 791/793, 980/984, elif 50,
else-if 0); seal 2280 offset +94; CLOSED 2180/2186; numstat
608/231/1+1/58 + leg attribution (C-port leg = rgramc.c only;
PY-merge leg = rgram.py + for-line + PINS); quiz-bank empty;
aae d6e27c97; PINS 22704 rows; RGRAM C 22702 (viewer FAST
covers C via seat PYID + cmp: split noted); edge pins +
formulas + ff 1+2 = 3 total; embeds 53/91 + 55/91; b0/b1
consts; ring const; seal/CLOSED deltas; A-965 CONFIRM 50/50
cited by GATE, matches banked.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487-b489 + CLAIM r80):
uniform — GATE (sweep) counts committed tables; viewer P338
dispute OPEN/deferred, NOT re-litigated: viewer TRUE-uniform
39 held (C10 DIVERGE 10/10).
RQ==M — GATE "reported, not gated" M==RQ 16/16 + memo
"PRESENT-CONFIRM this tier (41st even band)"; viewer ledger:
evens 59 -> 60 PRESENT. Agree PRESENT.
C-leg RGRAM — GATE ran RGRAM C 22702/22702; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
S-F lag — GATE "no-lag this tier" (impl==census); viewer
counter held at 44 pending sweep accounting.
Merge-subject note: PY-merge applied as single-parent commit
1e3ca791 on b396d725 (not a true merge; ^2 absent) — content
gate from C-port commit unaffected; parent-chain YES first-hand.

## Chain state for b491 + r85 (viewer ledger)
- TRUE-uniform 39 (b490: viewer convention NOT-TRUE, C10
  DIVERGE; P338 dispute OPEN).
- S-F tables-lag 44 held (b490 no-lag tier: impl 79/81/76/70
  == census excl).
- RQ==M odds 60 held (b489 ABSENT) / evens 59 -> 60 (b490
  PRESENT).
- Full/diff survey 37 held (b490 diff-flavor: PLAIN-PBA +
  DIFFSIG-C10 structure continues).
- Seal +94 vs CLOSED-T10P stable (2186/2280).
- aae d6e27c97 pinned-stable. rgramc sha recorded (build490).
- Content-line variance 233 -> 231 (rgram +231 this band).
- AC b84-87 e3/6d/98/27 (band value; was c7/70/c9/12).
- RC_N 70 (P381->P382 73->70).
- 348 pins contiguous 149673..150020, no RED anywhere.

Verdict: PASS. Ready for merge (oldest-first).
