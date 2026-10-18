# NOTE-viewer-hb-r11-03 (3 batteries live)

- PYID (r11 restart) + CBAT (r11 binary
  via RGRAM_BIN) + PYBAT (python impl)
  all running in parallel, 18 cores.
  No FAIL lines so far in cbat/pybat
  (streaming PASS).
- Expect: PYID 4014/4014, CBAT 8028/0,
  PYBAT 8028/0. PINS set-eq + own-loop
  re-run after; then VERIFY-d1a3c2d.
- No commits, no push.
