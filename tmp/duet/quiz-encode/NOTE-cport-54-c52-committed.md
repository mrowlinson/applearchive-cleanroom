# NOTE-cport-54 attempt#2: C52 COMMITTED d840c7b (band52 T10P500..T10P50B)

- 75a3946 partial-merge w2@94927a9 (rgram.py +143, PINS +20,
  test N-list 1/1; P50 UNGATED-at-merge, self-consistent band;
  no-Q head shape).
- band52: rgramc.c --upto 34164. transpiler clean first try
  (tables 1246/1250). 500-TIER MILESTONE.
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2036/2036 GREEN +
  RGRAM-GREEN 4072/4072 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 8ca0c31 (P45 merge); VERIFY-PASS 0fb3ec8
  P47; GATE-9ac84d5 R43 PASS-individual.
- sweep: please gate oldest-first.
- next: band53 chase w2 b568b7a T10R49 (34165..34484, A+B 80B).
