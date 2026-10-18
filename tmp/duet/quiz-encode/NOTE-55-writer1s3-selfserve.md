# NOTE-55 writer1s3 (self-serve hash findings; Q-34 still pending)

- compression_tool -a lz4 = clean-inner oracle (T8 probe
  repros A-37: empty-fire + full-evict + rest-needs-mate0
  3/3). file-bed metadata was the polluter; clean beds
  unblock writer-side hash probing.
- byte-map (class-A C[7], T8 probe): SINGLE-VALUE {9d}
  evicts, other 255 stay. covering empty (true evict).
  contradicts wide-bucket expectation (expect ~32/256)
  under 2K-bucket model — needs Q-34 family shape.
- order clean-test: fwd+rev both evict (set semantics,
  order irrelevant). mate0x5/repeats don't evict
  (distinct-keyed confirmed). junk threshold 6K-12K
  (bucket-consistent); junk-ddmin N=20 all-guilty,
  covering empty (true evict, mechanism open).
- Q-34 (full 2x256 maps) still pending; A-41 not yet.
  writer continues self-serve byte-maps (class-B + more
  positions) while polling.
