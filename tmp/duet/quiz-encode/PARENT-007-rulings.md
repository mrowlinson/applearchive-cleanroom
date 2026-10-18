# PARENT-007 rulings: libcompression REFUSE + turf SIGN + bed-war (encode)

1. libcompression src-use (A-12): CONCUR viewer REFUSE. Reasons stand
   (proprietary, defeats reimplementation, unpinnable shared-cache,
   kills portability, lzfse precedent opposite). Beds-OK
   (execution-only measurement) stays GREEN unconditionally. Revisit
   only with OS-build pin + re-gate-on-bump + portability waiver.
2. Turf redraw (NOTE-008): SIGNED as drawn. w1 = raw inner + lzfse
   outer + zlib/lzma/lz4 codec-byte identity. w2 = lzraven/lzbitmap
   outer + -b/-t matrix + big multi-block + pins/battery + RACE +
   AEA-encrypt beds. Boundaries per A-7 hold; never cross paths.
3. Raven path: w2 proceeds with bitmap/raven IMPL now (sign given).
4. lzma/lz4: endorse BED-WAR (bounded hunt, oracles green).
   Ship-without needs a second explicit parent decision. No fixed
   box today; parent revisits if stalled.
