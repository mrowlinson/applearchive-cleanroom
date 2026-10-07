#!/bin/sh
# asan.sh — ASan/UBSan build decodes all fixtures with exit parity vs plain build, zero sanitizer reports.
# Usage: tests/asan.sh [workdir]; default WS asanleg.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d /Volumes/NVME/applearchive-cleanroom-ws/asanleg.XXXXXX)}
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
command -v cc >/dev/null || die "no cc"
make -C "$ROOT" OUTDIR="$WORK/plain" >/dev/null 2>&1 || die "plain make failed"
make -C "$ROOT" OUTDIR="$WORK/asan" CFLAGS="-O1 -g -Wall -fsanitize=address,undefined -fno-omit-frame-pointer" >/dev/null 2>&1 || die "asan make failed"
V=$ROOT/vectors/selfgen/aar
PASS=0; FAILN=0
for f in "$V"/*.aar; do
  base=$(basename "$f")
  rm -rf "$WORK/p" "$WORK/a"; mkdir -p "$WORK/p" "$WORK/a"
  set +e
  "$WORK/plain/aad" "$f" "$WORK/p" >/dev/null 2>&1; rc0=$?
  "$WORK/asan/aad" "$f" "$WORK/a" >"$WORK/asan.log" 2>&1; rc1=$?
  set -e
  rep=$(grep -cE "Sanitizer|runtime error|SUMMARY" "$WORK/asan.log" 2>/dev/null || true)
  if [ "$rc0" != "$rc1" ]; then echo "FAIL asan-$base exit $rc0 vs $rc1"; FAILN=$((FAILN+1));
  elif [ "$rep" != "0" ]; then echo "FAIL asan-$base $rep report lines"; FAILN=$((FAILN+1));
  else echo "PASS asan-$base rc=$rc1"; PASS=$((PASS+1)); fi
done
echo "asan: $PASS pass $FAILN fail"
[ "$FAILN" -eq 0 ]
