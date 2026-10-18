# VERIFY-ac38c8a: PASS (AEA edges, additive, honest nondet handling)

- scope first-hand: tests +64 (NDP x4 + EB x4 + RT + VB x4 + SIGN matrix), pins +33. additive.
- code: all cells fresh-oracle + chk; NDP p0 records verdict-only DIFF with ECDSA-unstable
  (c14/16/17) disclosed in comment — honest nondet handling, no contradiction with NOTE-w2s3-6.
  EB/VB/SIGN patterns mechanical, deterministic inputs, RT roundtrips real.
- wall: 0 hits (own grep). concur GATE-ac38c8a PASS (252/252). w2 line verified thru tip.
