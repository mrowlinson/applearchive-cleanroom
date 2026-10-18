# NOTE-w2s3-12 writer2: table SELECTION closed, ORDER open, handoff state

- SELECTION = top-12 by (count DESC, pbc DESC, bitmap-value
  DESC): 3rd instance (f13 bed: 3x count-18 {04,08,40}
  -> top-2-by-value {40,08}; 04/0 CUT).
  pbc=1 beats pbc=0 at equal count (both chunks 6-7/6-7).
- ORDER: NOT selection order (f13: 01,02 before fe/20!),
  NOT count/firstpos/lastpos/hash (same key -> different
  slots across chunks kills fixed-hash). 00/0 pinned slot0
  3/3. decoder EXACT everywhere (analysis sound).
- next beds (queued): 12-keys-equal-counts (order = ?) +
  12-keys-distinct-counts (order = ?); then pbc=2 tier,
  rep-scheme verify, uncomp-fallback threshold, DP horizon.
- OSS log this shift: README.rst + libzbitmap.h +
  libzbitmap.c(full) + Makefile + test/Makefile (build
  only). decisions-only; zero OSS bytes in src.
- lane: tip ee9e454 == master (PV-006 merged). tree clean.
  shift: 6 commits (outer2 152->252, rb2 47 new), Q-15/16
  filed+answered, all VERIFY/GATE PASS, zero holds/wall/pyc.
- open: codec-hunt beds above, raven black-box, parent calls.
