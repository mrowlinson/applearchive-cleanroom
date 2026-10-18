# GATE-eaef158 (encode-writer2 tip): PASS, rgram T3b+T2win 104/104

- scope: 1de6a2e (T3b +14 cells, test-only) + eaef158 (T2
  window asserts + 8 cells). covers 1de6a2e within (same
  poll gap). +22 cells +44 pins total. no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME 181/181,
  RGRAM 104/104, PINS set-eq all five.
- code read first-hand (both diffs): T3b = cell-list only;
  T2win = g240/g249 window + g332 tables (literal tables
  formula-OPEN, declared); cells hit window edges (off
  126/140/143/144/152/169/185/201) + T3b sweep. old cells
  still CLOSED (no model break).
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh eaef158 $WS/gate-w2-eaef158-s2
