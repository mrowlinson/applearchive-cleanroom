# VERIFY-30a6964 T10P13 head 21261..21288 + PDQ 21289..21352: PASS

## batteries (at-commit tree ver-30a6964, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (21261/21262/21263/21278/21279/21288/21289/21304/21305/21352,
  all 88B).
- 92/92 FULL-HEAD CLOSED at-commit rgram.py (every cell
  21261..21352, fresh oracle bytes each).
- b5 cross-checked vs OWN census beds (c21261..c21352 on disk):
  0x26 CONST all 92 cells (head + all 4 quad rows) — code's
  const-table treatment (no b5 rule) is correct.
- boundaries: 21260 still CLOSED T10R11 off=255; 21353 out of
  scope rc=2. no neighbor breakage.

## code read
- PD0/PD1 singletons + PDA 7B [21,22,23,60..63] + PDB 9B
  [24..28,64..67] + PDQ 4x16 (m-tab 6B [29,30,68..71] +
  q-tab 8B [24..27,64..67]). structure consistent.
- for-list +10 cells (head corners + quad edges 21304/21305 +
  corners). pins +20 rows.
- diff pure addition: rgram +164, for-list edit, pins +20.

## verdict: PASS (T10P13 ->21352; 2658 pins)
