# NOTE-031 sweep: framework ff42363 committed, viewer burst read, polling

- framework: gate-tip.sh vacuous-PASS fix COMMITTED ff42363
  (REPO from script dir, split archive|tar pipe, rev-exists
  + non-empty-tree guards). proven first-hand: outside-repo
  cwd now full-legs GATE-PASS c81821f (was vacuous all-SKIP);
  bogus rev GATE-FAILs fast. bash -n clean. local-only.
- viewer burst read: A-13 (raven=ct+libcomp EXACT, bitmap=
  libcomp-only; beds-only steer, LIBCOMP leg unchanged),
  A-14 (+28 artifact, record-only), A-15 (8 -a values,
  no plaintext codec field, bogus rc1 — consistent with
  gated 592722d -v-echo pins). 9 VERIFYs all concur GATEs.
- coverage: 20/20 writer tips gated, ZERO holds. open: w2
  ~33-cell sign/edge commit (queued NOTE-w2s3-6), w1 lz4
  hunt, parent calls. no DONE anywhere. claim HELD @ff42363.
