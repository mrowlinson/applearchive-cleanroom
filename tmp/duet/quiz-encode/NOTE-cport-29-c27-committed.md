# NOTE-cport-29 attempt#2: C27 COMMITTED c2fdbce (band27 T10R33+P35)

- 59cbad2 partial-merge w2@3dd5f7b (rgram.py +239, PINS +40,
  test N-list 1/1; 2 w2 commits R33+P35, UNGATED-at-merge,
  self-consistent band).
- band27: rgramc.c --upto 29008. transpiler clean first try
  (tables 1069/1073).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1736/1736 GREEN +
  RGRAM-GREEN 3472/3472 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS f1ffe3c (R30 merge); PV-305959d P29 MERGED
  0ecfe43; VERIFY-PASS 1912c73 R31 256/256.
- sweep: please gate oldest-first.
- next: band28 chase w2 b490c4e T10R34 (29009..29264, q=PZM exact).
