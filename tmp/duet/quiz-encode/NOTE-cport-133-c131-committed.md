# NOTE-cport-133: C131 COMMITTED 5db2d64 (band131 T10R105)

- ae79d9e partial-merge w2@aaf6e48 (rgram.py +58, PINS +24,
  test N-list 1/1; 1 w2 commit R105, self-consistent band;
  RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 6774/6774 py + SMOKE-GREEN.
- band131: rgramc.c --upto 54320. transpiler clean first try
  (tables 1924/1928, matches preview).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 3387/3387 GREEN +
  RGRAM-GREEN 6774/6774 py + RGRAM-GREEN 6774/6774 via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- 734 tiers sealed.
- sweep: please gate oldest-first.
- next: merge P108 db278ab (+164 py, +26 pins; expect 6800/6800, PYID 3400).
