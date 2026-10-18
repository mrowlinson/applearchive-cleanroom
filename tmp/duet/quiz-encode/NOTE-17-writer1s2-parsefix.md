# NOTE-17 writer1s2: PARSE BUG found+fixed; search is DENSE, model simplified

- CORRECTION: my "tripwire 0/30 miss" was a PARSE BUG (glob/
  regex silently empty — lesson: always print counts). TRUTH:
  29/30 HIT at exact start, ref 186 (only X=0@matchend missed).
  N-hash, lookahead, content-skip, lazy theories: ALL DEAD
  (artifacts of the bug). apology for NOTE-15/16 churn; the
  EXTENSION rule + framing stand (independently verified).
- MODEL (simple, fits ~200 matches): DENSE search (every pos
  checked); last-pos table; on match table {mstart,mstart+1}
  ONLY (186 stable across all walls; off=3 explained);
  misses tabled; NO backext (r606 anomaly); extension =
  RULE-EXT v2; framing CLOSED; NO len-128 search limit
  (run@1125 fired).
- open micro-rules: (a) post-match resume (781 skipped after
  len-596, 791 checked after len-5 — length-dependent?);
  (b) SL1123/TailS5 run-misses = bucket CLOBBER (replay test
  queued: same wall, run sweep -> miss-iff-after-collider);
  (c) true search tail limit (runs at len-50..len-5);
  (d) HASH FUNCTION (still unknown — needed for exactness).
- gap: g-lz4hunt search-OPEN (hash + resume + collider-proof).
