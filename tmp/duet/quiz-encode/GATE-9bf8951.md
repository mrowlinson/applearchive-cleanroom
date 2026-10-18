# GATE-9bf8951 (encode-writer2 tip): PASS, T4J+T5E+flakefix 322/322

- scope: a873f7e (T4J tail + c3/c4/c5) + 889144c (T5E
  E-plateau) + 9bf8951 (p3 p0-treatment flake fix). covers
  first two within (same poll gap). +21 cells +42 rgram
  pins; outer2 1 pin char->DIFF. no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 284/284, RB2 47/47, RAVFRAME 181/181,
  RGRAM 322/322, PINS set-eq all five.
- code read first-hand: T4J/T5E branches (literals/tabs/
  formulas per NOTE-w2s7-23/24); paylen gate widen benign;
  flake fix = p3 verdict-only DIFF (1 pin row, exactly the
  NOTE-FLAKE remedy). nd cells all PASS fresh (p3 DIFF ✓).
- NOTE-FLAKE-a-nd-p3 CLEARED same turn (pin landed + this
  re-gate green).
- verdict: PASS all three commits. no FLAG. w2 line clear.
- repro: gate-tip.sh 9bf8951 $WS/gate-w2-9bf8951-s2
