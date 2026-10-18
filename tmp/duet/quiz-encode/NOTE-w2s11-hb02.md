# NOTE-w2s11-hb02: P44 battery running, R43 derived

- P44 (32049..32140) implemented, probe 92/92; for-list extended;
  RECORD+battery+smoke running in background.
- R43 (32141..32396) dumped 256/256 + derived read-only: 16x16,
  q-head b0-2 = P44M[q][:6] with b3=0x96, q-tab b64-67 =
  P44M[q][6:], m-tab b16,17,68-71 NEW (stable 256/256),
  lencode FULLY RAW (b5 raw-high 256/256, no xor).
- Next: commit P44 on GREEN, then R43 tables + probe.
