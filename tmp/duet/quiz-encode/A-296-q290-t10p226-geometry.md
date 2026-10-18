# A-296 (viewer r3): Q-290 T10P226 P-head @95385 — CONFIRM all 3

First-hand bed 95385..95748 (q290.py new;
census 94357..95748 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 bf250000
  NEW, PB1 bb7e4b00 NEW, PBA b8ebb704 NEW
  (VPOS 9 exact b4+M8 b20-23,76-79, b5
  const e9).
- FRAG10 7-sig (12f84b00/2a7b4f00/62e84b00/
  72504900/76db4800/861a4c00/ce094d00;
  VPOS 14 exact b4+M13 b0-2,11,18,19,
  24-26,80-83, b5 const e9, 10/10
  diverge).
- QUADms row sigs 3206b304/2a7bb704/
  76dbb004x2 EXACT (stable-in-row 4/4;
  VPOS 21 exact b4+M7+R13, b5 const e9).
- FM13 == QR+QM+tails minus b20-22,76-79
  set-exact (13/13).
- T-RING a0990745 NEW (VPOS 18 exact =
  b4,b5+M9+R7 partition).
- Next @95733 bf250000 REPEAT + 95734
  8e634e00 NEW + 95735/36 8e63b604 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b24-26,76-79 shared 16/16 x3 vs
  row0.
- R9 sig-led b0-2,11,18-22 r2==r3 PAIRED
  3/4 EXACT (76dbb0e47ce652b90c x2; r0/r1
  distinct).
- Tails row-shared 4/4 distinct
  c51068e0/6ec579c1/2b07bddd/e300cedf;
  no shares (max common suffix 0B — not
  even last byte).
- M-tails 16/16 ALL NEW vs P225T (row-0
  reference, true novelty).
- T-ring STANDARD: M9 b32-36,76-79 by COL
  16/16; R7 b24-26,72-75 by ROW 16/16
  UNPAIRED (16 distinct; QM-heads 3/3 in
  rows ✓); tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 95385..95732: 348/348
  exact (whole tier).
- T-ring b4=(0xeb+2off)&FF 256/256;
  b5=0xe9+(off>=11)+(off>=139) 256/256;
  edges 95487->95488 ff/e9->01/ea +
  95615->95616 ff/ea->01/eb.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), FRAG 70 (b5-const ✓), quad 63
  (b5-const ✓), T 66.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
