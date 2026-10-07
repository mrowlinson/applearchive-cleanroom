#!/bin/sh
# aea-wide.sh v1 -- writer2 wide corpus (FULL-equivalent) + holdout.
# Matrix: sizes x profiles{1,5} x algs{none,zlib} x cksum{none,sha256} + spots.
# Deterministic data (seeded). Exits 0 WIDE-GREEN / 1 any FAIL.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
AEAD_PY=${AEAD_PY:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/.venv/bin/python}
LZFSE_BIN=${LZFSE_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/lzfse/build/bin/lzfse}
ZBM_BIN=${ZBM_BIN:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/oss/zbm/zbmcat}
export LZFSE_BIN ZBM_BIN
WORK=$(mktemp -d "${TMPDIR:-/tmp}/aea-wide.XXXXXX")
trap 'rm -rf "$WORK"' EXIT
PASS=0; FAIL=0
PW='testpw32....................................'
head -c 32 /dev/urandom > "$WORK/key32.bin"

mkdata() { # size seed file
  python3 -c "
import random,sys
n,s=int(sys.argv[1]),int(sys.argv[2])
r=random.Random(s)
open(sys.argv[3],'wb').write(bytes(r.randrange(256) for _ in range(n)))
" "$1" "$2" "$3"
}

one() { # tag profile alg cksum infile
  tag=$1; prof=$2; alg=$3; ck=$4; in=$5
  case $prof in
    1) CRED="-key $WORK/key32.bin"; PCRED="--key $WORK/key32.bin";;
    5) CRED="-password-value $PW"; PCRED="--password $PW";;
  esac
  if ! eval aea encrypt -profile "$prof" "$CRED" -a "$alg" -padding none -checksum "$ck" -i "$in" -o "$WORK/t.aea" 2>/dev/null; then
    echo "FAIL $tag-enc"; FAIL=$((FAIL+1)); return
  fi
  # shellcheck disable=SC2086
  if ! "$AEAD_PY" "$REPO/proto/aead.py" decrypt $PCRED -i "$WORK/t.aea" -o "$WORK/t.out" 2>/dev/null; then
    echo "FAIL $tag-dec"; FAIL=$((FAIL+1)); return
  fi
  if cmp -s "$WORK/t.out" "$in"; then PASS=$((PASS+1)); else echo "FAIL $tag-cmp"; FAIL=$((FAIL+1)); fi
}

# FULL-equivalent: seed 7, 8 sizes x 2 prof x 2 alg x 2 ck = 64
for sz in 1 16 1024 65536 262144 1048576 1048577 3000000; do
  mkdata "$sz" 7 "$WORK/in.bin"
  for prof in 1 5; do for alg in none zlib; do for ck in none sha256; do
    one "full-$sz-$prof-$alg-$ck" "$prof" "$alg" "$ck" "$WORK/in.bin"
  done; done; done
done

# holdout: seed 99, 4 sizes x 2 prof, lzma+lz4 spots
for sz in 100 70000 500000 1500000; do
  mkdata "$sz" 99 "$WORK/h.bin"
  one "hold-$sz-1-lzma-sha" 1 lzma sha256 "$WORK/h.bin"
  one "hold-$sz-5-lz4-none" 5 lz4 none "$WORK/h.bin"
done

echo "PASS=$PASS FAIL=$FAIL"
[ "$FAIL" -eq 0 ] && echo WIDE-GREEN
