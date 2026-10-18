# Q-15 writer1s2 lz4 rare mid-random literal skip (w8-class, 5 samples)

- MODEL (own): Knuth-12 dense + mstart/+1/ends + continuous + never-K=127 =
  94.7% exact-src (6665/7037). residual includes 5 MID-chunk RANDOM-literal
  positions never inserted (each the sole same-slot mate: oracle holds older
  src): tiny/158 (run-5), 128/429 (run-600), w8/750 (run-600), t8192/73725,
  t32768/96310. no common offset/length/slot/gram/period found.
- ASK (behavior-only): (a) does the lz4 encoder ever skip hashing a generic
  mid-run literal (no match nearby, random content)? (b) if yes, what
  observable run/match context gates it (one example shape)?
