#!/bin/sh
# harness/impl-adapter.sh — LEGACY encode-side shim (writer1 race era).
# SCOPE: aar-encode only for raw/lzfse/zlib via src/encode.py; every other
# subcommand passes through to the ORACLE adapter (oracle bytes execute
# here — never mistake this shim for impl coverage). The shipped impl
# path is the unified CLI: src/aae-cli (Python reference) and
# ./build/aae-cli (C binary), exercised directly by tests/test_cli.sh.
# Same CLI contract as oracle-adapter.sh.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ORACLE=$HERE/oracle-adapter.sh
ENC=$HERE/../src/encode.py
cmd=${1:-}; shift || true
case "$cmd" in
  probe)
    echo "backend=encimpl(writer1)"
    echo "impl=$ENC"
    python3 -c "import sys; print('python=%s' % sys.version.split()[0])"
    sh "$ORACLE" probe
    ;;
  aar-encode)
    alg=raw; block=""; threads=""
    while [ $# -gt 2 ]; do
      case "$1" in
        --alg) alg=$2; shift 2;;
        --block) block=$2; shift 2;;
        --threads) threads=$2; shift 2;;
        *) echo "impl-adapter: bad flag $1" >&2; exit 2;;
      esac
    done
    [ $# -eq 2 ] || { echo "usage: impl-adapter aar-encode [--alg A] [--block S] [--threads N] SRCDIR OUT" >&2; exit 2; }
    exec python3 "$ENC" "$1" "$2" --alg "$alg" ${block:+--block "$block"} ${threads:+--threads "$threads"}
    ;;
  aar-decode|aar-list|aea-encrypt|aea-decrypt|aea-id)
    exec sh "$ORACLE" "$cmd" "$@"
    ;;
  *) echo "usage: impl-adapter probe|aar-encode|aar-decode|aar-list|aea-encrypt|aea-decrypt|aea-id ..." >&2; exit 2;;
esac
