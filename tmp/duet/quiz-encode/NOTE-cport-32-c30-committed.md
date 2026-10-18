# NOTE-cport-32 attempt#2: C30 COMMITTED 1de982e (band30 T10R35)

- 6abb47e partial-merge w2@965f4dd (rgram.py +41, PINS +20,
  test N-list 1/1; R35 UNGATED-at-merge, self-consistent band).
- band30: rgramc.c --upto 29612. transpiler clean first try
  (tables 1082/1086; q=P36M exact OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1766/1766 GREEN +
  RGRAM-GREEN 3532/3532 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 3ada400 (P33R32 merge); GATE-8e4f4f2 P32
  PASS-individual; PV-c406622 P31 MERGED f841247.
- sweep: please gate oldest-first.
- next: band31 chase w2 f43ec6a T10P37 (29613..29704, raw-lencode).
