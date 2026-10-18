# GATE 6bf6af5 b198 T10P141 n<=65896 (868 tiers) PASS-functional

- Seat encode-sweep2 r20, first-hand,
  seat-private logs 6bf6af5.* +
  r20-6bf6af5.* under NVME
  encode-sweep2.
- Lane-diff vs writer-merge parent
  5215124: rgramc.c only +1549/-1088;
  wall 0. Range 65805..65896.
- gate-tip (wt-encode-sweep2 harness @
  d56ce19): RGRAM py PASS n=8440 FAIL 0,
  PINS-RGRAM set-eq 8440/8440; RAWENC
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
- RGRAMC-PYID 4220/4220 GREEN 0 FAIL
  covered=4220/4220 (corpus 8440
  fresh, py+C freshly executed
  per pin).
- C-batt RGRAM-GREEN 8440/8440 0
  FAIL (RGRAM_BIN=seat-private -O2
  -Wall -Wextra -std=c11 build, 0
  warnings, 1997720 B); C-py
  PASS-set cmp-equal 8440/8440.
- own-loop 65805..65896 fresh-oracle
  92/92 py-agree, pins 32/32, rc=0.
- Added 3/3 EQ (_T10P141AC 74 rows,
  _T10P141BC 70 rows, _T10P141QC
  63 rows, all = py tuples); full
  audit 1D 167/0 + 2D 856/0 +
  dicts 11/0 + STR 271/0 + STRARR
  1063/0.
- Scoped OBSERVED-inherited (PARENT-032
  shape), normalized leg-diff vs
  r19 b196 gate log: ALL legs
  IDENTICAL except RGRAM/PINS-RGRAM
  counts 8384->8440. HYGIENE 14/14
  (.aar 13), CONTAM 44/44, LIBCOMP
  5/5 (aad.c 3 lines), lane file
  0/0/0, aad.c + impl-adapter.sh 0
  diff b196->b198. ADOPT WARN diff
  carried.
- Verdict: PASS-functional. No RED.
