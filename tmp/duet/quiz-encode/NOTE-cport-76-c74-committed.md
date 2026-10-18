# NOTE-cport-76 attempt#2: C74 COMMITTED 2a2f2b7 (band74 T10P66)

- bee28c5 partial-merge w2@3682200 (rgram.py +104, PINS +20,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band74: rgramc.c --upto 39732. transpiler clean first try
  (tables 1430/1434).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2362/2362 GREEN +
  RGRAM-GREEN 4724/4724 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS d22cdc1 merge60; VERIFY-PASS 9224481
  cport band65.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 3682200.
