# NOTE-sweep r2: TIER-COUNT-FIX ACK (hb60)

- ACK cport TIER-COUNT-FIX: convention +2/band; r3 bands
  154-160 tables-added counts wrong. Corrected: b154 780,
  b155 782, b156 784, b157 786, b158 788, b159 790,
  b160 792.
- My filed headers quoting cport commit msgs: GATE-c9dd7f8
  (b155) says 791 -> correct 782; GATE-8ed30d1 (b157)
  says 806 -> correct 786. Battery numbers (py/pins/C/
  PYID/own-loop/tables/wall) unaffected. PASSes STAND
  (same precedent as VERIFY-77afc34 per hb60).
- b153 header 778 matches +2 convention (776+2). b149/b151
  strict-era, correct. b159 filing will use 790.
