# NOTE-019 sweep: both new tips gated PASS same turn, FLAG cleared

- a71622b (w1): PASS (GATE-a71622b). hygiene clean, c13
  flagship byte-EXACT first-hand, code read, imports
  stdlib-only. FLAG-w1-pyc-cleanup CLEARED (all conditions
  + csv rename). w1 holds NOTHING from sweep.
- d6e2d7f (w2): PASS (GATE-d6e2d7f). 63/63 outer2, pins
  set-eq 63/63, independent sha/size audit 36/36 MATCH,
  matrix stable 84/84. w2 fully mergeable.
- framework: gate-tip e1be09e (PINS-OUTER2 setdiff leg for
  self-checking batteries) committed+live-fired same turn.
  NOTE-017b renamed per w2 suggestion (collision fixed).
- coverage: 8/8 writer tips gated (6 PASS + 2 RED-superseded;
  RED tips' behavior re-verified green at successor tips).
  open: Q-10 (viewer-directed, not mine), turf ruling
  (parent), raven path (parent). no DONE anywhere.
- sweep lane clean @e1be09e, claim held, polling.
