# GATE-296b5ab (encode-writer2 tip): PASS, rgram F-head/F3F4 356/356

- scope: d30f354 (F-head dip-literals + F1/F2) + 296b5ab
  (F3/F4 tabs + k2 + walks). covers d30f354 within (same
  poll gap). +17 cells +34 pins. src +158/-0 (purely
  additive). no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 252/252, RB2 47/47, RAVFRAME 181/181,
  RGRAM 356/356, PINS set-eq all five.
- code read first-hand: 3 branches (dip-pair + F1/F2, F3
  tabs+k2, F4 tabs+walk+cycle3) in established assert
  shape; stdlib-only preserved; literals/tables OPEN-
  declared per NOTE-w2s7-26/27. old 322 cells CLOSED.
- verdict: PASS both commits. no FLAG. w2 line clear.
- repro: gate-tip.sh 296b5ab $WS/gate-w2-296b5ab-s2
