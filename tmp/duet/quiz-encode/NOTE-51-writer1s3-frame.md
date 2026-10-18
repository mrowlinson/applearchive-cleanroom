# NOTE-51 writer1s3 (framing audit PASS; still blocked on A-40)

- EDGES (5MB-rand/5MB-zero/empty-dir): py==C all 3
  (5243162/32191/259 B). oracle: big5 EXACT, empty
  EXACT, zero5 same-size + same headers + same 64-chunk
  block1; div = block2-chunk0 content (bv41 65536/386
  both, bytes differ) = hash frontier, not framing.
- pbz4 multi-block/store/empty structure CORRECT both
  impls. framing audit closed.
- NO-A40 still. frontier 184/184 hash (NOTE-49).
  NEXT: unparked lzma-side checks (mb/mix/m1a/r361/rzc
  already green in pins?) + poll A-40 every turn.
