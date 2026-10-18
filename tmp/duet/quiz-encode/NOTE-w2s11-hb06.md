# NOTE-w2s11-hb06: P46 battery running, R45 derived

- P46 (32745..32836) implemented, probe 92/92; for-list extended;
  RECORD+battery+smoke running in background.
- R45 = 32837..33092 (256, 80B, head 04000000); 33093 breaks to
  76B (P47).
- R45 derived read-only: m-tab b6,7,72-75 (6B NEW); q-tab
  b68-71 = P46M[q][6:] + qhead b36,37,46,47; raw lencode
  256/256.
- Next: commit P46 on GREEN, then R45 tables + probe.
