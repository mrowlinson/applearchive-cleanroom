# NOTE-cport-30 attempt#2: C28 COMMITTED 0d8c629 (band28 T10R34)

- 1050d3d partial-merge w2@b490c4e (rgram.py +41, PINS +20,
  test N-list 1/1; R34 UNGATED-at-merge, self-consistent band).
- band28: rgramc.c --upto 29264. transpiler clean first try
  (tables 1071/1075; q=PZM exact OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1746/1746 GREEN +
  RGRAM-GREEN 3492/3492 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-696bb26 band20 PASS-functional 1646/1646 + storm 6/6;
  GATE-c406622 P31 PASS-individual; PV-4c5b869 R28 MERGED ecb3bde.
- sweep: please gate oldest-first.
- next: band29 chase w2 c108d1e T10P36 (29265..29356, numeric names).
