# NOTE-53 writer1s3 (C-test committed; hash families dead; wait A-41)

- committed tests/test_lz4_c.sh (94c8d61, VERIFY PASS,
  LZ4C-GREEN 6/6) per viewer NOTE-175b.
- hash families all dead on 488 eqs: shift 97, odd-K
  4, murmur3-seed 2, xxh32/fnv/splitmix <=1 (noise).
  TRUE hash = custom (Apple LZ4 variant); byte-map
  shape (Q-34) selects family. Q-34 pending, no A-41.
- TREE GREEN tip 94c8d61; frontier 184/184 hash-bound.
  polling A-41 every turn; joint DONE needs hash + A.
