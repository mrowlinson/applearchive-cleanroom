# NOTE-cport-79 attempt#2: C77 COMMITTED cc81d7f (band77 T10R67)

- 7d2affe partial-merge w2@c55aa3c (rgram.py +110, PINS +26,
  test N-list 1/1; UNGATED-at-merge, self-consistent band).
- band77: rgramc.c --upto 40748. transpiler clean first try
  (tables 1457/1461).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2421/2421 GREEN +
  RGRAM-GREEN 4842/4842 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 1b15add cport band71.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond c55aa3c.
