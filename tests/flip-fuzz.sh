#!/bin/sh
# flip-fuzz.sh — oracle-vs-C exit-class + tree differential, 200 seeded flips.
# Usage: tests/flip-fuzz.sh [workdir]; default WS flipfuzz.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d /Volumes/NVME/applearchive-cleanroom-ws/flipfuzz.XXXXXX)}
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
make -C "$ROOT" OUTDIR="$WORK/build" >/dev/null 2>&1 || die "make failed"
{ echo '#!/bin/sh'; echo "exec \"$WORK/build/aae-cli\" aar-decode \"\$@\""; } > "$WORK/aad-bin" && chmod +x "$WORK/aad-bin"
AAD_BIN="$WORK/aad-bin" python3 "$HERE/fuzz.py" orac 200 49420 "$WORK/cases"
