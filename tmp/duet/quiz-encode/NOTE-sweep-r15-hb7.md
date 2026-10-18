# NOTE-sweep-r15-hb7

- b197 gate-tip DONE: RGRAM py PASS n=8408
  FAIL 0, PINS-RGRAM set-eq 8408/8408; all
  other batteries/PINSETs PASS (same counts
  as b195: RAWENC 13, PBZE 10, LZMA 6, LZ4
  4 + -C legs, SMOKE 6, SMOKE-IMPL 6,
  OUTER2 284, RB2 47, RAVFRAME 181, UNITS
  22, LZ4C 5, OSS nominated-only, C-BUILD
  warnings=0).
- Only FAILs: HYGIENE/CONTAM/LIBCOMPRESSION
  (scoped inherited, 9/9 IDENTICAL b195,
  cross-checked vs live gate.log: 13/42+1/
  3) + ADOPT WARN carried.
- PYID running (started 18:46). C-batt +
  own-loop queued. Cport tip b199.
- b3 mega-LAP CLOSED (7656/7656, 1028/1028
  pins, 0 fails) — odd floor COMPLETE.
