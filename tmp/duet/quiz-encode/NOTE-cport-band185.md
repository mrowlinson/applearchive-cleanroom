# NOTE-cport-band185 T10R132 (n<=63716)

Merge 260016a (w2@cb315f7 partial, +54 py +24 pins).
Band 7c2e8d4 (842 tiers sealed).

Battery first-hand this seat (r9):
- blobs: rgram.py MATCH w2, PINS MATCH w2, test.sh = w2 + hook (auto-merge ok)
- regen no-upto fh rc=0 tables 2274/2278, 0 stderr (regen-b185-fh.c)
- RGRAM py GREEN 8100/8100 0 FAIL rc=0 (mrg-b185-py-r9.log)
- PYID exact 4050/4050 (12 new gen ok, pyid-band185-fh.log, pyidb185-fh/corpus seeded from b184-fh)
- RGRAM C GREEN 8100/8100 0 FAIL rc=0 (bat185-c-fh.log, build-band185/rgramc)
- SMOKE-GREEN + UNITS-GREEN rc=0 (post-C-cut re-run)
- build 0 warnings
