# A-28 op3=220 edge is OFFSET-PURE (content masks, never moves) (Q-25)

## signature confirmed (own bed, T2)
- 14-bit complex {52,53,54,98,245,246,247,250,253,337,340,343,346,350}: N=472
  11101101001111 -> N=473 00010010110000. ALL 14 invert = one coherent field flip.

## discriminator (dev-position vs edge at 472/473, pl=352-intact required)
- MOVES nothing: dev@445,448,450,455,458,460,465,470 (ANY of 01/7f/ff) -> edge
  EXACTLY at 472/473 (PRE/POST). late/tail-class content is edge-transparent.
- MASKS (no clean move anywhere): dev@<=400 + 435/438 -> TIER-CHANGE to L384
  (frame jumps, edge unreadable, value-blind); dev@440 -> PRE/PRE then L384 @474+
  (masked, POST unreachable); dev@442 -> OTH/OTH.
- NO position yields PRE->POST at any N != 473 with frame intact: the edge is never
  cleanly MOVED, only masked/destroyed.

## inference (for w2's naming)
- saturating field is WIDTH-DETERMINED BY TIER OFFSET (length-known at frame build),
  not content/parse-dependent. content can only destroy its readability (rewrite or
  tier-change), never shift its firing offset. consistent with: offset counter/marker
  whose width is fixed per tier-form (cf echo-high saturation model NOTE-w2s6-9).
- which semantic field (counter vs marker vs length-echo) needs their segmentation —
  my side constrains it to offset-pure + coherent-inversion.
