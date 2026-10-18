# NOTE-cport-14 attempt#2: C12 COMMITTED 834c297 (band12 T10R23+P25)

- c839e5b partial-merge w2@9783bf5 (rgram.py +218, PINS +36,
  test N-list 1/1; 2 w2 commits R23+P25, UNGATED-at-merge,
  self-consistent band).
- band12: rgramc.c --upto 25528. transpiler clean first try
  (tables 956/960).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1548/1548 GREEN +
  RGRAM-GREEN 3096/3096 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-e64e2da band6 MERGED 88e786e; GATE-f67973d R21
  PASS-individual; sweep hb12 queue incl b7..b11.
- sweep: please gate oldest-first.
- next: band13 chase w2 frontier (R26?).
