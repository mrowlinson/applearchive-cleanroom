# GATE-73cadd0 sweep: PASS (rgram 1560/1560, T9V1 storm + Q 4x16)

- tip: lanes/encode-writer2 @73cadd0 (parent 5576d43 gated PASS). rgram.py
  +117/-0, cells to 13000, pins 1526->1560 (+34/-0).
- code read (ALL): V1 dispatch (dip 12909 64B + dict-lit 4 + A 12912-26
  15-row + B 12928-36 9-row + gap-trap) + Q branch (m=(off-981)&15,
  q=(off-981)>>4, k15 early-edge QB[q]/QB[q+1], NO QN fallback). AST:
  dip 64B, dict keys exactly {12910,12911,12927,12937} (the 4 gaps),
  AT/BT/QT/QB lens 15/9/16/4 match ranges, QB[q+1] safe (m=15&q=3 needs
  off 1044 > max 1043, unreachable). coverage 1+4+15+9+63=92 cells.
  contiguous after T9U1 (12909 follows 12908). no imports/OSS/disasm.
- NITS (no FAIL): (1) _T9V1QN defined, never referenced (dead 8B const;
  2nd occurrence after B1). (2) message "(1562 pins)" counts 2 csv
  comments; data rows 1560 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-73cadd0-s4): HYGIENE/CONTAM clean,
  RGRAM n=1560, PINS-RGRAM set-eq 1560/1560, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 125/125 (NOTE-092 baseline + 18), ZERO holds.
