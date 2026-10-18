# NOTE-w2s6-2 writer2: SEGBED1 (zeros-N 63..130) — sub-tier edge + tier markers

- SUB-TIER EDGE at N=124/125 (inside "tier0" 64..127): b0/b1 0x40/0x00
  (N=64..124) -> 0x00/0x04 (N=125..127). head length field finer than
  tier — G1 b0 sub-map closing (bit6 vs bit10 = length-high split).
- markers 11/67 ABSENT across 64..127 (were 1 @N=128) => TIER-SPECIFIC,
  not universal. 131/290 const-1 across tier. 226/322 flip ONLY @N>=125
  (coupled to the head-field edge!). segmentation must be per-tier.
- tier-varying bits (30): 6,10 | 33-38 (byte4 off ✓G1) | 214-216,
  234-237, 258, 275-278 (echo-middle CANDIDATES — G2 "nowhere" may fall)
  | 226, 307-308 (echo ✓G2), 322, 325-331.
- N=63 paylen=63 stored ✓G1. b8 = 07 tier0 / 08 tier1 ✓.
- next: per-N value table for varying set (tiers 0+1) -> fit formulas.
  tool: bed-w2s6-seg/segbed1.py (own, oracle-exec only).
