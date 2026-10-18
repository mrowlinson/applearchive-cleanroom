# NOTE-sweep-r8-hb18: b181 setup done, long legs launched

- Gate tree r8-495edcb/ exported @495edcb;
  ownbuild rgramc 0 warn. Range 62765..63020.
  New pins 24 (vs b180 e5ed337). Lane-diff vs
  aef8ee6: rgramc.c only +1174/-1033; added-
  lines wall-grep 0 hits.
- Launched in parallel: (1) gate-tip.sh full
  battery -> r8-495edcb-gate/; (2) RGRAMC-
  PYID seeded from r7 corpus (-> expect
  4002/4002). Next: C-batt + own-loop +
  tables + inherited-wall, then GATE file.
- Cap 1/2 pending. No commits, no pushes.
