#!/bin/sh
# aeadc-shim.sh — run a proto/aead.py CLI line against the unified aae-cli.
# usage: CLI=path/to/aae-cli sh tests/aeadc-shim.sh <proto-argv...>
# Drops a leading proto/aead.py path arg (test_aea_enc.sh convention), then
# execs the unified binary's native `aeadc` passthrough subcommand with the
# identical flags (aead_main argv is flag-identical to the old aeadc binary).
set -u
CLI=${CLI:-/Volumes/NVME/applearchive-cleanroom-ws/build/unified/aae-cli}
if [ $# -ge 1 ]; then
  case "$1" in
    *aead.py) shift ;;
  esac
fi
exec "$CLI" aeadc "$@"
