# Q-352 (w2): T10P288 geometry 116961..117308 (348, first-hand)

PB0 n116961 sig0ac51600 NEW; PB1 n116962 sig3bf3942d NEW.
PBA88-PLAIN n116963..116978 16x88B sig02000000 M8 b25,26,27,35,80,81,82,83 16/16, b0-const, b5-const 91, consts 79.
C10-1SIG n116979..116988 sig3bf3942d x10 SAME-as-PB1, M12 b22,23,30-35,80-83 10/10, b5-const 91, consts 71.
QUAD88-4R n116989..117052 sig02000000 x64 88B-pay: M6 b40,41,80-83 16/16 + R12 b26,27,34-39,84-87 rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x91+(o>=3) edge o2->3 ff/91->01/92 (n116991->116992); NO frags; consts 68.
T88-RING256 n117053..117308 sig2f000000: M7 cols b39,46,47,80-83 / R6 rows b40,41,76-79 16/16; b4 0x7b step2; b5 0x92+(o>=67)+(o>=195); edges o66->67 ff/92->01/93, o194->195 ff/93->01/94; consts 73.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
