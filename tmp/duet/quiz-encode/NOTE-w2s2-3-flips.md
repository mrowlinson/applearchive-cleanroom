# NOTE-w2s2-3 writer2: per-alg flip points CLOSED + lzbitmap window anomaly

- CORRECTION of NOTE-w2s2-2: the v1 "already COMPRESSED at 100" reading
  was a probe bug (rule compared vs raw FILE bytes, not raw .aar bytes
  per the battery rule_of). fixed rule: STORED iff size==rawaar+28 and
  inner@28==AA01. v1 conclusion withdrawn; numbers below are fixed-rule.
- FLIP (random seed-42 input, raw-file bytes n, last-COMPRESSED /
  first-STORED): lzfse 658/659 (852/908B), lzma 170/171 (392/420B), lz4
  274/275 (492/524B), zlib 610/611 (806/860B), lzraven 287/288
  (504/537B). all monotonic on 100..3000 ramps + bisect. rows:
  out-flip2d/RESULTS-flip2.txt (UNTRACKED scratch).
- lzbitmap NON-MONOTONIC: STORED n<=50 (299=271+28), COMPRESSED
  52..68 (n=64: size 264 < rawsz 285), STORED n>=72 (321=293+28).
  anomaly bytes (n=64): outer pbzb, payload@28 = AA01 + raw-inner
  prefix EXACT (literal run), payload 236B vs inner 257B (saves 21B on
  metadata; 64 random bytes ride as literals). edges + round-trip +
  tiny-sweep all-algs running next.
- quiz: no A-13 yet, no new PARENT, no DONE. claim HELD.
