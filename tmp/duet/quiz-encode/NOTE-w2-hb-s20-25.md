# NOTE-w2-hb-s20-25: P130 COMMITTED, R128 RECORD running, R187 staged

- P130 RECORD first-hand: RC=0 RGRAM-GREEN 0
  FAIL. Pins REVIEW: 0 removals, +24 lines =
  12 new sizes exact. DET-P130 12/12.
  Committed 35a659c (py+PINS+test). 3 commits
  this run (P129, R127, P130).
- R128: applied r128-patch.txt via apply-one
  (7/40/42) + 12 test cells; WT == staged
  rgram-p130r128.py (blank-lines only);
  smoke CLOSED both edges. RECORD launched
  bat-r128-full (bg).
- Mapped R187 @82601: census 256+4; TWO-SIG
  zone (new R-variant: sig q<8/q>=8 + b23
  half-byte ac/d2); m-tab 6B ALL NEW; q-tab
  7B reuse 5/7 (tails + b31==P-b32; q-b21,22
  novel 0/16 pos+set; 129th); edges
  82688/82816; 0 stragglers. Staged
  w19-try-r187.py, sweep 256/256 err0 (after
  1 fix: b23 half-rule). Filed Q-251.
  Frontier P190 @82857 (PB0 REPEAT; PB1
  ==P189 SING).
- Streak 50 (A-253/254 pending). No joint DONE.
