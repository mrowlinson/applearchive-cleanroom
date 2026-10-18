# NOTE-45 writer1s3 (lzma b0 SHIPPED 906081f, m4m fixed py+C)

- COMMIT 906081f: b0 = 4 iff unc>=2**21 else 2 iff
  unc,comp<128 else 3 (py + C). bedded: tail-unc sweep
  (t119/t127->2, t128+->3, t50/100 stored) + vu-3 probes
  (u2M->3, u3M->4). NOT min-fit (t128 fits-12 but b0=3).
- VERIFY: m4m-exact (4194204B 0xCC) byte-identical py AND
  C. battery 6/6 green both (same SHAs). C builds clean.
- FLAG-w1-lzma-b0-hold: fix landed, needs sweep re-gate
  (holdout 12/12 expected).
- BACKLOG: Q-32 (hash triplets) open; framing/wrap verify;
  unpark mb/mix/m1a/r361/rzc (needs P1/EXT); C lz4 port;
  FULL/holdout/fresh lz4 batteries.
