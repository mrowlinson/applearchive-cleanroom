# VERIFY-9126bc1 T10P12 head 20913..20940 + PCQ 20941..21004: PASS

## batteries (at-commit tree ver-9126bc1, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (20913/20914/20915/20930/20931/20940/20941/20991/20992/21004,
  all 88B).
- 92/92 FULL-HEAD CLOSED at-commit rgram.py (every cell
  20913..21004, fresh oracle bytes each).
- b5 cross-checked vs OWN census beds (c20941..c21004 on disk):
  q0/q1 = 23, q2 = a3, q3 m<3 = 23 else 24 — w2 NOTE-w2s10-4
  claim EXACT; code `_T10PCQ5[q] - (q==3 and m<3)` implements it.
- boundaries: 20912 still CLOSED T10R10 off=255; 21005 out of
  scope rc=2. no neighbor breakage.

## code read vs NOTE-w2s10-4
- PC0/PC1 singletons + PCA 7B [5,6,7,56..59] + PCB 10B
  [5..10,68..71] + PCQ 4x16 (m-tab 7B [0,1,11,68..71] +
  q-tab 9B [6..10,64..67]): structure = derived claim.
- for-list +10 cells incl 20991/20992 b5 edge pair (q3 m2/m3:
  23->24 flip) + quad corners. pins +20 rows.
- diff pure addition: rgram +167, for-list edit, pins +20.

## verdict: PASS (T10P12 ->21004; 2622 pins)
