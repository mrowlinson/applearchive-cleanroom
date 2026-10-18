# GATE 711efa9 b210 T10P147 n<=67984 (892 tiers) PASS-functional

- Seat encode-sweep2 r25, first-hand,
  seat-private logs 711efa9.* +
  711efa9/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  79ea6f7: rgramc.c only +1591/-1130;
  wall 0. Range 67893..67984 (lo =
  b209 ceiling 67892 + 1, verified vs
  f8e426b msg; 92 n).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8772 FAIL 0,
  PINS-RGRAM set-eq 8772/8772; RAWENC
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
- RGRAMC-PYID 4386/4386 GREEN 0 FAIL
  covered=4386/4386 (corpus 8772
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8772/8772 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2066008 B); C-py
  PASS-set cmp-equal 8772/8772.
- own-loop 67893..67984 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P147 msg).
- Added 3/3 EQ (_T10P147AC 74 rows,
  _T10P147BC 69 rows, _T10P147QC
  63 rows, all = py tuples); full
  audit 1D 167/0 + 2D 880/0 +
  dicts 11/0 + STR 289/0 + STRARR
  1105/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b208).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b208 gate log: ZERO lines differ
  (sha + RGRAM counts 8716->8772
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  711efa9); no Q for sweep2, diff 0.
- Verdict: PASS-functional. No RED.
