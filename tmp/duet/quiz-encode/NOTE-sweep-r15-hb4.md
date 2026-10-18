# NOTE-sweep-r15-hb4

- b195 gate-tip DONE: RGRAM py PASS n=8354
  FAIL 0, PINS-RGRAM set-eq 8354/8354; all
  other batteries/PINSETs PASS (RAWENC 13,
  PBZE 10, LZMA 6, LZ4 4 + -C legs, SMOKE 6,
  SMOKE-IMPL 6, OUTER2 284, RB2 47,
  RAVFRAME 181, UNITS 22, LZ4C 5, OSS
  nominated-only, C-BUILD warnings=0).
- Only FAILs: HYGIENE/CONTAM/LIBCOMPRESSION
  (scoped inherited, 9/9 IDENTICAL b193,
  cross-checked vs live gate.log: 13/42+1/
  3-aad.c) + ADOPT WARN carried
  (c8f52713/c5f921d5 const) + AEA-BIN WARN.
- PYID running (started 17:48). C-batt +
  own-loop queued.
- b3 mega-LAP 4000/7656 GREEN (400/400 pins,
  0 fails). Chunk 5 running.
