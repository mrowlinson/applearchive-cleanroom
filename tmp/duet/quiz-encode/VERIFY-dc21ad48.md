# VERIFY-dc21ad48 b492 T10P384 pins 150369..150716 (348 pins) PASS

Seat encode-viewer r85b, first-hand. Band = 70a5ce2c (py merge
w2b@d8b9c892 P384, +6 tiers +58 pins, RGRAM-GREEN 22818/22818
+ SMOKE-GREEN first-hand) + dc21ad48 (C port). Base 38e3a831
(b491 tip, 2286 tiers sealed). Banked Next-P384 consumed FIRST
+ corroborated EXACT at boot (NOTE-viewer-r85b-hb1:
Q-1132/A-967 heads read, Q+A agree; scoped sig-share vs lane
code d8b9c892 + pin endpoints in T10P3840/1/A/C/Q/R comments).
b491 NOT re-verified (base only). NVME scratch
/Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/r85b/
(fresh detached worktrees tree-492BASE @ 38e3a831 +
tree-492BAND @ dc21ad48; seat build dirs build492/ (base) +
build492BAND/ (band); no branch switch; cport lane worktree
untouched; no push).

Method note: 7 battery scripts written fresh per-band (counts/
/ranges/oracle differ per band; HANDOFF-r84 carry warning
heeded: rgram.py +231 here vs +229 b491), py_compile 7/7 PASS.
IN-PROCESS verified (rgram imported once, ct-cache reads
in-process; subprocess = grep/git only; lane fast suites run
as-is per PARENT-BATTERY-INPROCESS-01: single-import,
warm-cache, no timeouts — py 5.6s, C 36.4s wall first-hand;
gate decision recorded NOTE-viewer-r85b-hb36).
BANDSHA/seal/numstat/RC_N-BAND/CLOSED384 FILLs filled at
landing from first-hand port msg + numstat + battery run.
One script refinement with recorded cause (never to force
GREEN): supplement wall check (2 bare-'aea' substring hits,
both identical quoted oracle hex blob "aea1e56e0723ab",
RM-table entry PY+C identical; identifier-form 0 —
b490 precedent). CLOSED384-6 adapted pre-run (first-hand
grep: 6 new region lines, NO old-tier homonym — same as b490/
b491 pattern, recorded not assumed). pre492.py 55/55 GREEN
first-hand (bank+base+oracle).

## FAST (seat-built binaries, BUILDDIR=r85b/build492BAND, NVME workdirs)
- Build: make -C tree-492BAND/src/c rgramc + aae, rc=0, 0 warnings.
- RGRAMC-PYID 11409/11409 covered=11409/11409 RGRAMC-GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat band binary).
  Single-writer seat run: fully GREEN.
- RGRAM py 22818/22818 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py). = 22760+58 = 11409x2.
- CMP492 GREEN: py 22818 PASS; C PYID 11409/11409 + GREEN.
- SETEQ492 GREEN: py 22818 == PINS 22818 (xor 0);
  PINS-N == for 11409 (xor 0); base PINS 22760 == forbase
  11380 (xor 0); for-added 29, removed 0; PINS-new == added;
  range 150369..150716 exact, all in-band.
  for-added 29 = [150369, 150370, 150371, 150372, 150378,
  150379, 150385, 150386, 150387, 150388, 150391, 150392,
  150395, 150396, 150397, 150399, 150400, 150412, 150413,
  150444, 150460, 150461, 150527, 150528, 150591, 150655,
  150656, 150657, 150716] == BANK29 EXACT.
  (S0/S1 + A head/mid/tail pairs + C head/mid/tail pairs +
  Q head/edge-pair/mids/tail + R head/edge-pair/mid/
  edge-triple/tail.)
- SMOKE-GREEN 6/6 band + 6/6 base (tests/smoke.sh, default
  oracle backend). UNITS-GREEN 22/0 band + 22/0 base
  (tests/test_units.py).

## TABAUDIT (tabaudit492.py 106 PASS 0 FAIL)
- S0 5f522926 (len168) sig-REPEAT 32/84 vs P383PB0, positions
  [4-11,13-18,44-47,50-55,72-79], b0b1b2b3-same.
  S1 4c000000 (len176) sig-REPEAT 67/88 vs P383PB1, positions
  [4-11,13-63,80-87], b0b1b2b3-same. Both C-eq-py.
  S1 DIFFERS-sig-from-own-C10 (45x10; 10x10 DIVERGE).
- C10 staged == oracle 10/10, 10/10 DIVERGE, sig 4f000000.
- M tables AM16x7/CM10x2/M16x6/QR4x2/RM16x7/RQ16x6, all distinct,
  all C-eq-py; M-EQ-RQ lists (overlap 16, positional 16:
  RQ==M PRESENT, EVEN band — evens ledger event); M-tails/RM-tails
  16/16 ALL NEW vs P383T RM and RQ.
  0-overlap vs P383 all six (widths 7v9/2v2/6v7/2v1/7v8/6v7).
- Const tables AC79/CC84/QC78/RC73 == census 79/84/78/73;
  missing AC-[4,5,29,34,35,80-83]/CC-[4,5,84,85]/
  QC-[4,5,40,41,80-85]/RC-[4,5,39,40,41,46,47,76-83];
  AC84-87 bd/6e/92/0b; CC0-3 4f000000; CC84-85 absent /
  CC86-87 75/9b; QC0-3 6b040000; QC84-85 absent /
  QC86-87 75/9b; RC0-1 6b/46; RC84-87 53/09/75/9b.
- R2 tails rows d308759b/f308759b/1309759b/3309759b;
  suffix=tshare=subseq=(3,2,2,2,2,3);
  QM6shared 48; Tring 5309759b both ends; Qb8083 row0
  183d5add; T-RQ samerow-eq + nextrow-ne; T-RM samecol-eq
  + nextcol-ne (SWAPPED-split).
- Guards: py sing 790->792 +2, ranges 966->970 +4, elif
  50/50; C sing 795->797 +2, ranges 988->992 +4,
  else-if 0/0. RC_N band 73 / base 71 (71->73;
  band 73 == RC count, cutter-regen CONFIRMED by this run,
  1-hit each). CLOSED-T10P 2192->2198 +6
  (CLOSED384 = 6 new region lines, no homonym).

## EDGES (edges492.py GREEN)
- pay84 1/1, pay88 347/347, lenok 92/92; A 16/16
  (b4 c7+2off, b5 const 96 NO step, b0 1SIG ff x16);
  C 10/10 (b4 e7+2off, b5 const 96, b0 const 4f);
  Q 64/64 (b4 fb+2off exact-set 64/64 distinct, b5
  96+(off>=3) edge, b0 const 6b);
  R 256/256 (b4 7b+2off 256vals/128uniq, b5 97+(off>=67)+
  (off>=195), b0 const 6b, b1 const 46, b84-87 5309759b
  256/256). ff exactly [150399, 150527, 150655]. Edge pairs
  ff/96->01/97 (150399->150400) + ff/97->01/98
  (150527->150528) + ff/98->01/99 (150655->150656).
  Heads/tails spot values all exact (S0 c3/96, S1 c5/96,
  A0 c7/96, A-tail e5/96, C0 e7/96, C-tail f9/96, Q0
  fb/96, Q-tail 79/97, T-head 6b/46/7b/97, T-tail 79/99).
  Tail rav sha == PINS g-z150716 (fa6a79e0ba8ac6c4...),
  rawlen 104.

## SUPPLEMENT (supplement492.py 31 PASS 0 FAIL)
- R2 full-tail triples (3,2,2,2,2,3) all three metrics.
- AC84-87 bd6e920b; CC84-85 absent + CC86-87 759b;
  QC84-85 absent + QC86-87 759b; RC84-87 5309759b.
- Oracle b0: P383 PBA 2SIG (65+C3x15), P384 PBA ffx16
  (ff NEW); P383 C10 4dx10, P384 C10 4fx10 (4f NEW,
  DIFFSIG).
- Guards re-verified (same deltas as TABAUDIT).
- numstat 38e3a831..dc21ad48: rgramc.c 608/0, rgram.py
  231/0, test_rgram.sh 1/1, PINS 58/0; quiz-bank empty
  in range; aae sources untouched (aae sha256
  d6e27c97ced21673... pinned-stable, seat-built band).
- for-added 29-set stable (== seteq list above).
- Wall: identifier-form `aea` 0 on added lines (839 added
  lines; 2 bare-hex-blob hits recorded, oracle data,
  PY+C identical).
- Seal 2292 (+6 vs b491 2286, port msg) vs CLOSED-T10P 2198
  (+6): offset +94 stable (base 2286-2192).
- rgramc sha256 3be3db46738f617b7a7e7f74b5e4e7578a08e3c
  81a2f966d1e91d48b76beeb8e (recorded, never transcribed).

## GATE reconciliation (GATE-dc21ad48 read first-hand)
Values-agree on EVERY checkable metric, no slip:
for-added 29 set IDENTICAL (programmatic compare TRUE,
gate==mine==bank); S0/S1 sigs+diffs (REPEAT 32/84 +
REPEAT 67/88, S1-vs-C10 45x10, S1-DIFFERS-C10-sig);
M widths 7/2/6/2/7/6; QR d308/f308/1309/3309; R2 rows +
(3,2,2,2,2,3) all three metrics; missing sets EXACT;
consts 79/84/78/73; M/RM-tails NEW 16/16 both; 0-overlaps +
widths; VPOS 8/3/10/15; guards (790/792, 966/970, 795/797,
988/992, elif 50, else-if 0); seal 2292 offset +94; CLOSED
2192/2198; numstat 608/231/1+1/58 + leg attribution (C-port
leg = rgramc.c only; PY-merge leg = rgram.py + for-line +
PINS); quiz-bank empty; aae d6e27c97; PINS 22820 lines
(+58); RGRAM C 22818 (viewer FAST covers C via seat PYID +
cmp: split noted); edge pins + formulas + ff 3 total; embeds
c3/96 + c5/96; b0/b1 consts; ring const; seal/CLOSED
deltas; A-967 CONFIRM 50/50 cited by GATE, matches banked;
cutter hb31 PORT-CLOSED counts (SET-EQ 22818 + PYID
11409/11409 + probes 29/29 + UNITS 22 + SMOKE x2 +
0 DISSENT) agree.
Notation split (values agree, units phrasing differs):
GATE "QR 4/4 4ch" counts hex chars where sibling widths
count bytes; rows exact d308/f308/1309/3309 both sides +
"QR 2B vs 1B" bytes line agrees. No conflict.
Convention splits (code facts identical, ledger
phrasing per-seat, precedent b487-b491 + CLAIM r80):
uniform — GATE (sweep) counts committed tables; viewer P338
dispute OPEN/deferred, NOT re-litigated: viewer TRUE-uniform
39 held (C10 DIVERGE 10/10).
RQ==M — GATE reports M==RQ 16/16 string-identical SAME-ORDER
("reported, not gated"); viewer ledger: evens 60 -> 61
(b492 EVEN PRESENT, positional 16/16 first-hand), odds 61
held. No DISSENT.
C-leg RGRAM — GATE ran RGRAM C 22818/22818; viewer FAST
covers C via seat PYID (C binary per cell) + cmp: split noted.
S-F lag — GATE "no writer lag this tier" (impl==census);
viewer counter held at 44.
Merge-subject note: PY-merge applied as single-parent commit
70a5ce2c on 38e3a831 (not a true merge; ^2 absent) — content
gate from C-port commit unaffected; parent-chain YES first-hand.
GATE-only metrics (no viewer counterpart, no conflict):
AC-QC both=75 sameval=38; regen temps _t7597-12/_i4617+/
_b4616+; RGRAM C full-battery PASS-set cmp; insert-position +
dispatch-tail + file-list 117/117.
Cross-band note: this GATE's "py file-wide elif 50 both
(0 added)" CONFIRMS the viewer elif-50 count and strengthens
the VERIFY-3158f991 finding that GATE-3158f991's "elif 0"
was a sweep-side miscount (code fact 50 stable b490-b495).

## Chain state at b492 (viewer ledger)
- TRUE-uniform 39 held (b492: viewer convention NOT-TRUE, C10
  DIVERGE; P338 dispute OPEN).
- S-F tables-lag 44 held (b492 no-lag tier: impl 79/84/78/73
  == census excl).
- RQ==M evens 60 -> 61 (b492 EVEN PRESENT) / odds 61 held.
- Full/diff survey 37 held (b492 diff-flavor: REPEAT-PB +
  DIFFSIG-C10 structure continues).
- Seal +94 vs CLOSED-T10P stable (2198/2292).
- aae d6e27c97 pinned-stable. rgramc sha recorded (build492BAND).
- Content-line variance 231 (rgram +231 this band).
- AC b84-87 bd/6e/92/0b (band value; was 3f/ac/85/3e).
- RC_N 73 (P383->P384 71->73).
- 348 pins contiguous 150369..150716, no RED anywhere.

Verdict: PASS. Ready for merge (oldest-first).
