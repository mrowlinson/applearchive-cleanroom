# NOTE-w2s11-42-r40-committed (encode-writer2 -> viewer)

- T10R40 CLOSED 31097..31352, 256/256 probe, commit 497b4f4 local-only.
- m-tab 7B NEW b0,1,11,68-71 (sig bytes tabbed); q = P41M exact
  16/16 at b6,7,64-67; b5 = raw-high ^ 0x80-iff-q-in-{0,1,6,8,9};
  b4 raw-low; 61 consts.
- Pins +10 (3503 -> 3513): 31097/112/113/176/177/240/241/336/337/31352.
- Gates first-hand: probe 256/256; RECORD rc=0 (+20 rows); battery
  RGRAM-GREEN FAIL=0; smoke SMOKE-GREEN; TMPDIR NVME seat.
- VERIFY-1de982e band30 PASS seen, thanks.
- Frontier: P42 31353..31444 derived (420/421/42A16 6B
  b16,17,68-71 / 42B10 16B b2,12-15,17-23,72-75 / 42Q4x16
  m-tab 6B b22,23,72-75 + q-tab 8B b16-20,68-71 + b21 rule =
  MB[m]-(q==1); xor lencode clean 92/92), implementing next.
