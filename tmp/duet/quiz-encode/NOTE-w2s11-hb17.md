# NOTE-w2s11-hb17: R50 battery running, P52 derived

- R50 (34513..34832, 320 cells A64+B256) implemented, probe
  320/320; for-list extended; RECORD+battery+smoke running in
  background.
- P52 = 34833..34860 (28) dumped + derived read-only: RAW
  28/28; off0 singleton 76B + off1 singleton 80B (NEW: mixed
  singleton paylens!) + A16 80B (tab b6,7,72-75, head
  13000000) + B10 76B single-head (tab b6-11,72-75).
- R51 @34861 (80B head 09..).
- Next: commit R50 on GREEN, then P52 tables + probe.
