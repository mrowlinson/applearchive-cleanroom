# NOTE-w2b-hb-r6-34: P192 (first T-tier) derived + staged, VERIFY 23%
- P147 VERIFY fresh: 1944/8486 PASS, 0 FAIL at file time. Tree untouched.
- P192 (A-262) derived FRESH first-hand: bed-p192 348x100B exact; an192: odd-lencode 92/92 (head), 10 SINGLES per-N exact (sharer diffs 27/6/3B), PBA M8 16/16 (consts 74 lane-bookkeeping — b5 via lencode, not A-262's 75; heads 16/16 full), quad b5 carry @off3 exact, M6 shared 16/16, R7 rows1==2 match A-262, QT match, QC 65B, T-ring b4/b5 formulas 256/256 + edges exact, TRANSPOSED M6-by-col 16/16 + Q6-by-row 16/16, row-const frame 0/16 REFUTED, TC 70B. M-novelty vs R189M SKIPPED (R-lane ref). p192-tables.py written.
- ins192.py WRITTEN (new G-singles + T-tring dispatch, anchor T10P191Q); chain P147-P192 applies 46/46 SYNTAX-OK; P192 sweep 348/348 CLOSED.
- CUT NOTE for P192 (future): 348-cell tier needs bigger DET than DET16 (cover G10 + T rows/cols + edges); design at cut time.
- NEXT: P193 derive (Q-257/A-?) while VERIFY rides -> VERIFY verdict -> commit T10P147 -> cut P148.
- INBOX: no PARENT/PROD for w2b, no joint DONE.
