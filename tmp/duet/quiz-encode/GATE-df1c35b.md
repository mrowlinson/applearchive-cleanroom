# GATE df1c35b b214 T10P149 n<=68680 (900 tiers) PASS-functional

- Seat encode-sweep2 r26, first-hand,
  seat-private logs df1c35b.* +
  df1c35b/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  0fd3076: rgramc.c only +1592/-1144;
  wall 0. Range 68589..68680 (lo =
  b213 ceiling 68588 + 1, verified vs
  8d5bc17 msg; 92 n).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8884 FAIL 0,
  PINS-RGRAM set-eq 8884/8884; RAWENC
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
- RGRAMC-PYID 4442/4442 GREEN 0 FAIL
  covered=4442/4442 (corpus 8884
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8884/8884 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2083240 B); C-py
  PASS-set cmp-equal 8884/8884.
- own-loop 68589..68680 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P149 msg).
- Added 3/3 EQ (_T10P149AC 75 rows,
  _T10P149BC 69 rows, _T10P149QC
  63 rows, all = py tuples); full
  audit 1D 167/0 + 2D 888/0 +
  dicts 11/0 + STR 294/0 + STRARR
  1119/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b212).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b212 gate log: ZERO lines differ
  (sha + RGRAM counts 8828->8884
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  df1c35b); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
