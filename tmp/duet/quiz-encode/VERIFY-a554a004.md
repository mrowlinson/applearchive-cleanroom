# VERIFY-a554a004 b488 T10P380 pins 148977..149324 (348 pins) PASS

Seat encode-viewer r83b, first-hand. Band = 2ba13ca6 (py merge
w2b@5870ae51 P380, +6 tiers +58 pins, RGRAM-GREEN 22586/22586
+ SMOKE-GREEN first-hand) + a554a004 (C port). Base ae87c904
(b487 tip, 2262 tiers sealed). Banked Next-P380 consumed FIRST
+ corroborated EXACT at seat boot (NOTE-viewer-r83b-hb1:
Q-1128/A-963 heads read, Q+A agree; scoped sig-share vs lane
code 5870ae51 + pin endpoints in T10P3800/T10P380R comments).
b484-b487 NOT re-verified (bases only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r83b/
(fresh detached worktrees tree-488BASE @ ae87c904 +
tree-488BAND @ a554a004; seat build dir build/; no branch
switch; cport lane worktree untouched; no push).

Method note: 6 battery scripts pre-written during poll-wait from
banked Q-1128/A-963 + lane PY commit 5870ae51 (git show, no
checkout) + ct-cache oracle, py_compile 6/6 PASS; BANDSHA/seal/
numstat/for29 FILLs filled at landing from first-hand port msg +
numstat + battery run. TABAUDIT needed 2 script-bug fixes at
battery time (CC86-87 R4-partial present, not absent; CLOSED
T10P380 count 7 = old-tier homonym + 6 new) — both corrected TO
verified code facts, never to force GREEN.

## FAST (seat-built binaries, BUILDDIR=r83b/build, NVME workdirs)
- Build: make -C src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11293/11293 covered=11293/11293 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary). Single-writer
  seat run: fully GREEN (resolves r69b-hb5 PYID nuance first-hand:
  no single tainted log; clean 11293/11293 exists).
- RGRAM py 22586/22586 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22528+58 = 11293x2.
- cmp488.py GREEN: py 22586 PASS; C PYID 11293/11293 + GREEN.
- seteq488.py GREEN: py 22586 == PINS 22586 (xor 0);
  PINS-N == for 11293 (xor 0); base PINS 22528 == forbase
  11264 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 148977..149324 exact, all in-band.
  for-added 29 = [148977, 148978, 148979, 148980, 148991,
  148992, 148993, 148994, 148995, 148996, 148999, 149000,
  149003, 149004, 149005, 149020, 149021, 149036, 149037,
  149052, 149068, 149069, 149119, 149120, 149183, 149247,
  149248, 149249, 149324]
  (S0/S1 + A head/edge/tail pairs + C head/mid/tail pairs +
  Q head/mids/tail + R head/edge-pair/mid/edge-triple/tail;
  A edge-pair + both R edge groups pair-covered).
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 (tests/test_units.py).

## TABAUDIT (tabaudit488.py 106 PASS 0 FAIL)
- S0 5d6af627 (len168) NEW-sig 32/84 vs P379PB0, positions
  [3,4,5,22-30,33,34,36-41,64-71,80-83], b3-IN b0b1b2-same.
  S1 43000000 (len176) NEW-sig 43/88 vs P379PB1, positions
  [0,4,5,19,26,27,34-46,48-59,68-75,84-87], b0-IN b1b2b3-same.
  Both C-eq-py. S1 DIFFERS-sig-from-own-C10 (54x10, cells
  DIVERGE 10/10).
- C10 staged == oracle 10/10, 10/10 DIVERGE, [0] sig
  4f000000, S1-vs-C10 diffs 54x10.
- M-tables AM16x7/CM10x2/M16x6/QR4x4/RM16x7/RQ16x6, all distinct,
  all C-eq-py; M-EQ-RQ lists (overlap 16, positional 16:
  RQ==M PRESENT, even-band ledger event); M/RM-tails 16/16 ALL
  NEW vs P379T RM and RQ.
  0-overlap vs P379 all six (widths 7v6/2v4/6v7/4v4/7v8/6v9).
- Const tables AC79/CC84/QC76/RC73 == census 79/84/76/73;
  missing AC-[4,5,6,7,9,80-83]/CC-[4,5,84,85]/
  QC-[4,5,10,11,80-87]/RC-[4,5,10,11,16,17,18,76-83];
  AC0-3 30040000; AC84-87 3b/72/84/a1;
  CC0-3 4f000000; CC84-85 absent (R4), CC86-87 c2/fc;
  QC0-3 6a050000; QC84-87 absent (R4 lanes);
  RC0-1 6a/4f; RC84-87 29a9f7fd.
- R1 tails exact rows; suffix=tshare=subseq=(3,3,0,3,0,0);
  QM6shared 48; ring b84-87 29a9f7fd both ends;
  Q b80-83 row0 a8e3b5b6; T b80-83 split.
- Guards: py sing 782->784 +2, ranges 950->954 +4, elif
  50/50; C sing 787->789 +2, ranges 972->976 +4,
  else-if 0/0. RC_N band 73 / base 69 (69->73 VARIES;
  73 pre-filled from cport-r69 regen, CONFIRMED by this run
  against landed code, 1-hit each). CLOSED-T10P 2168->2174 +6
  (CLOSED380 count 7 = 1 old-tier T42657 homonym base-identical
  + 6 new region lines).

## EDGES (edges488.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 e7+2off, b5 8b+(off>=13), edge 148991->148992);
  C 10/10 (b4 07+2off, b5 const 8c);
  Q 64/64 (b4 1b+2off range 1b..99, b5 const 8c
  NOEDGE, b0 6a); R 256/256 (b4 9b+2off,
  b5 8c+(off>=51)+(off>=179), b0 6a, b1 const 4f,
  b84-87 29a9f7fd 256/256). ff exactly [148991, 149119,
  149247]. Edge pairs ff/8b->01/8c (148991->148992) +
  ff/8c->01/8d (149119->149120) +
  ff/8d->01/8e (149247->149248). Heads/tails spot
  values all exact (S0 e3/8b, S1 e5/8b, A0 e7/8b, A1 05/8c,
  C0 07/8c, C1 19/8c, Q0 1b/8c, Q1 99/8c,
  T-head 9b/8c, T-tail 99/8e). Tail rav sha
  9d2f234f12f763d5fd8b927bdba94d2cfe36d420651d9faa86717c8ae17242b3
  == PINS g-z149324, rawlen 104.

## SUPPLEMENT (supplement488.py 29 PASS 0 FAIL)
- R1 full-tail triples (3,3,0,3,0,0) all three metrics.
- AC84-87 3b7284a1; CC84-85 absent + CC86-87 c2fc;
  QC84-87 absent; RC84-87 29a9f7fd.
- Oracle b0: P379 PBA 4dx16, P380 PBA 30x16 (30 NEW);
  P379 C10 4fx10, P380 C10 4fx10 (4f REPEAT-sig,
  cells diverge by formula).
- Guards re-verified (same deltas as TABAUDIT).
- numstat ae87c904..a554a004: rgramc.c 608/0, rgram.py
  232/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673cc73eee061ffdbd7... pinned-stable,
  seat-built).
- for-added 29-set stable (== seteq list above).
- Wall full scope: 0 `aea` on added lines.
- Seal 2268 (+6 vs b487 2262, port msg) vs CLOSED-T10P
  2174 (+6): offset +94 stable (base 2262-2168).
- rgramc sha256
  02cb4d5f7fe1927f780da79bd94ba6bb490bc29d0c9bd6075ebd20a84b872b41
  (recorded, never transcribed; computed from seat binary).

## GATE reconciliation (GATE-a554a004 read first-hand)
Values-agree on EVERY checkable metric, no slip:
for-added 29 set IDENTICAL; S0/S1 sigs+diffs (32/84, 43/88,
S1-vs-C10 54x10); R1 rows + (3,3,0,3,0,0) all three metrics;
missing sets EXACT; consts 79/84/76/73; VPOS 9/3/15 (quad:
GATE 11 vs Q-1128 13 — sweep-side accounting phrasing, code
lanes identical); M/RM/RQ-tails 16/16 NEW; 0-overlaps +
widths; guards (782/784, 950/954, 787/789, 972/976, elif 50,
else-if 0); seal 2268 offset +94; CLOSED 2168/2174;
numstat 608/232/1+1/58; for-line superset removed 0;
PINS 22588 rows (2 hdr + 22586); edge pins + formulas
(e7/8b/13, 07/8c, 1b/8c, 9b/8c/51/179) + ff 1+0+0+2;
embeds e3/8b + e5/8b; b0/b1 consts (A 30, C 4f, Q 6a,
R 6a/4f); RC ring 29a9f7fd; tier-head C 74 pairs NEW;
QM6shared pattern; Tb split; Qb row0 (probe-printed).
No DISSENT/FLAG on b488 (GATE quiz poll + filename/body
survey). A-963 CONFIRM 48/48 cited by GATE, matches banked.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487):
uniform — GATE silent (functional PASS) vs viewer NOT-TRUE
(C10 DIVERGE 10/10): viewer TRUE-uniform 39 held.
RQ==M — GATE "reported, not gated" vs viewer ledger event:
viewer evens 58 -> 59 (b488 PRESENT).
C-leg RGRAM — GATE ran RGRAM C 22586/22586; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
PYID nuance — GATE msg claims 11293/11293 GREEN; canonical
r69 log 11270/11293 RED (23 explained race FAILs); this
seat's clean single-writer PYID 11293/11293 GREEN resolves
it first-hand: full GREEN coverage exists.
S-F lag — GATE "no-lag this tier" (impl==census); viewer
counter held at 44 pending sweep accounting (precedent: viewer
does not own the count).

## Chain state for r84+ (viewer ledger)
- TRUE-uniform 39 (b488 NOT: C10 DIVERGE + S1 DIFFERS-sig;
  even band).
- S-F tables-lag 44 held (b488 no-lag tier: impl 79/84/76/73
  == census excl; counter ownership sweep-side).
- RQ==M evens 59 (b488 PRESENT; was 58) / odds 60 held.
- Full/diff survey 37 held (b488 diff-flavor).
- Seal +94 vs CLOSED-T10P stable (2174/2268).
- aae d6e27c97 pinned-stable. rgramc sha 02cb4d5f
  (recorded, never transcribed).
- Content-line variance 232 (rgram +232 carry).
- AC b84-87 3b/72/84/a1.
- 348 pins contiguous 148977..149324, no RED anywhere.
  RC_N 73 (P379->P380 69->73 VARIES; port anchor prev
  _T10P379RC_N=69 verified 1-hit).

Verdict: PASS. Ready for merge (oldest-first).
