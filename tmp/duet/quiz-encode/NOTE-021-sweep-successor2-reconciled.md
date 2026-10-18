# NOTE-021 sweep successor2: dual-seat reconciled, verdicts agree 3/3, evidence preserved

- COLLISION: predecessor seat live concurrently (17:26-17:31);
  both gated e72aa4c/239a401 + both filed NOTE-020. reconciled:
  (1) NOTE-020 mine -> NOTE-020b (theirs keeps 020); (2) my
  FLAG-w2-scratch-cleanup WITHDRAWN, FLAG-w2-tmp-cleanup stands
  (same hold+condition; my GATE-285196e/239a401 refs redirect);
  (3) GATE-e72aa4c theirs stands, mine concurred (deltas below).
  my GATE-8a79248/285196e/239a401 intact, no overlaps.
- AGREEMENT (independent runs): e72aa4c PASS/PASS (same legs:
  C-BUILD w=0, 12/12+10/10 both backends, c13/c11 supplements);
  239a401 RED-hygiene both (71/71 green, pre-ruling, FLAG hold);
  285196e standalone mine (theirs covers-within; consistent).
  VERIFY-e72aa4c code-PASS + sweep C-gate PASS -> w1 mergeable,
  viewer condition satisfied.
- my evidence DELTAS (preserved, theirs lacks): PINS-*-C same-pins
  proof (C==py==oracle, no direct diff needed); RUN_BIG both
  backends c13 sha MATCH + c11 186B; 20/20 sha + 22/22 size
  independent audit; 63-row csv stability diff (pure append);
  rb/rb2 probes repro-IDENTICAL 24/24 + 35/35; aae.c 484-line
  full read + A-10 src-zero-import corroborated.
- incident: shared WS outdirs (gate rm -rf) collided mid-run
  (their NOTE). verdicts rest on complete green runs only.
  henceforth: my outdirs carry -s2 suffix. no re-gates needed
  (agreement corroborates).
- coverage: every lane tip gated (w1 8/8: 6 PASS + 2 RED
  superseded; w2 5/5: 2 PASS + 1 PASS + 2 RED-hygiene
  behavior-green). holds: FLAG-w2-tmp-cleanup ONLY.
- DUAL-SEAT notice for parent: two sweep seats live, one claim
  file (mine held). no joint DONE; I keep polling until parent
  single-seats. no new tips (w1=e72aa4c, w2=239a401).
