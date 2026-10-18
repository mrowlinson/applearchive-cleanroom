# NOTE-w2s7-17 writer2: T4D shipped b69560e (204 pins, 0..1516 continuous)

- plateau D (N 1425..1516, off 604..695): D1 2-row literals + D2
  hole-counter (b6/b7, bit56=0) + D3 10-row bytes5-10 tab + D4 k2-tabs
  (b5/b6/b7/b8-10) + b15=(off-632)&15. T4D-FULL 92/92 fresh.
- self-caught: tuple-precedence bug in b8910 index (fresh-verify caught,
  fixed, re-verified) + b7-D4 table (misread mirror tail, corrected).
- lane tip b69560e. next: plateau E (N 1517.., off 696+, 16/32 sq-wave b0).
