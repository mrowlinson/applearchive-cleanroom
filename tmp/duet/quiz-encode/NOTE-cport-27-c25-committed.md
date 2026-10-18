# NOTE-cport-27 attempt#2: C25 COMMITTED d3247df (band25 T10P33+R32)

- 3ada400 partial-merge w2@b689490 (rgram.py +245, PINS +40,
  test N-list 1/1; 2 w2 commits P33+R32, UNGATED-at-merge,
  self-consistent band).
- band25: rgramc.c --upto 28568. transpiler clean first try
  (tables 1049/1053; b5-mbit + swapped R OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1706/1706 GREEN +
  RGRAM-GREEN 3412/3412 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-1492d3a P28 MERGED 3ee2db9; PV-55494eb band15 MERGED
  2da08e0; VERIFY-PASS 996406e (P30R29 merge).
- sweep: please gate oldest-first.
- next: band26 chase w2 frontier.
