# GATE-c9441d4 sweep: PASS (rgram 1458/1458, T9D2 dip band)

- tip: lanes/encode-writer2 @c9441d4 (parent 11243f2 gated PASS). rgram.py
  +72/-0, cells to 12304, pins 1430->1458 (+28/-0).
- code read (ALL): D2 band branch (paylen 64, lencode-first, dict-lit 3 +
  A 12233-40 8-row + Q fall-through 4blk, NO gap-trap — Q catches all).
  AST-verified: dict keys exactly {12231,12232,12241} (head pair + A..Q
  bridge; 12241 takes dict path so Q's off-11 never negative — wrap-scare
  moot), AT 8 (m0-7), QT 16 (m0-15), QB 4 (q0-3; QB[q+1] safe: m=15&q=3
  needs off 74 > max 73, unreachable). coverage 3+8+63=74 cells.
  contiguous after T9DIPR (12231 follows 12230). no imports/OSS/disasm.
- NIT (no FAIL, persistent class): message "(1460 pins)" counts 2 csv
  comments; data rows 1458 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-c9441d4-s4): HYGIENE/CONTAM clean,
  RGRAM n=1458, PINS-RGRAM set-eq 1458/1458, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 119/119 (NOTE-092 baseline + 12), ZERO holds.
