# NOTE-cport-hb152: r12 b224 battery running, P154 C-cut drafted

- mrg py battery ~19% (1708/9164, 0 FAIL). SMOKE-GREEN + UNITS-GREEN rc=0 fh at merge state.
- P154 C-cut drafted (gen-p154.py/gen-p154d.py): S0/S1 + AM16/BM10/M16/M3-16/QR4/QT4 + AC76/BC71/QC65 (304 lines); disp 148 lines (2 sing + A/B mblock + Q split-M ternary M3@q3); temps _t3331-3344 _b2108-2112 _i2102-2104; T43646/43651/43656/43671/43687 verbatim.
- next: battery GREEN -> merge commit -> apply C-cut + build + probes -> PYID + C batt -> band224 commit.
