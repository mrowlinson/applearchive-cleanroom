# NOTE-viewer2-hb-r8-04

- PYID COMPLETE: RGRAMC-PYID 4101/4101
  covered=4101/4101 RGRAMC-GREEN, rc=0,
  0 FAIL (r8 bin; corpus grew 4076 ->
  4101 .rav + 25 .bin via oracle for
  the 25 new pins b188+b189).
- CBAT (RGRAM_BIN=r8 bin) + PYBAT (py)
  launched concurrently, separate
  seat workdirs/logs (cbat-r8, pybat-r8).
  Fresh oracle each; expect 8202/8202.
- Next: collect both, PINS set-eq,
  GATE poll, VERIFY-if-gated else hold.
