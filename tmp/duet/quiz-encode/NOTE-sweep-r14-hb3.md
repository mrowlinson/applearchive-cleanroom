# NOTE-sweep-r14-hb3

- gate-tip b191 DONE: RGRAM py PASS n=8254
  FAIL 0, PINS-RGRAM set-eq 8254/8254;
  RAWENC 13, PBZE 10, LZMA 6, LZ4 4 (+ -C
  legs all PASS), SMOKE 6, SMOKE-IMPL 6,
  OUTER2 284, RB2 47, RAVFRAME 181, UNITS
  22, LZ4C 5, PINS-RAWENC 11/11 (+C),
  PINS-PBZE 10/10 (+C), PINSETs set-eq,
  OSS nominated-only, C-BUILD warnings=0.
- Only FAILs: HYGIENE/CONTAM/LIBCOMPRESSION
  (scoped inherited, cmp-IDENTICAL b190,
  cross-checked vs live gate.log: 13/42+1/
  3) + ADOPT WARN carried. GATE-FAIL line
  = PASS-functional pattern (as b189).
- PYID running (~15 min in, 0 FAIL lines
  so far); C-batt + own-loop queued.
- Quiz diff 0 recheck pending at filing.
