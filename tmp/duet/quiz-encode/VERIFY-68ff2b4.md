# VERIFY-68ff2b4 T10R10 16x16 20657..20912: PASS

## batteries (at-commit tree ver-68ff2b4, WS tmp/encode-viewer)
- 6/6 new-pin shas MATCH independent oracle re-runs
  (20657/20721/20736/20849/20864/20912, all 88B).
- 256/256 FULL-ZONE CLOSED at-commit rgram.py (every cell
  20657..20912, fresh oracle bytes each).
- b5 first-hand per q row (m0/m14/m15): base ramp q0..q4 a1,
  q5..q12 a2, q13..q15 a3 + carry +1 ONLY at (q4,m15)->a2 and
  (q12,m15)->a3. commit rule EXACT.
- boundaries: 20656 still CLOSED T10PBQ off=63; 20913 out of
  scope rc=2. no neighbor breakage.

## code read vs PRE-1106b
- geometry 16x16 m=off&15 q=off>>4, m-tab 7B
  [45,46,47,64,65,66,67] NEW 16/16, const-set incl b68-71:
  oracle-confirmed via 256/256.
- q-tab: commit checks 7B [40,41,42,60,61,62,63] vs _T10PBM.
  CORRECTION to PRE-1106b ("byte2 dropped"): pay42 varies per q
  (8f q0..8, 9f q9..15) and EQUALS PBM byte2 per row 16/16 —
  7B reuse is correct, PRE framing was conservative.
- b5 base+carry: PRE said q-pure ramp; commit's q4/q12 m15-carry
  confirmed first-hand above (extends PRE, no conflict).
- diff pure addition: rgram +44 branch+tables, for-list +6 cells
  (incl both carry edges 20736/20864), pins +12 rows.

## verdict: PASS (T10R10 ->20912; 2602 pins)
