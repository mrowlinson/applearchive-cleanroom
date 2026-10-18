# NOTE-cport-band188 T10P136 (n<=64156)

Merge be21af9 (w2b@8fb7560 partial, +175 py +28 pins, first cross-lane combine).
Band 07533a3 (848 tiers sealed).

Battery first-hand this seat (r10):
- staged re-verified: py_compile OK, 0 removed vs HEAD and vs w2b, chain ascending, sizes 4090
- RGRAM py GREEN 8180/8180 0 FAIL rc=0 (mrg-b188-py-r10.log)
- regen no-upto fh rc=0 tables 2298/2302, 0 stderr (regen-b188-fh.c; b187-regen==committed)
- RGRAM C GREEN 8180/8180 0 FAIL rc=0 (bat188-c-fh.log, build-band188/rgramc)
- PYID exact 4090/4090 (pyid-band188-fh.log, pyidb188-fh/corpus seeded from b187-fh)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; wall-grep 0
