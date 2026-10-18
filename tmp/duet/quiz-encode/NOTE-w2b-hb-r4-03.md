# NOTE-w2b-hb-r4-03: P143 RECORD riding (~23%), P144 derived first-hand
- P143: RECORD running, 1922/~8358 REC lines so far, riding to +32/-0 = 8358.
- P144 (A-164) derived fresh first-hand WHILE RECORD runs (seat-local, no tree contact):
  bed-p144 92x100B exact; shape CONFIRM (S0 02000000, S1 f5020000, PBA16 542f0000,
  PBB10 alternating f5,f5,7a,7a,7a,f5,7a,7a,7a,f5, quad fc11/251f/fc11/fc11, b5={0x0a} whole tier, NO singleton).
  an144.py: lencode 92/92, M7 16/16, M18 10/10, R6 pos [0,1,11,30,36,37] rows0==2==3
  values match A-164, QT match, QC 64B const. p144-tables.py written.
- NEXT: P143 RECORD verdict -> VERIFY -> smoke -> commit; then cut ins144 (anchor on committed P143Q).
- INBOX: no PARENT/PROD for w2b, no joint DONE.
