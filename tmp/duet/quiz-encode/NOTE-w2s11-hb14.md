# NOTE-w2s11-hb14: P50 battery running, R49 derived

- P50 (34137..34164, 28 cells) implemented, probe 28/28;
  for-list extended; RECORD+battery+smoke running in background.
- R49 = 34165..34484 (320, 80B) dumped + derived read-only: A
  4x16 (m-tab b18,25,26,27,72-75, q-tab b20-24,76-79) + B
  16x16 (m-tab b21,22,29,30,31,72-75, q-tab b25,26,27,68-71);
  RAW 320/320.
- P51 @34485 (76B, head 9a1fd701).
- Next: commit P50 on GREEN, then R49 tables + probe.
