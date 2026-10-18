# NOTE-cport-band224 T10P154 (n<=70420)

Merge 06bd3f5 (w2b@aba4a48 partial, +2 tiers +32 pins, P-lane combine).
Band f7d524d (920 tiers sealed).

Resolve: 3-file conflict (base 8567b02=P153, delta exactly P154). rgram.py blob-reconstructed (P154 S0/S1/AM/AC/BM/BC/M/M3/QR/QT/QC post-R151C + 66-line disp pre-scope-exit; 0 removed both sides; tail R151<P154 ascending; py_compile OK; +1 cosmetic blank vs theirs-delta, P154 content identical).
t.sh+PINS blob-reconstruct: union 4582 cells (+16: 70329..70420) ascending; PINS 9166 rows (2 hdr + 9164) 0 descents.

C-cut hand-built this seat (gen from py tables, P153-pattern + split-M ternary): S0/S1 + AM16/BM10/M16/M3-16/QR4/QT4 + AC76/BC71/QC65 + disp (2 sing + A/B lencode-mblock + Q M3@q3, mtab b19,26,27,76-79, rtab b20-25, ttab b80-83); temps _t3331-3344 _b2108-2112 _i2102-2104; T-comments +123 all 1177 (lookup-verified, T0/T1 consistent).

Battery first-hand this seat (r12):
- RGRAM py GREEN 9164/9164 0 FAIL rc=0 (mrg-b224-py-r12.log)
- RGRAM C GREEN 9164/9164 0 FAIL rc=0 (bat224-c-fh.log, build-band224/rgramc, RGRAM_BIN=C)
- PYID exact 4582/4582 covered 4582/4582 (pyid-band224-fh.log, corpus seeded work-mrg224)
- probes 10/10 C==py pre-battery (all P154 blocks incl M3 q=3 cell 70405 + R151 70328)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
