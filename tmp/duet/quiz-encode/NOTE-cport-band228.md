# NOTE-cport-band228 T10P156 (n<=71116)

Merge f9ad84f (w2b@44e7c02 partial, +2 tiers +32 pins, P-lane combine).
Band 8289f49 (928 tiers sealed).

Resolve: 3-file conflict (base fe948b1=P155, delta exactly P156). rgram.py blob-reconstructed (P156 S0/S1/S2/S3/AM/AC/BM/BC/M/QR/QT/QC post-R153C + 74-line disp pre-scope-exit; 0 removed both sides; exact +179 lines; tail ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4638 cells (+16: 71025..71116) ascending; PINS 9278 rows (2 hdr + 9276) 0 descents.

C-cut hand-built this seat (gen from py tables, P155-pattern, no M3): S0/S1/S2/S3 + AM16/BM8/M16/QR4/QT4 + AC75/BC72/QC65 + disp (4 sing + A + B + Q, atab b6,7,9,76-79, btab b6-11,80-83, qtab b13-15,76-79/rb6 b6-11/tb80-83); temps _t3369-3386 _b2122-2126 _i2110-2112; T-comments +105 all 1190 (lookup-verified: 1196 exact + 1 T1-ambiguous, 0 mismatch; new Ts = py disp lines 44138/44143/44148/44163/44168/44173/44188).

Battery first-hand this seat (r13):
- RGRAM py GREEN 9276/9276 0 FAIL rc=0 (mrg-b228-py-r13.log)
- RGRAM C GREEN 9276/9276 0 FAIL rc=0 (bat228-c-fh.log, build-band228/rgramc, RGRAM_BIN=C)
- PYID exact 4638/4638 covered 4638/4638 (pyid-band228-fh.log, corpus seeded work-mrg228)
- probes 11/11 C==py pre-battery (all 7 P156 sub-blocks incl endpoints + R153 71024)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
