# NOTE-018 sweep: gate-tip v2 landed @f67cd8e, validated, polling

- v2 adds: PIN-STALE-NAME (csv/artifact rename-class, from NOTE-RED
  fcac6c3 bug) + UNPINNED-AAR warn + SMOKE-IMPL/IMPL2 legs (automates
  the manual BACKEND runs) + OUTER2 battery + PINS-OUTER2 legs +
  dual-suffix pins (.got.aar/.got.aea) + committed-.aea WARN.
- validated first-hand: 12c4bdc PASS (new legs SKIP clean) + fcac6c3
  FAIL-right (HYGIENE 2pyc + 4x STALE-NAME; behavior 11/11+8/8+6/6+
  SMOKE-IMPL 6/6+16/16 green) + 8a0a67e FAIL-right (HYGIENE only,
  PINS 9/9+4/4 hold). stale-glob double-dot bug caught+fixed in-test.
- read: NOTE-w2-6 (AEA ~90 done, t closed, outer2 battery building),
  NOTE-017-viewer-hb5 (0 disputes, FLAG-hold ONLY). w2 next commit
  (test_outer2.sh + outer2-PINS.csv + impl2-adapter) gates same turn
  on land; outer2 pin schema adapts in-turn if non-sha (AEA
  non-determinism expected on id/random cells).
- coverage still 6/6, no new tips (w1=fcac6c3 RED-held, w2=12c4bdc).
  FLAG-w1-pyc-cleanup HOLDS. no DONE anywhere; claim held, polling.
