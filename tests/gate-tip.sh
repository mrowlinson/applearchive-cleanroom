#!/bin/sh
# tests/gate-tip.sh <rev> <ws-outdir> — sweep independent full-gate battery.
# legs: HYGIENE (PARENT-002 artifacts) / BATTERIES (rawenc/pbze/units/smoke
# as present in tip) / SMOKE-IMPL* (smoke via committed impl adapters) /
# PINS (vectors/*-PINS.csv vs fresh got.aar, stale-name detection) /
# CONTAM (vendor/disasm grep + Mach-O scan + PARENT-009 depload scan) / OSS (PARENT-003 new-dep scan; A-20 liblzma recognized)
# / ADOPT (A-1 harness pins vs lanes/harness-oracle, best-effort).
# exit 0 GATE-PASS / 1 GATE-FAIL. all work under /Volumes/NVME only.
# v2: PIN-STALE-NAME + UNPINNED-AAR, SMOKE-IMPL/IMPL2, committed-.aea WARN,
# OUTER2 battery + PINS-OUTER2 setdiff leg, dual-suffix (.got.aar/.got.aea) pin legs,
# C-BUILD + RAWENC-C/PBZE-C + PINS-*-C (ENC_BIN parity), HYGIENE tmp/scratch- (PARENT-005),
# RUN_BIG rawenc legs + PIN-ATTESTED log cross-check, LIBCOMPRESSION deny (PARENT-007),
# RB2 battery + PINS-RB2 setdiff leg (w2 frame IMPL),
# RAVFRAME battery + PINS-RAVFRAME setdiff leg (w2 raven IMPL),
# LZMA/LZMA-C batteries (w1 lzma IMPL, no pins csv yet).
set -u
REV=${1:?usage: gate-tip.sh <rev> <ws-outdir>}
OUT=${2:?usage: gate-tip.sh <rev> <ws-outdir>}
case "$OUT" in /Volumes/NVME/*) ;; *) echo "GATE-FAIL $REV outdir-not-nvme"; exit 1;; esac
SELFDIR=$(cd "$(dirname "$0")" && pwd)
REPO=$(git -C "$SELFDIR" rev-parse --show-toplevel 2>/dev/null || git rev-parse --show-toplevel 2>/dev/null || true)
[ -n "$REPO" ] || { echo "GATE-FAIL $REV no-repo-resolved"; exit 1; }
git -C "$REPO" cat-file -e "$REV^{commit}" 2>/dev/null || { echo "GATE-FAIL $REV no-such-rev"; exit 1; }
rm -rf "$OUT"; mkdir -p "$OUT/tree" "$OUT/work"
git -C "$REPO" archive "$REV" >"$OUT/tree.tar" || { echo "GATE-FAIL $REV archive"; exit 1; }
tar -x -C "$OUT/tree" -f "$OUT/tree.tar" || { echo "GATE-FAIL $REV extract"; exit 1; }
[ -n "$(ls -A "$OUT/tree")" ] || { echo "GATE-FAIL $REV empty-tree"; exit 1; }
find "$OUT/tree" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null
fail=0
say() { echo "GATELEG $1 $2"; }
# PARENT-003/A-20: nominated-dep files (lzfse always; liblzma iff pin-marked;
# system-libc-only FFI iff every load line is a system path — rawenc precedent).
nominated() {
  if grep -qi 'lzfse' "$1"; then return 0; fi
  if grep -qi 'lzma' "$1" && grep -q '5\.8\.4' "$1" && { grep -q '1b2e12cc' "$1" || grep -q 'A-20' "$1"; }; then return 0; fi
  loaded=$(grep -niE -i 'CDLL|LoadLibrary|\.dylib|(^|[^.a-zA-Z0-9])dylib' "$1" | grep -viE '/usr/lib/|/System/' || true)
  [ -z "$loaded" ] && return 0
  return 1
}

# 1. HYGIENE: artifact paths in the TIP TREE (not the stripped extract)
ARTS=$(git -C "$REPO" ls-tree -r --name-only "$REV" | grep -E '(__pycache__|\.pyc$|\.pyo$|\.o$|\.a$|\.dylib$|\.ktrace$|/traces/|DerivedData/|\.aar$|tmp/scratch-)' || true)
if [ -n "$ARTS" ]; then fail=1; say HYGIENE "FAIL artifacts:"; echo "$ARTS" | sed 's/^/  /';
else say HYGIENE "PASS no-artifacts"; fi
GI=$(git -C "$REPO" show "$REV:.gitignore" 2>/dev/null || true)
case "$GI" in *__pycache__*|*.pyc*) say GITIGNORE "PASS pyc-rules";; *) say GITIGNORE "WARN no-pyc-rules";; esac
AEAS=$(git -C "$REPO" ls-tree -r --name-only "$REV" | grep -E '\.aea$' || true)
if [ -n "$AEAS" ]; then say AEA-BIN "WARN committed-aea:"; echo "$AEAS" | sed 's/^/  /'; fi

# 2. CONTAM: vendor/disasm markers in tip text + Mach-O scan of extract
CPAT='ghidra|binary ninja|hopper|ida pro|\.framework/|PrivateFrameworks|LC_SEGMENT|__TEXT,|decompile|disassembl'
CHIT=$(grep -rniE -I "$CPAT" "$OUT/tree" 2>/dev/null | grep -v '^Binary' | grep -v 'CPAT=' || true)
MHIT=$(find "$OUT/tree" -type f -exec sh -c 'file -b "$1" | grep -q "Mach-O" && echo "$1"' _ {} \; 2>/dev/null || true)
# PARENT-009: bare dep-loader refs (catches wrapped `libzbm<nl>dylib` class).
# excluded: tests/ (beds-OK exec per PARENT-007(1)), docs/ + *FINDINGS*
# (dep records PARENT-008 REQUIRES named), system libc, nominated files.
DPAT='dylib|CDLL|dlopen|ctypes'
DHITRAW=$(grep -rniE -I "$DPAT" "$OUT/tree" --exclude-dir=tests --exclude-dir=docs --exclude='*FINDINGS*' --exclude='.gitignore' 2>/dev/null | grep -v '^Binary' | grep -viE '/usr/lib/|/System/|DPAT=|OHIT=' || true)
DHITF=""
for _f in $(echo "$DHITRAW" | cut -d: -f1 | sort -u); do
  [ -z "$_f" ] && continue
  nominated "$_f" || DHITF="$DHITF $_f"
done
if [ -n "$CHIT$MHIT$DHITF" ]; then fail=1; say CONTAM "FAIL:"; [ -n "$CHIT" ] && echo "$CHIT" | sed 's/^/  /'; [ -n "$MHIT" ] && echo "$MHIT" | sed 's/^/  mach-o /';
  for _f in $DHITF; do echo "$DHITRAW" | grep -F "$_f:" | sed 's/^/  depload /'; done
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
# 3a. C-BUILD (C port parity; build outputs to per-gate NVME dir only)
if [ -e "$OUT/tree/src/c/Makefile" ]; then
  if make -C "$OUT/tree/src/c" BUILDDIR="$OUT/build" >"$OUT/work-C-BUILD.log" 2>&1 && [ -x "$OUT/build/aae" ]; then
    nw=$(grep -ci 'warning' "$OUT/work-C-BUILD.log" || true)
    say C-BUILD "PASS warnings=$nw"
  else fail=1; say C-BUILD "FAIL (see work-C-BUILD.log)"; tail -20 "$OUT/work-C-BUILD.log" | sed 's/^/  /'; fi
else say C-BUILD "SKIP no-c-port"; fi
runb RAWENC tests/test_rawenc.sh env RUN_BIG=1 sh "$OUT/tree/tests/test_rawenc.sh" "$OUT/work/rawenc"
runb PBZE tests/test_pbze.sh sh "$OUT/tree/tests/test_pbze.sh" "$OUT/work/pbze"
runb LZMA tests/test_lzma.sh sh "$OUT/tree/tests/test_lzma.sh" "$OUT/work/lzma"
runb SMOKE tests/smoke.sh sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke"
runb OUTER2 tests/test_outer2.sh sh "$OUT/tree/tests/test_outer2.sh" "$OUT/work/outer2"
runb RB2 tests/test_rb2.sh sh "$OUT/tree/tests/test_rb2.sh" "$OUT/work/rb2"
runb RAVFRAME tests/test_ravframe.sh sh "$OUT/tree/tests/test_ravframe.sh" "$OUT/work/ravframe"
runb SMOKE-IMPL harness/impl-adapter.sh env BACKEND="$OUT/tree/harness/impl-adapter.sh" sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke-impl"
runb SMOKE-IMPL2 harness/impl2-adapter.sh env BACKEND="$OUT/tree/harness/impl2-adapter.sh" sh "$OUT/tree/tests/smoke.sh" "$OUT/work/smoke-impl2"
runb UNITS tests/test_units.py python3 "$OUT/tree/tests/test_units.py"
# 3b. C parity batteries (ENC_BIN override; c11/c13 bypass _IMP -> manual supplements at verdict)
if [ -e "$OUT/tree/src/c/aae.c" ]; then
  if [ -x "$OUT/build/aae" ]; then
    runb RAWENC-C tests/test_rawenc.sh env RUN_BIG=1 ENC_BIN="$OUT/build/aae" sh "$OUT/tree/tests/test_rawenc.sh" "$OUT/work/rawenc-c"
    runb PBZE-C tests/test_pbze.sh env ENC_BIN="$OUT/build/aae" sh "$OUT/tree/tests/test_pbze.sh" "$OUT/work/pbze-c"
    runb LZMA-C tests/test_lzma.sh env ENC_BIN="$OUT/build/aae" sh "$OUT/tree/tests/test_lzma.sh" "$OUT/work/lzma-c"
  else fail=1; say RAWENC-C "FAIL no-c-binary"; say PBZE-C "FAIL no-c-binary"; fi
else say RAWENC-C "SKIP no-c-port"; say PBZE-C "SKIP no-c-port"; fi

# 4. PINS: each csv row vs fresh got.aar (full sha256 + bytes)
# $4 (optional): battery log for attestation — rows whose artifacts the
# battery cleans in-band (RUN_BIG c13) PASS iff the log shows an exact
# bytes + sha-prefix match. trust basis: batteries read first-hand (honest
# cmp+shasum in code); attestation values must match the pin EXACTLY.
pinleg() { # $1=csv-in-tree $2=workdir $3=leg [$4=battery-log]
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
      att=$(grep -E "^PASS $name bytes=" "${4:-/dev/null}" 2>/dev/null | head -1)
      attb=$(printf '%s' "$att" | sed -n 's/.*bytes=\([0-9]*\).*/\1/p')
      atts=$(printf '%s' "$att" | sed -n 's/.*sha=\([0-9a-f]*\).*/\1/p')
      case "$sha" in "$atts"*) attm=1;; *) attm=0;; esac
      if [ -n "$att" ] && [ -n "$atts" ] && [ "$attb" = "$bytes" ] && [ "$attm" -eq 1 ]; then
        echo "  PIN-ATTESTED $name (in-band battery PASS, sha16+bytes match)"
      else
        cands=$(ls "$2/$name."*.got.aar "$2/$name."*.got.aea 2>/dev/null | sed "s|^$2/||" | tr '\n' ' ')
        bad=$((bad+1))
        if [ -n "$cands" ]; then echo "  PIN-STALE-NAME $name (no such artifact; candidates: $cands)";
        else echo "  PIN-MISSING-AAR $name"; fi
      fi
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
pinleg vectors/rawenc-PINS.csv "$OUT/work/rawenc" PINS-RAWENC "$OUT/work-RAWENC.log"
pinleg vectors/pbze-PINS.csv "$OUT/work/pbze" PINS-PBZE "$OUT/work-PBZE.log"
if [ -x "$OUT/build/aae" ]; then
  pinleg vectors/rawenc-PINS.csv "$OUT/work/rawenc-c" PINS-RAWENC-C "$OUT/work-RAWENC-C.log"
  pinleg vectors/pbze-PINS.csv "$OUT/work/pbze-c" PINS-PBZE-C "$OUT/work-PBZE-C.log"
else say PINS-RAWENC-C "SKIP no-c-binary"; say PINS-PBZE-C "SKIP no-c-binary"; fi
# 4b. PINSET: schema-agnostic pin coverage — battery-reported PASS set must
# equal the csv row set exactly (catches skipped/renamed/unpinned cells
# without duplicating the battery's name->artifact map). for outer2 the
# battery is self-checking (fresh-measured vs committed, read first-hand).
pinsetleg() { # $1=csv-in-tree $2=battery-log $3=leg
  [ -f "$OUT/tree/$1" ] || { say "$3" "SKIP no-csv"; return; }
  [ -f "$2" ] || { fail=1; say "$3" "FAIL no-battery-log"; return; }
  grep -vE '^(#|$)' "$OUT/tree/$1" | cut -d, -f1 | tr -d '\r' | sort -u > "$OUT/work-$3.rows"
  grep -oE '^PASS [^ ]+' "$2" | cut -d' ' -f2 | sort -u > "$OUT/work-$3.pass"
  miss=$(comm -23 "$OUT/work-$3.rows" "$OUT/work-$3.pass" | tr '\n' ' ')
  extra=$(comm -13 "$OUT/work-$3.rows" "$OUT/work-$3.pass" | tr '\n' ' ')
  n=$(wc -l < "$OUT/work-$3.rows" | tr -d ' ')
  if [ -n "$miss$extra" ]; then fail=1; say "$3" "FAIL rows=$n";
    [ -n "$miss" ] && echo "  PINSET-NEVER-PASS:$miss";
    [ -n "$extra" ] && echo "  PINSET-UNPINNED:$extra";
  else say "$3" "PASS set-eq $n/$n"; fi
}
pinsetleg vectors/outer2-PINS.csv "$OUT/work-OUTER2.log" PINS-OUTER2
pinsetleg vectors/rb2-PINS.csv "$OUT/work-RB2.log" PINS-RB2
pinsetleg vectors/ravframe-PINS.csv "$OUT/work-RAVFRAME.log" PINS-RAVFRAME

# 5. OSS: third-party lib loads in src+harness (PARENT-003 gate 3).
# system libc (/usr/lib, /System) + bare ctypes stdlib use are NOT deps.
# a loading file is clean iff it names an already-nominated lib (lzfse, NOTE-013;
# liblzma iff A-20 pin markers present: 5.8.4 + (1b2e12cc sha | A-20 cite)).
OHIT=$(grep -rniE -I 'dylib|CDLL|dlopen|ctypes|\.so\b|git submodule|add_subdirectory' "$OUT/tree/src" "$OUT/tree/harness" 2>/dev/null | grep -v '/usr/lib/' | grep -v '/System/' || true)
ONEW=""
for _f in $(echo "$OHIT" | cut -d: -f1 | sort -u); do
  [ -z "$_f" ] && continue
  nominated "$_f" || ONEW="$ONEW $_f"
done
if [ -n "$ONEW" ]; then fail=1; say OSS "FAIL new-oss:$ONEW"; echo "$OHIT" | sed 's/^/  /';
elif [ -n "$OHIT" ]; then say OSS "PASS nominated-only"; else say OSS "PASS none"; fi

# 5b. LIBCOMPRESSION (A-12 REFUSE, PARENT-007-confirmed: beds-OK green,
# src-use denied in src/harness unless a grant lands in quiz).
LHIT=$(grep -rniE -I 'libcompression|COMPRESSION_LZMA|COMPRESSION_LZ4|compression_encode_buffer|compression_decode_buffer' "$OUT/tree/src" "$OUT/tree/harness" 2>/dev/null || true)
if [ -n "$LHIT" ]; then fail=1; say LIBCOMPRESSION "FAIL ungranted-src-use:"; echo "$LHIT" | sed 's/^/  /';
else say LIBCOMPRESSION "PASS zero-refs"; fi

# 6. ADOPT: A-1 pins vs lanes/harness-oracle (impl lanes only — PV-001:
# framework lanes adopting nothing SKIP instead of WARN).
if git -C "$REPO" rev-parse -q --verify lanes/harness-oracle >/dev/null; then
  ok=1; adopted=0
  for p in harness/oracle-adapter.sh tests/smoke.sh; do
    git -C "$REPO" cat-file -e "$REV:$p" 2>/dev/null || continue
    adopted=1
    a=$(git -C "$REPO" show "lanes/harness-oracle:$p" 2>/dev/null | shasum -a 256 | cut -c1-8)
    b=$(git -C "$REPO" show "$REV:$p" 2>/dev/null | shasum -a 256 | cut -c1-8)
    [ -n "$a" ] && [ "$a" = "$b" ] || { ok=0; echo "  ADOPT-DIFF $p lane=$a tip=$b"; }
  done
  if [ "$adopted" -eq 0 ]; then say ADOPT "SKIP nothing-adopted"
  elif [ "$ok" -eq 1 ]; then say ADOPT "PASS match"
  else say ADOPT "WARN diff"; fi
else say ADOPT "SKIP no-harness-lane"; fi

[ "$fail" -eq 0 ] && echo "GATE-PASS $REV" || echo "GATE-FAIL $REV"
exit $fail
