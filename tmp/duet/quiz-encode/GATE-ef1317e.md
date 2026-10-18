# GATE-ef1317e sweep: PASS-individual (15752 RESTORE re-gate 2570/2570; FLAG-48ebfe0 CLEARED)

- tip: lanes/encode-writer2 @ef1317e (parent cb84e10 gated PASS).
  tests/test_rgram.sh 1-line (15743 15753 -> 15743 15752 15753,
  pure sorted insertion), pins +2 rows, ZERO src change.
- code read (FULL, 3-line diff): for-list insertion exact; pin rows
  g-z15752-closed CLOSED + g-z15752 sha bed9ad9.. 84B. nothing else.
- battery: GATE-PASS shipped legs (outdir gate-w2-ef1317e-s7):
  SMOKE 6, OUTER2 284, RB2 47, RAVFRAME 181, RGRAM n=2570,
  PINS-* set-eq ALL (RGRAM 2570/2570), HYGIENE/CONTAM/OSS/
  LIBCOMPRESSION/ADOPT green. diff wall-grep 0 hits.
- CELL-IN-BATTERY proof (first-hand): PASS g-z15752-closed +
  PASS g-z15752 grepped in work-RGRAM.log; 0 FAIL lines.
- manual fresh-oracle: sha bed9ad929f8.. == pin EXACT, 84B ==
  pin, rgram.py CLOSED T9L1Q N=15752 off=31 rc=0.
- verdict: PASS for THIS tip. CLEAR CONDITION MET: 15752
  restored on descendant tip + sweep re-gate green first-hand
  WITH the cell. FLAG-48ebfe0-hold LIFTED (see FLAG file close
  section). range UNBLOCKED for parent merge.
- coverage: 171/172 PASS-individual + 1 RED-cleared (48ebfe0
  hold LIFTED via this re-gate). ZERO holds vs NOTE-092 baseline.
