# PRE-080b 64 reframe @10565 + regime 10565..10782 (frontier stage)

## census (v5ba first-hand, 256 rows all 64B, 29 var)
- 10527..10564: body tail (b0 83/b1 00; dense edges 10533..
  10558; b5 52).
- 10565: 27-flip reframe (b0->31/b1->08).
- 10565..10782: regime (bands 10581..10773 step-16; b5
  16-cycle 52x6/92x7/d2x3 + low-nibble +1 @10624 (x3) /
  @10752 (x4)).
- b4 ramp. split: ..10564 / 10565... tabs on demand.
