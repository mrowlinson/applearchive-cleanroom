# PRE-057b K-zone 5601..5692: cluster (trans + 16-row + 10-row + 64-body)

## sectioning (v5ae/v5af, 92 rows all 56B, 36 var)
- 5601/5602: transition literals (b0 82/d4; b1 66/92; b2 00/33;
  b11 b3/73; b19 d1).
- 5603..5618: 16-row (b0 ef/b1 92/b2 39; b11 33; b19 11).
- 5619..5628: 10-row (b0 be/b1 2e/b2 67).
- 5629..5692: 64-body (b0 7e/b1 f1/b2 e4; b11 73; b19 a1;
  b20-23 const 8e/af/c3/9c; b24-31 const; b5 6b->6c @5632).
- edges>=8: 5602/5603/5619/5620/5627/5629 + bands 5645/5661/5677
  (top flips 5629:28, 5602:21, 5619:18).

## body tabs/bands from 5629
- b40: ff 7c 8d 2d bb bb 53 d0 e1 42 fe 0f 70 ed 3d cb (16).
- b41: 5d dc 5f dd da de dc 5a dd da d9 5d 59 5e dc d9 (10).
- b42: 7e 36 3b 8c 49 49 b7 70 74 79 7e 83 88 91 91 4e.
- b43: ramp-ish 7f..8b.
- b32/34/35/37/38: 16-bands @5645/5661/5677; b33: fc/fd/bf
  (32-tail); b36: 32-halves 74/d4.
- same architecture as C/G/I clusters. one commit 5601..5692.
