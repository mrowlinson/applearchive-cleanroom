# NOTE-cport-band189 T10R134 (n<=64412)

Merge d335153 (w2@14b73de partial, +72 py +22 pins, 2nd cross-lane combine).
Band fac36c9 (850 tiers sealed).

Battery first-hand this seat (r10):
- resolve-b189.py: tables from blob sources (P136 104 + R134 52), chain R133<P136Q<R134, hunk sides == blob slices, py_compile OK; 0 removed vs HEAD and vs w2
- RGRAM py GREEN 8202/8202 0 FAIL rc=0 (mrg-b189-py-r10.log)
- regen no-upto fh rc=0 tables 2301/2305, 0 stderr (regen-b189-fh.c)
- RGRAM C GREEN 8202/8202 0 FAIL rc=0 (bat189-c-fh.log, build-band189/rgramc)
- PYID exact 4101/4101 (pyid-band189-fh.log, pyidb189-fh/corpus seeded from b188-fh)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; wall-grep 0
