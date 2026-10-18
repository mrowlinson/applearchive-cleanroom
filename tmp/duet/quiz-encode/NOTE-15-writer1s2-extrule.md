# NOTE-15 writer1s2: lz4 EXTENSION RULE found (13/13), OSS axis CLOSED

- grid: 36 OSS settings (default + fast 1..16,20..200 + hc 1..12)
  0/5 hits every cell. Apple worse than fast:200 on dense beds.
  OSS-knob axis CLOSED (~66 trials incl prior). bed-war proper.
- microscope (scratch seqdump, own LZ4 parser): oracle vs OSS
  agree on header matches (same offs); DIVERGE on run matches.
- RULE-EXT (candidate, 13/13 beds+chunks): match extension =
  4B initial + 8B steps; mismatch-terminated = byte-precise
  (dtf/dtail zeros end EXACTLY at mend 1213); limit-terminated
  mend = (chunklen-121) - ((chunklen-121-mstart-4) mod 8)
  (8-quantized, NO byte fixup at limit). bound is PER-CHUNK
  (chk frame0 65536 + frame1 34691 both fit own chunklen).
- dict-link CONFIRMED first-hand: frame1 match@(0,off 65340)
  -> chunk0 out[196..] zeros. A-11 mechanism holds.
- open probes: tiny-tail-chunk (<136B) parse anomaly (debug
  next), P-tailstart (search-limit shape), SEARCH model
  (hash/skip: 1 header seq differs lit51 vs 46 + run offs
  3-vs-2). gap: g-lz4hunt extension-CLOSED/search-OPEN.
