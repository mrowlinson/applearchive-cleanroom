# NOTE-w2b-hb-r6-03: P163 derived + staged, VERIFY 53%
- P146 VERIFY fresh: 4462/8454 PASS, 0 FAIL at file time. Tree untouched.
- P163 (A-204) derived FRESH first-hand: bed-p163 92x100B exact; an163: lencode 92/92, DOUBLE shape CONFIRM, PBA b5 step @73472 exact, M6 16/16, M13 8/8, XOR-SPLIT B=(00,00,00,01) row3-only 0/64 viol, R7 rows0==1 match A-204, QT match, M-novelty 0/16 vs P162M, QC 64B const. p163-tables.py written.
- ins163.py WRITTEN (DOUBLE S0-S3 + XOR dispatch, anchor T10P162Q); chain P147-P163 applies in order 17/17 SYNTAX-OK; P163 sweep 92/92 CLOSED.
- NEXT: P164 derive (A-206) while VERIFY rides -> VERIFY verdict -> commit T10P146 -> cut P147.
- INBOX: no PARENT/PROD for w2b, no joint DONE.
