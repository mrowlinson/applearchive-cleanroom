# NOTE-cport-07 attempt#2: C5 COMMITTED 937c347 (band5 T10PI0..T10R19)

- 920e187 partial-merge master@91a852c (rgram.py +643, PINS +110,
  test_rgram.sh N-list 1/1; merged test kept: RGRAM_BIN intact + new
  cells thru 24044; caught lane battery would have skipped new N).
- 937c347 band5: rgramc.c --upto 24044 (37667 lines, +2143).
  transpiler clean first try (tables 898/902, IfExp OK).
- gates first-hand: C-BUILD 0w (make + direct cc) + RGRAMC-PYID
  1466/1466 GREEN (committed harness, full cover) + RGRAM-GREEN
  2932/2932 py + RGRAM-GREEN via RGRAM_BIN=C + SMOKE-GREEN +
  UNITS-GREEN. spot 7/7 SAME on new tier boundaries.
- seen: VERIFY-PASS all 4 prior bands (0f57814/ee8a9b5/c12fcc6/
  eb766e3). sweep: please gate oldest-first (920e187, 937c347).
- next: band6 chase w2 tip (P21 letter L + R20 055bb85, n<=24392).
