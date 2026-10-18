# PRE-199b 80: frameswap + lattice (frontier stage)

## census (v5d65 first-hand, 256 rows all 80B, nvar=33)
- frameswap @40493 (32-flip; b1/b2/b6/b8-10/
  b20-27/b76/b78-79 flip; b4 = per-row odd walk
  3f,41,43... = lencode counter).
- lattice: b68-71 16-step blocks, b14 3c/7c/bc
  eras, b5 3c->3d @40576 ->3e @40704.
- split: ..40492 / 40493... next 348-mark: 40749.
