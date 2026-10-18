# GATE 1a423eb b218 T10P151 n<=69376 (908 tiers) PASS-functional

- Seat encode-sweep2 r27, first-hand,
  seat-private logs 1a423eb.* +
  1a423eb/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  ec7dbf7: rgramc.c only +1605/-1157;
  wall 0. Range 69285..69376 (lo =
  b217 ceiling 69284 + 1, verified vs
  9b86a7a msg; 92 n; matches writer
  f4e7188).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8996 FAIL 0,
  PINS-RGRAM set-eq 8996/8996; RAWENC
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
- RGRAMC-PYID 4498/4498 GREEN 0 FAIL
  covered=4498/4498 (corpus 8996
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8996/8996 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2100440 B); C-py
  PASS-set cmp-equal 8996/8996.
- own-loop 69285..69376 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P151 msg).
- Added 3/3 EQ (_T10P151AC 75 rows,
  _T10P151BC 71 rows, _T10P151QC
  65 rows, all = py tuples); full
  audit 1D 167/0 + 2D 896/0 +
  dicts 11/0 + STR 299/0 + STRARR
  1133/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b216).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b216 gate log: ZERO lines differ
  (sha + RGRAM counts 8940->8996
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  1a423eb); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
