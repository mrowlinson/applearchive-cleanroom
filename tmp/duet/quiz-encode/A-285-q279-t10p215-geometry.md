# A-285 (viewer r3): Q-279 T10P215 P-head @91557 — CONFIRM + CORRECTION

First-hand bed 91557..91920 (q279.py new;
census 90877..91920 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 4b080000
  REPEAT x3, PB1 f89f1000 NEW, PBA
  64ff0901 NEW (VPOS 8 exact b4+M7
  b9-11,76-79, b5 const cb).
- PBB10 ee3f2100 NEW single-sig (VPOS 12
  exact b4+M11 b13-19,80-83, b5 const
  cb, 10/10 diverge; NO pair/C8).
- QUAD e5fe1302 NEW (VPOS 21 exact
  b4,b5+M8+R11; b5-carry cb->cc @91647->
  91648 ff->01 LAST-CELL edge).
- T-RING 408b0738 NEW (VPOS 20 exact =
  b4,b5+M9+R9 partition).
- Next @91905 9f100000 NEW (4b08 run
  ends) + 91906 4ab22600 NEW + 91907/08
  4ab21602 NEW.

## 2. quad + T-ring: CONFIRM + R-pair fix
- Quad M8 b20-23,76-79 shared 16/16 x3 vs
  row0.
- CORRECTION: R7 b13-19 is r2==r3
  BOTTOM-PAIRED (a2bc521ae5788f both; 3/4
  distinct: r0 777c22dabe9d89, r1
  5a3cc0dac07b8c) — NOT unpaired 4/4.
  (3rd consecutive R-pairing miss: P212
  r0==r3, P214 r1==r3, P215 r2==r3 —
  analyzer may under-check R-row equality.)
- Tails row-shared 4/4 distinct
  8df0e13d/a1ee58a8/fc3ad4a8/2b3bd4a8
  EXACT; r2/r3 share last 2B d4a8 ✓.
- B10 M-positions == quad-R positions
  11/11 set-exact.
- M-tails 16/16 ALL NEW vs P214T (row-0
  reference, true novelty).
- T-ring STANDARD: M9 b20,21,25-27,76-79
  by COL 16/16; R9 b12-15,19,72-75 by
  ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 91557..91904: 348/348
  exact (whole tier).
- T-ring b4=(0x03+2off)&FF 256/256;
  b5=0xcc+(off>=127)+(off>=255) 256/256
  (2nd step @off255 last-cell);
  edges 91775->91776 ff/cc->01/cd +
  91903->91904 ff/cd->01/ce (last-cell).
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), PBB 72 (b5-const ✓), quad 63
  (b5 varies carry ✓), T 64.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; R7 r2==r3 paired (not 4/4)
