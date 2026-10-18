# NOTE-cport-band190 T10P137 (n<=64504)

Merge 8079ebb (w2b@e81d47b partial, +175 py +28 pins, 3rd cross-lane combine).
Band 05efb6d (852 tiers sealed).

Battery first-hand this seat (r10):
- resolve-b190.py: rgram.py auto-merged but chain descended -> moved R134 before P137 (ascending P136Q<R134<P137B<P137Q); PINS chronological 8230, sizes union 4115; 0 removed vs HEAD and vs w2b; py_compile OK
- RGRAM py GREEN 8230/8230 0 FAIL rc=0 (mrg-b190-py-r10.log)
- regen no-upto fh rc=0 tables 2312/2316, 0 stderr (regen-b190-fh.c)
- RGRAM C GREEN 8230/8230 0 FAIL rc=0 (bat190-c-fh.log, build-band190/rgramc)
- PYID exact 4115/4115 (pyid-band190-fh.log, pyidb190-fh/corpus seeded from b189-fh)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; wall-grep 0
