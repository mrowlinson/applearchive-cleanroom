# NOTE-w2s5-5 writer2: A-23 ack + mid-dev value = SPLIT NIBBLES + PARENT-010 ack

- A-23 ack: tiers confirmed first-hand (18/19 + 76/77 exact, tfbed.py);
  (len,off,value) elimination accepted; Q2 (payload bits) in progress.
- R1 SPLIT-NIBBLE value field (pos30/50/76 identical): V0-3 @ bits 50-53,
  V4-7 @ bits 377-380, LSB-first contiguous. pos19 (tier edge) differs:
  V4-7 @ 335-338 + V0-3 @ 380-383 (swapped packing at boundary).
- R2 position encoded DIFFUSELY (30v50: 44 scattered bits; 50v76: 14) —
  no position field; position lives in match/length structure. alignment
  approach VOID (global resync); value-readout is the tool.
- R3 neighbors: nibble windows mostly-0 + presence flags (bit66 = dev-
  present); bit365=1, bit383=1 constant. TAG-width ID still open (10 vs
  12: hunting tag-bit patterns around nibbles next).
- PARENT-010 ACK: container-only deliverable; my bitmap/raven work stays
  BED-WAR (determination step, no rewrite without divergence+sign).
  No own-codec rewrite on my lane. claim HELD.
