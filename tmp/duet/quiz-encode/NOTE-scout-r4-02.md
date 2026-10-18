# NOTE-scout-r4-02: OSS-libzbitmap wall-ruling brief (queue 1b)

## Question for the wall (PARENT-032 channel)
May the container lane use eafer/libzbitmap as a BLACK-BOX
chunk-decode oracle in tests (COMPARE-ONLY: beds/byte-diffs,
never linked into src), or must per-chunk ZBM verification wait
for container decode?

## Current granted status (cited, not re-litigated)
- Lane docs/OSS-SURVEY.md §3: libzbitmap READ-nominated (A-16; no
  load) — READ-ONLY for format/decode-path decisions, MIT
  (Corellium 2022), pin libzbitmap.dylib sha256=43d4f5e9... (own
  re-hash MATCHES A-10). Copy/fork/vendor/link all require a
  follow-up LOAD nomination.
- Precedent for the ask: lz4 COMPARE-ONLY (A-10) — black-box
  encode/decode compares, never imported/linked/dlopened by src
  or build. This brief asks the same tier for libzbitmap, for
  container T2 legs only.

## Why the lane needs it (measured, r3-06)
- `-a lzbitmap` framing = same pbz* spec; payload rule =
  ZBM-when-compressed, RAW-stored otherwise (both signals agree).
- Whole-archive `aa convert` oracle: PROVEN both shapes (977-chunk
  + single-chunk treecmp clean) — archive-granularity verification
  works TODAY with no ruling.
- Sliced-chunk convert: REFUTED (stream-layer validation rejects
  fragments). compression_tool has NO lzbitmap path. So per-chunk
  ZBM payloads have NO oracle through Apple tools — the gap this
  ruling would close.

## Scope of the ask (narrow)
- GRANT: dlopen/call libzbitmap decode entry points from T2
  scratch scripts ONLY, asserting per-chunk payload bytes equal
  oracle-archive bytes. No libzbitmap bytes, headers, or source in
  src/, tests/, or vectors/; pin recorded by hash (hashes-not-bytes).
- NOT ASKED: LOAD into src, vendoring, linking the deliverable,
  or any use beyond black-box compare. Any future src use = fresh
  nomination first (same bar as lz4 §4).
- Suggested sunset: ruling lapses for a leg once that leg's
  payloads are verifiable through container decode or an Apple
  tool; whole-archive convert oracle already covers the
  archive-granularity half permanently.

## Fallback if denied (no lane block)
- Container T2 keeps archive-granularity lzbitmap legs (convert +
  treecmp, PROVEN) and marks per-chunk ZBM payload asserts
  DEFERRED-to-decode. Zero schedule impact; the brief just leaves
  precision on the table.

## Scout action
- Filed, not fetched: no libzbitmap clone, build, or execution
  this run (same posture as r3). Awaiting ruling via parent.
