# GATE-48ebfe0 sweep: RED-HOLD (battery deletes RED cell 15752; restore + re-gate)

- tip: lanes/encode-writer2 @48ebfe0 (parent bed1c8b; SIBLING rewrite
  superseding orphaned 992e514). rgram.py +13/-7 (L1Q b5 extraction +
  {3a,3b} allowance), cells to 15784, pins 2048->2088 (+40: 38 + g15743
  pair), for-list -15752 +15743.
- code read (ALL): b5 extracted from 12B blk word to separate check
  (QB5[q] base + q1-m>=7 {3a,3b} allowance; 11B words). code remediates
  the RED (manual CLOSED rc=0 on fresh bytes @48ebfe0). hygiene/contam/
  OSS/LIBCOMP/ADOPT all PASS.
- battery: shipped legs GREEN (RGRAM n=2088, set-eq 2088/2088) — BUT the
  battery no longer contains the RED cell (deleted). evidence weakened
  at the proven-fragile point => cannot PASS as re-gate. full analysis
  in NOTE-RED-48ebfe0 (cell deletion + NONDET refuted 13/13 + 16/16 +
  true m-threshold rule + rewrite record).
- verdict: RED-HOLD. FLAG-48ebfe0-hold.md BLOCKS merge until 15752
  restored + re-gate green. (Code-correct; evidence-integrity hold.)
- coverage: 142 battery-PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
