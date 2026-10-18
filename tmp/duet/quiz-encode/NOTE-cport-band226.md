# NOTE-cport-band226 T10P155 (n<=70768)

Merge 33b47ac (w2b@fe948b1 partial, +2 tiers +32 pins, P-lane combine).
Band aaed31b (924 tiers sealed).

Resolve: 3-file conflict (base aba4a48=P154, delta exactly P155). rgram.py blob-reconstructed (P155 S0/S1/S2/AM/AC/BM/BC/M/QR/QT/QC post-R152C + 70-line disp pre-scope-exit; 0 removed both sides; +1 cosmetic blank, P155 content identical; py_compile OK).
t.sh+PINS blob-reconstruct: union 4610 cells (+16: 70677..70768) ascending; PINS 9222 rows (2 hdr + 9220) 0 descents.

C-cut hand-built this seat (gen from py tables, P154-pattern, no M3): S0/S1/S2 + AM16/BM9/M16/QR4/QT4 + AC74/BC69/QC63 + disp (2 sing + A + S2-extra + B + Q, mtab b44-46,76-79, rtab b32,33,37-42, ttab b80-83); temps _t3349-3364 _b2115-2119 _i2106-2108; T-comments +105 all 1183 (lookup-verified, T0/T1 consistent).

Battery first-hand this seat (r12):
- RGRAM py GREEN 9220/9220 0 FAIL rc=0 (mrg-b226-py-r12.log)
- RGRAM C GREEN 9220/9220 0 FAIL rc=0 (bat226-c-fh.log, build-band226/rgramc, RGRAM_BIN=C)
- PYID exact 4610/4610 covered 4610/4610 (pyid-band226-fh.log, corpus seeded work-mrg226)
- probes 11/11 C==py pre-battery (all P155 blocks + R152 70676)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
