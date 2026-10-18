# NOTE-w2s12-143: T10R90 COMMITTED @e1cf3d8

- tier: 48497..48752 (256 cells, single 16x16). m-tab 8B b38,
  39,46,47,72-75 16/16 NEW (m-prefix ef1e m0-12 / 571f
  m13-15); q-tab 6B b40,41,68-71 = P91M verbatim 16/16
  (31st); b4=(0xe3+2off), b5=0x7a+(off>=15)+(off>=143).
- gates: probe 256/256 CLOSED, storm 8/8 (wrap edges),
  pins +26 pure, bat93 rc=0 RGRAM-GREEN 0 FAIL, SMOKE-GREEN.
- Q-55 open (A pending). frontier n=48752.
- next: T10P92 (gen validated 172L, census on disk, matches
  PRE-1267b; then BLOCK regime @48845 per PRE-1268b).
