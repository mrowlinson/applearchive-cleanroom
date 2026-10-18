# PRE-079b 64-cluster5 10473..10500 + body 10501.. (frontier stage)

## census (v5az first-hand, 256 rows all 64B, 53 var)
- 10271..10472: bands (b0 83/b1 03; 12 edges step-16 10281..
  10457; b5 50->51 @10368).
- 10473/10474: transition double (39/35 flips; b0 43/03).
- 10475..10490: 16-row (b0 83/b1 00 — regime repeat).
- 10491..10500: chatter-10 (23-flip @10491: b0 03/b1 10;
  edges 8/10 rows).
- 10501..10526: body (b0 83/b1 00; edges 10505..10526;
  b5 51->52 @10496). window cuts body (extend on demand).
- b4 ramp. split: ..10472 / 10473..10500 / 10501...
