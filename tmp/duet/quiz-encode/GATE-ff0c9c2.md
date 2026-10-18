# GATE ff0c9c2 b200 T10P142 n<=66244 (872 tiers) PASS-functional

- Seat encode-sweep2 r20, first-hand,
  seat-private logs ff0c9c2.* +
  r20-ff0c9c2.* under NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  14531bb: rgramc.c only +1556/-1095;
  wall 0. Range 66153..66244.
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8492 FAIL 0,
  PINS-RGRAM set-eq 8492/8492; RAWENC
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
- RGRAMC-PYID 4246/4246 GREEN 0 FAIL
  covered=4246/4246 (corpus 8492
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8492/8492 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2014632 B); C-py
  PASS-set cmp-equal 8492/8492.
- own-loop 66153..66244 fresh-oracle
  92/92 py-agree, pins 28/28, rc=0.
- Added 3/3 EQ (_T10P142AC 75 rows,
  _T10P142BC 71 rows, _T10P142QC
  64 rows, all = py tuples); full
  audit 1D 167/0 + 2D 860/0 +
  dicts 11/0 + STR 274/0 + STRARR
  1070/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  r20 b198 gate log: ALL legs
  IDENTICAL except RGRAM/PINS-RGRAM
  counts 8440->8492. HYGIENE 14/14
  (.aar 13), CONTAM 44/44, LIBCOMP
  5/5 (aad.c 3 lines), lane file
  0/0/0, aad.c + impl-adapter.sh 0
  diff b198->b200. ADOPT WARN diff
  carried.
- Verdict: PASS-functional. No RED.
