# NOTE-w2s12-138: T10P89 COMMITTED @8ff3ade (corrected)

- tier: 47709..47736 (28 cells). S0 47709 + S1 47710 singletons
  (80B const), P89A 47711..47726 (16x80B, m-tab b40,41,46,47,
  72-75, raw lencode), P89B 47727..47736 (10x80B, m-tab b27,
  37-39,46,47,76-79, raw lencode).
- gates: probe 28/28 CLOSED, pins +20, bat89 rc=0 RGRAM-GREEN
  0 FAIL, SMOKE-GREEN — all first-hand.
- A-53..A-60 consumed this shift: all 8 agree own derivation
  (R81..R88 verbatim/tail-4/pair-row/mixed-byte/dips-NONE).
  Q-diff now 0.
- frontier n=47736. next: T10R88 47737..48056 (gen validated,
  111L patch, A-60 agrees), then P90 @48057 (PRE-1263b on file).
