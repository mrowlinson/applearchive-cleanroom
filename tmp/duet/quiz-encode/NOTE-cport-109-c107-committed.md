# NOTE-cport-109: C107 COMMITTED ee6b913 (band107 T10R92)

- 8a131dc partial-merge w2@8438a5f (rgram.py +55/-1 paylen
  gate +84, PINS +26, test N-list 1/1; 1 w2 commit R92,
  UNGATED-at-merge, self-consistent band; RGRAM_BIN kept).
- merge gate first-hand: RGRAM-GREEN 6112/6112 py + SMOKE-GREEN.
- band107: rgramc.c --upto 49796. transpiler clean first try
  (tables 1761/1765).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3056/3056 GREEN +
  RGRAM-GREEN 6112/6112 py (merge tree, same-tree) +
  RGRAM-GREEN 6112/6112 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 682 tiers sealed.
- sweep: please gate oldest-first.
- next: chase w2 tip (P95 next; == w2 tip now).
