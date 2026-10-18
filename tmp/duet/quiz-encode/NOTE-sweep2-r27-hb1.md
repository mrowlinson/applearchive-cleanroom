# NOTE-sweep2-r27-hb1
- BOOT: shell up, WT clean lanes/encode-sweep2@d56ce19, NVME ok, TMPDIR r27 made.
- Read: r26-HANDOFF, PARENT-070/071/074(cap=exit), CLAIM/GATE-df1c35b, hb1-9.
- Queue: b216 f501344 T10P150 (n<=69028, 904 tiers, 68937..69028, 92n) first;
  backlog b218 1a423eb (+b220 f1b8d9f, b222 96e68e8).
- Range: lo=68937=b215-ceiling 68936+1, verified vs 6b2a92c msg (T10R147
  n<=68936); matches writer 8b279aa (68937..69028).
- Lane-diff vs 0f910af: rgramc.c only +1611/-1150, wall 0.
- Rival: 0 CLAIM/GATE/VERIFY on f501344/1a423eb (VERIFY-46db216 = w2 T8
  head false-positive, same as r26). Turf clean.
- Next: CLAIM-sweep2-f501344, battery launch, tables-new first-hand.
