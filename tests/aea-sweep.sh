#!/bin/sh
# aea-sweep.sh v2 -- proto robustness + oracle error-class parity.
# v1 cells: exit!=0 + no hang on sampled truncs/corrupts (proto only).
# v2 cells: exit-agreement + byte-agreement (when both accept) vs oracle.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
AEAD_PY=${AEAD_PY:-/Volumes/NVME/applearchive-cleanroom-ws/writer2/.venv/bin/python}
WORK=$(mktemp -d "${TMPDIR:-/tmp}/aea-sweep.XXXXXX")
trap 'rm -rf "$WORK"' EXIT
PW='testpw32....................................'
printf 'sweep-input-bytes\n' > "$WORK/in.bin"
aea encrypt -profile 5 -password-value "$PW" -a none -padding none -i "$WORK/in.bin" -o "$WORK/t.aea" 2>/dev/null
aea encrypt -profile 5 -password-value "$PW" -a none -i "$WORK/in.bin" -o "$WORK/u.aea" 2>/dev/null
SZ=$(stat -f%z "$WORK/t.aea")
PZ=$(stat -f%z "$WORK/u.aea")
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
python3 - "$WORK/t.aea" "$WORK" "$WORK/u.aea" <<'EOF'
import random,sys
blob=open(sys.argv[1],"rb").read()
r=random.Random(7)
for j in range(50):
    i=r.randrange(len(blob)); b=bytearray(blob); b[i]^=1<<r.randrange(8)
    open("%s/c%d.aea"%(sys.argv[2],j),"wb").write(bytes(b))
pblob=open(sys.argv[3],"rb").read()
r2=random.Random(77)
for j in range(50):
    i=r2.randrange(len(pblob)); b=bytearray(pblob); b[i]^=1<<r2.randrange(8)
    open("%s/d%d.aea"%(sys.argv[2],j),"wb").write(bytes(b))
EOF
j=0
while [ "$j" -lt 50 ]; do chk "$WORK/c$j.aea" "corrupt-$j"; j=$((j+1)); done
# padded leg: truncs + edges + corrupts must all exit!=0 too
i=0
while [ "$i" -lt "$PZ" ]; do
  head -c "$i" "$WORK/u.aea" > "$WORK/ptr.aea" 2>/dev/null
  chk "$WORK/ptr.aea" "p-trunc-$i"
  i=$((i+1024))
done
for k in 0 1 7 8 9 11 12 13 155 156 157; do
  head -c "$k" "$WORK/u.aea" > "$WORK/ptr.aea" 2>/dev/null
  chk "$WORK/ptr.aea" "p-edge-$k"
done
j=0
while [ "$j" -lt 50 ]; do chk "$WORK/d$j.aea" "p-corrupt-$j"; j=$((j+1)); done
# v2 parity: same corpus vs oracle (exit-agreement + accept-byte-agreement)
export WORK AEAD_PY REPO PW
PAR_OUT=$(python3 - <<'EOF'
import hashlib, os, subprocess
W = os.environ["WORK"]; py = os.environ["AEAD_PY"]
repo = os.environ["REPO"]; pw = os.environ["PW"]
files = []
bases = [("t.aea", "c%d.aea", ""), ("u.aea", "d%d.aea", "p-")]
blobs = {}
for base, _, _ in bases:
    blobs[base] = open(os.path.join(W, base), "rb").read()
for base, cpat, pfx in bases:
    sz = len(blobs[base])
    i = 0
    while i < sz:
        files.append((pfx + "trunc-%d" % i, (base, i, None))); i += 1024
    for k in (0, 1, 7, 8, 9, 11, 12, 13, 155, 156, 157):
        files.append((pfx + "edge-%d" % k, (base, k, None)))
    for j in range(50):
        files.append((pfx + "corrupt-%d" % j, (base, None, j)))
cpat_of = {b: c for b, c, _ in bases}
n = bad = acc = 0
for tag, (base, tr, cj) in files:
    if tr is not None:
        data = blobs[base][:tr]
    else:
        data = open(os.path.join(W, cpat_of[base] % cj), "rb").read()
    p = os.path.join(W, "par.aea")
    open(p, "wb").write(data)
    try:
        o = subprocess.run(["aea", "decrypt", "-password-value", pw,
                            "-i", p, "-o", W + "/par-ora.bin"],
                           capture_output=True, timeout=30)
        oexit = o.returncode
        ohash = hashlib.sha256(open(W + "/par-ora.bin", "rb").read()).hexdigest() \
            if oexit == 0 else "-"
    except Exception:
        oexit, ohash = "HANG", "-"
    try:
        r = subprocess.run([py, repo + "/proto/aead.py", "decrypt",
                            "--password", pw, "-i", p, "-o", W + "/par-pro.bin"],
                           capture_output=True, timeout=30)
        pexit = r.returncode
        phash = hashlib.sha256(open(W + "/par-pro.bin", "rb").read()).hexdigest() \
            if pexit == 0 else "-"
    except Exception:
        pexit, phash = "HANG", "-"
    n += 1
    if oexit == 0 and pexit == 0:
        acc += 1
    if (oexit == 0) != (pexit == 0) or (oexit == 0 and ohash != phash):
        bad += 1
        print("FAIL par-%s ora=%s pro=%s" % (tag, oexit, pexit))
print("PARITY n=%d bad=%d bothaccept=%d" % (n, bad, acc))
EOF
)
echo "$PAR_OUT" | grep -E '^FAIL' || true
PAR_BAD=$(echo "$PAR_OUT" | sed -n 's/^PARITY n=[0-9]* bad=\([0-9]*\).*/\1/p')
PAR_N=$(echo "$PAR_OUT" | sed -n 's/^PARITY n=\([0-9]*\).*/\1/p')
echo "$PAR_OUT" | grep '^PARITY'
BAD=$((BAD + PAR_BAD)); N=$((N + PAR_N))
echo "SWEEP n=$N bad=$BAD"
[ "$BAD" -eq 0 ] && echo SWEEP-GREEN
