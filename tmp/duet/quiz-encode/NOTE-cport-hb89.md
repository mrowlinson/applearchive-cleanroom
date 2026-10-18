# NOTE-cport-hb89: r7 band178 cut in flight, C GREEN

- merge 76233c8 (P131) committed. regen-b178-fh rc=0 tables 2232/2236 0 stderr -> src/c/rgramc.c.
- build-band178/rgramc: cc -O2 -Wall -Wextra -std=c11, rc=0, 0 warnings.
- RGRAM C GREEN fh: bat178-c-fh 7930/7930 0 FAIL rc=0 (RGRAM_BIN=C).
- PYID full running (pyidb178-fh seeded 4390 from b177, expect 3965/3965). then SMOKE/UNITS re-run + NOTE-band178 + band commit.
- run totals r7 so far: merges 1, bands 0 (1 in flight). no joint DONE. never push.
