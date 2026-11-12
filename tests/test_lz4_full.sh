#!/bin/sh
# tests/test_lz4_full.sh [workdir] [seedoff] — lz4 FULL census (oracle-vs-impl).
# CENSUS, not gate: exit 0 always; prints OK/BAD counts + BAD list.
# seedoff 0=FULL, 1000=holdout, 2000=fresh (disjoint random streams).
set -u
: "${TMPDIR:?must set TMPDIR to NVME scratch (never /tmp)}"
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
W=${1:-$(mktemp -d "$TMPDIR/lz4full.XXXXXX")}
SO=${2:-0}
ORACLE=${ORACLE:-/usr/bin/aa}
_IMP=${ENC_BIN:-python3 "$ROOT/src/encode.py"}
ok=0; bad=0; badlist=""
fix() { find "$1" -exec touch -d '2001-02-03 04:05:06' {} + 2>/dev/null; return 0; }
gen() { # $1=name $2=pycode(body bytes)
  mkdir -p "$W/in/$1"
  python3 -c "import random;random.seed($SO+$3);open('$W/in/$1/n','wb').write($2)"
  fix "$W/in/$1"
  "$ORACLE" archive -a lz4 -t 1 -d "$W/in/$1" -o "$W/$1.expect.aar" 2>/dev/null
  $_IMP "$W/in/$1" "$W/$1.got.aar" --alg lz4 2>/dev/null
  if cmp -s "$W/$1.expect.aar" "$W/$1.got.aar"; then ok=$((ok+1));
  else bad=$((bad+1)); badlist="$badlist $1"; fi
}
SZ="0 1 10 100 1000 4096 16384 65535 65536 65537 100000 131071 131072 262144"
i=0
for s in $SZ; do
  i=$((i+1))
  gen "z$s" "b'\x00'*$s" $i
  i=$((i+1))
  gen "c$s" "b'\xAB'*$s" $i
  i=$((i+1))
  gen "r$s" "bytes(random.randrange(256) for _ in range($s))" $i
  i=$((i+1))
  gen "p8_$s" "(b'abcdefgh'*$((s/8+1)))[:$s]" $i
done
i=$((i+1)); gen "mix1m" "bytes(random.randrange(256) for _ in range(524288))+b'\x00'*524288" $i
i=$((i+1)); gen "mix2m" "b'\x7f'*1048576+bytes(random.randrange(256) for _ in range(1048576))" $i
i=$((i+1)); gen "txt100k" "(b'the quick brown fox jumps over the lazy dog. '*2500)[:100000]" $i
i=$((i+1)); gen "rz70k" "bytes(random.randrange(256) for _ in range(69632))+b'\x00'*370" $i
echo "FULL-CENSUS seedoff=$SO OK=$ok BAD=$bad"
echo "BADLIST:$badlist"
exit 0
