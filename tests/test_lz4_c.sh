#!/bin/sh
# test_lz4_c.sh: committed C-parity test (py lz4enc vs unified C aar-encode).
# usage: sh tests/test_lz4_c.sh <beddir> ; needs CLI=path or default WS build.
# PASS iff every pin encodes byte-identical under py and C (diff empty).
#
# UNIFIED MAPPING (cport-unify): old `"$AAE_C" <dir> <out> --alg lz4` is now
# `"$CLI" aar-encode --alg lz4 <dir> <out>` — same ae_main code path, same
# bytes, same exits. Cell count and oracle comparisons unchanged.
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
BED=${1:?beddir}
HERE=$(dirname "$0")/..
CLI=${CLI:-/Volumes/NVME/applearchive-cleanroom-ws/build/unified/aae-cli}
TMPD=$TMPDIR/lz4c-$$
mkdir -p "$TMPD"
fail=0
[ -x "$CLI" ] || { echo "FAIL missing unified binary: $CLI (CLI=...)"; exit 1; }
for d in "$BED"/in/*; do
  [ -d "$d" ] || continue
  n=$(basename "$d")
  python3 "$HERE/src/lz4enc.py" "$d" "$TMPD/$n.py.aar" || { echo "FAIL $n py-exit=$?"; fail=1; continue; }
  "$CLI" aar-encode --alg lz4 "$d" "$TMPD/$n.c.aar" || { echo "FAIL $n c-exit=$?"; fail=1; continue; }
  if cmp -s "$TMPD/$n.py.aar" "$TMPD/$n.c.aar"; then
    echo "PASS $n py==C bytes=$(stat -f%z "$TMPD/$n.py.aar" 2>/dev/null || stat -c%s "$TMPD/$n.py.aar")"
  else
    echo "FAIL $n py!=C"; fail=1
  fi
done
rm -rf "$TMPD"
[ $fail -eq 0 ] && echo "LZ4C-GREEN" || echo "LZ4C-RED"
exit $fail
