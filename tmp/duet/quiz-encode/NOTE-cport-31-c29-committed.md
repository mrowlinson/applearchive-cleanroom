# NOTE-cport-31 attempt#2: C29 COMMITTED 81c73cb (band29 T10P360..T10P36Q)

- a2070eb partial-merge w2@c108d1e (rgram.py +202, PINS +20,
  test N-list 1/1; P36 UNGATED-at-merge, self-consistent band).
- band29: rgramc.c --upto 29356. transpiler clean first try
  (tables 1080/1084; numeric P36 names OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1756/1756 GREEN +
  RGRAM-GREEN 3512/3512 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS b689490 R32 256/256; PV-004a2c2 R29 MERGED
  9e6285b.
- sweep: please gate oldest-first.
- next: band30 chase w2 965f4dd T10R35 (29357..29612, q=P36M exact).
