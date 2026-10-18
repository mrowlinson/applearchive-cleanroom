# NOTE-23-writer1s2-hole1dead (heartbeat12, CORRECTS NOTE-21)

## HOLE1 WITHDRAWN: coord-mapping error (md=181, not 217)
- True inners decoded (lz4 blocks): pair differs at INNER 788 (e0->76), NOT 824.
- Flip@788 is INSIDE match-(4,off4)@789's own source window [785:789]: it CREATES
  (y4: [785:789]==[789:793]) / DESTROYS (y3) the match. 1B past, overlapping.
- Landscape: y3@789 len 0 (no match exists -> literal CORRECT); y4@789 (4,4) (taken).
- NO anomaly, NO future-dependence, NO lookahead needed. NOTE-21's "real" verdict
  was built on my bad coords. Marginal-lookahead hunt CANCELLED; one-pass unanimous
  (concurs A-17(c)). Window-mapping beds: w-skips = prefix table-state (wctl skips
  with no future match); k-style fires at all N (no window effect anywhere).
- Pair files stand but MEANING changes: match-creation pair, not future-pair.

## lz4 remaining: hash fn + eviction shape + tail-zone (all prefix-local now)
