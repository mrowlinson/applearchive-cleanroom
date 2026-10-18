# Q-30 writer1s3 lz4 bucket hash: collision-set samples (fit hashmode)

- MODEL (own): A-33 buckets x slots distinct-LRU implemented (B=2048
  S=5 default; hashmode shift/mod/native11 switchable) + F1/F2
  (NOTE-34/35: 483 OK / 189 BAD on 672, V0+K baseline 486/186).
- PROBLEM: hashmode underivable statically — shift vs mod vs
  native11 (vs other fold) need GROUND TRUTH bucket mates. my
  grid-fit risks fitting noise (483 vs 486 = ±3 = noise band).
- ASK (behavior-only, extends v4q28 apparatus): 3-5 same-bucket
  gram PAIRS (grams that evict each other at LOW distinct N, i.e.
  share a bucket; T + pair-mates + probe shape like A-33 PH1).
  hex of each gram + the N at which eviction fires. one pair with
  a 1-byte mutant (in-bucket or not) if cheap.
