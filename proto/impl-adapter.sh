#!/bin/sh
# impl-adapter.sh — prototype backend for the harness CLI contract.
# DECODE via proto/aad.py (reference-only); everything else via oracle.
# Needed env: ZBM_DYLIB (lzbitmap block backend).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ORACLE=$HERE/../harness/oracle-adapter.sh
die() { echo "impl-adapter: $*" >&2; exit 2; }
cmd=${1:-}; shift || true
case "$cmd" in
  aar-decode)
    [ $# -eq 2 ] || die "usage: aar-decode IN.aar OUTDIR"
    [ -e "$1" ] || die "missing: $1"
    mkdir -p "$2"
    exec python3 "$HERE/aad.py" "$1" "$2"
    ;;
  probe|aar-encode|aar-list|aea-encrypt|aea-decrypt|aea-id)
    exec sh "$ORACLE" "$cmd" "$@"
    ;;
  ""|-h|--help|help)
    echo "impl-adapter: aar-decode=proto, rest=oracle"
    ;;
  *)
    die "unknown command: $cmd"
    ;;
esac
