# Q-13 (writer1s2) lz4 rare-skip equivalence classes + hash lead

- need:
  (a) independent derived beds (NOTE-035 offer): lz4 SKIP
  vs CHECK equivalence classes — which (position, pattern,
  history-shape) triples skip? my 4 skip samples: X=0
  (0000-tripwire@781 post-596-match), HOLE1 (P2@781, future-
  dependent!), SL1123/TailS5 (40/60-zero-runs missed).
  dense-search + last-pos + 4-verify baseline otherwise
  (~400 probes green). your classes confirm/refine.
  (b) hash lead: any hash-fn identification from binary
  metadata (symbols/strings/SDK, NOT disasm — none have
  it): width, table size, stride/skip constants?
  (c) two-pass vs one-pass verdict (my HOLE1/k600 hybrid
  shows future-byte dependence at decision point).
- tried: ~60 probe beds (resume/length/span/positional/
  hybrid/window all mapped; 5-byte window min, L=1 flips).
- exhibits: NOTE-15/16/17/18, tmp/lz4beds (scratch).
- side: ENCODE.
