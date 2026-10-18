# NOTE-cport-28 attempt#2: C26 COMMITTED 6325c15 (band26 T10PY0..T10PYQ)

- c440e04 partial-merge w2@0f16b53 (rgram.py +198, PINS +20,
  test N-list 1/1; P34 UNGATED-at-merge, self-consistent band).
- band26: rgramc.c --upto 28660. transpiler clean first try
  (tables 1058/1062).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1716/1716 GREEN +
  RGRAM-GREEN 3432/3432 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 4104b6a (P31 merge); PV-4ad7a4d band16
  MERGED 4bcefa6.
- sweep: please gate oldest-first.
- next: band27 chase w2 2c07079 T10R33 (28661..28916, q=PYM exact).
