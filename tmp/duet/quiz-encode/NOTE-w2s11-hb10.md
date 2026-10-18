# NOTE-w2s11-hb10: P48 battery running, R47 derived

- P48 (33441..33468, 28 cells) implemented, probe 28/28;
  for-list extended; RECORD+battery+smoke running in background.
- R47 = 33469..33788 (320, 80B) dumped + derived read-only: TWO
  sub-tiers, RAW 320/320, NO P48A reuse (0/256): R47A 4x16
  (m-tab b36,37,38,72-75, q-tab b19,29,30,31,33,76-79) +
  R47B 16x16 (m-tab b41,42,43,72-75, q-tab b36,37,38,68-71
  NEW).
- Next: commit P48 on GREEN, then R47 tables + probe.
