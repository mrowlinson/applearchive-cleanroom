# NOTE-cport-100: C98 COMMITTED dfdf9d6 (band98 T10P87+T10R86)

- 2ed27ea partial-merge w2@27712a9 (rgram.py +225, PINS +46,
  test N-list 1/1; 2 w2 commits P87+R86, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5716/5716 py + SMOKE-GREEN.
- band98: rgramc.c --upto 47360. transpiler clean first try
  (tables 1674/1678; R86 row-b18 BASE+(q==0) handled).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2858/2858 GREEN +
  RGRAM-GREEN 5716/5716 py (merge tree, same-tree) +
  RGRAM-GREEN 5716/5716 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 654 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P88 ecfbde8 + R87 when committed).
