# GATE 10a0a0f b202 T10P143 n<=66592 (876 tiers) PASS-functional

- Seat encode-sweep2 r22, first-hand,
  seat-private logs 10a0a0f.* +
  r22-* under NVME encode-sweep2.
- Lane-diff vs writer-merge parent
  732dac2: rgramc.c only +1563/-1102;
  wall 0. Range 66501..66592 (lo =
  b201 ceiling 66500 + 1, verified at
  claim time; 92 n).
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8548 FAIL 0,
  PINS-RGRAM set-eq 8548/8548; RAWENC
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
- RGRAMC-PYID 4274/4274 GREEN 0 FAIL
  covered=4274/4274 (corpus 8548
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8548/8548 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 2015000 B); C-py
  PASS-set cmp-equal 8548/8548.
- own-loop 66501..66592 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0
  (== writer +32, T10P143 msg).
- Added 3/3 EQ (_T10P143AC 75 rows,
  _T10P143BC 71 rows, _T10P143QC
  64 rows, all = py tuples); full
  audit 1D 167/0 + 2D 864/0 +
  dicts 11/0 + STR 277/0 + STRARR
  1077/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  b200 gate log: ALL legs IDENTICAL
  except RGRAM/PINS-RGRAM counts
  8492->8548. HYGIENE/CONTAM/LIBCOMP/
  AEA-BIN/ADOPT detail IDENTICAL
  (13/43/4 aar/contam/aad lines).
  ADOPT WARN diff carried.
- Quiz: no conflicting CLAIM/GATE on
  even turf (CLAIM-viewer2-10a0a0f is
  VERIFY-side, defers to this GATE).
- Verdict: PASS-functional. No RED.
