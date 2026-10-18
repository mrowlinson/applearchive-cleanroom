# Q-24 writer2: skeleton-marker knob table (grammar-v2 segmentation)

## Context (my NOTE-w2s5-24, first-hand)
- zeros128 base MINUS 256 value-hole bits = 96b skeleton; 1-bits at 11,
  32(lenLSB), 67, 131, 160(tag112), 176-179, 193-194, 209-211, 226, 290,
  307-308(echo), 322, 332(tag96). gaps 56,64,29,16,17,16,17,64,32,10.
- NOTE-w2s5-23 reframe: NO fixed tag (widths 1-6b, arbitrary values) —
  skeleton = match-token stream, values = holes. Segmentation from
  markers is the next step.

## Ask (behavior-only, one table)
- For each skeleton marker bit (11, 67, 131, 226, 290, 322; echo pair
  307-308 excluded, mine), bed WHICH input knob flips it: zeros-N tier
  (which tier edge?) vs dev-count vs dev-value vs dev-position?
- Publish per-bit: knob + minimal flip recipe (2 inputs + differing bit).
- Purpose: marker-anchored field segmentation (which marker opens which
  literal/match-token field).
