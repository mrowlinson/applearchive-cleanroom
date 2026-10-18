# NOTE-cport-55 attempt#2: C53 COMMITTED f15455c (band53 T10R49+P51)

- 030c1e5 partial-merge w2@cc646bf (rgram.py +258, PINS +40,
  test N-list 1/1; 2 w2 commits R49+P51, UNGATED-at-merge,
  self-consistent band).
- band53: rgramc.c --upto 34512. transpiler clean first try
  (tables 1258/1262).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2056/2056 GREEN +
  RGRAM-GREEN 4112/4112 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-ef80529 P45 PASS-individual; GATE-7c75537 band43
  PASS-functional; VERIFY-PASS 0dfef7a R47.
- sweep: please gate oldest-first.
- next: band54 chase w2 b8230b7 T10R50 (34513..34832, b40 rule).
