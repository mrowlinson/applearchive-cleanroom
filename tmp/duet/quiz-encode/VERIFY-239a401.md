# VERIFY 239a401 (encode-writer2): PASS (payload beds verify; message wording stale)

- method: diff own-read (2 files, +36/-1) + RESULTS-rb2 rows first-hand (already read for A-11).
- bed claims VERIFIED in own rows: r100 unc=321 comps 292/288/237 (lzma/lz4/zlib) all COMPRESS <=300 ✓;
  r1000+ STORED (unc==comp, AA01-inline pay) ✓; b10k stored arith unc==comp=10000 EXACT ✓.
  ALGS param: 1-line loop change, additive default unchanged ✓.
- STALE WORDING (non-blocking): commit message says lz4 = "u32le unc + u32le comp-16 + flags + inner" —
  SUPERSEDED by A-11 (no flags word exists; w2's own pay32 rows show block at +12). bytes right, gloss wrong.
  no action needed (bed output, not spec); do not copy the gloss into impl.
- wall: execution-only probe tweak. tmp/scratch-encode2 pre-dates PARENT-005 — grandfather concur.
- verdict: PASS. no FLAG.
