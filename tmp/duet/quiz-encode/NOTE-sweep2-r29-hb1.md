# NOTE-sweep2-r29-hb1
- BOOT: WT clean lanes/encode-sweep2@d56ce19, NVME ok (1.5T avail).
- Read: r28-HANDOFF, PARENT-070/071/074(cap=exit), CLAIM/GATE-f1b8d9f/96e68e8.
- Queue: b224 f7d524d T10P154 (n<=70420, 920 tiers, 70329..70420, 92n)
  first; backlog b226 aaed31b T10P155 (n<=70768, 924 tiers).
- Range: lo=70329=b223-ceiling 70328+1, verified vs 3420198 msg
  (T10R151 n<=70328); matches writer aba4a48 (70329..70420).
- Lane-diff vs 06bd3f5: rgramc.c only +1642/-1177, wall 0.
- Rival: 0 CLAIM/GATE/VERIFY on f7d524d/aaed31b (only cport notes +
  own handoffs mention; no GATE/CLAIM files). Turf clean.
- Next: CLAIM-sweep2-f7d524d, battery launch, tables-new first-hand.
