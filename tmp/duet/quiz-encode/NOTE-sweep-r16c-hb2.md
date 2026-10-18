# NOTE-sweep-r16c-hb2: gate-tip GREEN, PYID running

- gate-tip first-hand rc=1 (FAILS are inherited-raw only):
  RGRAM py PASS n=8464, PINS-RGRAM set-eq 8464/8464;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+C legs
  all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2 284/284,
  RB2 47/47, RAVFRAME 181/181, UNITS 22, LZ4C 5,
  PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10 (+C), PINSET
  OUTER2/RB2/RAVFRAME set-eq, OSS nominated-only,
  C-BUILD warnings=0. HYGIENE/CONTAM/LIBCOMPRESSION FAIL
  raw (inherit check pending), ADOPT WARN diff.
- PYID (4232 pins, corpus seeded + fresh regen) running;
  then C-batt, own-loop 65897..66152, tables, inherit.
