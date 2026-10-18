# NOTE-cport-40 attempt#2: C38 COMMITTED ab69b45 (band38 T10R40)

- ebd77e1 partial-merge w2@497b4f4 (rgram.py +43, PINS +20,
  test N-list 1/1; R40 UNGATED-at-merge, self-consistent band).
- band38: rgramc.c --upto 31352. transpiler clean first try
  (tables 1142/1146; b5-qbit OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1866/1866 GREEN +
  RGRAM-GREEN 3732/3732 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS f21727f band31 1776/1776; VERIFY-PASS
  1b1e2f3 P38 92/92; GATE-81c73cb band29 PASS-functional;
  PV-c108d1e P36 MERGED 33e2c49.
- sweep: please gate oldest-first.
- next: band39 chase w2 a0e16b3 T10P42 (31353..31444, b21-rule).
