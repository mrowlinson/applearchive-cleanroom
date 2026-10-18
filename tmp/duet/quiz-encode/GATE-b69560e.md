# GATE-b69560e (encode-writer2 tip): PASS, rgram T4C+T4D 204/204

- scope: f97ce83 (T4C 16-table + counter + 9 cells) +
  b69560e (T4D D1..D4 dispatch + 13 cells). covers f97ce83
  within (same poll gap). +22 cells +44 pins. no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME 181/181,
  RGRAM 204/204, PINS set-eq all five.
- code read first-hand (both diffs): T4C = shared lencode
  + tab16 + b42 counter + 40 consts; T4D = D1 literals +
  D2 hole-counter + D3 tab + D4 k2-tabs + b15 counter.
  literals/tables declared formula-OPEN (honest). old 160
  cells still CLOSED.
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh b69560e $WS/gate-w2-b69560e-s2
