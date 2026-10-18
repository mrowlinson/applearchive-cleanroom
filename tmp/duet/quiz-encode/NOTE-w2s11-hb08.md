# NOTE-w2s11-hb08: P47 battery running, R46 derived

- P47 (33093..33184) implemented, probe 92/92; for-list extended;
  RECORD+battery+smoke running in background.
- R46 = 33185..33440 (256, 80B, head 0c000000); P48 @33441 (76B).
- R46 derived read-only: m-tab b25,26,27,72-75 (7B NEW); q =
  FULL P47M reuse (b20,21 = P47M[q][:4], b68-71 = P47M[q][4:],
  no new q table); raw lencode 256/256.
- Next: commit P47 on GREEN, then R46 tables + probe.
