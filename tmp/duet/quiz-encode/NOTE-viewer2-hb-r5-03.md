# NOTE-viewer2-hb-r5-03 (2026-10-16, static legs done)

- Lane-diff BOTH rgramc.c-only: b182
  +1484/-1034 (parent 4f8b304), b183
  +1180/-1039 (parent c525c8f, matches
  sweep-r9). py/PINS/tests identical to
  parent merges (0 non-rgramc.c files).
- PINS: b182 8030 lines (8028 + 2 hdr),
  b183 8050 lines (8048 + 2 hdr).
- Tables-EQ: b182 T10P133 occ 61
  (P-band scale, cf b174 60 T10P129),
  b183 T10R131 occ 16 (R-band scale,
  cf b177 15). Consistent +2 tiers.
- Wall-grep PARENT-032 scope
  (cpat|libcompression|depload|dlopen|
  dylib) on band diffs: 0 hits BOTH.
- Poll: no GATE-b182/b183, Q max 361,
  no joint DONE (2 ancient DONE-*
  unrelated). Launching b183 PYID leg
  (fresh-oracle, expect 4024/4024).
