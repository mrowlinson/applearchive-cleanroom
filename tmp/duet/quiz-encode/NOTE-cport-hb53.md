# NOTE-cport-hb53: r3 alive, band153 C port verifying

- tip bfa3762 (R116 259ce63 merge) wall-checked: 3 files only, py+pins MATCH w2, test = w2 + hook (RGRAM_BIN line). PASS.
- WIP rgramc.c preserved; regen fh rc=0 tables 2066/2070 0 stderr, REGEN-IDENTICAL (fh == preview == WIP).
- build fh rc=0, 0 warnings (build-band153/rgramc).
- running first-hand: PYID (pyidb153-fh) + RGRAM py + RGRAM C + SMOKE/UNITS. Expect 3656/3656 + 7312/7312.
