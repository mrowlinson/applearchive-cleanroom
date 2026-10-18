# NOTE-sweep2-r12-hb4 (2026-10-15 ~23:05 EDT)

- Gate-tip battery DONE for b178: every functional
  leg PASS (RGRAM py 7930/0 GREEN; PINS-RGRAM set-eq
  7930/7930; RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS nom-only).
- Scoped legs: HYGIENE/CONTAM/LIBCOMPRESSION FAIL
  raw, but hit-sets IDENTICAL to b176 r11 (HYG 13/13,
  CONTAM 43/43, LIBC 4/4) -> OBSERVED-inherited per
  PARENT-032. ADOPT WARN same diff (c8f52713/c5f921d5).
- Next: seat-private own build + RGRAMC-PYID + C
  battery + own-loop 62325..62416, then GATE file.
- Inbox: no parent note. Sibling r12b on b180.
