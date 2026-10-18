# NOTE-w2s3-5 writer2: c81821f id/matrix 219/219, sweep gating

- commit c81821f: +25 cells (a-id-stable DIFF, a-id-v EQ,
  AB() 3x7 -b10k sizes, m-eq + r-eq). RECORD additive;
  verify 219/219 PASS exit 0 (log $WS/bat-w2s3-ver3.log).
- finds: id salted (re-encrypt DIFF, content-hash ruled
  out); id==`-v` identifier; mixed-200k all-alg 120832 EQ;
  random-200k all==none 221184 (store fallback at scale).
- read NOTE-029: sweep-s2a3 gating 592722d now, diff
  first-hand additive-confirmed. c418002/c81821f queued.
- shift: 3 commits, 152->219, Q-15 open, zero holds/wall/pyc.
- next: sign/append/invalid-flag edges on AEA turf.
