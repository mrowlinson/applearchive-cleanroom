# VERIFY-c75c8e4 T10R14 16x16 22049..22304: PASS

## batteries (at-commit tree ver-c75c8e4, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (22049/22129/22143/22144/22257/22271/22272/22304 new +
  22048/22016 edge, all 88B).
- 256/256 FULL CLOSED at-commit rgram.py (every cell
  22049..22304, fresh oracle bytes each).
- tabs vs OWN census beds (c22049..c22304 on disk): R14M
  256/256, PFM-reuse 256/256, const-cells 256/256.
- b5 cross-checked vs OWN census: {0xac:95, 0xad:128,
  0xae:33} — EXACT vs code: 0xac+(off>=95)+(off>=223).
  edges confirmed first-hand: 22143 ac->22144 ad,
  22271 ad->22272 ae.
- boundaries: 22048 still CLOSED T10PFQ off=63; 22305 out
  of scope rc=2. no neighbor breakage.

## code read
- _T10R14M 16-tab 7B (b20-22,56-59) + q-tab reuses _T10PFM
  (b16,17,68-71) + _T10R14C consts + dispatch (paylen 72,
  lencode, b5 dbl-carry). consistent.
- for-list +8 cells, pins +16 rows append-only.
- diff pure addition: rgram +~20 lines, for-list edit,
  pins +16.

## verdict: PASS (T10R14 ->22304; 2750 pins)
