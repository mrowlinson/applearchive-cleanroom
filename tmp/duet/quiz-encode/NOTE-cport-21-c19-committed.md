# NOTE-cport-21 attempt#2: C19 COMMITTED a55b78c (band19 T10R28)

- fd60f19 partial-merge w2@4c5b869 (rgram.py +42, PINS +16,
  test N-list 1/1; R28 UNGATED-at-merge, self-consistent band).
- band19: rgramc.c --upto 27176. transpiler clean first try
  (tables 1003/1007).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1628/1628 GREEN +
  RGRAM-GREEN 3256/3256 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 55494eb band15 1584/1584; PV-1821f18 R24
  MERGED 6f5d55e.
- sweep: please gate oldest-first.
- next: band20 chase w2 5874e49 T10P30 (27177..27268).
