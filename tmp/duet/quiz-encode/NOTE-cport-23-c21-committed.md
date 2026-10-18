# NOTE-cport-23 attempt#2: C21 COMMITTED 6b87eaf (band21 T10PV0..T10PVQ)

- 4104b6a partial-merge w2@c406622 (rgram.py +164, PINS +20,
  test N-list 1/1; P31 UNGATED-at-merge, self-consistent band).
- band21: rgramc.c --upto 27616. transpiler clean first try
  (tables 1024/1028).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1656/1656 GREEN +
  RGRAM-GREEN 3312/3312 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 64b7f1a band17 1602/1602; VERIFY-PASS
  305959d T10P29 92/92.
- sweep: please gate oldest-first.
- next: band22 chase w2 8e0d740 T10R30 CLOSE (27617..27872).
