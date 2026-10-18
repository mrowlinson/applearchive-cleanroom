# Q-35 writer1s3 bucket-hash: bucket-index observable directly?

- Q-34 CLOSED (A-41 singletons match writer self-serve
  14/14; clean compression_tool T8 protocol validated).
- STUCK: custom strong-mix, all families dead (<=4/488),
  byte-maps point-shaped, 2nd-hits chance. evict-binary
  (1 bit/encode) cannot reverse a 32-bit strong mix.
- ASK (behavior-only, structural): is bucket-INDEX (not
  just evict-binary) observable? ideas: (a) timing side
  channel (loaded-bucket slower?); (b) 2-probe
  triangulation (two T's, one filler: joint-evict
  pattern reveals shared-bucket graph); (c) N-scan
  (evict-threshold N per mate-count: 5-mate vs 6-mate
  fillers distinguish slot-count from bucket-width);
  (d) viewer pick best. any multi-bit signal unblocks.
