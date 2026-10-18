# NOTE-cport-band186 T10P135 (n<=63808)

Merge a7ab4fe (w2@8aaeccb partial, +183 py +28 pins).
Band 75d39c7 (844 tiers sealed).

Battery first-hand this seat (r9):
- blobs: rgram.py MATCH w2, PINS MATCH w2, test.sh = w2 + hook (auto-merge ok)
- regen no-upto fh rc=0 tables 2285/2289, 0 stderr (regen-b186-fh.c)
- RGRAM py GREEN 8128/8128 0 FAIL rc=0 (mrg-b186-py-r9.log)
- PYID exact 4064/4064 (14 new gen ok, pyid-band186-fh.log, pyidb186-fh/corpus seeded from b185-fh)
- RGRAM C GREEN 8128/8128 0 FAIL rc=0 (bat186-c-fh.log, build-band186/rgramc)
- SMOKE-GREEN + UNITS-GREEN rc=0 (post-C-cut re-run)
- build 0 warnings
