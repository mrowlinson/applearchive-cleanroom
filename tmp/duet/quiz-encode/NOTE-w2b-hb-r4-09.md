# NOTE-w2b-hb-r4-09: P144 VERIFY riding clean, P146 derived first-hand
- P144 VERIFY: 3880+/8390 PASS, 0 FAIL, riding.
- P146 (A-168) derived fresh first-hand WHILE VERIFY runs (seat-local, no tree contact):
  bed-p146 92x100B exact; an146.py: lencode 92/92, M6 16/16, M11 9/9,
  R6 pos [20,21,22,23,24,25] all-4-distinct values match A-168, QT match, QC 64B const.
  p146-tables.py written.
- Pipeline: P144 (verify) -> P145 (bed+an+tables+ins staged) -> P146 (bed+an+tables staged).
- INBOX: no PARENT/PROD for w2b, no joint DONE.
