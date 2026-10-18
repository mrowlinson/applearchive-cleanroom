# NOTE-w2s11-hb12: P49 battery running, R48 derived

- P49 (33789..33816, 28 cells) implemented, probe 28/28;
  for-list extended; RECORD+battery+smoke running in background.
- R48 = 33817..34136 (320, 80B) dumped + derived read-only: A
  4x16 (m-tab b6,7,12,72-75, q-tab b11,34,35,46,47,76-79) + B
  16x16 (m-tab b13,72-75, q-tab b6,7,8,68-71); RAW 320/320.
- P50 @34137 (76B, head 9947ed00).
- Next: commit P49 on GREEN, then R48 tables + probe.
