#!/bin/sh
# oracle-adapter.sh — vendor backend for the harness CLI contract (see CLI-CONTRACT.md).
# Wave-1 stub: thin, working wrapper over /usr/bin/aa + /usr/bin/aea. No battery logic here.
# Usage: oracle-adapter.sh <probe|aar-encode|aar-decode|aar-list|aea-encrypt|aea-decrypt|aea-id> [args]
set -eu

AA=${AA:-/usr/bin/aa}
AEA=${AEA:-/usr/bin/aea}

die() { echo "adapter: $*" >&2; exit 2; }
need_file() { [ -e "$1" ] || die "missing: $1"; }

cmd=${1:-}; shift || true

case "$cmd" in
  probe)
    echo "backend=oracle"
    echo "date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "os=$(sw_vers -productVersion 2>/dev/null || echo unknown)"
    echo "arch=$(uname -m)"
    for t in "$AA" "$AEA"; do
      need_file "$t"
      echo "tool=$t sha256=$(shasum -a 256 "$t" | cut -d' ' -f1) bytes=$(stat -f%z "$t")"
    done
    ;;
  aar-encode)
    # adapter aar-encode --alg ALG [--block SIZE] [--threads N] SRCDIR OUT.aar
    alg=""; block=""; threads="1"
    while [ $# -gt 0 ]; do
      case "$1" in
        --alg) alg=$2; shift 2;;
        --block) block=$2; shift 2;;
        --threads) threads=$2; shift 2;;
        --) shift; break;;
        -*) die "unknown flag: $1";;
        *) break;;
      esac
    done
    [ -n "$alg" ] || die "aar-encode needs --alg"
    [ $# -eq 2 ] || die "usage: aar-encode --alg ALG [--block S] [--threads N] SRCDIR OUT.aar"
    [ -d "$1" ] || die "srcdir not a dir: $1"
    set -- "$AA" archive -d "$1" -a "$alg" -t "$threads" ${block:+-b "$block"} -o "$2"
    exec "$@"
    ;;
  aar-decode)
    # adapter aar-decode IN.aar OUTDIR
    # PARENT-024 (a): always -t 1 (deterministic block-layer
    # error-path mirror target; default threading races failure
    # cosmetics machine-dependently).
    [ $# -eq 2 ] || die "usage: aar-decode IN.aar OUTDIR"
    need_file "$1"
    mkdir -p "$2"
    exec "$AA" extract -t 1 -i "$1" -d "$2"
    ;;
  aar-list)
    # adapter aar-list IN.aar  (bytes-in, text-out)
    [ $# -eq 1 ] || die "usage: aar-list IN.aar"
    need_file "$1"
    exec "$AA" list -i "$1"
    ;;
  aea-encrypt)
    # adapter aea-encrypt --profile P [--alg A] [--block S] [--threads N] [--password PW | --key HEX] IN OUT
    # IN/OUT may be - for stdio. Flags verified vs local `aea encrypt -h` 2026-10-07.
    profile=""; alg=""; block=""; threads="1"; pass=""; key=""
    while [ $# -gt 0 ]; do
      case "$1" in
        --profile) profile=$2; shift 2;;
        --alg) alg=$2; shift 2;;
        --block) block=$2; shift 2;;
        --threads) threads=$2; shift 2;;
        --password) pass=$2; shift 2;;
        --key) key=$2; shift 2;;
        --) shift; break;;
        -*) die "unknown flag: $1";;
        *) break;;
      esac
    done
    [ -n "$profile" ] || die "aea-encrypt needs --profile"
    [ $# -eq 2 ] || die "usage: aea-encrypt --profile P [opts] IN OUT"
    [ "$1" != "-" ] && need_file "$1"
    # shellcheck disable=SC2086
    exec "$AEA" encrypt -profile "$profile" -t "$threads" \
      ${alg:+-a "$alg"} ${block:+-b "$block"} \
      ${pass:+-password-value "$pass"} ${key:+-key-value "$key"} \
      -i "$1" -o "$2"
    ;;
  aea-decrypt)
    # adapter aea-decrypt [--password PW | --key HEX] IN OUT
    pass=""; key=""
    while [ $# -gt 0 ]; do
      case "$1" in
        --password) pass=$2; shift 2;;
        --key) key=$2; shift 2;;
        --) shift; break;;
        -*) die "unknown flag: $1";;
        *) break;;
      esac
    done
    [ $# -eq 2 ] || die "usage: aea-decrypt [--password PW|--key HEX] IN OUT"
    [ "$1" != "-" ] && need_file "$1"
    # shellcheck disable=SC2086
    exec "$AEA" decrypt ${pass:+-password-value "$pass"} ${key:+-key-value "$key"} -i "$1" -o "$2"
    ;;
  aea-id)
    [ $# -eq 1 ] || die "usage: aea-id IN"
    need_file "$1"
    exec "$AEA" id -i "$1"
    ;;
  ""|-h|--help|help)
    sed -n '2,4p' "$0"
    echo "commands: probe aar-encode aar-decode aar-list aea-encrypt aea-decrypt aea-id"
    ;;
  *)
    die "unknown command: $cmd"
    ;;
esac
