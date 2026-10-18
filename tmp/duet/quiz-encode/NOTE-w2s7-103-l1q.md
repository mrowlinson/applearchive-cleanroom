# NOTE-w2s7-103-l1q (encode-writer2, own-side heartbeat)

- Shipped `48ebfe0` T9L1 15693..15720 + L1Q 4x16 15721..15784 (2090 pins, GREEN/GREEN, 0 dropped).
- FIRST CONFIRMED ORACLE NONDET (behavior-only, own-side): L1Q q1 m7-15 b5 flips {3a,3b} across runs (dump=3b, fresh-run1=3a, fresh-run2+=3b; stable within a run, 3x identical shas). All other bytes stable.
- Handling: grammar accepts set {3a,3b} (`T9L1Q b5nd`); sha pins avoid nondet rows (15752 dropped → 15743 q1m6 pinned instead).
- Transcription lesson (2x this zone): long hex splits misread (`0ad282`→`c0ad28`, `538ecb`→`c538ec`) — verify word tables against fresh bytes before verify loops.
- Next: map 15785+ (d28 break).
