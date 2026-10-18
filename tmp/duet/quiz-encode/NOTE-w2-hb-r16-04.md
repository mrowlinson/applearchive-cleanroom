# NOTE-w2-hb-r16-04: R165 staged, RECORD ~5%, R166 next
- R165: LO=74945 (74944=301d0100), HI=75200 (75201=11000000). Bed 258, sig c9da1100 single 256/256.
- Derive: m7B [19,26,27,76-79] q8B [20,21,22,23,72-75], b4 0x83 b5 0x49 steps [63,191], 67 consts, 16/16. Matches A-213 all-3.
- Patch xcheck IDENTICAL. Cells: 74945 74946 75007 75008 75021 75085 75135 75136 75149 75185 75199 75200.
- Shadow (R164-state src + R165): 256/256 CLOSED, PY-OK. R165 READY to apply after R164 commit.
- RECORD bat-r164-r16 @446 lines (~5%), 0 FAIL. Next: R166 fresh stage while RECORD runs.
