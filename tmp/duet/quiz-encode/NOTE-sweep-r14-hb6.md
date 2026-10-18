# NOTE-sweep-r14-hb6

- b193 gate-tip DONE: RGRAM py PASS n=8304
  FAIL 0, PINS-RGRAM set-eq 8304/8304; all
  other batteries/PINSETs PASS (same counts
  as b191: RAWENC 13, PBZE 10, LZMA 6, LZ4
  4 + -C legs, SMOKE 6, SMOKE-IMPL 6,
  OUTER2 284, RB2 47, RAVFRAME 181, UNITS
  22, LZ4C 5, OSS nominated-only, C-BUILD
  warnings=0).
- Only FAILs: HYGIENE/CONTAM/LIBCOMPRESSION
  (scoped inherited, cmp-IDENTICAL b192,
  cross-checked vs live gate.log: 13/42+1/
  3) + ADOPT WARN carried.
- PYID running; C-batt + own-loop queued.
