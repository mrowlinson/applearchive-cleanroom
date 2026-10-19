# GATE f7d524d b224 T10P154 n<=70420 (920 tiers) PASS-functional

- Seat encode-sweep2 r29, first-hand,
  seat-private logs f7d524d.* +
  f7d524d/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  06bd3f5: rgramc.c only +1642/-1177;
  wall 0. Range 70329..70420 (lo =
  b223 ceiling 70328 + 1, verified vs
  3420198 msg; 92 n; matches writer
  aba4a48).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=9164 FAIL 0,
  PINS-RGRAM set-eq 9164/9164; RAWENC
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
- RGRAMC-PYID 4582/4582 GREEN 0 FAIL
  covered=4582/4582 (corpus 9164
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 9164/9164 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2134600 B); C-py
  PASS-set cmp-equal 9164/9164.
- own-loop 70329..70420 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P154 msg).
- Added 3/3 EQ (_T10P154AC 76 rows,
  _T10P154BC 71 rows, _T10P154QC
  65 rows, all = py tuples); full
  audit 1D 167/0 + 2D 908/0 +
  dicts 11/0 + STR 307/0 + STRARR
  1155/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b222).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b222 gate log: ZERO lines differ
  (sha + RGRAM counts 9108->9164
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  f7d524d); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
