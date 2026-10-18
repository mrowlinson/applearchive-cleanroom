# GATE 4c9ff15 b196 T10P140 n<=65548 (864 tiers) PASS-functional

- Seat encode-sweep2 r19, first-hand,
  seat-private logs 4c9ff15.* +
  r19-4c9ff15.* under NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  55a1a81: rgramc.c only +1559/-1081;
  wall 0. Range 65457..65548.
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8384 FAIL 0,
  PINS-RGRAM set-eq 8384/8384; RAWENC
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
- RGRAMC-PYID 4192/4192 GREEN 0 FAIL
  covered=4192/4192 (corpus 8384
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8384/8384 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 1997368 B); C-py
  PASS-set cmp-equal 8384/8384.
- own-loop 65457..65548 fresh-oracle
  92/92 py-agree, pins 30/30, rc=0.
- Added 3/3 EQ (_T10P140AC 76 rows,
  _T10P140BC 71 rows, _T10P140QC
  62 rows, all = py tuples); full
  audit 1D 167/0 + 2D 852/0 +
  dicts 11/0 + STR 268/0 + STRARR
  1056/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  r19 b194 gate log: ALL legs
  IDENTICAL except RGRAM/PINS-RGRAM
  counts 8330->8384. HYGIENE 14/14
  (.aar 13), CONTAM 44/44, LIBCOMP
  5/5 (aad.c 3 lines), lane file
  0/0/0, aad.c + impl-adapter.sh 0
  diff b194->b196. ADOPT WARN diff
  carried (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED.
