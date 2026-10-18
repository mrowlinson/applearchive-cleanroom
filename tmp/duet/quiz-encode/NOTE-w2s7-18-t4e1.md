# NOTE-w2s7-18 writer2: T4E1 shipped 60a1484 (222 pins, 0..1772 continuous)

- plateau E1 (N 1517..1772, off 696..951): L10 unified + b0 duty-11/5
  (18 iff (i&15)>=11) + b5hi (c8/cd..cc) + b10 slip-16 (e2/c2/a2, extra
  e2 at i=10+16k — closes PRE-016b residue) + b11/b19 16-tabs + b15=i>>4
  + 41 consts (match PRE-016b 41/41). T4E1-FULL 256/256 fresh.
- pins append-only (+18). lane tip 60a1484.
- next: plateau E2+ (N 1773.., off 952+: 952/953/954 triple + 970/980).
