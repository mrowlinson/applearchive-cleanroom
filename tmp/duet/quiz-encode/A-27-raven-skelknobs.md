# A-27 skeleton-marker knob table (Q-24; N=128, ravbed)

## per-marker knobs (all flips 1->0; value-blind everywhere tested)
- m11: dev-PRESENCE @ early 0-18 or late 77-95 (38/38, any of 01/7f/80/ff).
  recipe: zeros128 vs dev@0=ff -> bit11 1->0.
- m67: NO knob (0/128 single-dev flips; immune). most stable bit in frame.
- m131: same ranges as m11 (0-18, 77-95). recipe: zeros128 vs dev@0=ff.
- m226: early {1,3-18} (EXCL 0,2!) + late 84-94. recipe: dev@1=ff flips, dev@0=ff quiet.
- m290: early 0-18 + late 84-92. recipe: dev@0=ff flips.
- m322: early 2-18 + late 84-92. recipe: dev@2=ff flips, dev@0=ff quiet (m322 only).
- TAIL 96-127: NO marker flips (any pos/val) — skeleton untouched, pure holes ✓.
- MID 19-76: TIER CHANGE 44->48B (markers relocate; N=128 offsets void there).
- COUNT: 2+ devs anywhere in 0-95 -> 44->48 (even late+late (80,84)); tail devs never
  trigger (pairs (0,100),(84,100) stay 44, flip-set = single). threshold = presence-count>=2.

## N-tier (fixed offsets; GEOMETRY CONFOUND — shifts ~every N, PRE-007)
- N=76..100: [0,0,1,0,1,0]; N=127: [0,0,1,1,1,1]; N=128/129/200: all-1;
  N=300: [0,1,1,1,1,1]; N=500: [0,1,0,1,0,1] (order 11,67,131,226,290,322).
- m131 = 1 at ALL N (only constant marker); m67 = 0 below N=127 (confounded: could be
  relocation, not response — do NOT cite as N-knob without field-relative track).
- geometry-stable adjacent pair found: N=128/129 share pos10-field (11,351,54).

## structural (for segmentation)
- early dev = SKELETON REWRITE (n≈60 diffs spanning bits 6-351), not local holes.
  tail dev = 8 local hole bits. mid dev = +4B token tier. three response classes by tier.
- m226/m322 position-holes (0,2 exclusions) = sharpest segmentation anchors: the marker
  that ignores dev@0 but fires on dev@1 bounds its token field between those positions.
