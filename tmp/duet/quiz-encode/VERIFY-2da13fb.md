# VERIFY-2da13fb T10P14 head 21609..21636 + PEQ 21637..21700: PASS

## batteries (at-commit tree ver-2da13fb, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (21609/21610/21611/21626/21627/21636/21637/21652/21653/
  21700, all 88B).
- 92/92 FULL-HEAD CLOSED at-commit rgram.py (every cell
  21609..21700, fresh oracle bytes each).
- b5 cross-checked vs OWN census beds (c21609..c21700 on disk):
  {40: 23, 41: 69} — EXACT vs code structure: PE0/PE1/PEA
  const 0x28 (18) + PEB rows 0-4 0x28 (5) = 23; PEB rows
  5-9 0x29 (lits start 29, verified) + PEQ const 0x29 (64)
  = 69. head split at 21631/21632 confirmed first-hand.
- boundaries: 21608 still CLOSED T10R12 off=255; 21701 out
  of scope rc=2. no neighbor breakage.

## code read
- PE0+PE1 singletons + PEA 16-tab (b37,64-67) + PEB 10-tab
  (b5,40-44,68-71, b5 embedded) + PEQ 4x16 (m-tab b45,46,
  68-71 + q-tab b40-43,64-67) + const tables + dispatch.
  structure consistent.
- for-list +10 cells (head corners + PEB edges 21626/21627
  + quad edges 21652/21653 + corners). pins +20 rows.
- diff pure addition: rgram +165, for-list edit, pins +20.

## verdict: PASS (T10P14 ->21700; 2694 pins)
