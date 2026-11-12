#!/bin/sh
# aeadc-shim.sh — run a proto/aead.py CLI line against the C aeadc binary.
# usage: AEADC=path/to/aeadc sh tests/aeadc-shim.sh <proto-argv...>
# Drops a leading proto/aead.py path arg (test_aea_enc.sh convention), then
# execs aeadc with the identical flags (aeadc CLI is flag-identical).
set -u
AEADC=${AEADC:-/Volumes/NVME/applearchive-cleanroom-ws/build/cport-aead/aeadc}
if [ $# -ge 1 ]; then
  case "$1" in
    *aead.py) shift ;;
  esac
fi
exec "$AEADC" "$@"
