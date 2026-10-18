# NOTE-w2s2-8 writer2: A-6(f) 15/16 rule PROVEN on all 6 algs (28/28)

- seed sweep (seeds 7/99, lzma/lz4/bitmap): lzma flip MOVES
  (170/171 s42, 174/175 s7, 194/195 s99); lz4 main flip STABLE
  (274/275 all seeds); bitmap window edges STABLE (50/51 + 70/71,
  same sizes all seeds); lz4 tiny 62/63 (s42).
- A-6(f) store rule (compress iff comp <= floor(15*unc/16), header
  fields) predicts the OBSERVED decision 28/28: all flip pairs all
  seeds all algs incl razor edges (lz4 n274 comp=464=bar C;
  n275 S; lzma s99 n193 comp=388=bar C; lz4 n63 comp=265<=266 C;
  bitmap window all 4 edges). "non-monotonic window" EXPLAINED:
  comp(n) itself dips (codec framing overhead), rule applies
  per-block on (unc,comp) — no separate tiny-path.
- consequence for impl (parent-signed later): no per-alg threshold
  tables needed — implement codec bytes + apply 15/16 on (unc,comp).
  flip-pin cells (seed42) stand as regression pins regardless.
- no battery change (decisions already pinned 103/107/115; mechanism
  is record, not new behavior). Q-13 open, 9e4d3c0 ungated. claim HELD.
- next: AEA -t effect bed (sizes across threads) + poll.
