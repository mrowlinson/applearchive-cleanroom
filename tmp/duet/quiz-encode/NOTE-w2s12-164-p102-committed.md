# NOTE-w2s12-164: T10P102 COMMITTED @5d1fe68

- tier: 52233..52324 (92 cells). S0 52233 (sig fcb20900)
  + S1 52234, PBA 52235..52250 (16x m-tab b40,41,42,
  72-75), split-PBB 52251..52260 (10x: single 52251 sig
  ..0a + 9x sig ..04, 17B m-tab), QUAD 52261..52324
  (4x16 SPLIT sig: M 8B b40,41,46,47,72-75, rows0-2 sig
  ..40 rb shared, row3 sig ..44 rb unique, tails
  07766cb8/b2ba6cb8/63b98cb9/53b05056). raw lencode
  92/92 (no wrap, max 0xc9).
- gates: probe 92/92 CLOSED, storm115 12/12 (fresh regen
  pin-identical), pins +24 pure, bat115 rc=0 RGRAM-GREEN
  6500 PASS 0 FAIL, SMOKE-GREEN.
- matches A-80 (3/3 CONFIRM). Q-75 (R100 head) open.
  frontier n=52324.
- next: T10R100 (census on disk, PRE-1288b: 100B 16x16,
  P102M-verbatim q (42nd), dbl-carry b5).
