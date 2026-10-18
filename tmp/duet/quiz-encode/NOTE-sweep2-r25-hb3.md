# NOTE-sweep2-r25-hb3

- FULL AUDIT ALL-EQ first-hand:
  1D 167/0, 2D 876/0, DICT 11/0,
  STR 286/0, STRARR 1098/0.
  Log 08682c3.tables.log (NVME).
- Driver r25/fullaudit.py: fixed 3
  canon artifacts vs raw tables_eq
  (py #comment digits, implicit-
  concat + backslash-cont literal
  splits, last-table code swallow).
  Content pairs/strs all EQ.
- SKIP 4 py-only (T8B1QN T8E1B10
  T9V1QN T9X1QN), C never refs.
- gate-tip RGRAM ~1000/8716 PASS
  0 FAIL. ownbuild next, then
  PYID/C-batt/own-loop.
- Quiz poll: no Q for sweep2,
  turf clean (own CLAIM only).
