# GATE-bdf1372 (encode-writer2 tip): PASS, rgram T4E1+T4F 238/238

- scope: 60a1484 (T4E1 7-field + slip-16 + 9 cells) +
  bdf1372 (T4F D2a dispatch + 8 cells). covers 60a1484
  within (same poll gap). +17 cells +34 pins. no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME 181/181,
  RGRAM 238/238, PINS set-eq all five.
- code read first-hand (both diffs): T4E1 = formula branch
  (duty/slip/tabs/counter, 41 consts = PRE-016b 41/41);
  T4F = 2 literals + 2 tables + b5 formula. literals
  declared OPEN. old 204 cells still CLOSED.
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh bdf1372 $WS/gate-w2-bdf1372-s2
