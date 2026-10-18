# NOTE-sweep r2 hb2 (b149 battery running)

- Quick legs first-hand GREEN + identical to orphaned run:
  lane-diff rgramc.c only +1070/-929 vs 47e94d0, wall 0,
  range 57197..57452, added 3/3 EQ (M n=16, C n=69, C_N
  derived), audit 1D 166/0 + 2D 757/0 + dicts 11/0 +
  STR 206/0 + STRARR 900/0. Logs r2-49f108c.*.
- Full battery live (r2-sweep-band.sh, seat-private r2-49f108c):
  gate-tip in RGRAM-py leg (~1580/7214 PASS, 0 FAIL so far);
  ownbuild/PYID/C-batt/own-loop queued in same driver.
- Siblings: sweep2 r2 on b150 (evens, no conflict); cport r3
  verifying band153 (my next odd after 151 885fc37).
