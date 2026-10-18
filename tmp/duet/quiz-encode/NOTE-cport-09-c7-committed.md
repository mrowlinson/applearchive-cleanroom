# NOTE-cport-09 attempt#2: C7 COMMITTED 9d7d20c (band7 T10PM0..T10PMQ)

- f145c51 partial-merge w2@f949df5 (rgram.py +165, PINS +20,
  test N-list 1/1; P22 UNGATED-at-merge, self-consistent band).
- band7: rgramc.c --upto 24484. transpiler clean first try
  (tables 920/924).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1494/1494 GREEN +
  RGRAM-GREEN 2988/2988 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS band5 937c347 + band6 e64e2da; GATE-c12fcc6
  RED-tree same inherited cause / band3 PASS-individual.
- sweep: please gate oldest-first.
- next: band8 chase w2 f67973d T10R21 (24485..24740, q=PMM reuse).
