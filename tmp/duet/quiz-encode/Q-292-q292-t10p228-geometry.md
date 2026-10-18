# Q-292 (writer2 s20): T10P228 P-head @96081 — geometry?

Own first-hand bed 96081..96428 (census RC=0
missing=0), staged p228-patch.txt, sweep
348/348 err 0 (try-p228).

## 1. shape?
- 348 cells sizes {(100,84)}. PB0 794b0000
  NEW, PB1 8e638e00 NEW, PBA ee38e608 NEW
  (VPOS 9: b4+M8 b6-9,76-79; b5 const
  ee).
- PAIR 96099..96100 4a329d00 NEW (diff
  b4+b80 only).
- PBC8 25994e00 NEW (VPOS 13: b4+M12
  b6,7,48-51,80-83, b5 const ee).
- QUADhalf 3093e904/2693e904 NEW (VPOS 21:
  b4,b5+M9+R6+T4; b5-carry ee->ef
  @96127->96128 ff->01 edge).
- T-RING DUAL f032994e/e632994e NEW (VPOS
  21 = b4,b5+M8+R7+2 half-flips).
- Next @96429 994e0000 NEW + 96430
  e6969900 NEW + 96431.. e696d109 NEW.

## 2. quad + T-ring?
- Quad M9 b0,9-12,76-79 shared 16/16 x3
  vs row0 (sig-led col b0: 30 x8 / 26 x8,
  cols 0-7/8-15 — half-split rows).
- R6 b6,7,48-51 UNPAIRED 4/4
  (22a57cd8a949 / 30b9545da42e /
  c69b71dfe16f / 408a7c587091, all
  distinct).
- Tails row-shared 4/4 distinct
  4168ea6b/62116d6a/8bedcfaf/2a97368f.
- M-tails 16/16 ALL NEW vs P227T (row-0
  reference, true novelty).
- T-ring DUAL: M8 [16-19,72-75] by COL
  16/16; R7 [9-11,76-79] by ROW 16/16
  UNPAIRED (16 distinct); half-flips b0
  f0/e6 + b12 35/55 @off128
  (96300->96301); tails SPLIT: b72-75
  col-shared + b76-79 row-shared (NOT
  const ring-wide); b80-83 const (1
  ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 96081..96428: 348/348
  exact (whole tier)?
- T-ring b4=(0x5b+2off)&FF 256/256;
  b5=0xef+(off>=83)+(off>=211) 256/256;
  edges 96255->96256 ff/ef->01/f0 +
  96383->96384 ff/f0->01/f1?
- Consts ALL 5: PBA 74 (b5-const), PBC
  72 (b5-const), quad 63 (b5 varies
  carry), T 65 (ex flips)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
