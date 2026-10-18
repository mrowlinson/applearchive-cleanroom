# GATE-05dd402 sweep: PASS (rgram 1256/1256, T8B1 storm + Q 4x16)

- tip: lanes/encode-writer2 @05dd402 (parent a21c15a gated PASS). rgram.py
  +107/-0, cells to 11260, pins 1222->1256 (+34/-0).
- code read (ALL): B1 dispatch (dict-lit 5 + A 11172-86 15-row + B 11188-96
  9-row + gap-trap) + Q branch (m=(off-2463)&15, q=(off-2463)>>4, k15
  early-edge exp=QB[q] if m<15 else QB[q+1]). AST-verified: dict keys
  exactly {11169,11170,11171,11187,11197} (the 5 gaps), AT/BT/QT lens
  15/9/16 match ranges, QB len 4 with QB[q+1] SAFE (m=15&q=3 needs
  off=2526 > branch max 2525 — unreachable by boundary arithmetic).
  ranges cover 29+63=92 cells (pins sample 34, sparse as usual).
  contiguous after T8A1 (11169 follows 11168).
- NITS (no FAIL): (1) _T8B1QN defined, never referenced (dead 8B const,
  grep 1 hit = def line). (2) message "(1258 pins)" counts 2 csv comments;
  data rows 1256 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-05dd402-s4): HYGIENE/CONTAM clean,
  RGRAM n=1256, PINS-RGRAM set-eq 1256/1256, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 112/112 (NOTE-092 baseline + 5), ZERO holds.
