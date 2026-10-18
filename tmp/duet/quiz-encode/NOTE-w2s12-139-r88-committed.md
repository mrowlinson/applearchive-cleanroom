# NOTE-w2s12-139: T10R88 COMMITTED @a8bb3fb

- tier: 47737..48056 (320 cells). R88A 47737..47800 (4x16 quad,
  m-tab b6-9,72-75 16/16 + pair-row q-tab b27,37-39,46,47,
  76-79, raw lencode), R88B 47801..48056 (16x16, sig-led m-tab
  b0-2,72-75 12-sig 16-cycle byte3=0x4a + q=AM verbatim 16/16
  pos[6-9,68-71], raw lencode).
- gates: probe 320/320 CLOSED, storm 10/10 (wrap edges
  47743/44, 47871/72, 47999/48000), pins +26 pure, bat88 rc=0
  RGRAM-GREEN 0 FAIL, SMOKE-GREEN — all first-hand.
- A-60 agrees (verbatim 16/16, 12-sig cycle, pair-rows, no
  dips; caveat even pair-row 6B PBB-shared noted, code unaffected).
- frontier n=48056. next: T10P90 (gen validated 175L, census
  on disk), then R89 (census on disk, Q-54 filed).
