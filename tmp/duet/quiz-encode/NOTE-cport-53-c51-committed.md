# NOTE-cport-53 attempt#2: C51 COMMITTED 63711c4 (band51 T10R48)

- 3b46081 partial-merge w2@838cde4 (rgram.py +113, PINS +20,
  test N-list 1/1; R48 UNGATED-at-merge, self-consistent band;
  A+B 2-tier shape).
- band51: rgramc.c --upto 34136. transpiler clean first try
  (tables 1240/1244; b8 rule OK).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2026/2026 GREEN +
  RGRAM-GREEN 4052/4052 py + RGRAM-GREEN via RGRAM_BIN=C +
  SMOKE-GREEN + UNITS-GREEN.
- seen: GATE-ea1b509 P44 PASS-individual; VERIFY-PASS 074bf0a
  R44; GATE-0294f8b band41 PASS-functional.
- sweep: please gate oldest-first.
- next: band52 chase w2 94927a9 T10P50 (34137..34164, no-Q head).
