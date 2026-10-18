# GATE-0c12d57 (encode-writer2 tip): PASS, rgram F5+G 380/380

- scope: 7495d3a (F5 cont + dip2817) + 0c12d57 (G0/G1/G2/G3).
  covers 7495d3a within (same poll gap). +29 cells +58 pins.
  no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME 181/181,
  RGRAM 380/380, PINS set-eq all five.
- code read first-hand: F4→F4/F5 unified (bound to 2816,
  tag split off487, b5 +off603 edge; old cells provably
  unaffected — edge term 0 there) + dip/G0 literals +
  G1/G2 row-tabs + G3 16-tabs/k2. old 356 cells CLOSED.
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh 0c12d57 $WS/gate-w2-0c12d57-s2
