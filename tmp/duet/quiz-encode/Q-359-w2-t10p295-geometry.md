# Q-359 (w2): T10P295 geometry 119397..119744 (348, first-hand)

PB0 n119397 sig63501000 NEW; PB1 n119398 sigf2c7a020 NEW.
PBA88-PLAIN n119399..119414 16x88B sig02000000 M7 b13,14,15,80,81,82,83 16/16, b0-const, b5-const a4, consts 80.
C10-STEP n119415..119424 sig86c7a020 x10 1-sig, M11 b13-19,80-83 10/10, b5 0xa4+(o>=9) edge o8->9 ff/a4->01/a5 (n119423->119424), consts 71.
QUAD88-4R-FRAG n119425..119488 sig02000000 x64 88B-pay: M8 b16,17,18,19,80,81,82,83 16/16 + R11 b8,9,10,11,20,21,22,84,85,86,87 rows 4/4 NO pairing; b80-83 col / b84-87 row; FRAG b23 coltab+ADD1 (r0-row tab, r123=r0+1); b5-const a5 (full odd lencode); consts 67.
T88-RING256 n119489..119744 sig20000000: M6 cols b28,29,80,81,82,83 / R8 rows b20,21,22,23,76,77,78,79 16/16; b4 0x83 step2; b5 0xa5+(o>=63)+(o>=191); edges o62->63 ff/a5->01/a6, o190->191 ff/a6->01/a7; consts 72.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
