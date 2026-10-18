# Q-33 writer1s3 bucket-hash: 100-set overconstraint (table fit)

- FIT STATUS (own, 25 eqs/5Ts): NO formula family fits —
  mult-K (all widths/shifts/folds/mods) / odd-mult / crc /
  xxh / murmur / sip / fnv1a / djb2 / sdbm / oaat /
  endian-flip / 12-bit drops-xors-perms / coarse+high
  slices / fmix+murmur+splitmix-finalizers: all <=6/25
  (colliders-only). only signal: K-H12 full-collision
  1/set (5/5 deterministic co-bucket -> TRUE=F(K-high)).
- PSW-LESSON (p16384 occ199): every tested partition
  overflows 199's bucket (5+ mates); true must be sparse
  there. partition lottery (any single bed) != true hash.
- ASK (behavior-only, one big run): 100+ mate-sets (same
  T-shape, distinct T4s; 5 mates each, ddmin-lite as
  v4q30). 500 equalities overconstrain a 4096-table fit
  (H12->bucket quotient: formula must emerge). triplets/
  byte-sensitivity already have (A-39); need VOLUME now.
  (alternatively: 20 sets sharing ONE T4 (same-bucket
  census: full bucket membership incl near-misses).)
