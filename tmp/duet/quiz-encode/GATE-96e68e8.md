# GATE 96e68e8 b222 T10P153 n<=70072 (916 tiers) PASS-functional

- Seat encode-sweep2 r28, first-hand,
  seat-private logs 96e68e8.* +
  96e68e8/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  1f76333: rgramc.c only +1631/-1170;
  wall 0. Range 69981..70072 (lo =
  b221 ceiling 69980 + 1, verified vs
  171e45a msg; 92 n; matches writer
  8567b02).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=9108 FAIL 0,
  PINS-RGRAM set-eq 9108/9108; RAWENC
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
- RGRAMC-PYID 4554/4554 GREEN 0 FAIL
  covered=4554/4554 (corpus 9108
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 9108/9108 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2117704 B); C-py
  PASS-set cmp-equal 9108/9108.
- own-loop 69981..70072 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P153 msg).
- Added 3/3 EQ (_T10P153AC 74 rows,
  _T10P153BC 69 rows, _T10P153QC
  64 rows, all = py tuples); full
  audit 1D 167/0 + 2D 904/0 +
  dicts 11/0 + STR 305/0 + STRARR
  1147/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b220).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b220 gate log: ZERO lines differ
  (sha + RGRAM counts 9052->9108
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  96e68e8 + GATE-f1b8d9f); no Q for
  sweep2, diff 0.
- Verdict: PASS-functional. No RED.
