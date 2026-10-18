# NOTE-cport-45 attempt#2: C43 COMMITTED 7c75537 (band43 T10R43)

- 1a0cab6 partial-merge w2@9ac84d5 (rgram.py +53, PINS +20,
  test N-list 1/1; R43 UNGATED-at-merge, self-consistent band).
- band43: rgramc.c --upto 32396. transpiler clean first try
  (tables 1178/1182; b3-rule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1926/1926 GREEN +
  RGRAM-GREEN 3852/3852 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 0cda438 R39 256/256; PV-1de982e band30
  MERGED c26589c.
- sweep: please gate oldest-first.
- next: band44 chase w2 ef80529 T10P45 (32397..32488, single-head).
