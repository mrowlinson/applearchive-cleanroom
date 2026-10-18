# PRE-099b 68: b0-frozen window + storm + body (frontier stage)

## census (v5br first-hand, 256 rows all 68B, 61 var, b0 FROZEN)
- b0 = c4 whole window (2nd b0-quiet zone; storm/chatter in
  other bytes).
- 14879..14996: bands (b1 61; 8 edges step-16 14885..14997;
  b5 74->75 @14976).
- 14997/14998/14999: transition triple (30/59/34 flips; b1
  03/eb).
- 15000..15014: 15-row (b1 eb).
- 15015..15088: chatter (53-flip @15015; dense edges; 35-flip
  @15089 boundary).
- 15089..15134: body (bands 15105/15121; b5 75->76 @15104).
- b4 ramp. split: ..14996 / 14997..15088 / 15089...
