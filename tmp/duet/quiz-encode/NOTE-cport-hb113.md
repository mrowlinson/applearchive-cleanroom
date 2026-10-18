# NOTE-cport-hb113: b186 battery running, w2b-combine procedure derived

- mrg-b186-py-r9 at 2494 PASS / 0 FAIL (~30%).
- band188 combine procedure (first w2b pull, no precedent): git merge --no-commit w2b@P136 -> expect 3 conflicts at same two rgram sites (tables @20270-post-P135QC, tier blocks @chain-end) + test.sh for-line + PINS EOF. resolve ALL by taking both sides in range order (R133 content first, P136 after; sizes union ascending; pins chronological). dispatch stays ascending; P-blocks use explicit lower bounds so order is convention-safe. battery GREEN decides.
- same pattern repeats for alternating lanes after (each merge appends newest at end). R-series reference prior tables only via shared base (own-copy q), no forward refs.
- no joint DONE. never push.
