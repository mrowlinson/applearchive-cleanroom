# NOTE-w2s6-13 writer2: T3-44 recon + op3=220 SHARED resync (Q-25 filed)

## T3-44 tier (N=512..820, 309/309 dumped, paylen 44 const)
- edge 820/821 bisected (44->48). L10 (bits32-41) = (off<<1)|1 EXACT 0/309.
- 106 varying bits; background 3-7b/off (length+echo counting).
- period-64 combs (8-9b): 25/89/153 + 64/128/192. cascade 217-245
  (32/14/18/11/23/... bits) + late edges 256/261/277/293.

## Cross-tier: op3=220 shared, op3=156 coincidence
- off=217: T2n=23 vs T3n=32, OVERLAP 15 (52-54,98,245-247,250,253,
  337,340,343,346,350) = shared resync complex (mid-counter + tail +
  far-tail). T3 adds head/extras.
- off=153: T2n=20 vs T3n=8, overlap 1 (length only) = DISJOINT.
- Q-25 filed (which field saturates at 220 — needs viewer bearings).

## Full T3 decode queued for successor (dumps t2.bin/t3.bin kept in
bed-w2s6-seg/). T3 rgram branch waits on formulas.
