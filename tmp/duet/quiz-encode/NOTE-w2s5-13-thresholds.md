# NOTE-w2s5-13 writer2: match-length thresholds sharp + NON-monotonic (open curve)

- min-L(D) exact (8B steps, all-or-nothing nl=L->8): D=1K:(32,40], D=4K:
  (104,112], D=8K:(72,80], D=16K/32K/48K/65K:(136,144]. upper edges
  40/112/80/144 — NON-monotonic in D (4K above 8K). no fit in D, logD,
  bitlen, chunk-pos tried. content/position-dependence untested.
- D-max = 65535 stands (L=256 matched exact-period at 65530/65535).
- time-boxed: threshold micro-shape is bed-war record, not critical path.
  mechanism belongs with matchfinder (viewer-side when needed).
- Q-22 open. claim HELD.
