# PRE-062b 60-regime2 6705..6992: sub-head + 16-tabs/bands (T7D stage)

## census (v5al first-hand, 288 rows all 60B, 29 var)
- 6705..6736 sub-head (b0 ba/b1 00; b26 0f->8f, b27 dc->00,
  b34/35/43/45 mid-flips @6721).
- 6737 edge (27 flips: b0->e0/b1->0b; b26-27/34-47 to body).
- 6737..6992 body: 15 edges step-16 (6753..6977 + 32-gap
  6849-6881).
- 16-tabs full-body (period16 ✓): b55=(06x4 12x2 16x2 1ex3
  22x2 2ex3), b56=(6d cd cd 4d 4d cd ed 4d 0d 8d ad ad 2d
  8d 8d 0d), b57=(7c bf 90 a1 c5 ed a7 cf 81 91 ff b8 e1
  bf 78 a1), b58=(07 7f 4f 57 5f c7 27 9f 1f 27 ef 5f c7
  6f df 47), b59=(71 80 81 d0 de de 2a 2e 8d dc dc 2c 2c
  3a 89 8a).
- bands from 6737: b48/b50 16-bands (+32 @6849-6880); b49
  4-val 16/32-mix; b51 ramp-ish 04..bf.
- b4 ramp; b5 128s 54/55/56 @6705/6784/6912.
- split: 6705..6736 / 6737..6848 / 6849..6992.
