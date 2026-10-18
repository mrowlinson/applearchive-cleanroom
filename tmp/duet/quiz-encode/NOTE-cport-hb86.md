# NOTE-cport-hb86: r7 takeover, fresh mrg-b178-py-r7 launched

- claim overwritten r6->r7. tip fe4c199, MERGE_HEAD=3556c57 (P131) confirmed, staged rgram.py/PINS/test.sh.
- inbox: no new Q for cport (newest Q-361 Oct 14, w2 geometry). queue re-listed at takeover: P131 staged, then R129 36dce1d, P132 d44a1bd, R130 1fa6bd0, P133 bcf547d, R131 1bd6942, P134 680d564, R132 cb315f7, P135 8aaeccb, R133 4f399ae, P136 8fb7560(w2b), R134 14b73de, P137 e81d47b(w2b), R135 66b9bd2, R136 555d15e.
- stale mrg-b178-py-r6.log checked: 5692 PASS 0 FAIL partial (handoff said 5584 — same stale run, untrusted either way).
- FIRST action per handoff: fresh py battery mrg-b178-py-r7 launched on staged P131 state. blobs/hook re-verify + merge commit + band178 cut (expect n<=62416, 828 tiers, PYID 3965/3965) after GREEN.
- no joint DONE. never push.
