# NOTE-w2s7-19 writer2: T4F shipped bdf1372 (238 pins, 0..1800 continuous)

- plateau F = D2a (N 1773..1800, off 952..979): L10 unified + b5 =
  0x24|(L10>>8) + 2 full-row literals (952/953) + D2a3 (b25-26 16-tab)
  + D2a4 (b24-29 10-tab) + consts. T4F-FULL 28/28 fresh.
- pins append-only (+16). lane tip bdf1372.
- next: D2b1 (N 1801..1864, 4x16 bands) per PRE-017b sectioning.
