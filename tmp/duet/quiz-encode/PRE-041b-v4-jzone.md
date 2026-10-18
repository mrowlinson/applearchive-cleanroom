# PRE-041b J-zone 3513..3768: singleton + bands + 3605 freeze (w2 next)

## sectioning (v5r 256 rows @52B, 40 var, NO 16-period full-span)
- J0 3513: singleton transition (b5/6/7/8/13/16/17 all settle @3514).
- J1 3514..3540: 3514-3530 (16) + 3531-3540 (10-row! b13 8f/41 split).
- J2 3541..3604: 16-bands (3541 edge = 26 flips, biggest; b13/b20/b21
  band-consts a5/0b/fe/f5 + 6d/0d/6d + b8/b3).
- J3 3605..3768: 24-flip edge @3605, then b13=21/b20=0d/b21=b5 FROZEN;
  b30/b31 chatter continues (155/166 runs).

## slow fields
- b5: 5b@3513, fb@3514-3583, fc@3584-3711 (128), fd@3712+.
- b4: L10-lo +2/row. 12 consts = TAIL b40..51: c8 75 9b 37 cc cd dd
  ad 2d cc 06 fc (var = head b0..39 — clean head/tail split).
