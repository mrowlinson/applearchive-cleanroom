# NOTE-w2-hb-r15-16: R163 staged first-hand, WT apply next
- Edges first-hand: LO=74249 (74248=ce1d0100), HI=74504 (74505=11000000). Bed 258 fresh-oracle, sig single 41571100 256/256.
- Derive: m6B [38,39,76-79] q7B [32,33,34,72-75], b4 0x13 b5 0x44 steps [119,247], 69 consts, 0 strag, 16/16. Matches Q-203/A-209 all-3.
- Patch xcheck TABS+CONSTS IDENTICAL (69). Cells: 74249 74250 74367 74368 74381 74445 74489 74495 74496 74499 74503 74504 (s2+13=260 OOR -> 250 sub).
- Shadow sweep 256/256 CLOSED. Next: WT apply -> pre -> RECORD -> VERIFY -> DET -> SMOKE -> commit (tier 4/4).
