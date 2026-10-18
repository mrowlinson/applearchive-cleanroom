# GATE-6c3855a sweep: PASS (rgram 1912/1912; covers dd538d0 F2Q-ext+G2 + H3/H3Q)

- chain: lanes/encode-writer2 71ba24c->dd538d0(F2Q ext to 14392 + G2 16x16
  14393-14648)->6c3855a(H3 3s+A15+B10 14649-76 + H3Q 4x16 14677-740).
  rgram.py +163/-2, cells to 14740, pins 1852->1876->1912 (+60/-0).
- code read (ALL). (a) F2Q-ext: bound-only change 14381->14392 (q3 to
  m0-14; m=15&q=3 needs off 63 > max 62, unreachable — QB len 4 safe).
  (b) G2: 16x16 (off=n-14393, m&q, G2T 16 6B, G2B5 16, F2QT-rot words
  (q+15)&15, b5=G2B5[q]+(m>=7&q in 4,12)). (c) H3: head-trio singles
  (68B each) + A 15 (off0-14, AT 15) + B fall-through 10 (off0-9, BT 10
  9B). (d) H3Q: 4x16 (m0-15 QT 16 7B, q0-3 QB 4, b5 0x72/0x73 rule).
  AST-verified all lens. contiguous throughout (14393/14649/14677 follow
  priors). no imports/OSS/disasm markers.
- NITS (no FAIL): (1) H3Q message "9B block words" but code reads 8 bytes
  and QB entries are 16 hex chars = 8B (message-only inaccuracy; battery
  decisive). (2) chain messages "(1878/1914 pins)" count 2 csv comments;
  data rows 1876/1912 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-6c3855a-s4): HYGIENE/CONTAM clean,
  RGRAM n=1912, PINS-RGRAM set-eq 1912/1912, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 137/137 (NOTE-092 baseline + 30), ZERO holds.
- quizmate: PV-051 read (merged w2@71ba24c; dd538d0 hold now clearable —
  this GATE evidences it).
