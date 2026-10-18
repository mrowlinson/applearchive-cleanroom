# NOTE-w2s11-hb18: P52 battery running, R51 derived

- P52 (34833..34860, 28 cells) implemented, probe 28/28;
  for-list extended; RECORD+battery+smoke running in background.
- R51 = 34861..35180 (320, 80B) dumped + derived read-only: A
  4x16 (m-tab b8,9,10,15,76-79, q-tab b6,7,12,13,14,72-75) +
  B 16x16 (m-tab b20,21,68-71, q-tab b13,14,15,76-79); RAW
  320/320.
- P53 @35181 (76B, head 9a1f7702).
- Next: commit P52 on GREEN, then R51 tables + probe.
