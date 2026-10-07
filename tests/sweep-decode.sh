#!/bin/bash
# sweep-decode.sh — independent full-gate battery for the DECODE side.
# Usage: CORPUS=<vectors/selfgen> [WRITER_BIN=<decode-binary>] tests/sweep-decode.sh [tier...]
# Tiers: pins oracle-health decode-compare full holdout fresh units (default: all)
# Verdicts: SWEEP-GREEN (exit 0) / SWEEP-RED (exit 1) / SWEEP-BASELINE (exit 3, no writer code yet)
# Scratch: <worktree>/tmp/sweep-scratch (repo tmp only; bulky stays out).
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORPUS="${CORPUS:-$ROOT/vectors/selfgen}"
SCRATCH="${SCRATCH:-$ROOT/tmp/sweep-scratch}"
ORACLE_AA="${ORACLE_AA:-/usr/bin/aa}"
ORACLE_AEA="${ORACLE_AEA:-/usr/bin/aea}"
WRITER_BIN="${WRITER_BIN:-}"
RESULT="${RESULT:-}"
FAIL=0; SKIPPED=""; RAN_COMPARE=0; ROWS=""
rec() { ROWS="$ROWS$1	$2	$3	$4	$5
"; } # tier, cell, status, bytes, sha

tier_pins() { # DRIFT-FAIL binding: any mismatch aborts the run
  [ -f "$CORPUS/SHA256SUMS" ] || { echo "TIER pins: FAIL (no SHA256SUMS in $CORPUS)"; return 1; }
  if (cd "$CORPUS" && shasum -c SHA256SUMS >/dev/null 2>&1); then
    n=$(grep -c . "$CORPUS/SHA256SUMS")
    echo "TIER pins: PASS ($n/$n)"; return 0
  else
    echo "TIER pins: FAIL (drift — HARD FAIL, run aborted)"; return 1
  fi
}
tier_oracle_health() { # oracle sanity: extract all AARs + decrypt both AEAs
  rm -rf "$SCRATCH/health" && mkdir -p "$SCRATCH/health"
  pass=0; total=0
  for a in "$CORPUS"/aar/*.aar; do
    total=$((total+1)); base=$(basename "$a" .aar); d="$SCRATCH/health/$base"
    mkdir -p "$d"; p0=$pass
    if "$ORACLE_AA" extract -t 1 -i "$a" -d "$d" >/dev/null 2>&1; then
      case "$base" in
        empty-*) [ -z "$(ls -A "$d")" ] && pass=$((pass+1)) || echo "  MISMATCH(empty-nonempty): $base" ;;
        *) diff -r "$d/hello" "$CORPUS/input/hello" >/dev/null 2>&1 && pass=$((pass+1)) || echo "  MISMATCH(content): $base" ;;
      esac
    else echo "  MISMATCH(extract-exit): $base"; fi
    [ "$pass" -gt "$p0" ] && st=PASS || st=FAIL
    rec oracle-health "$base" "$st" "$(wc -c < "$a" | tr -d ' ')" "$(shasum -a 256 "$a" | cut -d' ' -f1)"
  done
  for spec in "hello-p1-nopad.aea:-key:$CORPUS/aea/testkey.bin" "hello-p5.aea:-password-value:test-password-fixture"; do
    total=$((total+1)); f="${spec%%:*}"; rest="${spec#*:}"; flag="${rest%%:*}"; val="${rest#*:}"
    out="$SCRATCH/health/$f.plain"; p0=$pass
    if "$ORACLE_AEA" decrypt -i "$CORPUS/aea/$f" -o "$out" "$flag" "$val" >/dev/null 2>&1 \
       && cmp -s "$out" "$CORPUS/aar/hello-raw.aar"; then pass=$((pass+1)); else echo "  MISMATCH(aea): $f"; fi
    [ "$pass" -gt "$p0" ] && st=PASS || st=FAIL
    rec oracle-health "$f" "$st" "$(wc -c < "$CORPUS/aea/$f" | tr -d ' ')" "$(shasum -a 256 "$CORPUS/aea/$f" | cut -d' ' -f1)"
  done
  [ "$pass" -eq "$total" ] && { echo "TIER oracle-health: PASS ($pass/$total)"; return 0; }
  echo "TIER oracle-health: FAIL ($pass/$total)"; return 1
}
tier_compare() { # writer binary vs oracle, per AAR; $1=name $2...=aar files
  name="$1"; shift
  [ -n "$WRITER_BIN" ] || { echo "TIER $name: SKIP (no WRITER_BIN)"; SKIPPED="$SKIPPED $name"; return 0; }
  [ $# -eq 0 ] && { echo "TIER $name: SKIP (empty corpus slice)"; SKIPPED="$SKIPPED $name"; return 0; }
  [ -x "$WRITER_BIN" ] || { echo "TIER $name: FAIL (WRITER_BIN not executable: $WRITER_BIN)"; return 1; }
  rm -rf "$SCRATCH/$name" && mkdir -p "$SCRATCH/$name"
  pass=0; total=0
  for a in "$@"; do
    total=$((total+1)); base=$(basename "$a" .aar)
    od="$SCRATCH/$name/$base.oracle"; wd="$SCRATCH/$name/$base.writer"
    mkdir -p "$od" "$wd"; p0=$pass
    "$ORACLE_AA" extract -t 1 -i "$a" -d "$od" >/dev/null 2>&1 || { echo "  MISMATCH(oracle-exit): $base"; rec "$name" "$base" FAIL "$(wc -c < "$a" | tr -d ' ')" "$(shasum -a 256 "$a" | cut -d' ' -f1)"; continue; }
    # Writer CLI convention: oracle-compatible `extract -i X -d DIR` (revisit on writer/viewer prescription).
    if "$WRITER_BIN" extract -i "$a" -d "$wd" >/dev/null 2>&1 && diff -r "$od" "$wd" >/dev/null 2>&1; then
      pass=$((pass+1))
    else echo "  MISMATCH(writer): $base"; fi
    [ "$pass" -gt "$p0" ] && st=PASS || st=FAIL
    rec "$name" "$base" "$st" "$(wc -c < "$a" | tr -d ' ')" "$(shasum -a 256 "$a" | cut -d' ' -f1)"
  done
  RAN_COMPARE=$((RAN_COMPARE+total))
  [ "$pass" -eq "$total" ] && { echo "TIER $name: PASS ($pass/$total)"; return 0; }
  echo "TIER $name: FAIL ($pass/$total)"; return 1
}
tier_units() {
  [ -n "${WRITER_UNITS:-}" ] || { echo "TIER units: SKIP (no WRITER_UNITS)"; SKIPPED="$SKIPPED units"; return 0; }
  if $WRITER_UNITS >/dev/null 2>&1; then echo "TIER units: PASS"; return 0; else echo "TIER units: FAIL"; return 1; fi
}
mkdir -p "$SCRATCH"
tier_smoke_xcheck() { # adopted T0 as cross-check signal (A-004 Q3 per-tip gate, oracle leg)
  rm -rf "$SCRATCH/smoke-wd" && mkdir -p "$SCRATCH/smoke-wd"
  if sh "$ROOT/tests/smoke.sh" "$SCRATCH/smoke-wd" 2>&1 | grep -q SMOKE-GREEN; then
    echo "TIER smoke-xcheck: PASS (SMOKE-GREEN)"; return 0
  else echo "TIER smoke-xcheck: FAIL"; return 1; fi
}
TIERS="${*:-pins oracle-health smoke-xcheck decode-compare full holdout fresh units}"
for t in $TIERS; do
  case "$t" in
    pins) tier_pins || { FAIL=1; break; } ;;
    oracle-health) tier_oracle_health || FAIL=1 ;;
    smoke-xcheck) tier_smoke_xcheck || FAIL=1 ;;
    decode-compare|full) tier_compare "$t" "$CORPUS"/aar/*.aar || FAIL=1 ;;
    holdout|fresh) echo "TIER $t: SKIP (no disjoint seeds yet)"; SKIPPED="$SKIPPED $t" ;;
    units) tier_units || FAIL=1 ;;
    *) echo "TIER $t: unknown tier"; FAIL=1 ;;
  esac
done
if [ -n "$RESULT" ]; then # BATTERY.md result file: provenance header + 1 row per cell (rows: tier, cell, status, bytes, sha; ms omitted until timing protocol)
  { echo "# date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "# corpus=$CORPUS sha256sums=$(shasum -a 256 "$CORPUS/SHA256SUMS" 2>/dev/null | cut -d' ' -f1)"
    echo "# writer_bin=${WRITER_BIN:-none}"
    sh "$ROOT/harness/oracle-adapter.sh" probe 2>/dev/null | sed 's/^/# probe: /'
    printf '%s' "$ROWS"; } > "$RESULT"
  echo "RESULT $RESULT ($(printf '%s' "$ROWS" | grep -c .) rows)"
fi
if [ "$FAIL" -ne 0 ]; then echo "SWEEP-RED (decode)"; exit 1; fi
if [ "$RAN_COMPARE" -eq 0 ]; then echo "SWEEP-BASELINE (decode): framework green, no writer cases ran. skipped:$SKIPPED"; exit 3; fi
echo "SWEEP-GREEN (decode): $RAN_COMPARE cases. skipped:$SKIPPED"; exit 0
