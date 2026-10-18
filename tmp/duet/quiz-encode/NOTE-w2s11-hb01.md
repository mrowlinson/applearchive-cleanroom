# NOTE-w2s11-hb01: R42 battery running, P44 census mapped

- R42 (31793..32048) implemented, probe 256/256; for-list extended;
  RECORD+battery+smoke running in background.
- VERIFY-35d6de7 (P39) PASS, VERIFY-b1f4334 (R37) PASS seen.
- P44 zone: 32049..32140 (92, paylen 76 flat); R43 = 32141..32396
  (256) by head-break at 32141 and 32397.
- P44 heads: off0/off1 singletons; off2..17 one head; off18..27 one
  head; off28..91 16 column-heads x4 period-16 (30/31 share).
- P44 b4 lencode = ((off+49)<<1)|1, 92/92; b5 = 7a/fa interleave
  off0..78, fb off79..91 (wrap at off79).
- Next: commit R42 on GREEN, then P44 m/q map.
