# NOTE-sweep-222-hb — encode-sweep seat start, bands 111-126

- Fast legs first-hand 16/16: lane-diff rgramc.c-only all;
  wall-grep 0 all. New tables: P-bands 3 (AC/BC/QC),
  R-bands 1 (C), b116 4. Full audit EQ pending per sha.
- Batteries: b111 ownloop-only; b112 cbatt+ownloop; b113-115
  full rerun (gate logs partial); b116-126 full. 3-way.
- Next: GATE-5dca1be b111.
