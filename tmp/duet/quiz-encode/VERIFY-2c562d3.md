# VERIFY-2c562d3 T10R15 16x16 22397..22652: PASS

## batteries (at-commit tree ver-2c562d3, WS tmp/encode-viewer)
- 10/10 pin shas MATCH independent oracle re-runs
  (22397/22399/22400/22413/22525/22527/22528/22652 new +
  22396/22348 edge, all 88B).
- 256/256 FULL CLOSED at-commit rgram.py (every cell
  22397..22652, fresh oracle bytes each).
- tabs vs OWN census beds (c22397..c22652 on disk): R15M
  256/256, PGM-reuse 256/256, const-cells 256/256 (56).
- b5 cross-checked vs OWN census: {0xae:3, 0xaf:128,
  0xb0:125} — EXACT vs code: 0xae+(off>=3)+(off>=131).
  edges confirmed first-hand: 22399 ff/ae -> 22400 01/af
  (head-wrap form), 22527 ff/af -> 22528 01/b0.
- boundaries: 22396 still CLOSED T10PGQ off=63; 22653 out
  of scope rc=2. no neighbor breakage.

## code read
- _T10R15M 16-tab 6B (b36,37,60-63) + q-tab reuses _T10PGM
  (b33,34,68-71) + _T10R15C 56 consts + dispatch (paylen 72,
  lencode, b5 dbl-carry). consistent.
- for-list +8 cells, pins +16 rows append-only.
- diff pure addition: rgram +~20 lines, for-list edit,
  pins +16.

## verdict: PASS (T10R15 ->22652; 2786 pins)
