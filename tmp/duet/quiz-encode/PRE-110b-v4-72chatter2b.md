# PRE-110b 72: dip1 + 2-bit chatter + frames (frontier stage)

## census (v5c76 first-hand, 255x72B + 1x68B, nvar=67)
- bands ..17780 (b0 72, b1 01).
- 17781: SINGLE-ROW 68B dip (2nd after 17433).
- re-entry 17782 (b0 0b, 66-flip) -> CHATTER 17783..
  17798 (b0 churns 9c/9d/9e/9f — 2-bit pattern).
- body 17799..17808 (b0 09; 49-flip @17799 entry).
- frame 17809..17872 (b0 90; 40-flip @17809).
- frameswap @17873 (b0 06, b1 09; 32-flip); bands
  resume ..17937. b5 8a->8b @17792 ->8c @17920.
- split: ..17780 / 17781 / 17782..17798 / 17799..17808
  / 17809..17872 / 17873...
