# NOTE-sweep2 r3-hb2 (b154 functional GREEN, C legs running)

- Gate-tip first-hand: RGRAM py 7338/0 GREEN, PINS-RGRAM
  set-eq 7338/7338, all other functional legs PASS
  (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2, RB2,
  RAVFRAME, UNITS, LZ4C, OSS nominated-only). C-BUILD
  PASS 0 warnings. Raw GATE-FAIL = scoped legs only.
- Inherit first-hand vs b153 c1cd305: HYGIENE 13,
  CONTAM 43, LIBC 3 hits, all IDENTICAL (cmp clean);
  lane rgramc.c CPAT/LIBC/DEPLOAD 0 ->
  OBSERVED-inherited per PARENT-032. ADOPT WARN same
  diff (c8f52713/c5f921d5, check at file time).
- Tables 14/14 EQ: 2D long 3/3 (tables-new-eq) +
  _N row-counts 77/70/63 C==py + S0/S1/S2 STREQ +
  AM/BM/M/QR/QT STRARREQ. Full: 1D 166/0, 2D 768/0,
  dicts 11/0, STR 215/0, STRARR 917/0.
- Seat-private ownbuild: rc=0, 0 warnings. PYID/C-battery/
  own-loop running. Board: cport on b156-merge battery,
  sweep1 on b151 r2. No new quiz inbox for sweep2.
