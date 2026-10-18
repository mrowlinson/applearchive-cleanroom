# NOTE-viewer4-hb-r7-01 (plan + step-1 verdict)

- Step 1 (GATE PASS + no VERIFY + no live claim):
  full scan: 14 GATE shas lack VERIFY-*, but ALL are
  long-merged (in-master, Oct-12 era writer bands
  R86..P93 + cac2fafe/cd10315-era) with zero claims.
  Nothing VERIFY-able toward a merge: no unmerged
  gated band lacks VERIFY (b188 07533a3 GATE+VERIFY
  closed, awaiting parent merge; b187 and older all
  closed). Oldest-claim-wins respected (CLAIM-* read
  first; no live claim contested). -> interim REAUDITs.
- Step 2 targets (merged, lacking REAUDIT, not b180/
  b177): b187 5bfc21a T10R133 n<=64064, b170 267690f
  T10P127 n<=61024, b168 f01b41d T10P126 n<=60676.
  Cap 3. Fresh detached clone + seat-private 0-warning
  build + PYID/CBAT/PYBAT/own-loop/tables/ wall each.
- Quiz: Q max 361, A max 367, UNANSWERED [] -> diff 0,
  zero owed.
