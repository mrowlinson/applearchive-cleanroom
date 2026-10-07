#!/bin/sh
# tests/gate-tip.sh <rev> <ws-outdir> — sweep independent full-gate battery.
# legs: HYGIENE (PARENT-002 artifacts) / BATTERIES (rawenc/pbze/units/smoke
# as present in tip) / SMOKE-IMPL* (smoke via committed impl adapters) /
# PINS (vectors/*-PINS.csv vs fresh got.aar, stale-name detection) /
# CONTAM (vendor/disasm grep + Mach-O scan) / OSS (PARENT-003 new-dep scan)
# / ADOPT (A-1 harness pins vs lanes/harness-oracle, best-effort).
# exit 0 GATE-PASS / 1 GATE-FAIL. all work under /Volumes/NVME only.
# v2: PIN-STALE-NAME + UNPINNED-AAR, SMOKE-IMPL/IMPL2, committed-.aea WARN,
# OUTER2 battery + outer2 pins, dual-suffix (.got.aar/.got.aea) pin legs.
set -u
REV=${1:?usage: gate-tip.sh <rev> <ws-outdir>}
OUT=${2:?usage: gate-tip.sh <rev> <ws-outdir>}
case "$OUT" in /Volumes/NVME/*) ;; *) echo "GATE-FAIL $REV outdir-not-nvme"; exit 1;; esac
REPO=$(git rev-parse --show-toplevel)
rm -rf "$OUT"; mkdir -p "$OUT/tree" "$OUT/work"
git -C "$REPO" archive "$REV" | tar -x -C "$OUT/tree" || { echo "GATE-FAIL $REV archive"; exit 1; }
find "$OUT/tree" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null
fail=0
say() { echo "GATELEG $1 $2"; }

# 1. HYGIENE: artifact paths in the TIP TREE (not the stripped extract)
ARTS=$(git -C "$REPO" ls-tree -r --name-only "$REV" | grep -E '(__pycache__|\.pyc$|\.pyo$|\.o$|\.a$|\.dylib$|\.ktrace$|/traces/|DerivedData/|\.aar$)' || true)
if [ -n "$ARTS" ]; then fail=1; say HYGIENE "FAIL artifacts:"; echo "$ARTS" | sed 's/^/  /';
else say HYGIENE "PASS no-artifacts"; fi
GI=$(git -C "$REPO" show "$REV:.gitignore" 2>/dev/null || true)
case "$GI" in *__pycache__*|*.pyc*) say GITIGNORE "PASS pyc-rules";; *) say GITIGNORE "WARN no-pyc-rules";; esac
AEAS=$(git -C "$REPO" ls-tree -r --name-only "$REV" | grep -E '\.aea$' || true)
if [ -n "$AEAS" ]; then say AEA-BIN "WARN committed-aea:"; echo "$AEAS" | sed 's/^/  /'; fi

# 2. CONTAM: vendor/disasm markers in tip text + Mach-O scan of extract
CPAT='ghidra|binary ninja|hopper|ida pro|\.framework/|PrivateFrameworks|LC_SEGMENT|__TEXT,|decompile|disassembl'
CHIT=$(grep -rniE -I "$CPAT" "$OUT/tree" 2>/dev/null | grep -v '^Binary' || true)
MHIT=$(find "$OUT/tree" -type f -exec sh -c 'file -b "$1" | grep -q "Mach-O" && echo "$1"' _ {} \; 2>/dev/null || true)
if [ -n "$CHIT$MHIT" ]; then fail=1; say CONTAM "FAIL:"; [ -n "$CHIT" ] && echo "$CHIT" | sed 's/^/  /'; [ -n "$MHIT" ] && echo "$MHIT" | sed 's/^/  mach-o /';
else say CONTAM "PASS 0-hits"; fi

# 3. BATTERIES (each present script, own WS workdir, grepped oks)
runb() { # $1=leg $2=script-path-in-tree $3=invoke...
  leg=$1; sp=$2; shift 2
  [ -e "$OUT/tree/$sp" ] || { say "$leg" "SKIP absent"; return; }
  log="$OUT/work-$leg.log"
  if "$@" >"$log" 2>&1; then
    npass=$(grep -c '^PASS' "$log"); say "$leg" "PASS n=$npass"
  else fail=1; say "$leg" "FAIL (see work-$leg.log)"; grep -E '^(FAIL|.*RED)' "$log" | head -20 | sed 's/^/  /'; fi
}
runb RAWENC tests/test_rawenc.sh sh "$OUT/tree/tests/test_rawenc.sh" "$OUT/work/rawenc"
runb PBZE tests/test_pbze.sh sh "$OUT/tree/tests/test_pbze.sh" "$OUT/work/pbze"
runb SMOKE tests/smoke.sh sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke"
runb OUTER2 tests/test_outer2.sh sh "$OUT/tree/tests/test_outer2.sh" "$OUT/work/outer2"
runb SMOKE-IMPL harness/impl-adapter.sh env BACKEND="$OUT/tree/harness/impl-adapter.sh" sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke-impl"
runb SMOKE-IMPL2 harness/impl2-adapter.sh env BACKEND="$OUT/tree/harness/impl2-adapter.sh" sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke-impl2"
runb UNITS tests/test_units.py python3 "$OUT/tree/tests/test_units.py"

# 4. PINS: each csv row vs fresh got.aar (full sha256 + bytes)
pinleg() { # $1=csv-in-tree $2=workdir $3=leg
  [ -f "$OUT/tree/$1" ] || { say "$3" "SKIP no-csv"; return; }
  n=0; bad=0
  while IFS=, read -r name sha bytes rest; do
    case "$name" in ''|'#'*) continue;; esac
    name=$(printf '%s' "$name" | tr -d '\r'); sha=$(printf '%s' "$sha" | tr -d '\r'); bytes=$(printf '%s' "$bytes" | tr -d '\r')
    n=$((n+1)); f="$2/$name.got.aar"; [ -f "$f" ] || f="$2/$name.got.aea"
    if [ -f "$f" ]; then
      got=$(shasum -a 256 "$f" | cut -d' ' -f1); sz=$(stat -f %z "$f")
      [ "$got" = "$sha" ] && [ "$sz" = "$bytes" ] || { bad=$((bad+1)); echo "  PIN-MISMATCH $name got=$got/$sz want=$sha/$bytes"; }
    else
      cands=$(ls "$2/$name."*.got.aar "$2/$name."*.got.aea 2>/dev/null | sed "s|^$2/||" | tr '\n' ' ')
      bad=$((bad+1))
      if [ -n "$cands" ]; then echo "  PIN-STALE-NAME $name (no such artifact; candidates: $cands)";
      else echo "  PIN-MISSING-AAR $name"; fi
    fi
  done < "$OUT/tree/$1"
  for af in "$2"/*.got.aar "$2"/*.got.aea; do
    [ -e "$af" ] || continue
    base=$(basename "$af" .got.aar); hit=0
    while IFS=, read -r pname prest; do
      case "$pname" in ''|'#'*) continue;; esac
      pname=$(printf '%s' "$pname" | tr -d '\r')
      case "$base" in "$pname"|"$pname".*) hit=1; break;; esac
    done < "$OUT/tree/$1"
    [ "$hit" -eq 1 ] || echo "  UNPINNED-AAR $base (no csv row; ok iff live compare-only)"
  done
  [ "$bad" -eq 0 ] && say "$3" "PASS $n/$n" || { fail=1; say "$3" "FAIL bad=$bad/$n"; }
}
pinleg vectors/rawenc-PINS.csv "$OUT/work/rawenc" PINS-RAWENC
pinleg vectors/pbze-PINS.csv "$OUT/work/pbze" PINS-PBZE
pinleg vectors/outer2-PINS.csv "$OUT/work/outer2" PINS-OUTER2

# 5. OSS: third-party lib loads in src+harness (PARENT-003 gate 3).
# system libc (/usr/lib, /System) + bare ctypes stdlib use are NOT deps.
# a loading file is clean iff it names an already-nominated lib (lzfse, NOTE-013).
OHIT=$(grep -rniE -I 'CDLL\(|cdll\.LoadLibrary|\.dylib|\.so\b|git submodule|add_subdirectory' "$OUT/tree/src" "$OUT/tree/harness" 2>/dev/null | grep -v '/usr/lib/' | grep -v '/System/' || true)
ONEW=""
for _f in $(echo "$OHIT" | cut -d: -f1 | sort -u); do
  [ -z "$_f" ] && continue
  grep -qi 'lzfse' "$_f" || ONEW="$ONEW $_f"
done
if [ -n "$ONEW" ]; then fail=1; say OSS "FAIL new-oss:$ONEW"; echo "$OHIT" | sed 's/^/  /';
elif [ -n "$OHIT" ]; then say OSS "PASS lzfse-only"; else say OSS "PASS none"; fi

# 6. ADOPT: A-1 pins vs lanes/harness-oracle (best-effort)
if git -C "$REPO" rev-parse -q --verify lanes/harness-oracle >/dev/null; then
  ok=1
  for p in harness/oracle-adapter.sh tests/smoke.sh; do
    a=$(git -C "$REPO" show "lanes/harness-oracle:$p" 2>/dev/null | shasum -a 256 | cut -c1-8)
    b=$(git -C "$REPO" show "$REV:$p" 2>/dev/null | shasum -a 256 | cut -c1-8)
    [ -n "$a" ] && [ "$a" = "$b" ] || { ok=0; echo "  ADOPT-DIFF $p lane=$a tip=$b"; }
  done
  [ "$ok" -eq 1 ] && say ADOPT "PASS match" || say ADOPT "WARN diff-or-absent"
else say ADOPT "SKIP no-harness-lane"; fi

[ "$fail" -eq 0 ] && echo "GATE-PASS $REV" || echo "GATE-FAIL $REV"
exit $fail
