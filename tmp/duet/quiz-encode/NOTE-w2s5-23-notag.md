# NOTE-w2s5-23 writer2: NO-TAG MODEL (skeleton + holes reframes grammar)

- tag widths vary 1-6 bits (pos124:1b, pos116:3b, pos113/120:4b, pos103:5b,
  pos96/112:6b) with arbitrary values (0x00/0x01/0x08/0x0F/0x10/0xC0...) —
  NO fixed tag width/value => NO TAG. "tag bytes" = zeros-skeleton bits
  (match tokens for the zeros128 parse) adjacent to value holes.
- model: payload = SKELETON (96b: length code + match tokens, FIXED for
  zeros128) + HOLES (256b: 32 tail pos x 8 exclusive). R4 formulas stand
  (C = skeleton bits, constant). RAW8 = full-byte holes. splits = holes
  scattered among skeleton bits. mid +32B token = new match token(s) +
  fresh holes. early aliasing = holes reused + skeleton resync.
- PRE-006's "no adjacent tag" explained (nothing adjacent to find); word1
  byte0 = length code (skeleton) confirmed. TAG-01/0000 = skeleton-bit
  patterns (match-token types?), not value tags — width question becomes
  "which match-token type wraps this literal" (field-level beddable).
- next: skeleton decode (base MINUS 256 hole bits = 96b token stream).
