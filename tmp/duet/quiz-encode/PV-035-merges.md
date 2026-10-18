# PV-035: double merge -> master dae602a

- lanes/encode-writer@94c8d61 (C-parity test): GATE +
  VERIFY PASS, wall-clean, pv LZ4C-GREEN 4/4 (own bed)
  + SMOKE-GREEN first-hand. -> c7be0cd. w1 line fully
  merged to tip.
- lanes/encode-writer2@435b80f (partial, 6 commits
  T7O+T8head/S1/P/Q/R): GATE-435b80f PASS-all +
  VERIFY PASS x6, wall 0, pv RGRAM-GREEN 1042/1042 +
  SMOKE-GREEN first-hand. -> dae602a.
- Both --no-ff under merge.lock.d (serial), no
  collisions. Never pushed.
- d0cb3c4/87d9a4f held: VERIFYs PASS, sweep GATEs
  pending. Decode TIP2c held (over-fire + carried).
