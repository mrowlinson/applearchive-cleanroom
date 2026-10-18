# GATE-e9f127a (encode-writer2 tip): PASS, frame-lens 107/107

- scope: FRAMES() helper + 2 cells (lens+sha), pins +4
  rows, purely additive. no tmp/, no impl.
- legs (pristine, 393f490): HYGIENE/GITIGNORE/CONTAM
  clean, SMOKE 6/6, OUTER2 107/107, PINS-OUTER2 set-eq
  107/107, OSS none, LIBCOMP zero-refs, ADOPT match.
- code read first-hand: FRAMES magic-scans fresh oracle
  bytes (inline python, offsets diffed) + sha, honest
  chk vs pins. lens pins corroborate NOTE-w2s2-5 EXACT
  (rav 216:96x9:64 sum+28=1172; bm 234:110x9:90
  sum+28=1342).
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh e9f127a $WS/gate-w2-e9f127a
