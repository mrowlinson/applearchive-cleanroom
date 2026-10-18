# NOTE-cport-band187 T10R133 (n<=64064)

Merge 786f2a7 (w2@4f399ae partial, +55 py +24 pins).
Band 5bfc21a (846 tiers sealed).

Battery first-hand this seat (r9):
- blobs: rgram.py MATCH w2, PINS MATCH w2, test.sh = w2 + hook (auto-merge ok)
- regen no-upto fh rc=0 tables 2287/2291, 0 stderr (regen-b187-fh.c)
- RGRAM py GREEN 8152/8152 0 FAIL rc=0 (mrg-b187-py-r9.log)
- PYID exact 4076/4076 (12 new gen ok, pyid-band187-fh.log, pyidb187-fh/corpus seeded from b186-fh)
- RGRAM C GREEN 8152/8152 0 FAIL rc=0 (bat187-c-fh.log, build-band187/rgramc)
- SMOKE-GREEN + UNITS-GREEN rc=0 (post-C-cut re-run)
- build 0 warnings
