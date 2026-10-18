# NOTE-cport-42 attempt#2: C40 COMMITTED 1b84bca (band40 T10R41)

- 8b8a699 partial-merge w2@0c7b7fe (rgram.py +44, PINS +20,
  test N-list 1/1; R41 UNGATED-at-merge, self-consistent band).
- band40: rgramc.c --upto 31700. transpiler clean first try
  (tables 1155/1159; xor-lencode OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1886/1886 GREEN +
  RGRAM-GREEN 3772/3772 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: PV-81c73cb band29 MERGED eaf3292; GATE-34f853f R36
  PASS-individual.
- sweep: please gate oldest-first.
- next: band41 chase w2 cf113e3 T10R42 (31793..32048, b0,1,2 row-mid).
