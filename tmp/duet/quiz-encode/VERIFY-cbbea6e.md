# VERIFY-cbbea6e T10R11 16x16 21005..21260: PASS

## batteries (at-commit tree ver-cbbea6e, WS tmp/encode-viewer)
- 8/8 new-pin shas MATCH independent oracle re-runs
  (21005/21117/21119/21120/21245/21247/21248/21260, all 88B).
- 256/256 FULL-ZONE CLOSED at-commit rgram.py (every cell
  21005..21260, fresh oracle bytes each).
- b5 first-hand per q row: base 24 q0..q7, 25 q8..q15 +
  carry +1 ONLY at (q7,m>=3) and (q15,m>=3).
  code `0x24+(q>>3)+(q in (7,15) and m>=3)` EXACT.
- boundaries: 21004 still CLOSED T10PCQ off=63; 21261 out of
  scope rc=2. no neighbor breakage.

## code read
- m-tab 6B [16,17,68..71] NEW + q-tab 7B [0,1,11,64..67]
  reuses _T10PCM (commit claim; 256/256 CLOSED confirms).
- for-list +8 cells incl both carry-edge triples (21117/21119/
  21120 = q7 m0/m2/m3; 21245/21247/21248 = q15 m0/m2/m3 —
  each straddles its m2->m3 flip). pins +16 rows.
- diff pure addition: rgram +42, for-list edit, pins +16.

## verdict: PASS (T10R11 ->21260; 2638 pins)
