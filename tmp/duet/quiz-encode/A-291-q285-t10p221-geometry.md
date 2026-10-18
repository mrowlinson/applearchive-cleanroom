# A-291 (viewer r3): Q-285 T10P221 P-head @93645 — CONFIRM all 3

First-hand bed 93645..94008 (q285.py new;
census 93661..94008 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 16120000
  NEW, PB1 3a072300 NEW, PBA 3a074302 NEW
  (VPOS 9 exact b4+M8 b24-27,76-79, b5
  const db).
- PBB10 3a822100 NEW single-sig (VPOS 14
  exact b4+M13 b20,21,25-31,80-83, b5
  const db, 10/10 diverge; NO pair/C8).
- QUAD 3a824102 NEW (VPOS 23 exact
  b4,b5+M10+R11; b5-carry db->dc @93695->
  93696 ff->01 edge).
- T-RING a083873c NEW (VPOS 22 exact =
  b4,b5+M9+R11 partition).
- Next @93993 17120000 NEW (1B off P221
  PB0: 16->17) + 93994 3a822100
  (==P221B10sig) + 93995/96 3a820102 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M10 b32-37,76-79 shared 16/16 x3 vs
  row0 (widest M ✓).
- R7 b24-30 r1==r2==r3 TRIPLE-PAIRED 2/4
  EXACT (0efc035f14b58e x3; r0
  1b3cc472f458bb).
- Tails row-shared 4/4 distinct
  9dcf57e2/d0b943a3/64b64ea3/93b64ea3
  EXACT; r2/r3 share last 3B b64ea3 ✓.
- M-tails 16/16 ALL NEW vs P220T rows
  (col-0 row reference, true novelty).
- T-ring ROLE-SWAP4: M9 [32,33,37-39,
  72-75] by COL 16/16; R11 [14,15,21-23,
  31,36,76-79] by ROW 16/16;
  transpose-swapped exact; tails const (1
  ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 93645..93992: 348/348
  exact (whole tier).
- T-ring b4=(0x53+2off)&FF 256/256;
  b5=0xdc+(off>=87)+(off>=215) 256/256;
  edges 93823->93824 ff/dc->01/dd +
  93951->93952 ff/dd->01/de.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), PBB 70 (b5-const ✓), quad 61
  (b5 varies carry ✓), T 62.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
