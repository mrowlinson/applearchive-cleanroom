# PRE-071b 64: singleton dip @9081 + reframes 9082/9099/9173 (frontier)

## census (v5au first-hand, 255 rows 64B + 1-row 60B dip)
- 8991..9080: regime tail (b0 14/b1 00; bands 9001..9065; b5 06).
- 9081: SINGLETON 60B dip (1 row).
- 9082..9098: post-dip (50-flip @9082: b0 01->14; b5 46->47).
- 9099..9108: 54-flip @9099 (b0 01; 10-row block).
- 9109..9172: regime (b0 17/b1 00/b5 47; dense 9109-9114 then
  5/11-mix edges 9125/9130/9141/9146/9157/9162).
- 9173..9246: regime (40-flip @9173: b0 43/b1 01; bands 9189..
  9237 step-16/32; b5 47->48 @9216).
- b4 ramp. split: ..9080 / 9081 dip / 9082..9098 / 9099..9108 /
  9109..9172 / 9173... tabs on demand.
