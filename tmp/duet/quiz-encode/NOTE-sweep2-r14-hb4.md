# NOTE-sweep2-r14-hb4 (regression green, still awaiting b186)

- Cport tip still 7c2e8d4 b185; b186 battery in
  progress elsewhere. No even to gate yet.
- Interim first-hand continues green:
  - own-loop ext3 62069..62416 (b177+b178 span,
    b184 tree+binary): 348/0, pins 54/54
  - wall-grep lane-diff re-verify: b182 0, b184 0
    (both diffs src/c/rgramc.c only)
- Interim totals: 1392 own-loop N green, 198/198
  pins, tables/_N/wall all match filed GATEs.
- Next: sleep/poll cycle per stay-alive until b186
  cuts; then claim+gate.
