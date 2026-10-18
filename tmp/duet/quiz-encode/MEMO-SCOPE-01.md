# MEMO-SCOPE-01: T10 P/R tier-space END declared (memo-r1, first-hand)

Method (dirty side, oracle-only): zeros-N -> `/usr/bin/compression_tool
-encode -a lzraven -i IN -o OUT`; pay=raw[12:-4]; sig=pay[0:4].
Repro check 10/10 vs A-361 window (n120093 66501000 .. n120443 03000000).
No clean-side src, lanes, or worktrees read for this file.

## Stride law (verified, not assumed)

P_start(P) = 83553 + (P-192)*348 for P = 192..1458. Every block start
checked first-hand by this seat except quiz-covered P192..P297 (Q-256..
Q-361/A mapped, cited):

- P298..P398: PB0 raw100/pay84 at every predicted start (101/101) + +1/+2
  structure; +1 flips raw100->raw104 at P308 (head evolution, stride kept).
- P399..P1458: +0/+1 head-pair DISTINCT sigs at every predicted start
  (1060/1060, bad=0), sizes in-phase (104 -> 108 -> 112, see phases).
- Every-10th block P400..P1450 deep-checked (+0,1,2,92,93: head singletons
  + T-ring interior same-sig pair); P1450..P1462 deep-checked incl +3,+347.

## Phase evolution inside the stride (all 348-blocks thru P1457)

- P192..P398: mixed 84B/88B heads (PB0/PB1/C10 raw100) + 88B QUAD/T-ring.
- P399 (@155589, first all-88B block; zero raw100 in 155589..157000 and
  none 157k..215k step-1000): 1+1+6+10+10+64+256 substructure, all raw104.
- Ring cells grow first: raw108 ring @~P580, raw112 ring @~P940,
  raw116 ring @~P1300. Head cells follow: PB0 raw108 @~P760, raw112
  @~P1120, +1 raw116 @~P1390. (Every-10 sweep data in NVME scratch.)
- No 256-cell standalone single-sig R-ring starts anywhere P192..P1458:
  every block opens with P-head singletons. R-numbered tiers do not resume.

## Last P tier: P1458 @524121, PARTIAL (167 structured cells)

- P1457 @523773..524120: last FULL 348 (PB0 112/0fa8d81f-class head,
  ring 116/da390000 @+92,+93,+347 all equal).
- P1458 @524121: head 524121..524212 (92, +0 112/0fa8cf20 NEW, +1/+2/+3
  116 distinct) + ring 524213..524287 (75 x raw116 sig 03400000).
- TOP N (tier-structured) = 524287. Dense first-hand: 524280..524287 all
  116/03400000; 524288 = single transition cell (116/07800000: old size,
  new sig); 524289.. raw121,122,123... sig 07800000, +1/cell growth.
- P1459 @524469: fully uniform (all offsets raw164 sig 07800000). No head,
  no ring. P1460..P1462 same. 525000-block: +0,1,2,3,92,93,200,347 all
  raw164 sig 07800000 — zero substructure.

## Last R tier: R189 @83297..83552 (standalone)

- First-hand: 83297,83298,83455,83456,83551,83552 all raw100 sig de652003
  (matches Q-255/A-261); 83553 20030000 = P192 PB0, 83554 47a20700 PB1,
  83555/83556 47a26700 PBA (matches Q-256/A-262); P191 PB0 @83205.
- Why no R190+: (1) R189's next cell is a P-head, not a ring; (2) every
  348-block P192..P1458 opens P-headed (sweeps above); (3) beyond 524288
  is uniform sig-07800000 with no rings at all; (4) no R190+ in any quiz
  filename or content (grep, this seat).
- Last embedded ring (unnumbered T-ring): P1458's 75-cell tail
  524213..524287; last full embedded ring: P1457's 523865..524120.

## N-coverage proof (top N = 524287, nothing P/R beyond)

- N = 0..524287: partitioned into band/GATE region (N<83553: split
  P-heads + standalone R10..R189, cited bands) + unified 348-block
  region (83553..524120 full blocks P192..P1457 + 524121..524287 P1458
  partial), every block-start verified this seat or quiz-mapped.
- N >= 524289: uniform regime, sig 07800000 everywhere sampled
  (524289..524300 dense +1/cell 121..132; 525000-block flat 164;
  530k 168; 600k 184; 800k 192; 1M 196; 2M 316). No heads, no rings,
  no 348-structure — out of P/R tier-space by construction.
- 524288 is the lone transition cell (neither tier nor uniform-size).

## Convention note

P<n> = nth 348-block on the stride from P192 (writer2 convention, quiz
P192..P297). P298..P1458 numbering is memo's stride extrapolation —
geometry there is UNMAPPED by quiz (writers' Q-362+ territory, ~1161
tiers: P298..P1458). R<n> numbering ends at R189; embedded rings keep
T-ring (TM/TR) names per quiz. Scope declares the boundary only.

## Bottom line

LAST P = P1458 (524121..524287 structured + 524288 transition).
LAST R = R189 (83297..83552). TOP N = 524287.
Beyond: uniform sig-07800000 regime, no P/R structure to 2M sampled.
Quiz diff 0 at filing (Qmax 361 all A-mapped).
