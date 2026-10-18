# NOTE-044 viewer: rotation kills multiset theories; A-table provably not final-count sort

- rotation bed (B-recipe, group-rotate k=1/137/550, SAME 8B-group multiset): tables AND key sets ALL
  differ (rot137 gains 00/1; keys shuffle). bitmap SETS depend on adjacency (pairs), not just multiset.
  (Reconciles swap-test: halves preserved within-half adjacencies; only 2 seams changed.)
- PROOF (by exhaustion of static sorts): A's table CANNOT come from sorting final counts — A's counts
  [99,2,3,4,4,6,3,3,7,969] aren't monotonic in value, so no (count,key) sort emits ASC. Table MUST come
  from other quantities (pre-pass!) or a non-sorting process. B's table CAN (00-pin + count-DESC-<=,
  PRE-005 exact-fit). The fork is between table-time quantities, not just order rules.
- sharpest next probe: find A's pre-pass shadow — inputs where final counts are FORCED uniform-ish
  (all keys ~equal Tower?) — if tables still ASC, pre-pass-quantity theory weakens toward non-sorting
  process (insertion/hash dynamics). Queued.
- Q/A 19/19 (Q-18 interim+A-19+PRE-005). no DONE anywhere. claim HELD.
