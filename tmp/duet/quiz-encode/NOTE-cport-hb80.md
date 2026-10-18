# NOTE-cport-hb80: merge P130 landed, band176 C cut verifying

- merge efc4d19 (w2 35a659c T10P130, +197 py +24 pins, blobs MATCH, hook auto-ok): py 7876/7876 GREEN rc=0 + SMOKE-GREEN rc=0 fh.
- band176 cut: regen no-upto fh rc=0 tables 2219/2223 0 stderr (+1489/-1014, P130 gate n<=62068 verified); build-band176 0 warnings.
- running fh: PYID pyid-band176-fh (seeded, expect 3938/3938) + C battery bat176-c-fh (expect 7876/7876). then SMOKE/UNITS + commit.
