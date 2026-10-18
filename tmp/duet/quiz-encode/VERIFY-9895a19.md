# VERIFY-9895a19 writer1s3 (FULL census battery) PASS

- tip 9895a19 (tests/test_lz4_full.sh, non-gating).
- tests/test_lz4_full.sh full0 seedoff=0:
  FULL-CENSUS OK=36 BAD=24, BADLIST 24 names match
  (c1000 p8_1000 c4096 p8_4096 c16384 p8_16384
  c65535 p8_65535 z65536 c65536 p8_65536 z65537
  c65537 p8_65537 z100000 c100000 z131071 c131071
  z131072 c131072 z262144 c262144 p8_262144 mix1m).
- same turn: LZ4-GREEN 4/4, LZMA-GREEN py+C,
  UNITS-GREEN. tree clean at tip (scratch untracked).
