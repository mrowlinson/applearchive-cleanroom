# VERIFY-55fcd0d T10R13 16x16 21701..21956: PASS

## batteries (at-commit tree ver-55fcd0d, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (21701/21702/21709/21750/21759/21760/21885/21887/21888/
  21956, all 88B).
- 256/256 FULL-RANGE CLOSED at-commit rgram.py (every cell
  21701..21956, fresh oracle bytes each).
- q-tab == _T10PEM 256/256 vs OWN census beds (c21701..c21956
  on disk); m-tab == _T10R13M 256/256. identity confirmed.
- b5 cross-checked vs OWN census: {0x29:43, 0xA9:16, 0x2a:96,
  0xAA:32, 0x2b:53, 0xAB:16} — EXACT vs code structure:
  base 29x64/2ax128/2bx64, flips q3/q11 m11-15 (+5/-5/+5),
  spikes m-(1,2,3,8)|0x80 (16/32/16). flip+spike disjoint.
- boundaries: 21700 still CLOSED T10PEQ off=63; 21957 out
  of scope rc=2. no neighbor breakage.

## code read
- _T10R13M 16-tab (b6,7,48-51) + _T10R13B5 base + _T10R13C
  58 consts + dispatch (paylen + lencode + b5 flip/spike +
  mtab + qtab=PEM + consts). structure consistent.
- for-list +10 cells (spike/flip edges both rows + corners).
  pins +20 rows. diff pure addition: rgram +47, for-list
  edit, pins +20.

## verdict: PASS (T10R13 ->21956; 2714 pins)
