# VERIFY-38e3a831 b491 T10P383 pins 150021..150368 (348 pins) PASS

Seat encode-viewer r84d, first-hand. Band = 6d27ab5a (py merge
w2b@46adc59a P383, +6 tiers +58 pins, RGRAM-GREEN 22760/22760
+ SMOKE-GREEN first-hand) + 38e3a831 (C port). Base a7a890a8
(b490 tip, 2280 tiers sealed). Banked Next-P383 consumed FIRST
+ corroborated EXACT at boot (NOTE-viewer-r84d-hb1:
Q-1131/A-966 heads read, Q+A agree; scoped sig-share vs lane
code 46adc59a + pin endpoints in T10P3830/1/A/C/Q/R comments).
b490 NOT re-verified (base only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r84d/
(fresh detached worktrees tree-491BASE @ a7a890a8 +
tree-491BAND @ 38e3a831; seat build dirs build491/ (base) +
build491BAND/ (band); no branch switch; cport lane worktree
untouched; no push).

Method note: 6 battery scripts + pre491 carried r84c->r84d
(path+tag fix), py_compile 7/7 PASS. IN-PROCESS verified
(rgram imported once, ct-cache reads in-process; subprocess =
grep/git only). BANDSHA/seal/numstat/RC_N-BAND/CLOSED383 FILLs
filled at landing from first-hand port msg + numstat + battery
run. One script bug fixed to match verified code facts (never
to force GREEN): edges T-head b1-const index (oracle ab/4c
exactly right; check now asserts b0==ab AND b1==4c). No
wall-check refinement needed (0 bare hits). CLOSED383-6
adapted pre-run (first-hand grep: 6 new region lines, NO
old-tier homonym — same as b490 pattern, recorded not
assumed). pre491.py 76/76 GREEN first-hand (bank+base+oracle;
r84c prose said 70/70 on the identical script — undercount).

## FAST (seat-built binaries, BUILDDIR=r84d/build491BAND, NVME workdirs)
- Build: make -C tree-491BAND/src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11380/11380 covered=11380/11380 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat band binary).
  Single-writer seat run: fully GREEN.
- RGRAM py 22760/22760 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22702+58 = 11380x2.
- CMP491 GREEN: py 22760 PASS; C PYID 11380/11380 + GREEN.
- SETEQ491 GREEN: py 22760 == PINS 22760 (xor 0);
  PINS-N == for 11380 (xor 0); base PINS 22702 == forbase
  11351 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 150021..150368 exact, all in-band.
  for-added 29 = [150021, 150022, 150023, 150024, 150030,
  150031, 150037, 150038, 150039, 150040, 150043, 150044,
  150047, 150048, 150049, 150064, 150065, 150080, 150081,
  150096, 150112, 150113, 150143, 150144, 150208, 150271,
  150272, 150273, 150368] == BANK29 EXACT.
  (S0/S1 + A 2-sig/mid-pairs/tail-pair + C head/mid/tail
  pairs + Q head/mid-pairs/mid/tail + T head/edge-pair/mid/
  edge-triple/tail.)
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 band + 22/0 base
  (tests/test_units.py).

## TABAUDIT (tabaudit491.py 106 PASS 0 FAIL)
- S0 5f522926 (len168) NEW-sig 40/84 vs P382PB0, positions
  [3,4,5,22,23,30-43,48,52-71], b0b1b2-IN (2SIG: 65 NEW).
  S1 4c000000 (len176) NEW-sig 74/88 vs P382PB1, positions
  [0,4-79,84,85,86,87], b0-IN. Both C-eq-py.
  S1 DIFFERS-sig-from-own-C10 (79x10; 10x10 DIVERGE).
- C10 staged == oracle 10/10, 10/10 DIVERGE, sig 4d000000.
- M tables AM16x9/CM10x2/M16x7/QR4x1/RM16x8/RQ16x7, all distinct,
  all C-eq-py; M-EQ-RQ lists (overlap 16, positional 16:
  RQ==M PRESENT, ODD band — odds ledger event); M-tails/RM-tails
  16/16 ALL NEW vs P382T RM and RQ.
  0-overlap vs P382 all six (widths 9v7/2v5/7v8/1v4/8v7/7v6).
- Const tables AC77/CC84/QC78/RC71 == census 77/84/78/71;
  missing AC-[0,1,4,5,10,11,16,80-83]/CC-[4,5,84,85]/
  QC-[4,5,20,21,22,80-84]/RC-[4,5,20,21,22,28-31,76-83];
  AC2-3 00/00 (AC0-1 absent); AC84-87 3f/ac/85/3e;
  CC0-3 4d000000; CC84-85 absent / CC86-87 93/60;
  QC0-3 cb040000; QC84 absent / QC85-87 2e/93/60;
  RC0-1 ab/4c; RC84-87 9e/2e/93/60.
- R1 tails rows 1e2e9360/3e2e9360/5e2e9360/7e2e9360;
  suffix=tshare=subseq=(3,3,3,3,3,3);
  QM7shared 48; Tring 9e2e9360 both ends; Qb8083 row0
  77f8f54e; Tb8083 samerow-eq + nextrow-ne (SWAPPED).
- Guards: py sing 788->790 +2, ranges 962->966 +4, elif
  50/50; C sing 793->795 +2, ranges 984->988 +4,
  else-if 0/0. RC_N band 71 / base 70 (70->71;
  band 71 == RC count, cutter-regen CONFIRMED by this run,
  1-hit each). CLOSED-T10P 2186->2192 +6
  (CLOSED383 = 6 new region lines, no homonym).

## EDGES (edges491.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 0f+2off, b5 const 94 NO step, b0 2SIG 65+C3x15);
  C 10/10 (b4 2f+2off, b5 const 94, b0 const 4d);
  Q 64/64 (b4 43+2off exact-set 64/64 distinct, b5 const 94
  NO edge, b0 const cb);
  R 256/256 (b4 c3+2off 256vals/128uniq, b5 94+(off>=31)+
  (off>=159), b0 const ab, b1 const 4c, b84-87 9e2e9360
  256/256). ff exactly [150143, 150271]. Edge pairs
  ff/94->01/95 (150143->150144) + ff/95->01/96
  (150271->150272). Heads/tails spot values all exact
  (S0 0b/94, S1 0d/94, A0 0f/94, A-tail 2d/94, C0 2f/94,
  C-tail 41/94, Q0 43/94, Q-tail c1/94, T-head ab/4c/c3/94,
  T-tail c1/96). Tail rav sha == PINS g-z150368 (full sha
  in edges491.log), rawlen 104.

## SUPPLEMENT (supplement491.py 30 PASS 0 FAIL)
- R1 full-tail triples (3,3,3,3,3,3) all three metrics.
- AC84-87 3fac853e; CC84-85 absent + CC86-87 9360;
  QC84 absent + QC85-87 2e9360; RC84-87 9e2e9360.
- Oracle b0: P382 PBA 7ex16, P383 PBA 65x1+C3x15 (65+C3 NEW);
  P382 C10 45x10, P383 C10 4dx10 (4d NEW-sig, DIFFSIG).
- Guards re-verified (same deltas as TABAUDIT).
- numstat a7a890a8..38e3a831: rgramc.c 608/0, rgram.py
  229/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673...110785 pinned-stable, seat-built band).
- for-added 29-set stable (== seteq list above).
- Wall: `aea` 0 on added lines (837 added lines, 0 hits —
  no refinement needed this band).
- Seal 2286 (+6 vs b490 2280, port msg) vs CLOSED-T10P 2192
  (+6): offset +94 stable (base 2280-2186).
- rgramc sha256 bd5a303b37e3c4d436ac63764285f95624925f1f
  413efa6f80920dea3e01c8de (recorded, never transcribed).

## GATE reconciliation (GATE-38e3a831 read first-hand)
Values-agree on EVERY checkable metric, no slip:
for-added 29 set IDENTICAL (programmatic compare TRUE);
S0/S1 sigs+diffs (40/84, 74/88, S1-vs-C10 79/88,
DIFFSIG); M widths 9/2/7/1/8/7; QR 1e/3e/5e/7e; R2 rows +
(3,3,3,3,3,3) all three metrics; missing sets EXACT;
consts 77/84/78/71; M/RM-tails NEW 16/16 both; 0-overlaps +
widths; VPOS 10/3/9/17; guards (788/790, 962/966, 793/795,
984/988, elif 50, else-if 0); seal 2286 offset +94; CLOSED
2186/2192; numstat 608/229/1+1/58 + leg attribution (C-port
leg = rgramc.c only; PY-merge leg = rgram.py + for-line +
PINS); quiz-bank empty; aae d6e27c97; rgramc bd5a303b;
PINS 22762 rows (+58); RGRAM C 22760 (viewer FAST covers C
via seat PYID + cmp: split noted); edge pins + formulas +
ff 2 total; embeds 0b/94 + 0d/94; b0/b1 consts; ring const;
seal/CLOSED deltas; A-966 CONFIRM 51/51 cited by GATE,
matches banked; cutter hb15 PORT-CLOSED counts (SET-EQ 22760
+ PYID 11380/11380 + probes 29/29 + UNITS 22 + SMOKE x2 +
0 DISSENT) agree.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487-b490 + CLAIM r80):
uniform — GATE (sweep) counts committed tables; viewer P338
dispute OPEN/deferred, NOT re-litigated: viewer TRUE-uniform
39 held (C10 DIVERGE 10/10).
RQ==M — GATE silent on M==RQ positional (states M/RQ tables
only); viewer ledger: odds 60 -> 61 (b491 ODD PRESENT,
positional 16/16 first-hand), evens 60 held. No DISSENT.
C-leg RGRAM — GATE ran RGRAM C 22760/22760; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
S-F lag — GATE "no writer lag this tier" (impl==census);
viewer counter held at 44.
Merge-subject note: PY-merge applied as single-parent commit
6d27ab5a on a7a890a8 (not a true merge; ^2 absent) — content
gate from C-port commit unaffected; parent-chain YES first-hand.
GATE-only metrics (no viewer counterpart, no conflict):
S1-vs-prev-C10 58/88; regen temps _t7581-96/_i4607+/_b4606+;
RGRAM C full-battery PASS-set cmp.

## Chain state for b492 + r85 (viewer ledger)
- TRUE-uniform 39 held (b491: viewer convention NOT-TRUE, C10
  DIVERGE; P338 dispute OPEN).
- S-F tables-lag 44 held (b491 no-lag tier: impl 77/84/78/71
  == census excl).
- RQ==M odds 60 -> 61 (b491 ODD PRESENT) / evens 60 held.
- Full/diff survey 37 held (b491 diff-flavor: 2SIG-PBA +
  DIFFSIG-C10 structure continues).
- Seal +94 vs CLOSED-T10P stable (2192/2286).
- aae d6e27c97 pinned-stable. rgramc sha recorded (build491BAND).
- Content-line variance 229 (rgram +229 this band).
- AC b84-87 3f/ac/85/3e (band value; was e3/6d/98/27).
- RC_N 71 (P382->P383 70->71).
- 348 pins contiguous 150021..150368, no RED anywhere.

Verdict: PASS. Ready for merge (oldest-first).
