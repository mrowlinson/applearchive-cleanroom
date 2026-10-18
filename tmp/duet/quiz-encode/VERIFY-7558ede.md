# VERIFY-7558ede T10P11 head 20565..20592 + PBQ 20593..20656: PASS

## batteries (at-commit tree ver-7558ede, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (20565/20566/20567/20582/20583/20592/20593/20608/20609/20656, all 88B).
- 10/10 CLOSED at-commit rgram.py (PB0/PB1/PBA off0+15/PBB off0+9/
  PBQ off0+15+16+63 — incl b5-flip pair 20608/20609).
- 5/5 unpinned interior CLOSED: 20570 (PBA), 20588 (PBB), 20600 (q0),
  20630 (q2), 20645 (q3). all 4 quartets sampled (pinned q0,q1,q3 +
  unpinned q2/q3).

## code read vs A-43
- bounds PB0/PB1/PBA16/PBB10/PBQ4x16 = A-43 (28 + 20593) EXACT.
- _T10PBQ rows == A-43 Q0..Q3 byte-for-byte (q1/q3 5B prefix 05e05d5bf).
- b5 = 0xa0+((q>0)or(m==15)): flip at 20608 (q0m15), q1..3 const a1 —
  A-43 rule EXACT. m-tab 7B b40-42,64-67; PBA 7B; PBB 9B.
- diff pure addition: rgram +166, for-list +10 cells, pins +20 rows.

## verdict: PASS (T10P11 ->20656; 2590 pins)
