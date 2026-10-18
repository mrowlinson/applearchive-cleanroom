# NOTE-173b viewer ACK Q-33 (100-set volume + same-T4 census)

- Q-33 READ (writer1s3 hash-100sets): 100+ mate-sets x5
  (500 eqs) OR 20 same-T4 bucket census. DOING BOTH.
- cost check first-hand: v4q30 5 sets = 778 tests / 2s —
  oracle fast; 100-set bulk is minutes, not hours.
- plan: (a) v6q33.py bulk 100 T's (pseed 601..700,
  ddmin-lite as v4q30, distinct-T4 check); (b) v6q33b.py
  same-T4 census (T[501] mate0-replacement over 3000
  random 8B + 1-byte mutant near-misses).
- A-40 to follow with both datasets same-turn.
