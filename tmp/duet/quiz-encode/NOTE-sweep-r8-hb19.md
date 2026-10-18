# NOTE-sweep-r8-hb19: tables green, C-batt + ownloop launched

- Tables audit EQ vs py: 1D 166/0 + 2D
  821/0 + dicts 11/0 + STR 246/0 + STRARR
  1004/0 (1 skip _s, same shape as r7).
- Added 3/3 EQ: _T10R130C n=69, _C_N=69
  derived-consistent, _T10R130M n=16.
  (R130 has no QH in C or py — verified.)
- Launched: C-batt (RGRAM_BIN=C live over
  8004) + own-loop fresh-oracle 62765..63020
  (C + py-agree + new-pins 24). gate-tip.sh
  + PYID still running. Next: inherited-wall
  comparison, then GATE-495edcb.
- Cap 1/2 pending. No commits, no pushes.
