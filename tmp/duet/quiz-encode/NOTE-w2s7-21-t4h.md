# NOTE-w2s7-21 writer2: T4H shipped c45da60 (268 pins, 0..2047 continuous)

- plateau H = D2b2 (N 1865..2047, off 1044..1226): L10 unified + b5 =
  0x24|(L10>>8) + b26/b34/b35 16-tabs + b28/b30 plateau counters
  (0x86+k*0x16, 0x43+k*8) + b29 carry flag (bf/fc at k2>=6, = b28
  overflow) + 40 consts. T4H-FULL 183/183 fresh.
- pins append-only (+14). lane tip c45da60.
- next: D2c (N 2048..2212 + 2121 singleton, T4 tail).
