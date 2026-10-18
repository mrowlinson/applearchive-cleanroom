# NOTE-cport-38 attempt#2: C36 COMMITTED 8fa0d10 (band36 T10P400..T10P40Q)

- 0303b7a partial-merge w2@55dcb98 (rgram.py +198, PINS +20,
  test N-list 1/1; P40 UNGATED-at-merge, self-consistent band).
- band36: rgramc.c --upto 30748. transpiler clean first try
  (tables 1129/1133; xor-lencode OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1836/1836 GREEN +
  RGRAM-GREEN 3672/3672 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 1de982e band30 1766/1766; GATE-c2fdbce
  band27 PASS-functional; GATE-b490c4e R34 PASS-individual.
- sweep: please gate oldest-first.
- next: band37 chase w2 0cda438 T10R39 (30749..31004, q=P40M exact).
