# GATE ea56caf b206 T10P145 n<=67288 (884 tiers) PASS-functional

- Seat encode-sweep2 r23, first-hand,
  seat-private logs ea56caf.* +
  ea56caf/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  5be63bf: rgramc.c only +1589/-1115;
  wall 0. Range 67197..67288 (lo =
  b205 ceiling 67196 + 1, verified at
  claim time; 92 n).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8660 FAIL 0,
  PINS-RGRAM set-eq 8660/8660; RAWENC
  13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4
  (+ -C legs all PASS), SMOKE 6/6,
  SMOKE-IMPL 6/6, RB2 47/47, RAVFRAME
  181/181, UNITS 22, LZ4C 5,
  PINS-RAWENC 11/11 (+C), PINS-PBZE
  10/10 (+C), PINSET RB2/RAVFRAME
  set-eq 47/47 + 181/181, OSS
  nominated-only, C-BUILD warnings=0.
- OUTER2 PASS n=284 first try +
  PINS-OUTER2 set-eq 284/284: NO
  a-nondet flake this run, no rerun
  needed, no FLAG.
- RGRAMC-PYID 4330/4330 GREEN 0 FAIL
  covered=4330/4330 (corpus 8660
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8660/8660 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2032232 B); C-py
  PASS-set cmp-equal 8660/8660.
- own-loop 67197..67288 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P145 msg).
- Added 3/3 EQ (_T10P145AC 75 rows,
  _T10P145BC 71 rows, _T10P145QC
  65 rows, all = py tuples); full
  audit 1D 167/0 + 2D 872/0 +
  dicts 11/0 + STR 283/0 + STRARR
  1091/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b204 gate log: ZERO lines differ
  (sha + RGRAM counts 8604->8660
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  ea56caf); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
