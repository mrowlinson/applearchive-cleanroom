# NOTE-57 writer1s3 (hash STUCK-custom-strong; need idea, polling)

- findings: byte-maps single-value (14/14, 2 chance
  doubles); 2nd-hits chance (xors random, 21% rate vs
  12% expect = bucket-width hint only); H12 bit-agree
  55-62% (weak); all standard families <=4/488; mult
  dead all shifts; drop-bit all 97 (full-colliders).
- TRUE hash = custom strong-mix, K-high weakly related
  at best. single-byte avalanche ~255/256. no family
  shape to fit; 488 eqs overconstrain nothing known.
- STUCK: need new idea (not brute). options: (a) viewer
  structural probe (bucket-index observable? timing?);
  (b) table-structure rethink (not bucketsxslots?);
  (c) accept 488/672 + ship (hash frontier parked).
- tree green tip 94c8d61; polling viewer every turn.
