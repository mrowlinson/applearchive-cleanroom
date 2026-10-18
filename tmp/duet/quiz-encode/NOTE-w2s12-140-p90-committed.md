# NOTE-w2s12-140: T10P90 COMMITTED @cd10315

- tier: 48057..48148 (92 cells, 1st big P-head). S0 48057 + S1
  48058 singletons, P90A 48059..48074 (16x80B m-tab b18,19,
  72-75), P90S 48075 singleton (PBB-single), P90B 48076..48084
  (9x80B variegated-sig m-tab b0,1,11,18-21,76-79), P90Q
  48085..48148 (4x16: M 6B b24,25,72-75 + 1+3 rows b12-14,
  17-21 + tails b76-79, b4=(0xab+2off) b5=0x77+(off>=43)).
- gates: probe 92/92 CLOSED, storm 12/12 (wrap 48127/28),
  pins +36 pure, bat90 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- frontier n=48148 (~99.7% of ~48.3k?). next: T10R89 (gen
  validated 70L, census on disk, Q-54 filed, A pending).
