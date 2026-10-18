# NOTE-cport-band221 T10R150 (n<=69980)

Merge 3d13ec3 (w2@a286112 partial, +2 tiers +24 pins, R-lane combine).
Band 171e45a (914 tiers sealed).

Resolve: 3-file conflict. rgram.py blob-reconstructed (R150 M/Q/C + disp from w2 blob; post-P152QC + pre-scope-exit); multiset 0-removed both sides; ascending P152Q<R150 tail; py_compile OK. (first pass truncated tables at M-block end; caught + redone.)
t.sh+PINS blob-reconstruct: union 4538 cells (+12: 69725..69980) ascending; PINS 9078 rows 0 descents 0 missing.

C-cut hand-built this seat (gen from py tables, R149-pattern): M16/Q16/C71 + disp (b45 187/32 thr 35/163, mtab b44,76-79, qtab b36,37,72-75); temps _t3307-3310 _b2099-2100 _i2097; T-comments renumbered 1167+2 to current py lines.

Battery first-hand this seat (r11):
- RGRAM py GREEN 9076/9076 0 FAIL rc=0 (mrg-b221-py-r11.log)
- RGRAM C GREEN 9076/9076 0 FAIL rc=0 (bat221-c-fh.log, build-band221/rgramc, RGRAM_BIN=C)
- PYID exact 4538/4538 covered 4538/4538 (pyid-band221-fh.log, corpus seeded work-mrg221)
- probes 3/3 C==py pre-battery (69725/69980/69837)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings (x2, incl post-renumber); lane-diff rgramc.c-only; wall-grep 0
