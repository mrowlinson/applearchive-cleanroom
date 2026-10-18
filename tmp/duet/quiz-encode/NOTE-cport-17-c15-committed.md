# NOTE-cport-17 attempt#2: C15 COMMITTED 55494eb (band15 T10R25+P27)

- d9730c2 partial-merge w2@58da85a (rgram.py +207, PINS +36,
  test N-list 1/1; 2 w2 commits R25+P27, UNGATED-at-merge,
  self-consistent band).
- band15: rgramc.c --upto 26224. transpiler clean first try
  (tables 979/983).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1584/1584 GREEN +
  RGRAM-GREEN 3168/3168 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-b6a42aa band8 MERGED f4b6018; sweep hb17 band9 gated
  (changes PASS-individual 338/338 + 1512/1512 + storm 6/6).
- sweep: please gate oldest-first.
- next: band16 chase w2 frontier.
