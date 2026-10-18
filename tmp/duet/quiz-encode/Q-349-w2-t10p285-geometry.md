# Q-349 (w2): T10P285 geometry 115917..116264 (348, first-hand)

PB0 n115917 sig19f80a00 NEW; PB1 n115918 sigddbef415 NEW.
PBA88-PLAIN n115919..115934 16x88B sig01000000 M9 b28,29,30,31,32,80,81,82,83 16/16, b0-const, b5-const 89, consts 78.
C10-1SIG n115935..115944 sigcd23fd15 x10, M12 b24-31,80-83 10/10, b5-const 89, consts 71.
QUAD88-4R n115945..116008 sig01000000 x64 88B-pay: M8 b25,26,27,35,80,81,82,83 16/16 + R11 b28-34,84-87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x89+(o>=23) edge o22->23 ff/89->01/8a (n115967->115968); NO frags; consts 67.
T88-RING256 n116009..116264 sig16000000: M7 cols b40,41,42,76,77,78,79 / R7 rows b29,34,35,80,81,82,83 16/16; b4 0x53 step2; b5 0x8a+(o>=87)+(o>=215); edges o86->87 ff/8a->01/8b, o214->215 ff/8b->01/8c; consts 72.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
