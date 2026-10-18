# Q-353 (w2): T10P289 geometry 117309..117656 (348, first-hand)

PB0 n117309 sig0fc51600 NEW; PB1 n117310 sig3bf3f420 NEW.
PBA88-PLAIN n117311..117326 16x88B sig02000000 M7 b52,53,54,80,81,82,83 16/16, b0-const, b5-const 94, consts 80.
C10-2SIG n117327..117336 sigs 3bf3f420 x7 + 3bf3f41a x3 (2-sig 7+3 map), M12 b3,35,46-51,80-83 10/10, b5-const 94, consts 71.
QUAD88-4R n117337..117400 sig01000000 x64 88B-pay: M6 b6,7,80-83 16/16 + R10 b11,50,51,53,54,55,84,85,86,87 (b52-skipped) rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0x94+(o>=39) edge o38->39 ff/94->01/95 (n117375->117376); NO frags; consts 70.
T88-2SIG256 n117401..117656 sig 1f000000/1d000000 col-split c<9: M9 cols b0,9,10,11,20,80,81,82,83 / R6 rows b6,7,76,77,78,79 16/16; b4 0x33 step2; b5 0x95+(o>=103)+(o>=231); edges o102->103 ff/95->01/96, o230->231 ff/96->01/97; consts 71.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
