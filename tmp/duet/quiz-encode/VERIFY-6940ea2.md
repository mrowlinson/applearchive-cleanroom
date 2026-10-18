# VERIFY-6940ea2 T10P15 head 21957..21984 + PFQ 21985..22048: PASS

## batteries (at-commit tree ver-6940ea2, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (21957/21958/21959/21974/21975/21984/21985/22015/22016/
  22048, all 88B).
- 92/92 FULL-HEAD CLOSED at-commit rgram.py (every cell
  21957..22048, fresh oracle bytes each).
- tabs vs OWN census beds (c21957..c22048 on disk): PFM
  64/64, PFQ 64/64, PFA 16/16, PFB 10/10. all confirmed.
- b5 cross-checked vs OWN census: {0x2b:1, 0xab:58, 0xac:33}
  — EXACT vs code: PF0 0x2b (21957) + PF1/PFA/PFB const
  0xab (27) + PFQ 0xab+(off>=31) (31/33). edge off=30/31
  (22015 b5=ab -> 22016 b5=ac) confirmed first-hand.
- boundaries: 21956 still CLOSED T10R13 off=255; 22049 out
  of scope rc=2. no neighbor breakage.

## code read
- PF0+PF1 singletons + PFA 16-tab (b0,11,64-67) + PFB 10-tab
  (b0,1,11-13,68-71) + PFQ 4x16 (m-tab b16,17,68-71 + q-tab
  b0,1,11-13,64-67) + const tables + dispatch. consistent.
- for-list +10 cells (head corners + PFA/PFB edges + quad
  edges 22015/22016 + corners). pins +20 rows.
- diff pure addition: rgram +166, for-list edit, pins +20.

## verdict: PASS (T10P15 ->22048; 2734 pins)
