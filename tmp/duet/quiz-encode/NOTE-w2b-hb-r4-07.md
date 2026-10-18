# NOTE-w2b-hb-r4-07: P144 RECORD riding (~22%), P145 derived first-hand
- P144 RECORD running, 1884/~8390 REC, riding to +32/-0 = 8390.
- P145 (A-166) derived fresh first-hand WHILE RECORD runs (seat-local, no tree contact):
  bed-p145 92x100B exact; shape CONFIRM (S0 02000000, S1 e3020000, PBA16 882b0000 b5 0c->0d @67200,
  DSING 67215 b7030000 + 67216 b7020000, PBB8 77020000, quad single-sig 7d270000, Q b5={0x0d}).
  an145.py: lencode 92/92, M7 16/16, M11 8/8, R7 DERIVED pos [44,45,46,47,49,50,51] (A-166 gave no
  positions) rows2==3 values match A-166, QT match, QC 65B const. p145-tables.py written.
- NEXT: P144 RECORD verdict -> VERIFY -> smoke -> commit; then cut P145 (ins145 to stage, DSING needs 2 singleton branches).
- INBOX: no PARENT/PROD for w2b, no joint DONE.
