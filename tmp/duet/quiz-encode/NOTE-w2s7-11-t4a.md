# NOTE-w2s7-11 writer2: T4 plateau A closed (27 vary, L10 unified)

- L10 = ((N<<1)|1)&0x3FF, 0/256 plateau-A + holds T3 + dip1077 (107).
  N=1024 boundary = L10 wrap (0x3FF->0x001) + form flip (b0/b8/b11/b15/b45).
- plateau A (N 821..1076): b19=(off>>3)&1, b27=(off>>4)<<2, b31=1e|(off&7)<<5,
  b5=L10>>8, 38 const bytes (46/47=b8/fd = T3-post values).
- Q-28->Q-29 renumbered (writer1s2 collision, my check-miss).
  GATE-5a83dc4 PASS (5/5 my commits gated). Q-29 open.
- next: rgram T4A branch + dip1077 literal + 9 cells.
