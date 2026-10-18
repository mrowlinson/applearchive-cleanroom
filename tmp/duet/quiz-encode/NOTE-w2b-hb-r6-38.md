# NOTE-w2b-hb-r6-38: P196 derived + staged, VERIFY 75%
- P147 VERIFY fresh: 6401/8486 PASS, 0 FAIL at file time. Tree untouched.
- P196 (A-266) derived FRESH first-hand: bed-p196 348x100B exact; an196: odd-lencode 92/92 (head), PBA M7 16/16 (consts 75 lane), PBB2 M10 2/2 (consts 72 lane, 84966 NOT member), mid-8 sharer diffs 3/5/6/6/2B exact, ALT sigs 3e,3d,3e,3d exact, ALT row1 B5-CARRY exact, M7 shared 16/16, per-row consts 76/75/76/76, R DERIVED [0,6-11] all-distinct (sig b0 alternates) + QT 4/4 + QC 64B, M-novelty 0/16 vs P195Q, T-ring formulas 256/256 + edges @83/211, TRANSPOSED (6th) + TAILS-SWAPPED (3rd) M7-by-col + Q7-by-row 16/16, TC 68B. p196-tables.py written.
- ins196.py WRITTEN (G8 + ALT-as-quad + M7/Q7 T-ring, anchor T10P195T); chain P147-P196 applies 50/50 SYNTAX-OK; P196 sweep 348/348 CLOSED.
- NEXT: P197 derive (A-267) while VERIFY rides -> VERIFY verdict -> commit T10P147 -> cut P148.
- INBOX: no PARENT/PROD for w2b, no joint DONE.
