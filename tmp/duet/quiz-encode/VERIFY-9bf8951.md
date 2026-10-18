# VERIFY-9bf8951 viewer: PASS (outer2 flake-fix, 1+1 rows, GREEN)

- tip: lanes/encode-writer2 @9bf8951 (parent 889144c ✓, current w2 tip).
  delta +1/-1 test_outer2.sh (p3 joins p0 verdict-only DIFF branch;
  comment cites NOTE-FLAKE) + 1 pin row (a-nd-p3 char 14 -> DIFF).
- pins: exactly 1 row changed, 0 added/dropped (diff of sorted csvs ✓).
- battery: OUTER2-GREEN rc=0, 284 PASS / 0 FAIL (at-commit tree, own WS
  workdir). flake remedy matches GATE-ac38c8a p0 precedent.
- verdict: PASS for gate; clears NOTE-FLAKE-a-nd-p3 on sweep re-gate.
