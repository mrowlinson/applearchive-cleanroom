# GATE bd1ca6d b192 T10P138 n<=64852 (856 tiers) PASS-functional

- Seat encode-sweep2 r19, first-hand,
  seat-private logs bd1ca6d.* +
  r19-bd1ca6d.* under NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  eec085d: rgramc.c only +1520/-1069;
  wall 0. Range 64761..64852.
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8280 FAIL 0,
  PINS-RGRAM set-eq 8280/8280; RAWENC
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
  needed, no FLAG. (Precedent legs
  GATE-965f4dd/GATE-7081fd5/GATE-
  05efb6d covered flake-only case.)
- RGRAMC-PYID 4140/4140 GREEN 0 FAIL
  covered=4140/4140 (corpus 8280
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8280/8280 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 1947048 B); C-py
  PASS-set cmp-equal 8280/8280.
- own-loop 64761..64852 fresh-oracle
  92/92 py-agree, pins 26/26, rc=0.
- Added 4/4 EQ (_T10P138X26 1D n=16,
  _T10P138AC 77 rows, _T10P138BC
  71 rows, _T10P138QC 63 rows, all =
  py tuples); full audit 1D 167/0 +
  2D 844/0 + dicts 11/0 + STR
  263/0 + STRARR 1041/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  r17 b190 gate log: HYGIENE 14/14
  IDENTICAL (.aar 13), CONTAM 44/44
  IDENTICAL, LIBCOMP 5/5 IDENTICAL
  (aad.c 3 lines), lane file 0/0/0,
  aad.c + impl-adapter.sh 0 diff
  b190->b192. Only diffs: RGRAM/
  PINS-RGRAM counts 8230->8280 +
  OUTER2/PINS-OUTER2 flake->clean.
  ADOPT WARN diff carried (c8f52713/
  c5f921d5 const).
- Verdict: PASS-functional. No RED.
