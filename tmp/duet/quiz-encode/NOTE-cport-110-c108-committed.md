# NOTE-cport-110: C108 COMMITTED f8fe14f (band108 T10P95)

- 8da55b7 partial-merge w2@7cacebb (rgram.py +182, PINS +22,
  test N-list 1/1; 1 w2 commit P95, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6134/6134 py + SMOKE-GREEN.
- band108: rgramc.c --upto 49888. transpiler clean first try
  (tables 1772/1776).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3067/3067 GREEN +
  RGRAM-GREEN 6134/6134 py (merge tree, same-tree) +
  RGRAM-GREEN 6134/6134 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 684 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (R93 next; == w2 tip now).
