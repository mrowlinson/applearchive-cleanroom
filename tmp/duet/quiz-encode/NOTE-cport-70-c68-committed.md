# NOTE-cport-70 attempt#2: C68 COMMITTED cac2faf (band68 T10R60+P62)

- 57108c8 partial-merge w2@3917ba1 (rgram.py +211, PINS +40,
  test N-list 1/1; 2 w2 commits R60+P62, UNGATED-at-merge,
  self-consistent band).
- band68: rgramc.c --upto 38340. transpiler clean first try
  (tables 1384/1388).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2276/2276 GREEN +
  RGRAM-GREEN 4552/4552 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 3917ba1.
