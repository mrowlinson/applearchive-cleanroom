# NOTE-w2s11-hb11: R47 battery running, P49 derived

- R47 (33469..33788, 320 cells A64+B256) implemented, probe
  320/320; for-list extended; RECORD+battery+smoke running in
  background.
- P49 = 33789..33816 (28) dumped + derived read-only: RAW
  28/28; 2 singletons (76B) + A16 80B (tab b37,46,47,72-75,
  head 04000000) + B10 76B per-offset heads in tab
  (b2,3,30,31,41,42,43,72-75).
- R48 @33817 (80B head 02..).
- Next: commit R47 on GREEN, then P49 tables + probe.
