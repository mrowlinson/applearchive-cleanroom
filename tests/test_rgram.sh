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
for s in 0 1 63 64 65 124 125 126 127 128 129 189 253 255 256 257 380 381 382 384 396 399 400 408 409 425 441 457 473 474 511 512 521 537 601 640 665 728 729 730 731 746 747 748 756 757 758 772 773 789 805 820 821 822 896 949 1023 1024 1025 1076 1077 1078 1079 1086 1094 1095 1099 1104 1105 1112 1120 1121 1128 1136 1137 1144 1152 1153 1160 1168 1169 1184 1185 1232 1296 1360 1408 1423 1424 1425 1426 1427 1434 1442 1443 1447 1452 1453 1468 1484 1500 1516 1517 1526 1527 1533 1600 1663 1664 1728 1772 1773 1774 1775 1782 1790 1791 1795 1800 1801 1816 1817 1832 1833 1848 1849 1864 1865 1880 1920 1960 1961 2000 2047 2048 2064 2080 2096 2112 2120 2121 2122 2123 2130 2138 2139 2143 2148 2149 2165 2181 2197 2212 2213 2228 2244 2304 2432 2440 2453 2468 2469 2470 2471 2478 2479 2486 2487 2496 2497 2513 2529 2545 2560 2561 2613 2688 2700 2701 2756 2816 2817 2818 2819 2834 2835 2844 2845 2877 2908 2909 2944 2973 3072 3101 3164 3165 3166 3167 3182 3183 3192 3193 3209 3225 3241 3256 3257 3321 3328 3353 3433 3456 3512 3513 3515 3516 3524 3525 3530 3531 3540 3541 3557 3573 3584 3589 3604 3605 3712 3840 3860 3861 3862 3863 3878 3879 3888 3889 3905 3921 3937 3952 3953 3968 4095 4096 4144 4208 4209 4210 4211 4212 4226 4227 4236 4237 4253 4269 4285 4300 4301 4352 4480 4556 4557 4559 4560 4574 4575 4584 4585 4601 4608 4617 4633 4648 4649 4736 4864 4904 4905 4907 4908 4922 4923 4932 4933 4949 4965 4981 4992 4996 4997 5120 5221 5248 5252 5253 5255 5256 5270 5271 5280 5281 5297 5313 5329 5344 5345 5376 5504 5600 5601 5603 5604 5618 5619 5628 5629 5632 5645 5661 5677 5692 5693 5709 5760 5888 5948 5949 5951 5952 5966 5967 5976 5977 5993 6009 6025 6040 6041 6137 6144 6296 6297 6298 6299 6314 6315 6324 6325 6341 6357 6373 6388 6389 6400 6460 6528 6596 6597 6644 6645 6646 6647 6648 6662 6663 6664 6672 6673 6689 6705 6721 6736 6737 6784 6849 6912 6960 6961 6992 6993 6995 6996 7010 7011 7012 7020 7021 7037 7053 7069 7084 7085 7168 7296 7340 7341 7342 7343 7358 7359 7368 7369 7385 7401 7417 7424 7432 7433 7552 7680 7688; do
  GCELL "$s"
done
[ -n "${RECORD:-}" ] && mv "$PINS.new" "$PINS" && echo "RECORDED $PINS"
echo "== $WORK =="
[ "$FAIL" -eq 0 ] && echo RGRAM-GREEN || echo RGRAM-RED
exit "$FAIL"
