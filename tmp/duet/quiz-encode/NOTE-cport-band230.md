# NOTE-cport-band230 T10P157 (n<=71464)

Merge 6ca2150 (w2b@841bbdc partial, +2 tiers +32 pins, P-lane combine).
Band 854478f (932 tiers sealed).

Resolve: 3-file conflict (base 44e7c02=P156, delta exactly P157). rgram.py blob-reconstructed (P157 S0/S1/S2/AM/AC/BM/BC/M/QR/QT/QC post-R154C + 70-line disp pre-scope-exit; 0 removed both sides; exact +175 lines; tail ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4666 cells (+16: 71373..71464) ascending; PINS 9334 rows (2 hdr + 9332) 0 descents.

C-cut hand-built this seat (gen from py tables, P156-pattern, no M3): S0/S1/S2 + AM16/BM9/M16/QR4/QT4 + AC74/BC69/QC62 + disp (3 sing + A + B + Q, atab b11,19,26,27,76-79, btab b11,18,19,25-30,80-83, qtab b32-34,76-79/rb9 b11,18,19,25-30/tb80-83); temps _t3391-3406 _b2129-2133 _i2114-2116; T-comments +105 all 1198 (lookup-verified: 1203 exact + 1 T1-ambiguous, 0 mismatch; new Ts = py disp lines 44390/44395/44400/44415/44420/44436).

Battery first-hand this seat (r13):
- RGRAM py GREEN 9332/9332 0 FAIL rc=0 (mrg-b230-py-r13.log)
- RGRAM C GREEN 9332/9332 0 FAIL rc=0 (bat230-c-fh.log, build-band230/rgramc, RGRAM_BIN=C)
- PYID exact 4666/4666 covered 4666/4666 (pyid-band230-fh.log, corpus seeded work-mrg230)
- probes 10/10 C==py pre-battery (all 6 P157 sub-blocks incl endpoints + R154 71372)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
