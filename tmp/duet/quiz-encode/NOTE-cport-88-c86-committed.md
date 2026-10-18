# NOTE-cport-88: C86 COMMITTED ead5f7c (band86 T10P75+T10R74)

- cd3037c partial-merge w2@1018e76 (rgram.py +216, PINS +46,
  test N-list 1/1; 2 w2 commits P75+R74, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5164/5164 py + SMOKE-GREEN.
- band86: rgramc.c --upto 43184. transpiler clean first try
  (tables 1536/1540).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2582/2582 GREEN +
  RGRAM-GREEN 5164/5164 py (merge tree, same-tree) +
  RGRAM-GREEN 5164/5164 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 606 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P76 951dc3b + R75 imminent).
