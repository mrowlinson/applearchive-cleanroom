# VERIFY-5d1715c T10R12 16x16 21353..21608 (m-tab + PDM q-tab): PASS

## batteries (at-commit tree ver-5d1715c, WS tmp/encode-viewer)
- 8/8 new-pin shas MATCH independent oracle re-runs
  (21353/21369/21375/21376/21497/21503/21504/21608, all 88B).
- 256/256 FULL-RANGE CLOSED at-commit rgram.py (every cell
  21353..21608, fresh oracle bytes each).
- b5 cross-checked vs OWN census beds (c21353..c21608 on disk):
  {38: 23, 39: 128, 40: 105} — EXACT vs code's _T10R12B5
  (0x26 x2 / 0x27 x8 / 0x28 x6 + q1/q9 m7-carry):
  23 = 16+7, 128 = 9+112+7, 105 = 9+96.
- boundaries: 21352 still CLOSED T10PDQ off=63; 21609 out of
  scope rc=2. no neighbor breakage.

## code read
- m-tab _T10R12M 16 lits (b33,34,64-67) + _T10R12B5 16-tuple
  + q1/q9 m>=7 carry + q-tab reuses _T10PDM (b29,30,68-71)
  + const table + dispatch clause. structure consistent.
- for-list +8 cells (head/corner/edge picks incl 21369/21375/
  21376 + 21497/21503/21504 wrap edges). pins +16 rows.
- diff pure addition: rgram +44, for-list edit, pins +16.

## verdict: PASS (T10R12 ->21608; 2674 pins)
