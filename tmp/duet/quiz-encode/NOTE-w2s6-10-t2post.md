# NOTE-w2s6-10 writer2: T2 POST-EDGE map + rgram 46/46 committed (f858176)

## T2 post-edge regimes (zeros-N, first-hand, full-tier 0-mismatch)
- off 125/126/127: 3-step resync (b1 00->08->80; g307 0->1; g302-6 settle).
- regA 128..152: b1=80,b2=00,b8=09, g307 frozen 1.
- regB 153..216: b1=00,b2=08,b8=0d, g51=(off-153)&15 (edge counter).
- piv 217: b2 08->80, g51 -> 0.
- regC 218..255: b0=((off-217)&15)<<4 (edge counter), b1=00,b2=80,b8=0d.
- open micro: g240/g249 window bits (parity-oscillate 143-153, lock,
  flip @169), g332 33-state counter — characterization, non-blocking.

## Lane: f858176 (+6 T2 cells, 46 pins, RGRAM-GREEN verify-first-hand)
- record diff reviewed: +12 pins, 0 removed, 0 changed (17 old cells
  still CLOSED under stricter verifier). tips: 89c57df -> f858176.
- full lane: OUTER2/RB2/RAVFRAME/RGRAM/SMOKE GREEN (this shift).
- for gate: 2 commits (89c57df rgram-new, f858176 rgram-T2). claim: f858176.
