# VERIFY-b396d725 b489 T10P381 pins 149325..149672 (348 pins) PASS

Seat encode-viewer r83b, first-hand. Band = f2c92037 (py merge
w2b@f87b6631 P381, +6 tiers +58 pins, RGRAM-GREEN 22644/22644
+ SMOKE-GREEN first-hand) + b396d725 (C port). Base a554a004
(b488 tip, 2268 tiers sealed). Banked Next-P381 consumed FIRST
+ corroborated EXACT at boot (NOTE-viewer-r83b-hb1:
Q-1129/A-964 heads read, Q+A agree; scoped sig-share vs lane
code f87b6631 + pin endpoints in T10P3810/T10P381R comments).
b484-b488 NOT re-verified (bases only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r83b/
(fresh detached worktrees tree-489BASE @ a554a004 +
tree-489BAND @ b396d725; seat build dir build489/; no branch
switch; cport lane worktree untouched; no push).

Method note: 6 battery scripts pre-written during poll-wait from
banked Q-1129/A-964 + lane PY commit f87b6631 (git show, no
checkout) + ct-cache oracle, py_compile 6/6 PASS; BANDSHA/seal/
numstat/RCN-BAND/for29 FILLs filled at landing from first-hand
port msg + numstat + battery run. One tabaudit addition at
battery time (M-tails-EQ-sibRQ-tails check confirming cutter
claim first-hand; one NameError fixed before run — script bug,
no code finding). CLOSED381-7 pre-fixed for old-T42668 homonym
(same pattern as b488's T42657).

## FAST (seat-built binaries, BUILDDIR=r83b/build489, NVME workdirs)
- Build: make -C src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11322/11322 covered=11322/11322 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary). Single-writer
  seat run: fully GREEN.
- RGRAM py 22644/22644 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22586+58 = 11322x2.
- CMP489 GREEN: py 22644 PASS; C PYID 11322/11322 + GREEN.
- SETEQ489 GREEN: py 22644 == PINS 22644 (xor 0);
  PINS-N == for 11322 (xor 0); base PINS 22586 == forbase
  11293 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 149325..149672 exact, all in-band.
  for-added 29 = [149325, 149326, 149327, 149328, 149334,
  149335, 149341, 149342, 149343, 149344, 149347, 149348,
  149351, 149352, 149353, 149368, 149369, 149375, 149376,
  149400, 149416, 149417, 149503, 149504, 149567, 149631,
  149632, 149633, 149672]
  (S0/S1 + A head/mid pairs + C head/mid/tail pairs + Q head/
  mids/edge-pair/mid/tail + T head/edge-pair/mid/edge-triple/
  tail).
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 (tests/test_units.py).

## TABAUDIT (tabaudit489.py 104 PASS 0 FAIL)
- S0 5d6af627 (len168) REPEAT-sig 30/84 vs P380PB0, positions
  [4-11,34,35,42,45-55,72-79], b0b1b2b3-same.
  S1 4f000000 (len176) NEW-sig 61/88 vs P380PB1, positions
  [0,4-11,13-17,19-27,36,37,40-43,48-55,60-79,84-87],
  b0-IN b1b2b3-same. Both C-eq-py. S1 SAME-sig-as-own-C10
  (40x10, cells DIVERGE 10/10).
- C10 staged == oracle 10/10, 10/10 DIVERGE, [0] sig
  4f000000, S1-vs-C10 diffs 40x10.
- M tables AM16x7/CM10x5/M16x7/QR4x4/RM16x7/RQ16x6, all distinct,
  all C-eq-py; M-ne-RQ lists (overlap 0, positional 0:
  RQ==M ABSENT, odd band); M-tails-EQ-sibRQ-tails (full DIFFER)
  confirming cutter claim first-hand; M/RM-tails 16/16 ALL
  NEW vs P380T RM and RQ.
  0-overlap vs P380 all six (widths 7v7/5v2/7v6/4v4/7v7/6v6).
- Const tables AC79/CC81/QC75/RC73 == census 79/81/75/73;
  missing AC-[4,5,28,29,30,80-83]/CC-[4,5,28,84-87]/
  QC-[4,5,29,34,35,80-87]/RC-[4,5,32,33,40,41,42,76-83];
  AC0-3 f0040000; AC84-87 c7/70/c9/12;
  CC0-3 4f000000; CC84-87 absent (R4 lanes);
  QC0-3 77040000; QC84-87 absent (R4 lanes);
  RC0-1 77/48; RC84-87 a1bd3f25.
- R1 tails exact rows; suffix=tshare=subseq=(1,0,0,0,0,3);
  QM7shared 48; Tring a1bd3f25 both ends;
  Qb8083 row0 0bc8e819; Tb8083 split.
- Guards: py sing 784->786 +2, ranges 954->958 +4, elif
  50/50; C sing 789->791 +2, ranges 976->980 +4,
  else-if 0/0. RC_N band 73 / base 73 (73->73 SAME;
  73 pre-filled from cutter notes, CONFIRMED by this run
  against landed code, 1-hit each). CLOSED-T10P 2174->2180 +6
  (CLOSED381-7 = 1 old-T42668 homonym base-identical
  + 6 new region lines).

## EDGES (edges489.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 9f+2off, b5 const 8e NO step, b0 const f0);
  C 10/10 (b4 bf+2off, b5 const 8e, b0 const 4f);
  Q 64/64 (b4 d3+2off, b5 8e+(off>=23) STEP edge 149375->
  149376, b0 const 77);
  R 256/256 (b4 53+2off, b5 8f+(off>=87)+(off>=215),
  b0 const 77, b1 const 48, b84-87 a1bd3f25 256/256).
  ff exactly [149375, 149503, 149631]. Edge pairs
  ff/8e->01/8f (149375->149376) + ff/8f->01/90
  (149503->149504) + ff/90->01/91 (149631->149632).
  Heads/tails spot values all exact (S0 9b/8e, S1 9d/8e,
  A0 9f/8e, A1 bd/8e, C0 bf/8e, C1 d1/8e, Q0 d3/8e,
  Q1 51/8f, T-head 53/8f, T-tail 51/91). Tail rav sha
  == PINS g-z149672 (full sha recorded in edges489.log),
  rawlen 104.

## SUPPLEMENT (supplement489.py 29 PASS 0 FAIL)
- R1 full-tail triples (1,0,0,0,0,3) all three metrics.
- AC84-87 c770c912; CC84-87 absent; QC84-87 absent;
  RC84-87 a1bd3f25.
- Oracle b0: P380 PBA 30x16, P381 PBA f0x16 (f0 NEW);
  P380 C10 4fx10, P381 C10 4fx10 (4f REPEAT-sig,
  cells diverge by formula).
- Guards re-verified (same deltas as TABAUDIT).
- numstat a554a004..b396d725: rgramc.c 608/0, rgram.py
  233/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673cc73eee061ffdbd7... pinned-stable,
  seat-built).
- for-added 29-set stable (== seteq list above).
- Wall full scope: 0 `aea` on added lines.
- Seal 2274 (+6 vs b488 2274? NO: 2274 vs b488 2268 = +6,
  port msg) vs CLOSED-T10P 2180 (+6): offset +94 stable
  (base 2268-2174).
- rgramc sha256 (recorded in supplement489.log from seat
  binary, never transcribed).

## GATE reconciliation (GATE-b396d725 read first-hand)
Values-agree on EVERY checkable metric, no slip:
for-added 29 set IDENTICAL; S0/S1 sigs+diffs (30/84, 61/88,
S1-vs-C10 40/88 SAME-sig); R1 rows + (1,0,0,0,0,3) all three
metrics; missing sets EXACT; consts 79/81/75/73; VPOS 8/6/13/15
(viewer doesn't track VPOS; code lanes identical); M/RM-tails
NEW 16/16 both; 0-overlaps + widths; guards (784/786,
954/958, 789/791, 976/980, elif 50, else-if 0); seal 2274
offset +94; CLOSED 2174/2180; numstat 608/233/1+1/58;
for-line superset removed 0; PINS 22646 rows (2 hdr + 22644);
edge pins + formulas (9f/8e, bf/8e, d3/8e/23, 53/8f/87/215) +
ff 1+0+1+2 = 3 total; embeds 9b/8e + 9d/8e; b0/b1 consts (A f0,
C 4f, Q 77, R 77/48); RC ring a1bd3f25; tier-head C 74 pairs
pre-staged; QM7shared pattern; Tb split; Qb row0.
No DISSENT/FLAG on b489 (GATE quiz poll + filename/body
survey). A-964 CONFIRM 48/48 cited by GATE, matches banked.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487/b488 + CLAIM r80):
uniform — GATE (sweep) counts b489 TRUE #30 (40/88 SAME-sig);
viewer P338 dispute OPEN/deferred, NOT re-litigated:
viewer TRUE-uniform 39 held (C10 DIVERGE 10/10).
RQ==M — GATE "NOT counted (widths differ)" vs viewer ledger:
viewer odds 60 held (b489 ABSENT).
C-leg RGRAM — GATE ran RGRAM C 22644/22644; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
S-F lag — GATE "no-lag this tier" (impl==census); viewer
counter held at 44 pending sweep accounting.
Merge-subject hash note (GATE: @f87b6631 object missing,
real f87b6631d67366d chain-verified) — content gate from
C-port commit unaffected; my merge-base YES first-hand.

## Chain state for r84+ (viewer ledger)
- TRUE-uniform 39 (b489: viewer convention NOT-TRUE, C10
  DIVERGE; sweep #30 noted as split; P338 dispute OPEN).
- S-F tables-lag 44 held (b489 no-lag tier: impl 79/81/75/73
  == census excl).
- RQ==M odds 60 held (b489 ABSENT) / evens 59 (b488 PRESENT).
- Full/diff survey 37 held (b489 diff-flavor).
- Seal +94 vs CLOSED-T10P stable (2180/2274).
- aae d6e27c97 pinned-stable. rgramc sha recorded (build489).
- Content-line variance 233 (rgram +233 carry).
- AC b84-87 c7/70/c9/12.
- 348 pins contiguous 149325..149672, no RED anywhere.
  RC_N 73 (P380->P381 73->73 SAME).

Verdict: PASS. Ready for merge (oldest-first).
