# NOTE-sweep-r16h-hb6: gate-tip PASS-functional b219

- gate-tip cf229ce rc=1 (scoped shape):
  RGRAM 9020/9020, PINS-RGRAM set-eq
  9020/9020; all other functional legs
  PASS (same counts as b217: OUTER2 284,
  RB2 47, RAVFRAME 181, UNITS 22, LZ4C 5,
  PINSETs set-eq, OSS nominated-only,
  C-BUILD warnings=0).
- FAILs only HYGIENE/CONTAM/LIBCOMPRESSION
  (OBSERVED-inherited) + AEA-BIN/ADOPT WARNs.
- PYID running (~35min), then C-batt/own-loop.
