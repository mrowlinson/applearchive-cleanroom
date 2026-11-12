#!/bin/sh
# c-adapter.sh — LEGACY C-decode shim (decode-writer era).
# SCOPE: aar-decode only via $AAD_BIN (default: WS build output); every
# other subcommand passes through to the ORACLE adapter (oracle bytes
# execute here — never mistake this shim for impl coverage). The shipped
# impl path is the unified CLI ./build/aae-cli (all commands, no oracle).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ORACLE=$HERE/../harness/oracle-adapter.sh
AAD=${AAD_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/build/decode-writer/aad}
die() { echo "c-adapter: $*" >&2; exit 2; }
cmd=${1:-}; shift || true
case "$cmd" in
  aar-decode)
    [ $# -eq 2 ] || die "usage: aar-decode IN.aar OUTDIR"
    [ -e "$1" ] || die "missing: $1"
    [ -x "$AAD" ] || die "missing binary: $AAD (build via make)"
    mkdir -p "$2"
    exec "$AAD" "$1" "$2"
    ;;
  probe|aar-encode|aar-list|aea-encrypt|aea-decrypt|aea-id)
    exec sh "$ORACLE" "$cmd" "$@"
    ;;
  *)
    die "unknown command: $cmd"
    ;;
esac
