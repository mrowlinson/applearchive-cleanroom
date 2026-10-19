# NOTE-sweep2-r29-hb6
- b226 gate-tip: OUTER2 leg FLAKED
  (a-nondet 283/284, "got char 14
  want char 13") — KNOWN oracle-only
  nondet per GATE-965f4dd/GATE-
  7081fd5 precedent (lives in AEA
  oracle bytes; rgramc.c-only lane
  cannot influence). RGRAM leg
  grinding clean (~7252+ PASS, 0 FAIL).
- Plan: let battery finish, then
  isolated test_outer2.sh rerun on
  IDENTICAL tree + PINS-OUTER2
  set-eq first-hand; document in
  GATE, no FLAG (not tip-caused).
- Quiz: no Q for sweep2. Turf clean.
- Next: RGRAM done, PYID/C-batt/
  own-loop, OUTER2 rerun, GATE #2.
