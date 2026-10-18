# NOTE-cport-band220 T10P152 (n<=69724)

Merge d903ab7 (w2b@50c892a partial, +2 tiers +32 pins, P-lane combine).
Band f1b8d9f (912 tiers sealed).

Resolve: rgram.py auto-merged DESCENDING (P152 disp pre-R149) -> moved R149 block first per b190 precedent, ascending now; multiset 0-removed both sides; py_compile OK.
t.sh+PINS blob-reconstructed (never hunk-stitched): union 4526 cells (+16: 69633..69724) ascending; PINS 9054 rows 0 dupes 0 descents 0 missing.

C-cut hand-built this seat (gen from py tables, P151-pattern): S0/S1/S2 + AM16/BM9/M16/QR4/QT4 + AC75/BC71/QC63 + disp 0/1/A/2/B/Q; temps _t3291-3306 _b2094-2098 _i2094-2096; T-comments renumbered 1163 to current py lines (lane convention).

Battery first-hand this seat (r11):
- RGRAM py GREEN 9052/9052 0 FAIL rc=0 (mrg-b220-py-r11.log)
- RGRAM C GREEN 9052/9052 0 FAIL rc=0 (bat220-c-fh.log, build-band220/rgramc, RGRAM_BIN=C)
- PYID exact 4526/4526 covered 4526/4526 (pyid-band220-fh.log, corpus seeded work-mrg220)
- probes 5/5 C==py pre-battery (69633/69634/69651/69652/69724)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings (x2, incl post-renumber); lane-diff rgramc.c-only; wall-grep 0
