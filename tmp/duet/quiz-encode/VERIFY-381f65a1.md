# VERIFY-381f65a1 b494 T10P386 pins 151065..151412 (348 pins) PASS

Seat encode-viewer r85b, first-hand. Band = 65b59899 (py merge
w2b@15adb3a8 P386, +6 tiers +58 pins, RGRAM-GREEN 22934/22934
+ SMOKE-GREEN first-hand) + 381f65a1 (C port). Base 3158f991
(b493 tip, 2298 tiers sealed). Banked Next-P386 consumed FIRST
+ corroborated EXACT at boot (NOTE-viewer-r85b-hb70:
Q-1134/A-969 heads read, Q+A agree; scoped sig-share vs lane
code 15adb3a8 + pin endpoints in T10P3860/1/A/C/Q/R comments).
b493 NOT re-verified (base only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r85b/
(fresh detached worktrees tree-494BASE @ 3158f991 +
tree-494BAND @ 381f65a1; seat build dirs build493BAND-as-base
+ build494BAND/ (band); no branch switch; cport lane worktree
untouched; no push).

Method note: 7 battery scripts written fresh per-band (counts/
/ranges/oracle differ per band), py_compile 7/7 PASS.
IN-PROCESS verified (rgram imported once, ct-cache reads
in-process; subprocess = grep/git only; lane fast suites run
as-is per PARENT-BATTERY-INPROCESS-01: single-import,
warm-cache, no timeouts — py 5.5s, C 27.3s wall first-hand).
BANDSHA/seal/numstat/RC_N-BAND/CLOSED386 FILLs filled at
landing from first-hand port msg + numstat + battery run.
No script refinement needed (0 bare wall hits).
CLOSED386-6 adapted pre-run (first-hand grep: 6 new region
lines, NO old-tier homonym — same as b491-b493 pattern,
recorded not assumed). pre494.py 59/59 GREEN first-hand
(bank+base+oracle).

## FAST (seat-built binaries, BUILDDIR=r85b/build494BAND, NVME workdirs)
- Build: make -C tree-494BAND/src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11467/11467 covered=11467/11467 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat band binary).
  Single-writer seat run: fully GREEN.
- RGRAM py 22934/22934 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22876+58 = 11467x2.
- CMP494 GREEN: py 22934 PASS; C PYID 11467/11467 + GREEN.
- SETEQ494 GREEN: py 22934 == PINS 22934 (xor 0);
  PINS-N == for 11467 (xor 0); base PINS 22876 == forbase
  11438 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 151065..151412 exact, all in-band.
  for-added 29 = [151065, 151066, 151067, 151068, 151074,
  151075, 151081, 151082, 151083, 151084, 151087, 151088,
  151091, 151092, 151093, 151108, 151109, 151124, 151125,
  151140, 151156, 151157, 151167, 151168, 151232, 151295,
  151296, 151297, 151412] == BANK29 EXACT.
  (S0/S1 + A head/mid/tail pairs + C head/mid/tail pairs +
  Q head/mid-pairs/mid/tail + R head/edge-pair/mid/
  edge-triple/tail.)
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 band + 22/0 base
  (tests/test_units.py).

## TABAUDIT (tabaudit494.py 104 PASS 0 FAIL)
- S0 5f943026 (len168) sig-REPEAT 32/84 vs P385PB0, positions
  [4,5,32-35,37-40,42-51,64-75], b0b1b2b3-same.
  S1 4d000000 (len176) NEW-sig 63/88 vs P385PB1, positions
  [0,4-11,13-19,36-43,45-79,84-87], b0-IN. Both C-eq-py.
  S1 DIFFERS-sig-from-own-C10 (24x10; 10x10 DIVERGE).
- C10 staged == oracle 10/10, 10/10 DIVERGE, sig 4c000000.
- M tables AM16x9/CM10x4/M16x8/QR4x4/RM16x7/RQ16x8, all distinct,
  all C-eq-py; M-EQ-RQ lists (overlap 16, positional 16:
  RQ==M PRESENT, EVEN band — evens ledger event); M-tails/RM-tails
  16/16 ALL NEW vs P385T RM and RQ.
  0-overlap vs P385 all six (widths 9v8/4v2/8v8/4v2/7v6/8v8).
- Const tables AC77/CC82/QC74/RC71 == census 77/82/74/71;
  missing AC-[4,5,20-24,80-83]/CC-[4,5,84-87]/
  QC-[4,5,28-31,80-87]/RC-[4,5,27-31,34,35,76-83];
  AC84-87 44/a7/ca/91; CC0-3 4c000000; CC84-87 all absent;
  QC0-3 c0040000; QC84-87 all absent; RC0-1 e6/4d;
  RC84-87 14/0d/a7/c6.
- R4 tails rows 80c8ccc0/b40ca7c6/d40ca7c6/f40ca7c6;
  suffix=tshare=subseq=(0,0,0,3,3,3);
  QM8shared 48; Tring 140da7c6 both ends; Qb8083 row0
  5ba9599e; T-b8083 samecol-eq + nextcol-ne; T-b7679
  samerow-eq + nextrow-ne (STANDARD-split).
- Guards: py sing 794->796 +2, ranges 974->978 +4, elif
  50/50; C sing 799->801 +2, ranges 996->1000 +4,
  else-if 0/0. RC_N band 71 / base 72 (72->71 VARIES;
  band 71 == RC count, cutter-regen CONFIRMED by this run,
  1-hit each). CLOSED-T10P 2204->2210 +6
  (CLOSED386 = 6 new region lines, no homonym).

## EDGES (edges494.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 37+2off, b5 const 9c NO step, b0 1SIG c1 x16);
  C 10/10 (b4 57+2off, b5 const 9c, b0 const 4c);
  Q 64/64 (b4 6b+2off exact-set 64/64 distinct, b5
  const 9c NO edge, b0 const c0);
  R 256/256 (b4 eb+2off 256vals/128uniq, b5 9c+(off>=11)+
  (off>=139), b0 const e6, b1 const 4d, b84-87 140da7c6
  256/256). ff exactly [151167, 151295]. Edge pairs
  ff/9c->01/9d (151167->151168) + ff/9d->01/9e
  (151295->151296). Heads/tails spot values all exact
  (S0 33/9c, S1 35/9c, A0 37/9c, A-tail 55/9c, C0 57/9c,
  C-tail 69/9c, Q0 6b/9c, Q-tail e9/9c, T-head e6/4d/eb/9c,
  T-tail e9/9e). Tail rav sha == PINS g-z151412
  (86b68a6350e19828...), rawlen 104.

## SUPPLEMENT (supplement494.py 30 PASS 0 FAIL)
- R4 full-tail triples (0,0,0,3,3,3) all three metrics.
- AC84-87 44a7ca91; CC84-87 all absent; QC84-87 all absent;
  RC84-87 140da7c6.
- Oracle b0: P385 PBA 6bx16, P386 PBA c1x16 (c1 NEW);
  P385 C10 46x10, P386 C10 4cx10 (4c NEW, DIFFSIG).
- Guards re-verified (same deltas as TABAUDIT).
- numstat 3158f991..381f65a1: rgramc.c 608/0, rgram.py
  231/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673... pinned-stable, seat-built band).
- for-added 29-set stable (== seteq list above).
- Wall: `aea` 0 on added lines (839 added lines, 0 hits —
  no refinement needed this band).
- Seal 2304 (+6 vs b493 2298, port msg) vs CLOSED-T10P 2210
  (+6): offset +94 stable (base 2298-2204).
- rgramc sha256 edff851a34b07b91b90432fbb57aad45672dcadc
  85fabed7ce6eea1eaac10c5d (recorded, never transcribed).

## GATE reconciliation (GATE-381f65a1 read first-hand)
Values-agree on EVERY checkable metric, no slip except one
noted GATE-side typo (R-tail b4, below — code facts agree):
for-added 29 set IDENTICAL (programmatic compare TRUE,
gate==mine==bank); S0/S1 sigs+diffs (REPEAT 32/84 + NEW
63/88, S1-vs-C10 24x10, S1-DIFFERS-C10-sig); M widths
9/4/8/4/7/8; QR 80c8ccc0/b40ca7c6/d40ca7c6/f40ca7c6; R4
rows + (0,0,0,3,3,3) all three metrics; missing sets EXACT;
consts 77/82/74/71; M/RM-tails NEW 16/16 both; 0-overlaps +
widths; VPOS 10/5/13/17; guards (794/796, 974/978, 799/801,
996/1000, elif 50, else-if 0); seal 2304 offset +94; CLOSED
2204/2210; numstat 608/231/1+1/58 + leg attribution (C-port
leg = rgramc.c only; PY-merge leg = rgram.py + for-line +
PINS); quiz-bank empty; aae d6e27c97; PINS 22936 lines
(+58); RGRAM C 22934 (viewer FAST covers C via seat PYID +
cmp: split noted); edge pins + formulas + ff 2 total; embeds
33/9c + 35/9c; b0/b1 consts; ring const; seal/CLOSED
deltas; A-969 CONFIRM 48/48 cited by GATE, matches banked;
cutter hb71 PORT-CLOSED counts (SET-EQ 22934 + PYID
11467/11467 + probes 29/29 + UNITS 22 + SMOKE x2 +
0 DISSENT) agree.
GATE-SLIP noted with first-hand evidence (code facts agree,
verdict unaffected): GATE states "R head eb/9c tail ed/9e";
seat triple-confirms tail b4 = 0xE9: (1) oracle pay(151412)
b4/b5 = e9/9e first-hand, (2) counter formula
(0xeb+2*255)&FF = 0xE9, (3) raw lencode ((151412<<1)|1)&FFFF
= 0x9EE9 — plus GATE's own ring b4==formula + b5==raw-lencode
256/256 claims entail e9. Single-hex-digit prose typo (ed vs
e9); no code finding, no DISSENT on the band (flagged here
for sweep correction).
Notation split (values agree, units phrasing differs):
GATE "QR 4/4 8ch" counts hex chars where sibling widths
count bytes (same seat convention as GATE-dc21ad48's "QR 4/4
4ch"); rows exact both sides + "QR 4B vs 2B" bytes line
agrees. No conflict.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487-b493 + CLAIM r80):
uniform — GATE (sweep) counts committed tables; viewer P338
dispute OPEN/deferred, NOT re-litigated: viewer TRUE-uniform
39 held (C10 DIVERGE 10/10).
RQ==M — GATE reports M==RQ 16/16 string-identical SAME-ORDER
("reported, not gated"); viewer ledger: evens 61 -> 62
(b494 EVEN PRESENT, positional 16/16 first-hand), odds 62
held. No DISSENT.
C-leg RGRAM — GATE ran RGRAM C 22934/22934; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
S-F lag — GATE "no writer lag this tier" (impl==census);
viewer counter held at 44.
Merge-subject note: PY-merge applied as single-parent commit
65b59899 on 3158f991 (not a true merge; ^2 absent) — content
gate from C-port commit unaffected; parent-chain YES first-hand.
GATE-only metrics (no viewer counterpart, no conflict):
AC-QC both=69 sameval=30; regen temps _t7629-44/_i4637+/
_b4636+; RGRAM C full-battery PASS-set cmp; insert-position +
dispatch-tail + file-list 117/117.

## Chain state at b494 (viewer ledger)
- TRUE-uniform 39 held (b494: viewer convention NOT-TRUE, C10
  DIVERGE; P338 dispute OPEN).
- S-F tables-lag 44 held (b494 no-lag tier: impl 77/82/74/71
  == census excl).
- RQ==M evens 61 -> 62 (b494 EVEN PRESENT) / odds 62 held.
- Full/diff survey 37 held (b494 diff-flavor: REPEAT-PB +
  DIFFSIG-C10 structure continues).
- Seal +94 vs CLOSED-T10P stable (2210/2304).
- aae d6e27c97 pinned-stable. rgramc sha recorded (build494BAND).
- Content-line variance 231 (rgram +231 this band).
- AC b84-87 44/a7/ca/91 (band value; was 0c/ef/5f/db).
- RC_N 71 (P385->P386 72->71 VARIES).
- 348 pins contiguous 151065..151412, no RED anywhere.

Verdict: PASS. Ready for merge (oldest-first).
