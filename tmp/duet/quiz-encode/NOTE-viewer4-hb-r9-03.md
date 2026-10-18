# NOTE-viewer4-hb-r9-03 (PYID slow on contended box, own-loop GREEN)

- Own-loop 59981..60236: pass=256
  fail=0 pins=12 pinfail=0 OWN-GREEN
  (12 cells == VERIFY 24/24 closed+sha
  convention).
- PYID still running ~25 min, 0 FAIL
  in log: box contended (parent PV
  pv-ef0144b + pv-676626e, viewer3
  b196, r17 b165 PYID all concurrent;
  my worker alive per ps). Seeded
  4101-strong corpus, no oracle regen
  expected — purely CPU-queued.
- Next on PYID green: CBAT + PYBAT +
  set-eq, then suffixed REAUDIT filing
  (pre-filing backstop re-check per
  plan). Quiz diff 0.
