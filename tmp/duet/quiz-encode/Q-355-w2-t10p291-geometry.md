# Q-355 (w2): T10P291 geometry 118005..118352 (348, first-hand)

PB0 n118005 sig5f6f1300 SAME-as-P290PB0; PB1 n118006 sig2b81c726 NEW.
PBA88-STEP n118007..118022 16x88B sig02000000 M8 b40,41,42,43,80,81,82,83 16/16, b0-const, b5 0x99+(o>=9) edge o8->9 ff/99->01/9a (n118015->118016), consts 78.
C10-2SIG n118023..118032 sigs 2b81c726 x8 + 2b816713 x2 (2-sig 8+2 map), M16 b2,3,34-43,80-83 10/10, b5-const 9a, consts 67.
QUAD88-2SIG-FRAG n118033..118096 sig r0=01000000/r123=02000000 88B-pay: M4 b80-83 16/16 + R12 b0,19,40-45,84-87 rows 4/4 NO pairing; FRAG b38,39,46,47 rowpair-tabs (r0-row vs r123-row, r1==r2==r3); b5-const 9a (full odd lencode); consts 67.
T88-RING256 n118097..118352 sig23000000: M9 cols b50,52,53,54,55,80,81,82,83 (b51-skipped) / R8 rows b38,39,46,47,76,77,78,79 16/16; b4 0xa3 step2; b5 0x9a+(o>=47)+(o>=175); edges o46->47 ff/9a->01/9b, o174->175 ff/9b->01/9c; consts 69.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
