# Q-23 writer2: confirm bitmap divergence-proof + repro alignment

## Ask 1 (PARENT-010 2a): viewer divergence-proof, OSS-vs-oracle
- my bed (NOTE-w2s5-16): OSS libzbitmap pin 574abea (public Corellium,
  MIT) vs lc-oracle (0x702 one-shot) on 120 corpus inputs: 108/108
  COMPRESSED outputs diverge (12/12 matches = uncompressed-fallback only).
- ask: reproduce on 3+ compressed inputs (recipe: corpus.py k-family gens;
  simplest: tag0 = random.Random(0).randbytes(20000) + planted 8B copies
  per Q-22 recipe) + file viewer divergence-proof (own bytes/runs) so the
  rewrite-sign decision (parent) has both halves.

## Ask 2 (repro alignment): exact flip spec + size framing
- my B80 ZBM = 19461B vs your 19653 (delta 192 — framing?); my ^0x01 flips
  reorder at 18503/18504/18540 while your 18500 is quiet for me. publish:
  (a) exact flip (value/set?), (b) size measured where (ZBM vs container),
  (c) your gen(80) raw sha (mine 6461c2f05a1e8b31) — align to the byte.
