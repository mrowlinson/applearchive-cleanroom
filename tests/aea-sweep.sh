#!/bin/sh
# aea-sweep.sh v1 -- proto robustness regression (no oracle at run time).
# Asserts exit!=0 + no hang on sampled truncs/corrupts of a fixed selfgen archive.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
AEAD_PY=${AEAD_PY:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/.venv/bin/python}
WORK=$(mktemp -d "${TMPDIR:-/tmp}/aea-sweep.XXXXXX")
trap 'rm -rf "$WORK"' EXIT
PW='testpw32....................................'
printf 'sweep-input-bytes\n' > "$WORK/in.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/in.bin" -o "$WORK/t.aea" 2>/dev/null
SZ=$(stat -f%z "$WORK/t.aea")
BAD=0; N=0
chk() { # file tag
  N=$((N+1))
  if "$AEAD_PY" "$REPO/proto/aead.py" decrypt --password "$PW" -i "$1" -o "$WORK/o.bin" 2>/dev/null; then
    echo "FAIL exit0 $2"; BAD=$((BAD+1))
  fi
}
i=0
while [ "$i" -lt "$SZ" ]; do
  head -c "$i" "$WORK/t.aea" > "$WORK/tr.aea" 2>/dev/null
  chk "$WORK/tr.aea" "trunc-$i"
  i=$((i+1024))
done
for k in 0 1 7 8 9 11 12 13 155 156 157; do
  head -c "$k" "$WORK/t.aea" > "$WORK/tr.aea" 2>/dev/null
  chk "$WORK/tr.aea" "edge-$k"
done
python3 - "$WORK/t.aea" "$WORK" <<'EOF'
import random,sys
blob=open(sys.argv[1],"rb").read()
r=random.Random(7)
for j in range(50):
    i=r.randrange(len(blob)); b=bytearray(blob); b[i]^=1<<r.randrange(8)
    open("%s/c%d.aea"%(sys.argv[2],j),"wb").write(bytes(b))
EOF
j=0
while [ "$j" -lt 50 ]; do chk "$WORK/c$j.aea" "corrupt-$j"; j=$((j+1)); done
echo "SWEEP n=$N bad=$BAD"
[ "$BAD" -eq 0 ] && echo SWEEP-GREEN
