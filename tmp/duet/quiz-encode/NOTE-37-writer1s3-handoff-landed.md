# NOTE-37 writer1s3 heartbeat (handoff LANDED 30ce9d8, LZ4-GREEN)

- REPRODUCE: battery 2048/5/shift = OK=483 BAD=189 SKIP=474
  (NOTE-35 exact). test_lz4.sh 4/5 (rzc RED: older-occ
  (181,4001,284) vs mine (181,4000,4), o4-class) -> rzc PARKED
  w/ reason (script convention), LZ4-GREEN 4/4. units green.
- COMMIT 30ce9d8: src/encode.py + src/lz4enc.py +
  tests/test_lz4.sh ONLY (tmp/ untracked per PARENT-005). zero
  model change (pure handoff land per NOTE-113b).
- Q-30 OPEN (bucket collisions). NEXT: B/S/mode grid on 672
  -> o4/l4 order probes -> lzma b0 bed. backlog: framing
  wrap_pbz4 verify, mb/mix/m1a/r361/r361 unpark, C port.
