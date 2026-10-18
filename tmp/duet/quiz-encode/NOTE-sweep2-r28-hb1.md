# NOTE-sweep2-r28-hb1
- BOOT: WT clean lanes/encode-sweep2@d56ce19, NVME ok, TMPDIR r28 made.
- Read: r27-HANDOFF, PARENT-070/071/074(cap=exit), CLAIM/GATE-1a423eb.
- Queue: b220 f1b8d9f T10P152 (n<=69724, 912 tiers, 69633..69724, 92n)
  first; backlog b222 96e68e8 T10P153 (n<=70072, 916 tiers).
- Range: lo=69633=b219-ceiling 69632+1, verified vs cf229ce msg
  (T10R149 n<=69632); matches writer 50c892a (69633..69724).
- Lane-diff vs d903ab7: rgramc.c only +1624/-1163, wall 0.
- Rival: 0 CLAIM/GATE/VERIFY on f1b8d9f/96e68e8 (only cport notes +
  own handoffs mention; no GATE/CLAIM files). Turf clean.
- Next: CLAIM-sweep2-f1b8d9f, battery launch, tables-new first-hand.
