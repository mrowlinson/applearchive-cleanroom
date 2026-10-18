# NOTE-cport-26 attempt#2: C24 COMMITTED 9f87a07 (band24 T10R31)

- 3dc2720 partial-merge w2@1912c73 (rgram.py +41, PINS +20,
  test N-list 1/1; R31 UNGATED-at-merge, self-consistent band).
- band24: rgramc.c --upto 28220. transpiler clean first try
  (tables 1038/1042; q=PWM exact OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1686/1686 GREEN +
  RGRAM-GREEN 3372/3372 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS a55b78c band19 1628/1628; PV-ff3ef8a band14
  MERGED 3caa309.
- sweep: please gate oldest-first.
- next: band25 chase w2 8da8428 T10P33 (28221..28312, b5-mbit).
