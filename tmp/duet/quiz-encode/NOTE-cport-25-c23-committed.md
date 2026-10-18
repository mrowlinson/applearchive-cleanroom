# NOTE-cport-25 attempt#2: C23 COMMITTED 336a303 (band23 T10PW0..T10PWQ)

- 4d27cf1 partial-merge w2@8e4f4f2 (rgram.py +198, PINS +20,
  test N-list 1/1; P32 UNGATED-at-merge, self-consistent band).
- band23: rgramc.c --upto 27964. transpiler clean first try
  (tables 1036/1040).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1676/1676 GREEN +
  RGRAM-GREEN 3352/3352 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS fd60f19 (R28 merge); sweep hb31 band15 gated
  PASS-functional no FLAG; PV-11cfc70 R25 MERGED 183b0db.
- sweep: please gate oldest-first.
- next: band24 chase w2 1912c73 T10R31 CLOSE (27965..28220).
