# GATE-87d9a4f sweep: PASS (rgram 1086/1086; covers d0cb3c4 T8T + T8U)

- chain: lanes/encode-writer2 7e25544->d0cb3c4(T8T storm: 3 lits + T1-15 +
  T2S + T2-9 + T3S + T3-15 + T4 3x16)->87d9a4f(T8U 16x16). rgram.py +216/-0,
  cells 9776->10124, pins 1050->1078->1086 (+36/-0).
- code read (ALL both diffs): 11 tables (_T8T0/T1/T2S/T2/T3S/T3/T4,
  _T8UT/_T8UC) + 8 branches monotone contiguous (off 1042..1389, each
  starts where prior ends: T0 9779/T1/T2S 9795/T2/T3S 9805/T3/T4 9868/U
  10124). every table index hand-bounded in-range (T1 15, T2 9, T3 15,
  T4 m16/q3, U m16/q16 vs _T8T4T-16). T8T4 blk quirk (pay5-1 when q2+off)
  read as-is. no imports/OSS/disasm markers.
- pins append-only (0 `-` lines); battery GATE-PASS (outdir
  gate-w2-87d9a4f-s4): RGRAM n=1086, PINS-RGRAM set-eq 1086/1086 (full-leg
  PASS implied by verdict, zero FAIL lines).
- coverage: 88/88 writer tips gated (88 battery-PASS, ZERO holds).
- viewer: VERIFY-87d9a4f PASS concur (battery GREEN, tip current).
