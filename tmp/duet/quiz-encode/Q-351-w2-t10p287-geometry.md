# Q-351 (w2): T10P287 geometry 116613..116960 (348, first-hand)

PB0 n116613 sig85620b00 NEW; PB1 n116614 sig4c0ac516 NEW.
PBA88-PLAIN n116615..116630 16x88B sig01000000 M10 b8,13,14,15,16,17,80,81,82,83 16/16, b0-const, b5-const 8f, consts 77.
C10-1SIG n116631..116640 sig86148a2d x10, M11 b13-19,80-83 10/10, b5-const 8f, consts 72.
QUAD88-4R n116641..116704 sig02000000 x64 88B-pay: M9 b16,17,18,19,23,80,81,82,83 16/16 + R11 b8,9,10,11,20,21,22,84,85,86,87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5-const 8f (full odd lencode); NO frags; consts 67.
T88-RING256 n116705..116960 sig2d000000: M8 cols b28,29,30,31,80,81,82,83 / R8 rows b20,21,22,23,76,77,78,79 16/16; b4 0xc3 step2; b5 0x8f+(o>=31)+(o>=159); edges o30->31 ff/8f->01/90, o158->159 ff/90->01/91; consts 70.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
