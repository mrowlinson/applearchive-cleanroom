# PRE-073b 64 churn-regime 9521..9758 (tail churn + band triplets)

## census (v5aw + flip-disect first-hand, 256 rows all 64B)
- 9503..9520: tail (b0 b3/b1 00; band 9505).
- 9521: 40-flip reframe (b0->d3/b1->0a, frozen after).
- 9521..9758: CHURN regime — EVERY row flips: b4 ramp + tail
  b59-63 churn every row (hash-like, cf 032b b60-63) + band
  events in 16-cycle triplets (+0/+2/+5 slots: b43/b51-55;
  45 edges>=8 total).
- b5 128s 4a/4b/4c @9503/9600/9728.
- texture differs from tabbed zones (no tabs here; model =
  churn-tail + triplet bands). split at 9521/9600/9728.
