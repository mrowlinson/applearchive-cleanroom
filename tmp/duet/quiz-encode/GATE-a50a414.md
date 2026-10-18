# GATE a50a414 b212 T10P148 n<=68332 (896 tiers) PASS-functional

- Seat encode-sweep2 r26, first-hand,
  seat-private logs a50a414.* +
  a50a414/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  1a0d95c: rgramc.c only +1598/-1137;
  wall 0. Range 68241..68332 (lo =
  b211 ceiling 68240 + 1, verified vs
  8516151 msg; 92 n).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8828 FAIL 0,
  PINS-RGRAM set-eq 8828/8828; RAWENC
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
- RGRAMC-PYID 4414/4414 GREEN 0 FAIL
  covered=4414/4414 (corpus 8828
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8828/8828 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2066392 B); C-py
  PASS-set cmp-equal 8828/8828.
- own-loop 68241..68332 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P148 msg).
- Added 3/3 EQ (_T10P148AC 75 rows,
  _T10P148BC 71 rows, _T10P148QC
  64 rows, all = py tuples); full
  audit 1D 167/0 + 2D 884/0 +
  dicts 11/0 + STR 292/0 + STRARR
  1112/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b210).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b210 gate log: ZERO lines differ
  (sha + RGRAM counts 8772->8828
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  a50a414); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
