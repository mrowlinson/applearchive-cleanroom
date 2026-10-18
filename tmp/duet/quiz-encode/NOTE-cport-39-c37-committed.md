# NOTE-cport-39 attempt#2: C37 COMMITTED a40bede (band37 T10R39+P41)

- 5918420 partial-merge w2@47eb5fa (rgram.py +242, PINS +40,
  test N-list 1/1; 2 w2 commits R39+P41, UNGATED-at-merge,
  self-consistent band).
- band37: rgramc.c --upto 31096. transpiler clean first try
  (tables 1140/1144; b5-mbit OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1856/1856 GREEN +
  RGRAM-GREEN 3712/3712 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-c108d1e P36 PASS-individual; PV-b490c4e R34 MERGED
  6c064dc.
- sweep: please gate oldest-first.
- next: band38 chase w2 497b4f4 T10R40 (31097..31352, b5-qbit).
