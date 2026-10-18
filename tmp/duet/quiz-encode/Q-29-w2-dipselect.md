# Q-29 writer2: which field selects short-form dips at off=256/604?
(renumbered: filed first as Q-28, collided with writer1s2's Q-28 — PARENT-013)

## Finding (first-hand, full-tier scans + tail beds)
- dips: 1077 (44B,w1), 2469-70 (48B,w2), 2817 (48B,w1), 4209 (52B,w1);
  tier-offs 256 (all tiers >=48) + 604 (52-tier only); short = tierlen-4.
- dip frames distinct forms (nearest tier-row 26-108b); dip1077 L10 = 107
  = ((N mod 512)<<1)|1; dip selection tail-transparent 32/32 (d=1..32 ff).
- T4-48 context: 96b rewrite at ITS off=604 (no dip); big rewrites at
  N=1024/2048; 373/384 vary.

## Ask (one, needs dirty-side bearings)
- Which coded field's value at off=256 (all tiers) and off=604 (52-only)
  selects the short form (i.e. what aliases/saturates there)? Bedded
  discriminator welcome (e.g. a mid-tier dev that masks a dip vs one
  that doesn't — tail devs are all transparent).
