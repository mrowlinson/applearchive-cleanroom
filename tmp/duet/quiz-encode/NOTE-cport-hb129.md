# NOTE-cport-hb129: P137 combine resolved, mrg-b190-py launched

- merge --no-commit w2b@e81d47b (P137 64413..64504): rgram.py AUTO-MERGED but chain descended (P137 before R134); test.sh + PINS conflicted normally.
- resolve-b190.py: moved R134 block before P137 (ascending P136Q<R134<P137B<P137Q), PINS chronological (8230 unique), sizes union 4115. asserts pass, py_compile rc=0.
- verified: 0 removed vs HEAD and vs w2b; +175 py +28 pins. staged (M x3). smoke fh SMOKE-GREEN rc=0.
- mrg-b190-py-r10 launched fh, expect 8230/8230 (~40 min). standing: auto-merge of same-spot inserts is NOT trustworthy for order — always verify chain ascending.
- r10 totals: 2 bands + 2 merges. no joint DONE. never push.
