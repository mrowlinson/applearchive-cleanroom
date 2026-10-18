# NOTE-cport-hb77: merge 394b22e landed, band175 C cut verifying

- merge 394b22e (w2 39113ce T10R127, +55 py +22 pins, hook 2 lines): py 7852/7852 GREEN rc=0 + SMOKE-GREEN rc=0 fh.
- band175 cut: regen no-upto fh rc=0 tables 2208/2212 0 stderr (+1154/-1013, R127 gate n<=61976 verified); build-band175 0 warnings.
- running fh: PYID pyid-band175-fh (seeded 4320, expect 3926/3926) + C battery bat175-c-fh (expect 7852/7852). then SMOKE/UNITS + commit.
