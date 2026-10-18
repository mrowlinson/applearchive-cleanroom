# NOTE-sweep2-r11-hb5 (b174 gate-tip green, C legs running)

- Gate-tip first-hand: RGRAM py 7830 PASS,
  PINS-RGRAM set-eq 7830/7830, all other
  functional legs PASS (RAWENC/PBZE/LZMA/LZ4
  + -C, SMOKE/IMPL, OUTER2, RB2, RAVFRAME,
  UNITS, LZ4C, OSS nominated-only).
- Scoped legs: HYGIENE 13 / CONTAM 43 /
  LIBC 3 all IDENTICAL vs b172 gate log
  (incl. known-FP depload ZBM_DYLIB);
  ADOPT WARN same c8f52713/c5f921d5.
- Ownbuild 0 warnings (rgramc 1861176 B).
  PYID + C-batt + own-loop running. Quota 0/2.
