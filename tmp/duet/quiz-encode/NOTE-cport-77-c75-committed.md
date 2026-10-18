# NOTE-cport-77 attempt#2: C75 COMMITTED f563e5f (band75 T10R65+P67)

- 97e5ee8 partial-merge w2@1030015 (rgram.py +214, PINS +46,
  test N-list 1/1; 2 w2 commits R65+P67, UNGATED-at-merge,
  self-consistent band).
- band75: rgramc.c --upto 40080. transpiler clean first try
  (tables 1441/1445). crosses n=40000.
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2385/2385 GREEN +
  RGRAM-GREEN 4770/4770 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate oldest-first.
- next: chase w2 tip beyond 1030015.
