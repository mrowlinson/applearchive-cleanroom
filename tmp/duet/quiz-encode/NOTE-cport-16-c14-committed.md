# NOTE-cport-16 attempt#2: C14 COMMITTED ff3ef8a (band14 T10PQ0..T10PQQ)

- f3d0773 partial-merge w2@4b30e1e (rgram.py +167, PINS +20,
  test N-list 1/1; P26 UNGATED-at-merge, self-consistent band).
- band14: rgramc.c --upto 25876. transpiler clean first try
  (tables 968/972).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1566/1566 GREEN +
  RGRAM-GREEN 3132/3132 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: sweep hb15 band8 gated (changes PASS-individual 333/333 +
  1502/1502 + storm 6/6).
- sweep: please gate oldest-first.
- next: band15 chase w2 11cfc70 T10R25 (25877..26132, q=PQM reuse).
