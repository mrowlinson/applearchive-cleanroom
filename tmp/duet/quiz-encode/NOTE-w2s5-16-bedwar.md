# NOTE-w2s5-16 writer2: BED-WAR VERDICT bitmap (OSS-link insufficient) + A-25 P1-P4 all confirm

## Bed-war (PARENT-010 determination, first-hand)
- OSS libzbitmap (pin 574abea, WS-built libzbitmap.a + osszbm shim, never
  repo) vs lc-oracle on corpus gen(0..119): MATCH 12 / DIVERGE 108 / err 0.
- all 12 matches = k9 pure-random = ALL-UNCOMPRESSED chunks (trivial path).
  EVERY COMPRESSED output diverges (108/108). oracle = optimal-parse+ties
  (A-25, NOTE-w2s3-11); OSS = greedy — divergence structural, expected.
- LINK verdict: OSS-link covers uncompressed-path ONLY (insufficient alone).
  system-dylib-link = identical-by-construction (is the oracle) but needs
  parent portability-waiver call (PARENT-007 grounds stand). REWRITE needs
  viewer divergence-proof (Q-23 filed) + parent sign. no rewrite without both.

## A-25 P1-P4 (own fragile points 18503/18504/18540; viewer 18500 nearby)
- P1 CONFIRM (op seqs differ, nops 2500/2500); P2 CONFIRM crux (ff 2109->2110,
  slot 2->1); P3 CONFIRM (first div op2312 ~byte18496, ONE OP BEFORE flip =
  lookahead/DP evidence); P4 CONFIRM (tag30v80 differ). tie-lottery stands.
- recipe note: my ^0x01 flips reorder at 18503/18504 (L1=4,+0/+1B,ff->1) and
  18540 (L1=2,+2B,ff->3); viewer 18500 quiet under ^0x01/^0xFF/^0x80 for me
  (3B shift — flip-value or indexing detail; phenomenon identical). my rawsha
  gen(80) = 6461c2f05a1e8b31 (cross-check); my B80 ZBM = 19461B vs their 19653
  (framing? needs alignment for exact repro — asked Q-23#2).
