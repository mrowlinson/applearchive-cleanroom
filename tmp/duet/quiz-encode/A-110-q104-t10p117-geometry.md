# A-110 (Q-104): T10P117 P-head geometry — DERIVED

Bed: census N=57453..57544 own bed (.rav[12:-4]).
First-hand; P116-M re-derived 57133 row0 (A-108).

## 1. shape: CONFIRM
- PB0 57453 96B/80B sig 003fb501 NEW; PB1 57454
  100B/84B fat sig 01000000; PBA 57455..57470 (16,
  100B/84B sig 1b000000 NEW); SINGLETON 57471
  100B/84B sig 01000000; PBB 57472..57480 (9,
  96B/80B sig c07870da NEW); QUAD 57481..57544
  (64=4x16, ALL 100B/84B, SINGLE sig 0d000000).
- 10x96B + 82x100B exact. PBA VPOS
  [4,11,18,19,26,27,76-79] (b11 IN, b5 const
  0xc0); PBB VPOS [4,14,15,21-26,76-79].
- Quad sig =P116-quad first-hand (P116 row0
  57133..57148 all 0d000000, 100B). "8th consec"
  ordinal = writer's count, run continues.

## 2. quad rows: CONFIRM + M-novelty ANSWERED
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct. NOTE: heads b32-34
  15/16 distinct (m9/m10 share effc37, tails
  differ; full-7B rows still 16/16).
- R-band b18,19,25,27,28,29 row-only EXACT:
  rows0,1,3 f5f76377102b, row2 d585e30350aa.
- Tails b80..83 row-const 2e5fd16e/985fd16e/
  f5e58310/20ddbf80 exact.
- M-novelty vs P116-M: ALL NEW first-hand (0/16
  tails, 0/16 heads overlap; 7B vs 6B layout).
- PBA M 9B pos[11,18,19,26,27,76-79] 16/16;
  PBB M 12B pos[14,15,21-26,76-79] 9/9.

## 3. counters + dips: CONFIRM, NONE
- Tier b4=(0xdb+2off)&FF 92/92; b5 0xc0->0xc1
  step exactly at 57472 (PBA const 0xc0,
  PBB+quad 0xc1).
- Quad b4=(0x13+2off)&FF 64/64, b5 const 0xc1.
- pay[4:6]==LE((n<<1)|1)&FFFF 92/92.
- NO D-class dips (runs/VPOS/counters exact,
  0 stragglers).

## geometry agrees on all 3 legs
