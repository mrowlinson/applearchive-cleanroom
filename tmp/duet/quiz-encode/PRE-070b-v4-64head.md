# PRE-070b 64-tier head 8735..8990: dip + 2 regimes (frontier stage)

## census (v5at first-hand, 246 rows 64B + 10-row 60B dip)
- 8735..8750: quiet-16 (b0 01; b5 84).
- 8751..8760: 60B DIP (59-flip exit @8761).
- 8761..8824: regime-A (b0 01/b5 04; edges 8777/8793/8809).
- 8825..8990: regime-B (24-flip @8825: b0 14; bands 8841..
  8985 step-16; b5 05/06 @8832/8960).
- b4 ramp. nvar=61 (b1/2/3 const). tabs on demand.
- split: ..8750 / 8751..8760 dip / 8761..8824 / 8825...
