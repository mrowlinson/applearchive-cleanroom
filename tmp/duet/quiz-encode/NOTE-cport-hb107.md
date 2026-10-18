# NOTE-cport-hb107: r8 refill-exit, R132 handoff (clean band boundary)

- run totals r8: bands 4 (b181 495edcb, b182 d1a3c2d, b183 066fa1c, b184 a31520e) + merges 4, all GREEN fh (PYID 4002/4014/4024/4038, C+py 8004/8028/8048/8076, 0w). tip a31520e clean apart from staged R132.
- handoff: R132 cb315f7 merged --no-commit (auto-ok, MERGE_HEAD set): rgram.py MATCH (+54), PINS MATCH +24, hook 1/1 fh. SMOKE-GREEN rc=0 (mrg-b185-smoke-r8.log).
- r8 launched NO py battery for b185 (batteries die with the session). successor: launch mrg-b185-py-r9 FRESH first-hand, expect 8100/8100, then merge commit + band185 cut (T10R132 n<=63716, 842 tiers; PYID expect 4050/4050; seed pyidb184-fh/corpus).
- queue after R132 oldest-first: P135 8aaeccb, R133 4f399ae, P136 8fb7560(w2b), R134 14b73de, P137 e81d47b(w2b), R135 66b9bd2, P138 34684a9(w2b), R136 555d15e, P139 c16ad2d(w2b), R137 ef9bbf0, P140 b3ec35c(w2b), R138 2b38c3c, P141 76b080e(w2b), R139 f82ac5e, R140 c14cec6, R141 b701d00, R142 1de0986, R143 4a2dbcf, R144 4e70d52, R145 c9aac21 (+new; re-list at takeover, tips were w2 R145 / w2b P141 mid-r8).
- no joint DONE. never push. claim needs successor holder overwrite.
