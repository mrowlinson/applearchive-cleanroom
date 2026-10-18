# VERIFY-906081f writer1s3 (lzma b0 rule) PASS + HOLD-CLEAR

- tip 906081f (lzma b0=4/2/3 rule, py+C).
- tests/test_lzma.sh lz4t1: PY LZMA-GREEN 6/6
  (mb PASS bytes=1612 sha=a515abc6e91b8297).
- ENC_BIN=WS/build/aae/aae same: C LZMA-GREEN 6/6
  (mb same bytes+sha). m4m-class fixed both impls.
- FLAG-w1-lzma-b0-hold: CLEAR (re-gated green).
- no regress: LZ4-GREEN 4/4, UNITS-GREEN (same turn).
