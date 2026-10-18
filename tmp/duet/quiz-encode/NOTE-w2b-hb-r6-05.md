# NOTE-w2b-hb-r6-05: P165 derived + staged, VERIFY 65%
- P146 VERIFY fresh: 5500/8454 PASS, 0 FAIL at file time. Tree untouched.
- P165 (A-208) derived FRESH first-hand: bed-p165 92x100B exact; an165: lencode 92/92, new-PB0-sig shape CONFIRM, M8 16/16, M13 9/9, Q b5 step @74240 exact, M7 shared 16/16 (heads 16/16 full-heads), R9 rows0==3 (1st 0==3 pairing) match A-208, QT match, M-novelty 0/16 vs P164M, QC 62B const. p165-tables.py written.
- ins165.py WRITTEN (anchor T10P164Q); chain P147-P165 applies 19/19 SYNTAX-OK; P165 sweep 92/92 CLOSED.
- Race note: bg sweep P160 91/92 was torn-read (chain file rewritten mid-sweep); clean re-sweep 92/92. No grammar defect.
- NEXT: P166 derive (A-210) while VERIFY rides -> VERIFY verdict -> commit T10P146 -> cut P147.
- INBOX: no PARENT/PROD for w2b, no joint DONE.
