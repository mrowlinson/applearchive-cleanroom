# A-288 (viewer r3): Q-282 T10P218 P-head @92601 — CONFIRM all 3

First-hand bed 92601..92964 (q282.py new;
census 92617..93660 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 56110000
  NEW, PB1 8aac2200 NEW, PBA a1c82a02 NEW
  (VPOS 9 exact b4+M8 b20-23,76-79, b5
  const d3).
- FRAG10 6-sig (02b92100/0a962600/0ea62100/
  328b1000/86901400/d2a32500; VPOS 19
  exact b4+M18 b0-2,11,18-27,80-83, b5
  const d3, 10/10 diverge).
- QUADms row sigs d2a32d02/328b1001/
  02b92902x2 EXACT (stable-in-row 4/4;
  VPOS 25 exact b4,b5+M8+R15; b5-carry
  d3->d4 @92671->92672 ff->01 edge).
- FM18 == QR+QM+tails minus b3,76-79
  set-exact (18/18).
- T-RING 609ce72e NEW (VPOS 18 exact =
  b4,b5+M8+R8 partition).
- Next @92949 56110000 REPEAT + 92950
  36bf2200 NEW + 92951/52 36bf2a02 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M8 b24-27,76-79 shared 16/16 x3 vs
  row0.
- R11 sig-led b0-3,11,18-23 r2==r3 PAIRED
  3/4 EXACT (02b92902e1b25ff229015b x2;
  r0/r1 distinct).
- Tails row-shared 4/4 distinct
  092744bf/02ab6e3b/c6aeb4af/f5aeb4af
  EXACT; r2/r3 share last 3B aeb4af ✓.
- M-tails 16/16 ALL NEW vs P217T (row-0
  reference, true novelty).
- T-ring STANDARD: M8 b32-35,76-79 by COL
  16/16; R8 b24-27,72-75 by ROW 16/16
  UNPAIRED (16 distinct; QM-heads b24-27
  in rows ✓); tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 92601..92948: 348/348
  exact (whole tier).
- T-ring b4=(0x2b+2off)&FF 256/256;
  b5=0xd4+(off>=107)+(off>=235) 256/256;
  edges 92799->92800 ff/d4->01/d5 +
  92927->92928 ff/d5->01/d6.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), FRAG 65 (b5-const ✓), quad 59
  (b5 varies carry ✓), T 66.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
