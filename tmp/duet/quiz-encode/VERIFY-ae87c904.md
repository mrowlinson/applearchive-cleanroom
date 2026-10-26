# VERIFY-ae87c904 b487 T10P379 pins 148629..148976 (348 pins) PASS

Seat encode-viewer r83, first-hand. Band = 673eb8e3 (py merge
w2b@67bdb25e P379, +6 tiers +58 pins, RGRAM-GREEN 22528/22528
+ SMOKE-GREEN) + ae87c904 (C port). Base e988dbb5 (b486 tip,
2256 tiers sealed). Banked Next-P379 consumed FIRST +
corroborated EXACT at seat boot (NOTE-viewer-r83-hb1:
scripted sig-share 67bdb25e hits 2/4/2/1 + pins 148629/148976;
Q-1127/A-962 read first-hand). b484/b485/b486 NOT re-verified
(bases only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r83/
(fresh detached worktrees tree-487BASE @ e988dbb5 +
tree-487BAND @ ae87c904; seat build dir build/; no branch
switch; cport lane worktree untouched; no push).

Method note: r82's carried templates (seteq/cmp/edges/tabaudit/
supplement/probe 487) were found b486-stale on first read
(counts 22470/22412, for 11235/11206, pins 148281..148728 =
b486 values; r82 never ran them, nothing landed). Fresh b487
scripts written from Q-1127 P379 section + probe487.py
first-hand oracle values; stale template copies removed.
py_compile 6/6 PASS.

## FAST (seat-built binaries, BUILDDIR=r83/build, NVME workdirs)
- Build: make -C src/c, rc=0, 0 warnings (aae + rgramc).
- RGRAMC-PYID 11264/11264 covered=11264/11264 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary). = 11235+29.
- RGRAM py 22528/22528 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22470+58 = 11264x2.
- cmp487.py GREEN: py 22528 PASS; C PYID 11264/11264 + GREEN.
- seteq487.py GREEN: py 22528 == PINS 22528 (xor 0);
  PINS-N == for 11264 (xor 0); base PINS 22470 == forbase
  11235 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 148629..148976 exact, all in-band.
  for-added 29 = [148629, 148630, 148631, 148632, 148638,
  148639, 148645, 148646, 148647, 148648, 148651, 148652,
  148655, 148656, 148657, 148672, 148673, 148688, 148689,
  148704, 148720, 148721, 148735, 148736, 148800, 148863,
  148864, 148865, 148976]
  (S0/S1 + A head/mid/tail pairs + C head/mid/tail pairs +
  Q head/boundary-pairs/mid/tail + R head/edge-pair/mid/
  edge-pair+mate/tail; both counter edges pair-covered).
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 (tests/test_units.py).

## TABAUDIT (tabaudit487.py 103 PASS 0 FAIL)
- S0 5d6af624 (len168) NEW-sig 29/84 vs P378PB0, positions
  [0,1,2,4-7,9,10,13-15,17-21,56-63,76-79], b0b1b2-IN
  b3-same, embed 2b/89 = lencode. S1 4f000000 (len176)
  NEW-sig 49/88 vs P378PB1, positions [0,4,5,14-43,60-67,
  80-87], b0-IN b1b2b3-same, embed 2d/89. Both C-eq-py.
- C10 staged == oracle 10/10, 10/10 DIVERGE, [0] sig
  4f000000 SAME-as-PB1, S1-vs-C10 diffs 25x10.
- M-tables AM16x6/CM10x4/M16x7/QR4x4/R4-rows-e9371c43-
  09381c43-a77da495-e67da495/RM16x8/RQ16x9, all distinct,
  all C-eq-py; M-ne-RQ, overlap 0, positional 0.
  M/RM-tails 16/16 ALL NEW vs P378T RM and RQ.
  0-overlap vs P378 all six (widths 6v7/4v5/7v8/4v1/8v8/9v8).
- Const tables AC80/CC82/QC75/RC69 == census 80/82/75/69;
  missing AC-[4,5,40,41,80-83]/CC-[4,5,84-87]/
  QC-[4,5,30,39,47,80-83,84-87]/RC-[4,5,40-42,46,47,
  52-55,76-83]; AC0-3 4d040000; AC84-87 a3/09/81/68;
  CC0-3 4f000000; QC0-3 4d040000; QC84-87 absent (R4 lanes);
  RC0-1 4d/4e; RC84-87 c9311baa.
- R1 tails exact rows; suffix=tshare=subseq (2,0,0,0,0,3);
  QM7shared 48; ring b84-87 c9311baa both ends;
  Q b80-83 row0 abec59c1; T b80-83 split.
- Guards: py sing 780->782 +2, ranges 946->950 +4, elif
  50/50; C sing 785->787 +2, ranges 968->972 +4,
  else-if 0/0. RC_N band 69 / base 70 (1-hit each,
  70->69 VARIES). CLOSED-T10P 2162->2168 +6 (379-count 6).

## EDGES (edges487.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 2f+2off, b5 89); C 10/10 (b4 4f+2off, b5 89,
  b0 4f); Q 64/64 (b4 63+2off range 63..e1, b5 89
  NOEDGE, b0 4d); R 256/256 (b4 e3+2off, b5
  89+(off>=15)+(off>=143), b0 4d, b1 const 4e,
  b84-87 c9311baa 256/256). ff exactly [148735, 148863].
  Edge pairs ff/89->01/8a (148735->148736) +
  ff/8a->01/8b (148863->148864). Heads/tails spot
  values all exact (S0 2b/89, S1 2d/89, A0 2f/89,
  A1 4d/89, C0 4f/89, C1 61/89, Q0 63/89, Q1 e1/89,
  T-head 4d/e3/89, T-tail e1/8b). Tail 148976 rav sha
  bd2f7f6a75e6446a... == PINS g-z148976, rawlen 104.

## SUPPLEMENT (supplement487.py 28 PASS 0 FAIL)
- R1 full-tail triples (2,0,0,0,0,3) all three metrics.
- AC84-87 a3098168; QC84-87 absent; RC84-87 c9311baa.
- Oracle b0: P378 PBA 9bx16, P379 PBA 4dx16 (4d NEW);
  P378 C10 49x10, P379 C10 4fx10 (4f NEW).
- Guards re-verified (same deltas as TABAUDIT).
- numstat e988dbb5..ae87c904: rgramc.c 608/0, rgram.py
  232/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched.
- for-added 29-set stable (== seteq list above).
- Wall full scope (899 added lines = 894 content + 5
  blank-only): `aea' exactly 2 hits, both PINS sha-256
  hex (g-z148639 e714...aea14f..., g-z148673
  3c25...aea5367...), 0 invocations.
- Seal 2262 (+6 vs b486 2256, port msg) vs CLOSED-T10P
  2168 (+6): offset +94 stable (base 2256-2162).
- rgramc sha256
  bde8ed4c51024c084acb94e7f51526e10efde5978521f4200aa500279d09065
  (recorded, never transcribed; computed from seat binary).

## GATE reconciliation (GATE-ae87c904 read first-hand)
Values-agree on EVERY metric, no slip:
for-added 29 set IDENTICAL; S0/S1 diff positions EXACT;
S1-vs-C10 25x10; S1-vs-P378C10[0] 40/88 SIG-DIFFERS
(re-verified first-hand: 40, sigs 49 vs 4f); R1 rows +
(2,0,0,0,0,3) all three metrics; missing sets EXACT;
consts 80/82/75/69; VPOS 7/5/13/19 (follows from
asserted 1+6/1+4/2+7+4/2+8+9); tail rav sha full
bd2f7f6a75e6446ad771abf0d0ca96efc7293491da6df7087853cb6476132d65
EXACT; rgramc sha bde8ed4c EXACT (independent builds,
same hash); aae sha256 d6e27c97 pinned (seat build
d6e27c97ced21673...); PYID/RGRAM/SMOKE/UNITS;
numstat 608/232/1/1/58; seal 2262 offset +94;
RC_N 69/70; C py-line mirrors T99758/T99763/T99768/
T99783/T99798/T99818 EXACT; M/RM/RQ-tails 16/16 NEW;
no DISSENT/FLAG on b487 (per GATE filename+body survey).
Convention splits (code facts identical, ledger
phrasing per-seat convention, precedent b486):
uniform — GATE TRUE-uniform-29th (sweep accounting
owns the count) vs viewer NOT-TRUE (C10 DIVERGE
10/10): viewer stays 39-NOT.
RQ==M absent this tier (M DISJOINT vs RQ/RM) —
viewer evens 58 held / odds 60 held (b486 was 58th even).
Full/diff survey 37 held (b487 diff-flavor).

## Chain state for r84+ (viewer ledger)
- TRUE-uniform 39 (b487 NOT: C10 DIVERGE + S1 SAME-sig-
  but-cells-diverge; odd band).
- S-F tables-lag 44 (impl 80/82/75/69 == census excl).
- RQ==M evens 58 held / odds 60 held (b487 absent).
- Full/diff survey 37 held (b487 diff).
- Seal +94 vs CLOSED-T10P stable (2168/2262).
- aae d6e27c97 pinned-stable. rgramc sha bde8ed4c
  (recorded, never transcribed).
- Content-line variance 232 (rgram +232 carry).
- AC b84-87 a3/09/81/68 (b85 0x09 noted first-hand).
- 348 pins contiguous 148629..148976, no RED anywhere.
  RC_N 69 (P378->P379 70->69 VARIES; port anchor prev
  _T10P378RC_N=70 verified 1-hit).

Verdict: PASS. Ready for merge (oldest-first).
