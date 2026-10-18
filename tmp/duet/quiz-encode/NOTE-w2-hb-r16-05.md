# NOTE-w2-hb-r16-05: R166 staged, RECORD ~13%, R167 next
- R166: LO=75293 (75292=0be40200), HI=75548 (75549=23000000). Bed 258, sig 0be43600 single 256/256.
- Derive: m6B [42,43,76-79] q7B [36,37,38,72-75], b4 0x3b b5 0x4c steps [99,227], 69 consts, 16/16. Matches A-215 all-3.
- Patch xcheck IDENTICAL. Cells: 75293 75294 75391 75392 75405 75469 75519 75520 75533 75543 75547 75548 (s2+13=240 collides q15-240 -> 250 sub per r15 OOR precedent).
- Shadow (R164+R165 chain + R166): 256/256 CLOSED, PY-OK. R166 READY.
- RECORD bat-r164-r16 @1174 (~13%), 0 FAIL. Next: R167 fresh stage (read A-217/Q-211 first).
