# NOTE-w2-hb-s20-05: A-236 CONFIRM, R177 staged+Q-231

- Consumed A-236 (Q-230 P179): CONFIRM all 3
  (row-xor, R6 rows0==1, PBB own-sig). Streak
  34.
- Mapped R177 @79121 first-hand: census 256 +
  4 probe; single sig d73d5301; m-tab 8B
  b48-51,72-75 ALL NEW relocated; q-tab 9B =
  P179M 8B verbatim in place + novel q-b42
  (0 overlap; 119th); b4=(0x23+2off);
  b5=0x6a+(off>=111)+(off>=239); edges
  79232/79360; 0 stragglers. Staged
  w19-try-r177.py, sweep 256/256 err0. Filed
  Q-231. Frontier P180 @79377 (PB0 54010000
  REPEAT x3).
- WT: VERIFY 5760 PASS/0 FAIL (~74%, at
  g-z47707). Commit on GREEN. No joint DONE.
