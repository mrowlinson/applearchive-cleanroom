# NOTE-cport-hb153: r12 b224 merged + C-cut, PYID/C-batt running

- merge 06bd3f5 committed (w2b@aba4a48 P154 partial, parents 3420198+aba4a48; RGRAM-GREEN 9164/9164 rc=0 + SMOKE-GREEN fh).
- C-cut applied: P154 S0/S1 + AM16/BM10/M16/M3-16/QR4/QT4 + AC76/BC71/QC65 + disp 148 lines (split-M ternary M3@q3); _t3331-3344 _b2108-2112 _i2102-2104; T-renumber +123 all 1177 (lookup-verified, T0/T1 consistent).
- build rc=0 0 warnings (build-band224/rgramc). probes 10/10 C==py (all P154 blocks incl M3 q=3 cell 70405 + R151 neighbor).
- PYID (pyidb224-fh, 4582 seeded) + C batt (work-c224) running concurrently.
