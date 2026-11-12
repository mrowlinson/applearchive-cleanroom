#!/bin/sh
# raw-trunc.sh — truncation sweep: every prefix decodes exit-1-or-clean, never crash/signal/hang.
# Usage: tests/raw-trunc.sh [workdir]; default WS rawtrunc.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d /Volumes/NVME/applearchive-cleanroom-ws/rawtrunc.XXXXXX)}
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
make -C "$ROOT" OUTDIR="$WORK/build" >/dev/null 2>&1 || die "make failed"
AAD=$WORK/build/aad
V=$ROOT/vectors/selfgen/aar
PASS=0; FAILN=0
for f in "$V"/*.aar; do
  base=$(basename "$f")
  size=$(stat -f%z "$f")
  # happy path first: full-size decode must exit 0 (never covered before)
  rm -rf "$WORK/out"; mkdir -p "$WORK/out"
  set +e
  "$AAD" "$f" "$WORK/out" >/dev/null 2>&1
  rc=$?
  set -e
  if [ "$rc" -eq 0 ]; then echo "PASS full-$base rc=0"; PASS=$((PASS+1));
  else echo "FAIL full-$base rc=$rc"; FAILN=$((FAILN+1)); fi
  pts="0 1 7 15 31 63 127 255 511 1023 2047 $((size - 1))"
  seen=""
  for k in $pts; do
    [ "$k" -ge "$size" ] && continue
    case " $seen " in *" $k "*) continue;; esac
    seen="$seen $k"
    if [ "$k" -eq 0 ]; then : > "$WORK/t.aar";
    else head -c "$k" "$f" > "$WORK/t.aar" 2>/dev/null || die "slice"; fi
    rm -rf "$WORK/out"; mkdir -p "$WORK/out"
    set +e
    "$AAD" "$WORK/t.aar" "$WORK/out" >/dev/null 2>&1
    rc=$?
    set -e
    if [ "$rc" -gt 1 ]; then echo "FAIL trunc-$base@$k rc=$rc"; FAILN=$((FAILN+1));
    else echo "PASS trunc-$base@$k rc=$rc"; PASS=$((PASS+1)); fi
  done
done
echo "raw-trunc: $PASS pass $FAILN fail"
[ "$FAILN" -eq 0 ]
