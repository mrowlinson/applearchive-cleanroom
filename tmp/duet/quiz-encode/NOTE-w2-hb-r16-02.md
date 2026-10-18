# NOTE-w2-hb-r16-02: R164 staged first-hand, WT apply next
- Edges first-hand: LO=74597 (74596=99000100), HI=74852 (74853=11000000). Bed 258 fresh-oracle, sig single 95091000 256/256.
- Derive: m6B [6,7,76-79] q8B [48,49,50,51,72-75], b4 0xcb b5 0x46 steps [27,155], 68 consts, 0 strag, 16/16. Matches Q-205/A-211 all-3.
- Patch xcheck TABS+CONSTS IDENTICAL (12 const lines). Cells: 74597 74598 74623 74624 74637 74701 74751 74752 74765 74837 74851 74852 (s1+77=104, s2+13=168 in-range).
- Shadow sweep 256/256 CLOSED, PY-OK. Self-nick: derive sed missed out-path, clobbered r163-derive-r15.txt; restored via deterministic regen (content verified vs hb-r15-16).
- Next: WT apply (7/56/58) -> cells append -> pre 20/20 -> RECORD -> VERIFY -> DET -> SMOKE -> commit (tier 1/4).
