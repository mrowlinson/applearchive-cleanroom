# Q-360 (w2): T10P296 geometry 119745..120092 (348, first-hand)

PB0 n119745 sig63501000 SAME-as-P295PB0; PB1 n119746 sig7b80af20 NEW.
PBA88-PLAIN n119747..119762 16x88B sig02000000 M10 b18,19,25,26,27,35,80,81,82,83 16/16, b0-const, b5-const a7, consts 77.
C10-1SIG n119763..119772 sig7b80af20 x10 SAME-as-PB1, M12 b22,23,30-35,80-83 10/10, b5-const a7, consts 71.
QUAD88-4R n119773..119836 sig02000000 x64 88B-pay: M8 b40,41,42,43,80,81,82,83 16/16 + R11 b26,27,34-38,84-87 (b39-skipped) rows 4/4 NO pairing; b80-83 col / b84-87 row; b5 0xa7+(o>=35) edge o34->35 ff/a7->01/a8 (n119807->119808); NO frags; consts 67.
T88-RING256 n119837..120092 sig26000000: M8 cols b30,39,46,47,80,81,82,83 / R8 rows b40,41,42,43,76,77,78,79 16/16; b4 0x3b step2; b5 0xa8+(o>=99)+(o>=227); edges o98->99 ff/a8->01/a9, o226->227 ff/a9->01/aa; consts 70.
Battery: staged try-file sweep 348/348 CLOSED err 0. Confirm?
