# NOTE-cport-band225 T10R152 (n<=70676)

Merge 338f25c (w2@65ee394 partial, +2 tiers +24 pins, R-lane combine).
Band 99edcde (922 tiers sealed).

Resolve: 3-file conflict (base 3b83e62=R151, delta exactly R152). rgram.py blob-reconstructed (R152 M/Q/C post-P154QC + 20-line disp pre-scope-exit; 0 removed both sides; exact +73 lines; tail ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4594 cells (+12: 70421..70676) ascending; PINS 9190 rows (2 hdr + 9188) 0 descents.

C-cut hand-built this seat (gen from py tables, R151-pattern): M16/Q16/C69 + disp (b45 43/38 thr 107/235, mtab b32-34,72-75, qtab b26,27,76-79); temps _t3345-3348 _b2113-2114 _i2105; T-comments +53 all 1182 (lookup-verified, T0/T1 consistent).

Battery first-hand this seat (r12):
- RGRAM py GREEN 9188/9188 0 FAIL rc=0 (mrg-b225-py-r12.log)
- RGRAM C GREEN 9188/9188 0 FAIL rc=0 (bat225-c-fh.log, build-band225/rgramc, RGRAM_BIN=C)
- PYID exact 4594/4594 covered 4594/4594 (pyid-band225-fh.log, corpus seeded work-mrg225)
- probes 5/5 C==py pre-battery (70421/70528/70656/70676 + P154Q 70420)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
