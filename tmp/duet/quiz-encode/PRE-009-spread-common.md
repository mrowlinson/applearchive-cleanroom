# PRE-009 spread-zone correction to w2s6-7 (common-10/39, value slots stable)

## zone rule CONFIRMED + spread sizes CONFIRMED
- HOLES ⟺ d<=32: N=129 p100 (d=29) = clean contiguous-8 @248-255, common-0 ✓.
- spread n-sizes: N=129 p96 (d=33) ff n=18 ✓; N=131 p96 (d=35) ff n=47 ✓ (=8+39).

## correction: spread common is NOT 0 (cell-specific)
- w2s6-7 "spread 8-value scans @N=129/131: common=0" — their locations (129: 233-237+...,
  131: 297-304 contiguous) match HOLES-zone cells (pos~100), not spread cells. overgeneralized.
- spread-cell scans (pos96, reproduced 2/2 deterministic): N=129 common-10
  {11,20,66,98,99,131,307,308,309,347}; N=131 common-39 (list in bench log).
- VALUE SLOTS STABLE: {3,4,5,6,50,51,52,53} identical N=129/131 — only the common
  rewrite grows (10->39). value exact-8 everywhere; spread = stable split-holes + growing
  presence rewrite. predicted N=130: common-24 (n=32-8).
