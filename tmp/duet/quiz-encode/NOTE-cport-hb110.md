# NOTE-cport-hb110: b185 merge landed, PYID running

- mrg-b185-py-r9 GREEN 8100/8100 rc=0 fh; smoke fh SMOKE-GREEN rc=0.
- merge 260016a landed (w2@cb315f7 partial, T10R132 n<=63716 +2 tiers +24 pins).
- regen no-upto fh rc=0 tables 2274/2278, 0 stderr; seat build -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings.
- PYID full running (pyidb185-fh seeded 4566 corpus files from b184); expect 4050/4050. Then C GREEN + SMOKE/UNITS + band185 cut.
- no joint DONE. never push.
