# GATE aaed31b b226 T10P155 n<=70768 (924 tiers) PASS-functional

- Seat encode-sweep2 r29, first-hand,
  seat-private logs aaed31b.* +
  aaed31b/ workdir on NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  33b47ac: rgramc.c only +1643/-1183;
  wall 0. Range 70677..70768 (lo =
  b225 ceiling 70676 + 1, verified vs
  99edcde msg; 92 n; matches writer
  fe948b1).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=9220 FAIL 0,
  PINS-RGRAM set-eq 9220/9220; RAWENC
  13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4
  (+ -C legs all PASS), SMOKE 6/6,
  SMOKE-IMPL 6/6, RB2 47/47, RAVFRAME
  181/181, UNITS 22, LZ4C 5,
  PINS-RAWENC 11/11 (+C), PINS-PBZE
  10/10 (+C), PINSET RB2/RAVFRAME
  set-eq 47/47 + 181/181, OSS
  nominated-only, C-BUILD warnings=0.
- OUTER2 shipped-run FLAKE (a-nondet
  283/284, "got char 14 want char
  13"): KNOWN oracle-only nondet per
  GATE-965f4dd/GATE-7081fd5 (pin
  compares first-diff-char of TWO
  fresh AEA oracle encryptions;
  rgramc.c-only lane cannot affect
  AEA bytes). PROOF: isolated
  test_outer2.sh rerun on IDENTICAL
  tree -> rc=0, 284/284 GREEN incl
  PASS a-nd-p2 (aaed31b.outer2-
  rerun.log); PINS-OUTER2 first-hand
  set-eq 284/284, miss+extra empty.
  Flake documented, no FLAG (not
  tip-caused).
- RGRAMC-PYID 4610/4610 GREEN 0 FAIL
  covered=4610/4610 (corpus 9220
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 9220/9220 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2135000 B); C-py
  PASS-set cmp-equal 9220/9220.
- own-loop 70677..70768 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P155 msg).
- Added 3/3 EQ (_T10P155AC 74 rows,
  _T10P155BC 69 rows, _T10P155QC
  63 rows, all = py tuples); full
  audit 1D 167/0 + 2D 912/0 +
  dicts 11/0 + STR 310/0 + STRARR
  1162/0 via r25/fullaudit.py
  (comment-strip + literal-fusion +
  depth-end canon). SKIP 4 py-only,
  C never refs (same as b224).
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b224 gate log: 7 lines, ALL
  flake-scoped (OUTER2 FAIL +
  OUTER2-RED + PINS-OUTER2 FAIL +
  PINSET-NEVER-PASS:a-nd-p2; sha +
  RGRAM counts 9164->9220
  normalized). HYGIENE/CONTAM/LIBCOMP
  FAILs + AEA-BIN/ADOPT WARNs
  detail-IDENTICAL inherited.
- Quiz: no conflicting CLAIM/GATE on
  even turf (only own CLAIM-sweep2-
  aaed31b + GATE-f7d524d); no Q for
  sweep2, diff 0.
- Verdict: PASS-functional. No RED.
