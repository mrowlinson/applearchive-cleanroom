# NOTE-cport-hb122: mrg-b188-py 44%, queue re-listed

- mrg-b188-py-r10 at 3604 PASS / 0 FAIL (~44%), oracle-paced, ~20 min to go.
- queue re-listed fh (tips w2 a286112 R150 / w2b 1991268 P145): after P136 oldest-first: R134 14b73de, P137 e81d47b(w2b), R135 66b9bd2, P138 34684a9(w2b), R136 555d15e, P139 c16ad2d(w2b), R137 ef9bbf0, P140 b3ec35c(w2b), R138 2b38c3c, P141 76b080e(w2b), R139 f82ac5e, P142 557c98f(w2b), R140 c14cec6, P143 a05c4cb(w2b), R141 b701d00, P144 fa38cd1(w2b), R142 1de0986, P145 1991268(w2b), R143 4a2dbcf, R144 4e70d52, R145 c9aac21, R146 8e75ea8, R147 4982fa8, R148 5f6d6a3, R149 77c282f, R150 a286112(new). ranges interleave cleanly (P145 ends 67288, R143 starts 67289).
- next merge after b188 (R134 w2) is another cross-lane combine (cport holds w2b P136, w2 lacks it): same resolve pattern as P136 (append-newest-last + tables + sizes union + pins chronological).
- no joint DONE. never push.
