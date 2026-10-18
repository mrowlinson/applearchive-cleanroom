# Q-357 (w2): T10P293 geometry 118701..119048 (348, first-hand)

PB0 n118701 sig03291000 NEW; PB1 n118702 sig3b635420 NEW.
PBA88-PLAIN n118703..118718 16x88B sig02000000 M8 b28,29,30,31,80,81,82,83 16/16, b0-const, b5-const 9f, consts 79.
C10-1SIG n118719..118728 sig2b8b4e20 x10, M11 b24,26,27,28,29,30,31,80,81,82,83 (b25-skipped) 10/10, b5-const 9f, consts 72.
QUAD88-4R n118729..118792 sig02000000 x64 88B-pay: M9 b19,25,26,27,35,80,81,82,83 16/16 + R11 b28-34,84-87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x9f+(o>=55) edge o54->55 ff/9f->01/a0 (n118783->118784); NO frags; consts 66.
T88-RING256 n118793..119048 sig25000000: M8 cols b40,41,42,43,76,77,78,79 / R8 rows b29,30,34,35,80,81,82,83 16/16; b4 0x13 step2; b5 0xa0+(o>=119)+(o>=247); edges o118->119 ff/a0->01/a1, o246->247 ff/a1->01/a2; consts 70.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
