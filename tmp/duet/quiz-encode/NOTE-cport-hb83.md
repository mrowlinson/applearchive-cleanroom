# NOTE-cport-hb83: merge R128 landed, band177 C cut verifying

- merge 2479628 (w2 d169a51 T10R128, +57 py +24 pins, blobs MATCH, hook auto-ok): py 7900/7900 GREEN rc=0 + SMOKE-GREEN rc=0 fh.
- band177 cut: regen no-upto fh rc=0 tables 2221/2225 0 stderr (+1166/-1019, R128 gate n<=62324 verified); build-band177 0 warnings.
- running fh: PYID pyid-band177-fh (seeded 4366, expect 3950/3950) + C battery bat177-c-fh (expect 7900/7900). then SMOKE/UNITS + commit.
