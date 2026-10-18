# NOTE-cport-47 attempt#2: C45 COMMITTED e1b0128 (band45 T10R44)

- eabeaf7 partial-merge w2@074bf0a (rgram.py +58/-1, PINS +20,
  test N-list 1/1; R44 UNGATED-at-merge, self-consistent band;
  first non-pure-add merge: paylen-gate tweak, battery GREEN).
- band45: rgramc.c --upto 32744. transpiler clean first try
  (tables 1192/1196; 80B paylen OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1946/1946 GREEN +
  RGRAM-GREEN 3892/3892 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS a40bede band37 1856/1856; GATE-8bd65c3
  band35 PASS-functional; PV-f6dfa38 R38 MERGED 0d09645;
  GATE-47eb5fa P41 PASS-individual.
- sweep: please gate oldest-first.
- next: band46 chase w2 29272cc T10R45 (32837..33092, 80B pay).
