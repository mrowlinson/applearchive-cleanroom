# GATE-9e4d3c0 (encode-writer2 tip): PASS, UNC-rule 115/115

- scope: UNC() helper + 4 cells (verdict+sha), pins +8
  rows, purely additive. no tmp/, no impl.
- legs (pristine, 393f490): HYGIENE/GITIGNORE/CONTAM
  clean, SMOKE 6/6, OUTER2 115/115, PINS-OUTER2 set-eq
  115/115, OSS none, LIBCOMP zero-refs, ADOPT match.
- code read first-hand: UNC walks header chain in inline
  python (BE unpack, zero-asserts, unc-sum vs raw inner,
  chain-end exact) — honest fresh-bytes measurement.
  pins corroborate NOTE-w2s2-6 (NB11 b10k both, NB1
  default both, INNER-EQ-CHAIN-EQ 4/4; b10k shas ==
  FRAMES pins, same inputs ✓).
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh 9e4d3c0 $WS/gate-w2-9e4d3c0
