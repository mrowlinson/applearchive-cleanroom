# Q-9 (writer1) raven/bitmap path, B/C stamps, >4GB

- need (behavior-only, beds+numbers):
  (a) lzraven/lzbitmap comp bytes: reproducible from any public
  codec (OSS path like lzfse/zlib), or Apple-internal? per-alg
  store-rule flips (A-6(f) unpinned for lzma/lz4/raven/bitmap) —
  mine next: OSS-compare lzma/lz4/zlib myself; need raven/bitmap
  verdict + any flip beds already run.
  (b) B/C entries: CTM/MTM present (same S/T shapes as F?) —
  assumed yes in impl; confirm or correct. UID/GID/MOD/FLG
  widths per 1/2/4 rule assumed; confirm.
  (c) >4GB inputs: u32 width behavior (DAT'B', pbze unc/comp) —
  bedded or OPEN? (mine: unprobed; flag only.)
- tried: lzfse closed (OSS-exact); zlib/lzma/lz4 OSS-compare in
  progress own worktree. (a-c) need root beds / matrix already run.
- exhibits: own p9/p10/p11/p12 + lane 8a0a67e batteries.
- side: ENCODE. (writer2 -b/-t turf respected; not asked here.)
