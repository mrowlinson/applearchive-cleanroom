# NOTE-012 viewer: 15/16 rule now 6-ALG (lz4/lzma/lzraven/lzbitmap beds)

- 12-cell sweep (urandom n=100/300/500 x 4 algs): EVERY verdict matches 15/16 prediction (comp<=floor(15unc/16)).
- lz4: C(306<=315) S S. lzma: C(312<=315) S S. lzraven: C(300<=315) S S.
- lzbitmap: S(n=100, comp==unc, grew past bar) C(n=300, 494<=503) S(n=500) — non-monotonic in size, rule-exact.
- rule UNIVERSAL across all 6 compressed algs (lzfse/zlib flips + these). CR-108 updated on lane (commit next).
- writer1 "then zlib/lzma/lz4 OSS-compare": decision rule needs no per-alg work; only codec BYTE identity per alg remains.
