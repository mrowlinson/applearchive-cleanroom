# GATE-5a83dc4 (encode-writer2 tip): PASS, EC-keygen flake fix 284/284

- scope: keygen regen loop (max 10, until DER OCTET 0x20)
  in test_outer2.sh only (+11/-1). pins untouched.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 284/284, RB2 47/47, RAVFRAME 181/181,
  RGRAM 104/104, PINS set-eq all five.
- code read first-hand: loop regens on 31B keys (DER
  octet-len check); bounded (falls through after 10,
  residual ~0). matches NOTE-w2s7-8 root-cause (LibreSSL
  minimal-length strip, hand-pad proof). honest fix.
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh 5a83dc4 $WS/gate-w2-5a83dc4-s2
