# NOTE-viewer2-hb-r13-02 (own battery running; diff/wall/quiz green)

- Own r13 tree: fresh git archive 02c66ac
  diff-identical to staged (diff -r rc=0).
- Own r13 build: cc -O2 -Wall -Wextra
  -std=c11 rc=0, 0 warnings, 2015048B
  (== r11/r12 staged).
- Lane diff f8ad2af..02c66ac: rgramc.c
  only +1267/-1108. Wall lane-diff 0.
  PINS 8574 lines = 8572 + 2 hdr.
- Quiz: Q max 361, qmiss=0 first-hand
  (fixed own ls-glob bug), diff 0.
- Full r13 battery (PYID/CBAT/PYBAT/
  set-eq/own-loop/tables) running managed;
  VERIFY files when legs land.
