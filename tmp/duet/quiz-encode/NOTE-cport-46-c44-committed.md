# NOTE-cport-46 attempt#2: C44 COMMITTED c693fdd (band44 T10P450..T10P45Q)

- 8ca0c31 partial-merge w2@ef80529 (rgram.py +205, PINS +20,
  test N-list 1/1; P45 UNGATED-at-merge, self-consistent band).
- band44: rgramc.c --upto 32488. transpiler clean first try
  (tables 1189/1193; single-head + q>=2-bit OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 1936/1936 GREEN +
  RGRAM-GREEN 3872/3872 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: VERIFY-PASS 497b4f4 R40; PV-35d6de7 P39 MERGED 7c97bd7.
- sweep: please gate oldest-first.
- next: band45 chase w2 074bf0a T10R44 (32489..32744, first 80B tier).
