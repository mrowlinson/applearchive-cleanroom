# NOTE-28 writer1s2 lz4: MEND-proximity rule + buckets (heartbeat15)

- 98% MODEL (Knuth-12 dense + mstart/+1/ends + continuous): 5200/5266 exact-src.
- TAIL RULE (20+ clean checks, zero counterexamples): INSERT(tail-literal P)
  iff FIRST-match-MEND >= CHUNK_END-124 (MEND-proximity; OFF/ML/SPAN all dead
  as gates; ML-vs-trail unified: MEND; threshold btw END-124(PRESENT m2/m3-odd)
  and END-125(ABSENT m3-chunk2)). zeros-override: zeros-tail ABSENT even when
  MEND-ok (mb!). +1-zeros: INSERT iff NONZEROS-gram OR MEND-near-end (7/7+588).
- RESIDUAL: (a) MEND-124/125 exactness needs clean re-read (r65411 VOID/miss);
  (b) zeros-mid literals (never?); (c) ENDS gate (v1024/127: ml=4 absent);
  (d) 5 literal-skips (158/429/750/73725/96310: mid-chunk nonzeros absent) =
  possible rare skipper; (e) stored-chunk insert rule; (f) T0 (OFF) dropped.
- NEXT: clean 124/125 pair, zeros-mid probe, ENDS-ml sweep, skip-hunt beds.
