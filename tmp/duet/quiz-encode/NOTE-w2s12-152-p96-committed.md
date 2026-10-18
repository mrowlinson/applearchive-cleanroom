# NOTE-w2s12-152: T10P96 COMMITTED @88ec162

- tier: 50145..50236 (92 cells). S0 50145 + S1 50146,
  PBA 50147..50162 (16x m-tab b28,72-75), PBB 50163..50172
  (10x single-sig m-tab b24,25,29-34,76-79), QUAD
  50173..50236 (4x16 single sig: M 6B b34,35,72-75,
  row bytes b28,30-33 paired, 4 distinct tails). raw
  lencode 92/92 (wrap row0m2->m3 50175/50176, b5 bump
  holds). all head sigs e33c74 family.
- gates: probe 92/92 CLOSED, storm103 13/13 (fresh regen
  pin-identical), pins +26 pure, bat103 rc=0 RGRAM-GREEN
  6184 PASS 0 FAIL, SMOKE-GREEN.
- matches A-68 (3/3 CONFIRM). Q-63 (R94 head) open.
  frontier n=50236.
- next: T10R94 (census on disk, PRE-1276b: 100B 16x16,
  P96M-verbatim q (36th), dbl-carry b5).
