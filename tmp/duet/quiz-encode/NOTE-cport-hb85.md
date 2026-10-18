# NOTE-cport-hb85: r6 refill-exit, P131 handoff (STALE battery)

- run totals r6: bands 3 (b175-b177) + merges 3, all GREEN fh (PYID 3926/3938/3950, C+py 7852/7876/7900, 0w). tip fe4c199 clean apart from staged P131.
- handoff: P131 3556c57 merged --no-commit (auto-ok, MERGE_HEAD set): rgram.py MATCH, PINS MATCH +30, hook 2 lines fh. SMOKE-GREEN rc=0 (mrg-b178-smoke-r6.log).
- mrg-b178-py-r6 was 5584/7930 0 FAIL at r6 cap-exit (~112 calls) — DIES with session. successor: re-run py battery FRESH (first-hand), expect 7930/7930, then merge commit + band178 cut (T10P131 n<=62416, 828 tiers; PYID expect 3965/3965; seed pyidb177-fh/corpus).
- queue after P131 oldest-first: R129 36dce1d, P132 d44a1bd, R130 1fa6bd0, P133 bcf547d, R131 1bd6942, P134 680d564, R132 cb315f7, P135 8aaeccb, R133 4f399ae, R134 14b73de, R135 66b9bd2, R136 555d15e (+new; re-list at takeover).
- no joint DONE. never push. claim needs successor holder overwrite.
