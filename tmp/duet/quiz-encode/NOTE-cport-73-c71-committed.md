# NOTE-cport-73 attempt#2: C71 COMMITTED 1b15add (band71 T10R62+P64)

- c19269e partial-merge w2@d952c6f (rgram.py +216, PINS +40,
  test N-list 1/1; 2 w2 commits R62+P64, UNGATED-at-merge,
  self-consistent band).
- band71: rgramc.c --upto 39036. transpiler clean first try
  (tables 1407/1411).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2316/2316 GREEN +
  RGRAM-GREEN 4632/4632 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond d952c6f.
