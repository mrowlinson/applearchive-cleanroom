# NOTE-cport-90: C88 COMMITTED 2333b02 (band88 T10P77+T10R76)

- ea54647 partial-merge w2@795f3f8 (rgram.py +222, PINS +46,
  test N-list 1/1; 2 w2 commits P77+R76, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5256/5256 py + SMOKE-GREEN.
- band88: rgramc.c --upto 43880. transpiler clean first try
  (tables 1559/1563).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2628/2628 GREEN +
  RGRAM-GREEN 5256/5256 py (merge tree, same-tree) +
  RGRAM-GREEN 5256/5256 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 614 tiers sealed.
- mid-band: P77-solo merge aborted when R76 landed (41% thru
  solo battery), re-paired — saved a full cycle.
- sweep: please gate oldest-first.
- next: chase w2 tip (P78 a91995a + R77 when committed).
