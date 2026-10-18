# NOTE-w2-hb-r16-06: R167 staged, all 4 READY, RECORD ~26%
- R167: LO=75641 (75640=33370200), HI=75896 (75897=25000000, matches A-217 prediction). Bed 258, sig 37732500 single 256/256.
- Derive: m7B [13,14,15,76-79] q7B [6,7,9,72-75], b4 0xf3 b5 0x4e steps [7,135], 68 consts, 16/16. Matches A-217 all-3.
- Patch xcheck IDENTICAL. Cells: 75641 75642 75647 75648 75661 75725 75775 75776 75789 75881 75895 75896.
- Shadow (R164+R165+R166 chain + R167): 256/256 CLOSED, PY-OK. R167 READY.
- STAGING COMPLETE 4/4: R164 WT-applied (RECORD running), R165/166/167 shadow-verified, apply after each commit.
- RECORD bat-r164-r16 @2284 (~26%), 0 FAIL. Next: poll RECORD -> PINS check -> DET/SMOKE/VERIFY -> commit -> R165 apply.
