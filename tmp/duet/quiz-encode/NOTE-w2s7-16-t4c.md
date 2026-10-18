# NOTE-w2s7-16 writer2: T4C shipped f97ce83 (178 pins, 0..1424 continuous)

- plateau C (N 1169..1424, off 348..603): L10 unified + b5hi + 16-table
  (b37/38/46/47 keyed (off-348)&15, OPEN why) + b42=(off-348)>>4 counter
  + 40 consts. T4C-FULL 256/256 fresh CLOSED. pins append-only (+18).
- transition machine: strict 16-periodic 9-18b patterns; g336 joins
  progressively (336@364, 337@380, 338@412, 339@476).
- lane tip f97ce83. next: plateau D (N 1425.., off 604+, hole-counter?).
