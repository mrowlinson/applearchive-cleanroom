# NOTE-w2s7-78-t9d2 (encode-writer2 heartbeat)

- T9D2 dip band N=12231..12304 CLOSED, tip `c9441d4`, 1460 pins (+28), battery RGRAM-GREEN, SMOKE-GREEN, comm 0 dropped.
- Shape: 3 singleton literals (12231/32/41) + A 8-row tab (b40-47) + Q 16-row tab (b48-53) x4 (last truncated m0-14) + 8B words (b40-47, k15 early-edge) + b5=5f+(n>=12288). Paylen 64 throughout.
- Fresh-verify 74/74 vs t9dip.bin, first-try green.
- cont 0..12304 CLOSED. Next: 68-tier resume 12305+ (t9.bin rows 348+).
