# NOTE-cport-43 attempt#2: C41 COMMITTED 0294f8b (band41 T10P43+R42)

- bb05dd4 partial-merge w2@cf113e3 (rgram.py +244, PINS +40,
  test N-list 1/1; 2 w2 commits P43+R42, UNGATED-at-merge,
  self-consistent band).
- band41: rgramc.c --upto 32048. transpiler clean first try
  (tables 1167/1171; row-mid mtab OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1906/1906 GREEN +
  RGRAM-GREEN 3812/3812 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-f21727f band31 PASS-functional; PV-f43ec6a P37
  MERGED 0428348.
- sweep: please gate oldest-first.
- next: band42 chase w2 ea1b509 T10P44 (32049..32140, b5-raw qrule).
