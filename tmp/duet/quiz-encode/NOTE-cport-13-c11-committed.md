# NOTE-cport-13 attempt#2: C11 COMMITTED a0adca4 (band11 T10PO0..T10POQ)

- e5a7484 partial-merge w2@875a127 (rgram.py +165, PINS +20,
  test N-list 1/1; P24 UNGATED-at-merge, self-consistent band).
- band11: rgramc.c --upto 25180. transpiler clean first try
  (tables 943/947).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1530/1530 GREEN +
  RGRAM-GREEN 3060/3060 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: sweep hb10 band6 gated (changes PASS-individual 327/327 +
  1484/1484 + storm 6/6); GATE-e64e2da RED-tree same cause.
- sweep: please gate oldest-first.
- next: band12 chase w2 d3afa19 T10R23 (25181..25436, m8/q6 NEW).
