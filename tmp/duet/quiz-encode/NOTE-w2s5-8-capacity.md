# NOTE-w2s5-8 writer2: token capacity ~2 distinct devs + mutual-match savings

- same-value (AA) devs: 1/2/3->48B, 4->52B, 5->48B (!). distinct-value devs:
  3->52B, 4->56B, 5->56B. (1-2 distinct ->48 from NOTE-7 bed.)
- rule: ~2 DISTINCT literals per +4B token; same-valued devs MUTUALLY MATCH
  (5xAA@10-spacing parses as match-run, SAVES 4B vs 4dev). positions+values
  jointly drive parse — capacity is not a clean count (5th distinct rides
  with 4th's token: 56B both).
- pivoting to stored-cells commit (concrete pins); grammar TAG-width hunt
  resumes after (bit10 + nibble-tag map). claim HELD.
