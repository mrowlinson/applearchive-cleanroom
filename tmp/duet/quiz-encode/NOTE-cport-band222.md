# NOTE-cport-band222 T10P153 (n<=70072)

Merge 1f76333 (w2b@8567b02 partial, +2 tiers +32 pins, P-lane combine).
Band 96e68e8 (916 tiers sealed).

Resolve: rgram.py auto-merged DESCENDING (P153 disp pre-R150) -> moved R150 first, ascending; multiset 0-removed both sides; py_compile OK.
t.sh+PINS blob-reconstruct: union 4554 cells (+16: 69981..70072) ascending; PINS 9110 rows 0 descents 0 missing.

C-cut hand-built this seat (gen from py tables, P152-pattern): S0/S1/S2 + AM/BM/M/QR/QT + AC74/BC69/QC64 + disp 0/1/A/2/B/Q (A 8B b48-51,76-79; B 13B b0,1,44-47,49-51,80-83; Q m7/r7/t4); temps _t3311-3326 _b2101-2105 _i2098-2100; T-comments renumbered 1170 to current py lines.

Battery first-hand this seat (r11):
- RGRAM py GREEN 9108/9108 0 FAIL rc=0 (mrg-b222-py-r11.log)
- RGRAM C GREEN 9108/9108 0 FAIL rc=0 (bat222-c-fh.log, build-band222/rgramc, RGRAM_BIN=C)
- PYID exact 4554/4554 covered 4554/4554 (pyid-band222-fh.log, corpus seeded work-mrg222)
- probes 5/5 C==py pre-battery (69981/69982/69999/70000/70072)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings (x2, incl post-renumber); lane-diff rgramc.c-only; wall-grep 0
