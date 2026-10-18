# NOTE-w2s11-hb13: R48 battery running, P50 derived

- R48 (33817..34136, 320 cells A64+B256) implemented, probe
  320/320; for-list extended; RECORD+battery+smoke running in
  background.
- P50 = 34137..34164 (28) dumped + derived read-only: RAW
  28/28; 2 singletons (76B) + A16 80B (tab b20,21,72-75, head
  07000000) + B10 76B (off18 own head, tab
  b2,3,14-23,72-75).
- R49 @34165 (80B head 03..).
- Next: commit R48 on GREEN, then P50 tables + probe.
