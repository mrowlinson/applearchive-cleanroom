# NOTE-sweep-r16d-hb3: b203 gate-tip GREEN-functional, PYID running

- gate-tip first-hand: RGRAM py PASS n=8572,
  PINS-RGRAM set-eq 8572/8572; RAWENC/PBZE/
  LZMA/LZ4 +C legs, SMOKE/IMPL, OUTER2/RB2/
  RAVFRAME + PINSET, UNITS, LZ4C, OSS
  nominated-only, C-BUILD warnings=0 all PASS.
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw
  (inherit pending), ADOPT WARN. rc=1 shape
  matches b199/b201.
- PYID (4286 pins, 28 fresh-oracle regen)
  running since 03:15; then C-batt, own-loop
  66593..66848, tables, inherit b201->b203.
