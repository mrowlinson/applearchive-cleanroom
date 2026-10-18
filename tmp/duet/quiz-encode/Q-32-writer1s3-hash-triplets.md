# Q-32 writer1s3 bucket-hash family: triplets + sets + byte-sensitivity

- FIT STATUS (own, A-37 4x5 mates): NO family explains all
  20 equalities — multiplicative (K/odd-1..99/prime32/xxh-
  mult/fnv, widths 11/12/16, shifts 0..21, folds id/xor16/
  xor11, mod 1920/2048/1999/4096): best 5/20. crc32/adler/
  xxh32/murmur3/siphash(k0/kff): 0/20. ONLY signal: K-H12
  full-collision 1/set (4/4 sets, 1000x over chance ->
  ddmin selects H12-colliders; true hash correlates w/ H12
  but != F(H12) (4/set H12-scattered span 2000+)).
- ASK (behavior-only, 3 micro-parts, any order):
  (a) TRIPLETS: pick 2 mates A,B from one set; does {A,B}
  + 3 fresh grams evict T (transitivity: same-bucket)?
  (b) 6+ MORE mate-sets (overconstrain family fit; 20 eqs
  underconstrain).
  (c) BYTE-SENSITIVITY of T4: single-byte mutants (each of
  4 bytes x few values): which move bucket (mate-test)?
  (multiplicative=all-bytes vs prefix=byte0-only vs ...).
