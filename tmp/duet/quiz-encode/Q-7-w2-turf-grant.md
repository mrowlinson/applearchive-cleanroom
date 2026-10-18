# Q-7 (writer2) turf grant: disjoint encode split

- seat: encode-writer2, lane lanes/encode-writer2, SECOND writer side ENCODE.
- need: viewer grant of disjoint turf vs writer1 (raw inner closed NOTE-3,
  impl src/rawenc.py + test_rawenc.sh NEXT). propose: OUTER wrapper encode
  (pbze/pbzz framing, block layout, store-vs-compress rule, multi-block,
  -b/-t effects on outer) + outer-side pins/battery. confirm or redraw.
- need: writer1 file boundaries (exact paths writer2 must not touch).
- tried: read Q-1..Q-6 + A-1..A-5 + NOTE-1/2/3 + NOTE-001/002/003.
  Q-6(f) overlaps outer rule; will read A-6 when filed, not re-ask.
- meanwhile (unblocked, no grant needed): own black-box pbze probes in
  own worktree scratch; harness adoption per A-1 prescription
  (git-show read-only + hash-verify + own contamination grep).
- ADDENDUM (NOTE-4 seen): writer1 g6 now claims pbze stored wrapper +
  boundary sweep + multi-block in impl. OVERLAP with this proposal.
  alternative split: writer1 = lzfse/raw outer path; writer2 = other
  algs outer (lzma/lz4/zlib/lzraven/lzbitmap magics+framing) + -b/-t
  outer effects + big multi-block. viewer redraws as fit.
- side: ENCODE.
