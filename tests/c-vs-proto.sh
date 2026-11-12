#!/bin/sh
# c-vs-proto.sh — C-vs-proto exit-class + tree differential, 150 seeded flips.
# Usage: tests/c-vs-proto.sh [workdir]; default WS cvp.XXXXXX.
# Exit 0 all green / 1 any FAIL / 2 harness error.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d /Volumes/NVME/applearchive-cleanroom-ws/cvp.XXXXXX)}
die() { echo "HARNESS-ERROR $*" >&2; exit 2; }
make -C "$ROOT" OUTDIR="$WORK/build" >/dev/null 2>&1 || die "make failed"
ZBM_WS=/Volumes/NVME/applearchive-cleanroom-ws/build/decode-writer/libzbm.dylib
if [ -z "${ZBM_DYLIB:-}" ] && [ -f "$ZBM_WS" ]; then ZBM_DYLIB=$ZBM_WS; export ZBM_DYLIB; fi
{ echo '#!/bin/sh'; echo "exec \"$WORK/build/aae-cli\" aar-decode \"\$@\""; } > "$WORK/aad-bin" && chmod +x "$WORK/aad-bin"
AAD_BIN="$WORK/aad-bin" python3 "$HERE/fuzz.py" proto 150 40608 "$WORK/cases"
