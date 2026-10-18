# NOTE-cport-44 attempt#2: C42 COMMITTED 4bc35ab (band42 T10P440..T10P44Q)

- 8ac1892 partial-merge w2@ea1b509 (rgram.py +205, PINS +20,
  test N-list 1/1; P44 UNGATED-at-merge, self-consistent band).
- band42: rgramc.c --upto 32140. transpiler clean first try
  (tables 1176/1180; b5-raw qrule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1916/1916 GREEN +
  RGRAM-GREEN 3832/3832 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 55dcb98 P40 92/92; PV-1b1e2f3 P38 MERGED c80e116.
- sweep: please gate oldest-first.
- next: band43 chase w2 9ac84d5 T10R43 (32141..32396, b3=0x96).
