# Q-350 (w2): T10P286 geometry 116265..116612 (348, first-hand)

PB0 n116265 sig1df80a00 NEW; PB1 n116266 sigcd23fd15 SAME-as-P285C10sig.
PBA88-PLAIN n116267..116282 16x88B sig01000000 M6 b38,46,47,80,81,82,83 16/16, b0-const, b5-const 8c, consts 80.
C10-1SIG n116283..116292 sigcd236d10 x10, M13 b34,35,41-47,80-83 10/10, b5-const 8c, consts 70.
QUAD88-4R n116293..116356 sig01000000 x64 88B-pay: M9 b51-55,80-83 16/16 + R11 b38,39,46-50,84-87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x8c+(o>=59) edge o58->59 ff/8c->01/8d (n116351->116352); NO frags; consts 66.
T88-RING256 n116357..116612 sig10000000: M8 cols b6,7,12,13,76-79 / R9 rows b51-55,80-83 16/16; b4 0x0b step2; b5 0x8d+(o>=123)+(o>=251); edges o122->123 ff/8d->01/8e, o250->251 ff/8e->01/8f; consts 69.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
