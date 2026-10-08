#!/bin/sh
# test_rgram.sh -- lzraven zeros-N grammar battery (NOTE-w2s6-2/3/7).
# rgram.py asserts tier length-code + echo + markers + form-flip live;
# sha pins freeze oracle bytes. Oracle = TEST-TIME EXEC ONLY:
# compression_tool -encode -a lzraven. Exit 0 GREEN/1 RED/2 err.
# Usage: sh tests/test_rgram.sh [workdir]
# RECORD=1 sh tests/test_rgram.sh [workdir]  (rewrite PINS; REVIEW diff!)
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
WORK=${1:-$(mktemp -d "${TMPDIR:-/tmp}/rgram.XXXXXX")}
PINS=$ROOT/vectors/rgram-PINS.csv
FAIL=0
GEN=test_rgram.sh
OS=$(sw_vers -productVersion 2>/dev/null || echo unknown)
CT=${CT:-/usr/bin/compression_tool}
RG=$ROOT/src/rgram.py
command -v python3 >/dev/null || { echo "need python3" >&2; exit 2; }
mkdir -p "$WORK" "$ROOT/vectors"
pin_get() { grep "^$1," "$PINS" | head -1 | cut -d, -f3; }
chk() { # name check val [bytes]
  if [ -n "${RECORD:-}" ]; then
    echo "$1,$2,$3,${4:-0},$GEN,$OS,ct-lzraven" >> "$PINS.new"
    echo "REC $1=$3"
  else
    [ -f "$PINS" ] || { echo "missing $PINS (RECORD=1 first)" >&2; exit 2; }
    exp=$(pin_get "$1")
    if [ "$3" = "$exp" ]; then echo "PASS $1"; else echo "FAIL $1: got $3 want $exp"; FAIL=1; fi
  fi
}
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
sz() { wc -c < "$1" | tr -d ' '; }
echo "== probe =="
[ -x "$CT" ] || { echo "need $CT" >&2; exit 2; }
"$CT" -encode -a lzraven -i /dev/null -o "$WORK/probe.bin" 2>/dev/null || { echo "ct raven failed" >&2; exit 2; }
if [ -n "${RECORD:-}" ]; then
  echo "# rgram pins: name,check,expect,bytes,generator,os,backend" > "$PINS.new"
  echo "# closed = rgram grammar verdict; sha = output hash (deterministic zeros-N)" >> "$PINS.new"
fi
GCELL() { # nbytes : closed + sha pins
  n=$1
  head -c "$n" /dev/zero > "$WORK/g$n.bin" 2>/dev/null || : > "$WORK/g$n.bin"
  "$CT" -encode -a lzraven -i "$WORK/g$n.bin" -o "$WORK/g$n.rav" 2>/dev/null || { echo "FAIL g$n ct rc"; FAIL=1; return; }
  if v=$(python3 "$RG" "$WORK/g$n.rav" "$n" 2>"$WORK/g$n.rgram"); then
    case "$v" in
      *CLOSED*) c=CLOSED;; *) c=BAD;;
    esac
    chk "g-z$n-closed" str "$c" "$(sz "$WORK/g$n.rav")"
    chk "g-z$n" sha "$(sha "$WORK/g$n.rav")" "$(sz "$WORK/g$n.rav")"
  else echo "FAIL g$n rgram: $(head -1 "$WORK/g$n.rgram")"; FAIL=1; fi
}
echo "== rgram zeros-N (stored + T0 + edge + T1 + T2 + T3) =="
for s in 0 1 63 64 65 124 125 126 127 128 129 189 253 255 256 257 380 381 382 384 396 399 400 408 409 425 441 457 473 474 511 512 521 537 601 640 665 728 729 730 731 746 747 748 756 757 758 772 773 789 805 820 821 822 896 949 1023 1024 1025 1076 1077; do
  GCELL "$s"
done
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo RGRAM-GREEN || echo RGRAM-RED
exit "$FAIL"
