# GATE-0ca588b sweep: PASS (rgram 1836/1836, E2Q q15-ext + T9F2)

- tip: lanes/encode-writer2 @0ca588b (parent bdc63f2 gated PASS). rgram.py
  +81/-3, cells to 14329, pins 1808->1836 (+28/-0).
- code read (ALL). (a) E2Q MODIFICATION (3 lines): bound 14285->14300 +
  exp restructure ((QB[q] if q<15 else QN) if m<15 else ...). SAFE: q<=14
  arms byte-identical to before (no behavior change on gated rows); new
  q15 rows (off 240-254, 15 cells) assert blk==QN. pure extension.
  (b) F2 branch: inline-dict 5 singles {14301,14302,14303,14319,14329}
  (68B each, AST-verified) + B 14304-18 15-row (off0-14, BT 15) + C
  fall-through 14320-28 9-row (off0-8, CT 9). coverage 3+15+1+9+1=29
  cells. contiguous after E2Q-ext (14301 follows 14300). paylen 68 +
  lencode-first. no imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1838 pins)" counts 2 csv
  comments; data rows 1836 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-0ca588b-s4): HYGIENE/CONTAM clean,
  RGRAM n=1836, PINS-RGRAM set-eq 1836/1836, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 134/134 (NOTE-092 baseline + 27), ZERO holds.
