# NOTE-w2s11-hb15: R49 battery running, P51 derived

- R49 (34165..34484, 320 cells A64+B256) implemented, probe
  320/320; for-list extended; RECORD+battery+smoke running in
  background.
- P51 = 34485..34512 (28) dumped + derived read-only: RAW
  28/28; 2 singletons (76B) + A16 80B (tab b36,37,72-75, head
  0c000000) + B10 76B single-head (tab b32-37,72-75).
- R50 @34513 (80B head 07..).
- Next: commit R49 on GREEN, then P51 tables + probe.
