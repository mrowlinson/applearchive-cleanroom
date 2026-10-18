# NOTE-w2b-hb-r6-35: P193 derived + staged, VERIFY 36%
- P147 VERIFY fresh: 3096/8486 PASS, 0 FAIL at file time. Tree untouched.
- P193 (A-263) derived FRESH first-hand: bed-p193 348x100B exact; an193: odd-lencode 92/92 (head), PBA M8 16/16 (consts 74 lane, heads 16/16), PBB2 M11 2/2 (consts 71 lane), SINGs exact, PBC6 M12 6/6 (consts 70 lane, 83921 NOT member), Q b5 step @83968 exact, M6 shared 16/16 (heads FULL), R8 all-distinct match A-263, QT match, QC 64B (VPOS 20), M-novelty 0/16 vs P192T, T-ring formulas 256/256 + edges @103/231, TRANSPOSED (3rd) M6-by-col + Q6-by-row 16/16, TC 70B. p193-tables.py written.
- ins193.py WRITTEN (B + S2/S3 + new C-band + Q + T dispatch, anchor T10P192T); chain P147-P193 applies 47/47 SYNTAX-OK; P193 sweep 348/348 CLOSED.
- Bookkeeping (3rd instance): lane consts exclude b5 (lencode-covered) → 74/71/70 vs A-263's 75/72/71; derived behavior identical.
- NEXT: VERIFY verdict -> commit T10P147 -> cut P148 (staged, re-sweep fresh on tree).
- INBOX: no PARENT/PROD for w2b (top PARENT-070), no joint DONE.
