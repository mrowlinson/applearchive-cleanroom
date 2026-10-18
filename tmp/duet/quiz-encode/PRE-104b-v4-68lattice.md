# PRE-104b 68: band lattice + ramp storm + parity chatter (frontier stage)

## census (v5bw first-hand, 256 rows all 68B, nvar=67 no-b16)
- head ..16383 (b0 85, b1 66; dense band lattice step 7-9;
  b5 churns 149 runs).
- staging 16384..16388 (b0 0b, b1 cd).
- STORM 16389..16414: single-rows b0 d0/5e @16389/90
  (63-flip), ramp e2..e7 (16391..16406), then PARITY
  alternation 16411+ (b0 80/16, b1 67/65 row to row).
- split: ..16383 / 16384..16388 / 16389..16406 / 16407...
