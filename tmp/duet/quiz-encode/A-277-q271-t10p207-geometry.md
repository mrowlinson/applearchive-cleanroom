# A-277 (viewer r3): Q-271 T10P207 P-head @88773 — CONFIRM + CORRECTION

First-hand bed 88773..89124 (q271.py new;
census 88781..89128 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 94070000
  (REPEAT P206 PB0 PREDICTED-exact), PB1
  e0300f00, PBA 5e0ff300 (VPOS 8 exact
  b4+M7 b9-11,76-79, b5 const b5).
- FRAG pattern EXACT f42/7a-2/f41/7a-3/
  f41/7a-1: f4x4 @88791,92,95,99 f4300f00
  NEW (VPOS 12, 4/4) + 7ax6 @88793,94,96,
  97,98,88800 7a980700 NEW (VPOS 12 same
  template, 6/6); both b4+M11 b13-19,
  80-83, b5 const SAME value b5.
- H1-16 a2877900 NEW + H2-16 440ff300 NEW
  (VPOS b4,b5+M6, b5 CARRY b5/b6) + H32
  a2877900 (== H1).
- MOTIF-RING 256x 10 blocks EXACT:
  16/32/32/16/16/32/32/32/16/32 sigs
  e4/e5/e6/e7/e9/ec/ed/ef/f1/f3 +e22a0d
  (b1..3 const e22a0d 256/256) ALL NEW.
- Next @89121 98070000 NEW + 89122
  bfab0e00 NEW + 89123/24 bfabf200 NEW.

## 2. H-shared + motif: CONFIRM
- H1/H2/H32 share ONE M6 b20,21,76-79 V0
  positional 16/16/32 (H32 = V0x2).
- H32 = mini-quad: R6 b13-15,17-19 (b16
  gap: b16 const 0x39 H32-wide) 2/2
  halves (127c67c317bb/b6fcd2d05bb6) +
  tails 2/2 halves.
- M-tails 16/16 ALL NEW vs P206T (true
  novelty polarity).
- MOTIF-ring TRANSPOSED (17th) 10-sig:
  slot-tab 9B b20,21,25-27,76-79 by SLOT
  16/16; Q7 b0,11,19,72-75 by ROW 16/16
  (b0 = 10 block-sigs).

## 3. counters + dips: CONFIRM counts, NONE
- Odd-lencode all 88773..88864: 92/92 exact.
- Motif b4=(0x43+2off)&FF 256/256;
  b5=0xb6+(off>=95)+(off>=223) 256/256;
  edges 88959->88960 ff/b6->01/b7 (e7
  16-block) + 89087->89088 ff/b7->01/b8
  (f1 16-block) — the 2 b5-carry blocks.
- Consts ALL 7 COUNTS EXACT: PBA 76, FRAG
  72/72, H1 77, H2 76, H32 67, motif 66.
- CORRECTION (5 tags, same inverted set as
  Q-270): FRAG f4/7a b5 CONST b5 (VPOS 12
  ex-b5; leg-1 "b5 const SAME value" was
  right); H1 b5 CONST b5 (VPOS 7 ex-b5);
  H32 b5 CONST b6 (VPOS 17 ex-b5) — all
  three NOT b5-in; H2 b5 VARIES b5/b6
  carry (VPOS 8 in-b5) — IS b5-in
  (untagged in Q). Counts stand.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 5 b5-tags corrected (4 off, 1 on)
