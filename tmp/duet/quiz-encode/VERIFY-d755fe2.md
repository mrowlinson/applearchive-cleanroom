# VERIFY-d755fe2: PASS (ravframe verifier + 156-pin battery, additive, honest)

- scope first-hand: src/ravframe.py +143 (new), tests/test_ravframe.sh +79 (new),
  vectors/ravframe-PINS.csv +158 lines (156 rows + 2 headers). full read of both code files.
- ravframe.py: PURE structural verifier, stdlib-only (struct/sys). zero oracle/OSS/libcompression
  contact. implements own-bedded rules (magic/trailer, F3=pay*4096+store + %4096 assert, 512K
  first-cap, overrun/close asserts, F2 closed form (4+U%4)*2^(14+U//4), empty-12B rule, MIN-64 const).
  matches NOTE-w2s4-5/6/9 claims EXACT.
- test: CT test-time exec (beds-OK rb2-precedent ✓) + ravframe CLOSED verdict + f2-hex + sha pins.
  matrix covers every F2 threshold as n/n+1 edge pairs (matches NOTE-w2s4-9 list), zeros 63/64/65
  min-64 edges, pattern cells. deterministic inputs (seedN/z/pat), honest chk.
- provenance: OSS-read=ZERO claimed (framing-only, needs none) ✓ consistent. no GATE yet; code PASS, no FLAG.
