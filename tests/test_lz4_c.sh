#!/bin/sh
# test_lz4_c.sh: committed C-parity test (py lz4enc vs C aae --alg lz4).
# usage: sh tests/test_lz4_c.sh <beddir> ; needs AAE_C=path or default WS build.
# PASS iff every pin encodes byte-identical under py and C (diff empty).
set -u
BED=${1:?beddir}
HERE=$(dirname "$0")/..
AAE_C=${AAE_C:-/Volumes/NVME/applearchive-cleanroom-ws/build/aae/aae}
TMPD=${TMPDIR:-/tmp}/lz4c-$$
mkdir -p "$TMPD"
fail=0
for d in "$BED"/in/*; do
  [ -d "$d" ] || continue
  n=$(basename "$d")
  python3 "$HERE/src/lz4enc.py" "$d" "$TMPD/$n.py.aar" || { echo "FAIL $n py-exit=$?"; fail=1; continue; }
  "$AAE_C" "$d" "$TMPD/$n.c.aar" --alg lz4 || { echo "FAIL $n c-exit=$?"; fail=1; continue; }
  if cmp -s "$TMPD/$n.py.aar" "$TMPD/$n.c.aar"; then
    echo "PASS $n py==C bytes=$(stat -f%z "$TMPD/$n.py.aar" 2>/dev/null || stat -c%s "$TMPD/$n.py.aar")"
  else
    echo "FAIL $n py!=C"; fail=1
  fi
done
rm -rf "$TMPD"
[ $fail -eq 0 ] && echo "LZ4C-GREEN" || echo "LZ4C-RED"
exit $fail
