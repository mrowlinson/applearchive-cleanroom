# NOTE-cport-hb155: r12 b225 merged + C-cut, PYID running

- merge 338f25c committed (w2@65ee394 R152 partial, parents f7d524d+65ee394; RGRAM-GREEN 9188/9188 rc=0 + SMOKE-GREEN fh).
- C-cut applied: R152 M16/Q16/C69 + disp (b45 43/38 thr 107/235, mtab b32-34,72-75, qtab b26,27,76-79); _t3345-3348 _b2113-2114 _i2105; T-renumber +53 all 1182 (lookup-verified, T0/T1 consistent).
- build rc=0 0 warnings (build-band225/rgramc). probes 5/5 C==py (70421/70528/70656/70676 + P154Q 70420).
- C batt GREEN 9188/9188 rc=0 (bat225-c-fh.log). PYID running (pyidb225-fh, 4594 seeded). SMOKE-GREEN + UNITS-GREEN rc=0 (merge + post-cut). lane-diff rgramc.c-only; wall-grep 0.
