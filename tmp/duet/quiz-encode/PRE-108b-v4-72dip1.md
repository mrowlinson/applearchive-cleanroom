# PRE-108b 72: bands + single-row dip + frameswap (frontier stage)

## census (v5c74 first-hand, 255x72B + 1x68B, nvar=57)
- bands 17193..17401 16-step (b0 29; b5 toggles bit7
  per band: 06/86/87/07...).
- 17433: SINGLE-ROW 68B dip (b0 7a, b1 b6 vs frame
  b1 00).
- re-entry 17434 (51-flip; b0 02) -> frameswap @17435
  (b0 2f, 22-flip; edges 17436/17438).
- split: ..17432 / 17433 / 17434...
