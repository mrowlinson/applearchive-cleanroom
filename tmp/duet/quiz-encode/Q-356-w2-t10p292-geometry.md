# Q-356 (w2): T10P292 geometry 118353..118700 (348, first-hand)

PB0 n118353 sig436f1300 NEW; PB1 n118354 sig2b81e720 NEW.
PBA88-PLAIN n118355..118370 16x88B sig02000000 M6 b6,7,80,81,82,83 16/16, b0-const, b5-const 9c, consts 81.
C10-2SIG n118371..118380 sigs 08075220 x7 + 84032910 x3 (2-sig 7+3 map), M17 b0,1,2,3,6,7,8,10,11,48-51,80-83 (b9-skipped) 10/10, b5-const 9c, consts 66.
QUAD88-4R n118381..118444 sig01000000 x64 88B-pay: M7 b13,14,15,80-83 16/16 + R10 b6,7,52-55,84-87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x9c+(o>=19) edge o18->19 ff/9c->01/9d (n118399->118400); NO frags; consts 69.
T88-RING256 n118445..118700 sig11000000: M8 cols b8,9,10,19,80-83 / R7 rows b13,14,15,76-79 16/16; b4 0x5b step2; b5 0x9d+(o>=83)+(o>=211); edges o82->83 ff/9d->01/9e, o210->211 ff/9e->01/9f; consts 71.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
