#!/bin/sh
# test_rgram_c.sh -- py-vs-C parity over sealed rgram pins (encode-cport).
# usage: sh tests/test_rgram_c.sh [workdir]
# RGRAMC=/path/to/rgramc (default: NVME build). Corpus cached in workdir
# (oracle regen for missing only; first run pays oracle time once).
# PASS iff every COVERED N verifies identically under py and C (rc +
# stdout + stderr all equal). N the C binary reports "N out of scope"
# (exit 2) is UNCOVERED: counted, never compared. Exit 0/1/2.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "${TMPDIR:-/tmp}/rgramc.XXXXXX")}
RGRAMC=${RGRAMC:-/Volumes/NVME/applearchive-cleanroom-ws/build/aae/rgramc}
CT=${CT:-/usr/bin/compression_tool}
PINS=$ROOT/vectors/rgram-PINS.csv
PY=$ROOT/src/rgram.py
[ -x "$RGRAMC" ] || { echo "need C binary: $RGRAMC (make -C src/c)" >&2; exit 2; }
[ -f "$PINS" ] || { echo "missing $PINS" >&2; exit 2; }
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$W/corpus"
NS=$(grep -o "^g-z[0-9]*-closed" "$PINS" | sed 's/^g-z//; s/-closed$//' | sort -n)
fail=0; id=0; cov=0; unc=0; se=0
for n in $NS; do
  se=$((se + 1))
  rav=$W/corpus/g$n.rav
  if [ ! -s "$rav" ]; then
    head -c "$n" /dev/zero > "$W/corpus/g$n.bin" 2>/dev/null || : > "$W/corpus/g$n.bin"
    "$CT" -encode -a lzraven -i "$W/corpus/g$n.bin" -o "$rav" 2>/dev/null \
      || { echo "FAIL g$n ct"; fail=1; continue; }
  fi
  python3 "$PY" "$rav" "$n" > "$W/py.out" 2> "$W/py.err"; prc=$?
  "$RGRAMC" "$rav" "$n" > "$W/c.out" 2> "$W/c.err"; crc=$?
  if [ "$crc" = 2 ] && grep -q "N out of scope" "$W/c.err"; then
    unc=$((unc + 1)); continue
  fi
  cov=$((cov + 1))
  if [ "$prc" = "$crc" ] && cmp -s "$W/py.out" "$W/c.out" && cmp -s "$W/py.err" "$W/c.err"; then
    id=$((id + 1))
  else
    echo "FAIL g$n py[$prc]=$(head -c 120 "$W/py.out") C[$crc]=$(head -c 120 "$W/c.out")"
    fail=1
  fi
done
echo "RGRAMC-PYID $id/$cov covered=$cov/$se"
[ "$id" = "$cov" ] && [ "$cov" -gt 0 ] && [ "$fail" -eq 0 ] && echo RGRAMC-GREEN || { echo RGRAMC-RED; exit 1; }
exit 0
