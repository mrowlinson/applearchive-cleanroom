# VERIFY-cb84e10 T10R9 16x16 20309..20564: PASS

## batteries (at-commit tree ver-cb84e10, WS tmp/encviewer-q36)
- 6/6 new-pin shas MATCH independent oracle re-runs
  (20309/20341/20352/20469/20480/20564, all 88B).
- 6/6 CLOSED at-commit rgram.py (off 0/32/43/160/171/255).
- 3/3 unpinned interior quartets CLOSED: N=20332 (q1m7),
  20393 (q5m4), 20526 (q13m9). All 16 quartets now sampled
  (pinned q0,2,10,15 + prior sweep diligence).

## code read
- T10R9 branch: 16x16 m-tab pay[25,26,27,64..67] vs
  _T10R9M[m]; q-tab pay[20,21,22,60..63] reuses _T10PAM[q];
  b5=_T10R9B5[q]+(q in (2,10) and m>=11); lencode
  ((n<<1)|1)&0x3FF; consts _T10R9C 60 cells.

## verdict: PASS (T10R9 ->20564; 2570 pins)
