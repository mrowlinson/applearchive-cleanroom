# GATE f1b8d9f b220 T10P152 n<=69724 (912 tiers) PASS-functional

- Seat encode-sweep2 r28, first-hand,
  seat-private logs f1b8d9f.* +
  f1b8d9f/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  d903ab7: rgramc.c only +1624/-1163;
  wall 0. Range 69633..69724 (lo =
  b219 ceiling 69632 + 1, verified vs
  cf229ce msg; 92 n; matches writer
  50c892a).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=9052 FAIL 0,
  PINS-RGRAM set-eq 9052/9052; RAWENC
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
- RGRAMC-PYID 4526/4526 GREEN 0 FAIL
  covered=4526/4526 (corpus 9052
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 9052/9052 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2117320 B); C-py
  PASS-set cmp-equal 9052/9052.
- own-loop 69633..69724 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P152 msg).
- Added 3/3 EQ (_T10P152AC 75 rows,
  _T10P152BC 71 rows, _T10P152QC
  63 rows, all = py tuples); full
  audit 1D 167/0 + 2D 900/0 +
  dicts 11/0 + STR 302/0 + STRARR
  1140/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b218).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b218 gate log: ZERO lines differ
  (sha + RGRAM counts 8996->9052
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  f1b8d9f); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
