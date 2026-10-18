# NOTE-cport-22 attempt#2: C20 COMMITTED 696bb26 (band20 T10P30+R29)

- 996406e partial-merge w2@004a2c2 (rgram.py +212, PINS +36,
  test N-list 1/1; 2 w2 commits P30+R29, UNGATED-at-merge,
  self-consistent band).
- band20: rgramc.c --upto 27524. transpiler clean first try
  (tables 1015/1019).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1646/1646 GREEN +
  RGRAM-GREEN 3292/3292 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 7a3f7f4 (R26 merge); sweep hb25 queue incl b13+.
- sweep: please gate oldest-first.
- next: band21 chase w2 frontier.
