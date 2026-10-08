# DPROBE-11 M3 residuals: decode unification + token + chained + DAT-rule

## Decode unification (M3-proto root cause)
- proto lzfse was ctool subprocess (all-or-nothing); C uses
  buffer API (truncate-tolerant). Proto now ctypes-calls the
  SAME primitive (libcompression.dylib, LZFSE=2049 decimal).
- tri-state both sides: ok (got==unc) / mismatch (0<got<unc,
  bytes discarded) / fail (got==0). Mismatch -> outSize=got.
- frame structure (283B-ok/292B-fail) inherited free, both
  sides IDENT (paylo-10 vs paylo-1 first-hand).
- kept: lz4/lzraven via ctool (shortfall unpinned, no gap);
  pbzx lzma + pbzz zlib tri-stated (mismatch analog, unprobed).

## unchi token (residual 2)
- outSize = actual decoded bytes on mismatch (2445, all
  deltas 1/10/100/500); -1 iff undecodable (got==0: corrupt
  payload, stored-as-codec EU1/sthi). C+proto IDENT.

## paylo chained (residual 3)
- (header)-decfail with trailing 1..4 bytes: trunchdr line
  FIRST (`Truncated block header (have/16)`), then decoder
  block (inSize=pay', outSize=-1). Sharp: have 4 chained 2/2,
  have 5 plain 2/2. C+proto IDENT (1/4/5/10/100).
- have2==0 (payload-to-EOF): no chained (nothing to describe)
  ASSUMED, unprobed (Batch-2). (blob)+tiny-tail: Q-020 open.
- mismatch+trail combo (unchi+3B): chained-by-analogy,
  unprobed (Batch-2).

## unclo DAT-rule (residual 1 + M2-under)
- present <=> B OR avail >= DATlen; content FULL iff DAT
  complete else chunks. T=36 EXACT == DAT-end (2409):
  D36 FULL 3/3, D37 greet-only 3/3, boundary-inclusive.
- u10/u25/u36 byte-IDENTICAL (content+mode+xattr); u37/u100
  greet-only (repeat absent, no fsts line).
- XAT-short tolerated (XAT cut both sides, pre-existing).
- C normal-path short-F: no-DAT-entry -> fsts; DAT-short ->
  silent skip; DAT-complete -> normal FULL. Proto: shortidx
  dropped on normal path (pre-existing) + entries-DAT fsts
  gate + DAT-short skip. Mirrored, battery-locked.
- raw-1: mine FULL 8/8 vs viewer 1/2 -> pooled race EXISTS
  (rare/vector-dependent). Battery ships raw-10+ (stable);
  raw-1 band documented, never pinned.

## Open (TIP2)
- M1 tails (rp/count map, Batch-2) + M2-large (avail-gate at
  big kcut + end-gates + race bands, Batch-2) + fsts trigger
  (Q-025) + have2=0/unchi+trail probes.
