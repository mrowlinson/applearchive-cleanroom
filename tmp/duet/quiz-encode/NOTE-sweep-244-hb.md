# NOTE-sweep-244 — hb, toolkit ready, polling b132+

- cport tip still 5db2d64 (gated). No new bands.
- Seat toolkit (NVME encode-sweep/): gate-band-meta.sh
  (diff/wall/range), ownloop.sh (fresh-oracle + newpins),
  tables-check.sh (added-tables + 3 audits). All smoked
  vs b131: diff rgramc.c-only +1011/-871, wall 0, range
  54065..54320, tables 3/3 + audits 0-mismatch.
- Next: 9-min poll chunks; gate oldest-first on landing.
