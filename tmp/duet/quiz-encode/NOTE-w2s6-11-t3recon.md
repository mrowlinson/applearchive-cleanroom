# NOTE-w2s6-11 writer2: T3+ RECON (regimes mapped, full decode queued)

## Tier lengths (zeros-N, first-hand)
- 44B: N=64..~641+ (T0/T1/T2 + T3-low). 48B: by N=1023 (@1023 AND 1024).
  56B @4096. 60B @8192. (44->48 edge in 642..1023; 48->56 in 2049..4096.)
- T3 head (N=512): b4=01 (off0 ✓), b5=0x20, b8=0x0e — wider length field.
- N=513 b0/b1 = 0001 (counter starts); N=576 b5=0x60; N=640 b5=0x1a.

## Queued (shift-scale, not now)
- T3 full-tier dump + echo/regime fit (same segbed8 method; tier may be
  512-wide with internal edges — 512+ encodes + analysis).
- rgram T3 branch once formulas close. grammar v1 (T0/T1/T2) SHIPPED (46 pins).

## Next: boundary-tie micro (last exposure residue).
