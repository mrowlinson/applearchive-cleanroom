# NOTE-cport-band229 T10R154 (n<=71372)

Merge 0008eef (w2@a987522 partial, +2 tiers +24 pins, R-lane combine).
Band 0b66530 (930 tiers sealed).

Resolve: 3-file conflict (base a0517cd=R153, delta exactly R154). rgram.py blob-reconstructed (R154 M/Q/C post-P156QC + 20-line disp pre-scope-exit; 0 removed both sides; exact +73 lines; tail ascending; py_compile OK).
t.sh+PINS blob-reconstruct: union 4650 cells (+12: 71117..71372) ascending; PINS 9302 rows (2 hdr + 9300) 0 descents.

C-cut hand-built this seat (gen from py tables, R153-pattern): M16/Q16/C67 + disp (b45 155/43 thr 51/179, mtab b20-23,76-79, qtab b13-15,72-75); temps _t3387-3390 _b2127-2128 _i2113; T-comments +53 all 1197 (lookup-verified: 1197 exact + 1 T1-ambiguous, 0 mismatch; new T44265 = py disp line).

Battery first-hand this seat (r13):
- RGRAM py GREEN 9300/9300 0 FAIL rc=0 (mrg-b229-py-r13.log)
- RGRAM C GREEN 9300/9300 0 FAIL rc=0 (bat229-c-fh.log, build-band229/rgramc, RGRAM_BIN=C)
- PYID exact 4650/4650 covered 4650/4650 (pyid-band229-fh.log, corpus seeded work-mrg229)
- probes 5/5 C==py pre-battery (71117/71245/71309/71372 + P156Q 71116)
- SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-C-cut re-run)
- build 0 warnings; lane-diff rgramc.c-only; wall-grep 0
