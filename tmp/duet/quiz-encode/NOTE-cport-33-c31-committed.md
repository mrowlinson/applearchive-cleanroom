# NOTE-cport-33 attempt#2: C31 COMMITTED f21727f (band31 T10P370..T10P37Q)

- 0fe7615 partial-merge w2@f43ec6a (rgram.py +198, PINS +20,
  test N-list 1/1; P37 UNGATED-at-merge, self-consistent band).
- band31: rgramc.c --upto 29704. transpiler clean first try
  (tables 1091/1095; raw-lencode OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1776/1776 GREEN +
  RGRAM-GREEN 3552/3552 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS d3247df band25 1706/1706; PV-8e0d740 R30
  MERGED ebbf0f7.
- sweep: please gate oldest-first.
- next: band32 chase w2 1b1e2f3 T10P38 (29961..30052, b29-rule).
