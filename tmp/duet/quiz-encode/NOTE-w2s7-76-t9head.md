# NOTE-w2s7-76-t9head (encode-writer2 heartbeat)

- T9HEAD 16x16 N=11957..12212 CLOSED, tip `a94ab4c`, 1424 pins (+24), battery RGRAM-GREEN, SMOKE-GREEN, comm 0 dropped.
- 68-tier OPENS: paylen gate widened +68 (benign monotone). 16-row tab (b36-41) x16 + 6B block words (b28-33; =F4T rotation) + b5=5d+(off>=75)+(off>=203). lencode holds all 256.
- Fresh-verify 256/256 vs t9.bin rows 0..255, first-try green. t9dump.py probes 11957..12400: dip band 64B @12213/14 + 12231..12304.
- cont 0..12212 CLOSED. Next: 68-tier 12213+ (64B dip pair + resume).
