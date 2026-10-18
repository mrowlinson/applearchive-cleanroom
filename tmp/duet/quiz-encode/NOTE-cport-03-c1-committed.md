# NOTE-cport-03 attempt#1: C1 COMMITTED 0f57814 (band1 stored..T2)

- 0f57814 encode-cport band1: rgramc.{c,h} n<=511 (346 lines C, 3 tables)
  + Makefile rgramc target + RGRAM_BIN override (ENC_BIN pattern, default
  python unchanged) + committed tests/test_rgram_c.sh (parity harness).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 31/31 GREEN + RGRAM-GREEN
  2822/2822 (python default, 3m) + SMOKE-GREEN + UNITS-GREEN.
- sweep: please gate (oldest-first; lane tag encode-cport in msg).
- next: band2 n<=6040 (~T7, ~68 tiers).
