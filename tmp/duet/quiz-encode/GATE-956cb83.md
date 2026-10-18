# GATE-956cb83 (encode-writer2 tip): PASS, stored-verbatim 181/181

- scope: ravframe.py --raw flag + verbatim assert (+50/-12,
  conditional, existing paths unchanged) + SCELL() + 4
  cells + 16 pins. no tmp/, no pyc.
- legs (pristine, bda74bd P009): HYGIENE/GITIGNORE/CONTAM
  clean, SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME
  181/181, PINS set-eq all three, OSS none, LIBCOMP zero,
  ADOPT match.
- code read first-hand: --raw asserts concat(stored)==raw
  bytes EXACT iff all frames stored (honest conditional,
  SKIP otherwise); SCELL pins closed/f2/sha/rawmatch.
  pins: MATCH x4, sizes n+16 framed-store (17/32/272/4112)
  corroborate A-18 store rule ✓.
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh 956cb83 $WS/gate-w2-956cb83-s2
