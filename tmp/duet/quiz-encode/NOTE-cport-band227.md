# NOTE-cport-band227 T10R153 (n<=71024)

Merge 500c37e (w2@a0517cd partial, +2 tiers +24 pins, R-lane combine).
Band 42affd9 (926 tiers sealed).

Resolve: 3-file conflict (base 65ee394=R152, delta exactly R153). rgram.py blob-reconstructed (R153 M/Q/C post-P155QC + 20-line disp pre-scope-exit; 0 removed both sides; exact +73 lines; tail ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4622 cells (+12: 70769..71024) ascending; PINS 9246 rows (2 hdr + 9244) 0 descents.

C-cut hand-built this seat (gen from py tables, R152-pattern): M16/Q16/C67 + disp (b45 227/40 thr 15/143, mtab b44,45,50,51,72-75, qtab b34,42,43,76-79); temps _t3365-3368 _b2120-2121 _i2109; T-comments +53 all 1189 (lookup-verified: 1189 exact + 1 T1-ambiguous, 0 mismatch; new T44013 = py disp line).

Battery first-hand this seat (r13):
- RGRAM py GREEN 9244/9244 0 FAIL rc=0 (mrg-b227-py-r13.log)
- RGRAM C GREEN 9244/9244 0 FAIL rc=0 (bat227-c-fh.log, build-band227/rgramc, RGRAM_BIN=C)
- PYID exact 4622/4622 covered 4622/4622 (pyid-band227-fh.log, corpus seeded work-mrg227)
- probes 5/5 C==py pre-battery (70769/70861/70961/71024 + P155Q 70768)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
