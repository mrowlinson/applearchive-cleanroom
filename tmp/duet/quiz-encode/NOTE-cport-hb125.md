# NOTE-cport-hb125: R134 combine resolved, mrg-b189-py launched

- merge --no-commit w2@14b73de (R134 64157..64412): 3 conflicts (rgram.py 3 hunks: H1+H2 tables with xdiff-aligned closers, H3 chain).
- resolve-b189.py: tables reconstructed from blob sources (P136 104 + R134 52 minus shared closer), chain HEAD+return+blank+THEIR, PINS chronological (8202 unique), sizes union 4101. all asserts pass, py_compile rc=0. hunk sides cross-checked == blob slices.
- verified: 0 removed vs HEAD and vs w2; +72 py +22 pins. staged (M x3). smoke fh SMOKE-GREEN rc=0.
- mrg-b189-py-r10 launched fh, expect 8202/8202 (~40 min).
- no joint DONE. never push.
