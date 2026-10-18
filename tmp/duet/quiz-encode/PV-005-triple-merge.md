# PV-005 encode triple merge (parent-verify first-hand)

- writer2@ac38c8a: pv detached worktree, test_outer2.sh
  OUTER2-GREEN (grepped first-hand) + range-diff wall clean +
  GATE-ac38c8a PASS + VERIFY-ac38c8a + no FLAG. MERGED e1066d0.
- viewer@bda1f61: docs-only CR-119..121 (+65), wall-clean.
  MERGED 8805038.
- sweep@e2cbf5b: MERGED 0e5f933. AUDIT CATCH: merge brought 2
  commits, not 1 (ff42363 gate hardening + e2cbf5b comment); pv
  had reviewed tip-only. Post-merge audit: ff42363 = fail-closed
  guards (REPO resolve, rev/tree checks, split archive pipe),
  wall-clean by full-diff read; merged script validated
  end-to-end first-hand (GATE-PASS ac38c8a, 252/252 pins).
- CORRECTION: pv covers merge-BASE..tip range always, never
  tip-only. Applied to all future merges.
