# NOTE-cport-band223 T10R151 (n<=70328)

Merge e6ff313 (w2@3b83e62 partial, +2 tiers +24 pins, R-lane combine).
Band 3420198 (918 tiers sealed).

Resolve: 3-file conflict (base a286112=R150, delta exactly R151). rgram.py blob-reconstructed (R151 M/Q/C post-P153QC + disp pre-scope-exit; 0 removed both sides; tail R150<P153<R151 ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4566 cells (+12: 70073..70328) ascending; PINS 9134 rows (2 hdr + 9132) 0 descents.

C-cut hand-built this seat (gen from py tables, R150-pattern): M16/Q16/C68 + disp (b45 115/35 thr 71/199, mtab b13-15,76-79, qtab b6,7,9,72-75); temps _t3327-3330 _b2106-2107 _i2101; T-comments +53 all 1176 (1174 lookup-exact).

Battery first-hand this seat (r12):
- RGRAM py GREEN 9132/9132 0 FAIL rc=0 (mrg-b223-py-r12.log)
- RGRAM C GREEN 9132/9132 0 FAIL rc=0 (bat223-c-fh.log, build-band223/rgramc, RGRAM_BIN=C)
- PYID exact 4566/4566 covered 4566/4566 (pyid-band223-fh.log, corpus seeded work-mrg223)
- probes 5/5 C==py pre-battery (70073/70144/70272/70328 + P153Q 70072)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
