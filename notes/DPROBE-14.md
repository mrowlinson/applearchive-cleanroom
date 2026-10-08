# DPROBE-14 decode-writer TIP2d: M2-dev + A-028 + single-block-modal + po6c

## 1. M2-dev (truncpay LONG held-discount, NOTE-060 10/10)

Below-gate truncpay LONG (nch>=2, !datcomplete): held -= dev.
- big bsize (>=192K, 256k/1m): dev = nch/2-1
- small (128k): dev = (nch>=4)
Verified: n12t/n14t/t15-t19/b256/f14/TR8 + M1T/M5T modal-middle-3
(all stable points; myth2d/probe1.log, own 20-vector x4 runs).
(tails,count) DOUBLE-RACE: content {full,full-1} x (t,c)
{(0,1),(2,1),(2,2),(4,2)} independent-ish; mcnorm covers stderr.
Reduced content = byte-prefix (verified).
OPEN carried: w3 (n>=10), frac-band, tr6-creation (closed by A-028).

## 2. Trunchdr cap

Trunchdr LONG: held capped at 2ch (own h-bed probes).
w3/frac/tr6-creation OPEN (tr6-creation closed by A-028).

## 3. A-028 below-gate create rule (viewer answer, implemented + refined)

Q-028 (mine): below-gate truncpay EMPTY-vs-ABSENT splitter.
A-028 (viewer, 42 cuts/168 legs): EMPTY <=> floor(end/256K) <= nch
(DAT-first, have2=-64K class; k6/k8 windows mapped, k4/k5/k7
never-EMPTY explained; exact-boundary untestable in construction).
Implemented in unified short handler (C + proto mirror).

### 3a. Refinement: nch>=1 (LONG-only)

A-028-plain over-fired CREATE on 6 battery shapes (all nch-0,
all oracle-ABSENT, 20+ legs):
- po/f3 (CLEAN blobover, end 216), m3uc37/100 (CLEAN, end 409)
- mc2 (truncpay k2, whole 262144, end 202, below via WHOLE-fail)
- mcbv (badval, same), mz1 (decfail k1, end 199)
Gate added: create iff nch>=1 && floor(end/256K) <= nch.
Vacuous in A-028's class: have2=-64K + nch-0 + end<256K needs
kcut-1 with savail<0 (impossible); k4/k5 band-start > 262144
(A-028's own analysis). Suppressor for out-of-class only.

### 3b. Clean path KEEPS the rule (n6c, NOT midchain-only)

n6c (CLEAN, innerlen 786432, nch 1, sidx 2, savail 274105,
send 512327, below-gate): oracle big2 0B EMPTY 3/3.
n5c (CLEAN, innerlen 655360, nch 0, same send): oracle ABSENT 3/3.
C: N6C-IDENT + N5C-IDENT (trees). Midchain-only gating REFUTED;
nch>=1 is THE unified gate (clean + midchain).
Battery pin: NEW po6c cell (self-crafted clean-long n6c-analog:
512000+409600 urandom, lzfse 128k, setbloblen big2 2M ->
innerlen 921963, nch 1, savail 409636 < 458752, send 512327;
oracle big2-0B 3/3, C IDENT + ERR-IDENT).

### 3c. mc2/mcbv/mz1: C-ABSENT principled, o-SET defensive

22:59 mc2-tree fail was C-side (A-028-plain create), not oracle.
Oracle: ABSENT 15+ legs (12/12 probe + batteries), 0 EMPTY legs.
C: ABSENT via nch>=1 (rule-false anyway: floor 0? mc2 send 202:
floor 0 <= 0 FIRES-plain, suppressed by nch>=1; below via
whole-fail, have2 +196K far out-of-class).
Battery: o-SET {0B,ABS} (race-tolerant per sweep cxC lesson) +
C-ABSENT pin + oracle-mode-when-present pin.

## 4. FLAG-462e86f-viewer fix (single-block modal)

TIP2c fixed tails2/count2 on single-block-content: viewer 15/15
oracle-modal (0t/c1) on m21m1 + mb505839. My M1sc-4/4-tails
WITHDRAWN (same-session phase-flip to 4/4 modal; viewer 15/15
confirms modal). FIXED: modal-only emission (0t/c1) + oracle
SET {(0t,c1),(2t,c2)} in m2single oshape + C-self ccbytes pin.
M1sc craft (POSTED per FLAG ask; WS probe/ck3.sh mkpair v1m 1 M1s,
'c'-leg): src {big1 500K, big2 3M} urandom, lzfse --block 1m -t 1,
head-cut at bs[1][0] (chain-cut after block 0; single decoded
block, whole = raw0 = 1048576, big2 1ch content). NOTE-058 era:
tails 4/4; myth2d/probe1.log (same input): ck3_M1st + ck3_m1s2t
tails {0,0,2,2} = intra-run RACE; viewer m21m1/mb505839 15/15
modal. Verdict: session-phase race, modal (0t/c1) everywhere,
no shape gate. ('t'-leg M1st = truncpay mid-block-1, same race.)

## 5. Q-029 (OPEN): complete-item partial content

e800-big1 (COMPLETE 800K DAT): oracle 512K-prefix 4/4 + ABSENT x1
(3t/c2 all legs) vs C FULL. e750/d600/all-other complete items
FULL. Dead: nch-cap, (nch+1)-cliff, whole-kcut*64K (all killed by
d600-FULL). Live: dl-threshold (750K,800K]?), tails-leg-carried,
phase. Battery -big1 cell skipped for edge800 meanwhile (all
other e800 cells pass). C keeps FULL (principled default).

## 6. Scope notes

- M1sc single-branch unification: single-block cell now modal +
  SET (tails2/count2 emission REMOVED from C+proto).
- craft.py: setbloblen (and all inner-patch cmds) extended to
  multiblock-all-stored (inner-concat + scatter map; width-kept
  assert). Needed for po6c (8 stored blocks).
- M1-507500-modal-x2 + M2-OVER-modal + mb-recipes -> TIP2e (Q-030
  for input recipes; NOTE-141 outputs absorbed).
- A-028 exact-equality boundary (end == (nch+1)*256K): still
  untestable (end = b1+323); C uses <= (A-028 verdict form).
