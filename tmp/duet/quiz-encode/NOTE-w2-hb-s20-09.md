# NOTE-w2-hb-s20-09: R179 staged+Q-235, R127 RECORD 36%

- Mapped R179 @79817 first-hand: census 256 +
  4 probe; single sig 274f4802; CLASSIC
  layout returns (tails-swap ends): m-tab 6B
  b37,38,76-79 in place ALL NEW; q-tab 8B
  b21-23,31,72-75 relocated; q-reuse 5/8
  from P181M (tails 16/16 + b31==P-b32;
  q-b21,22,23 novel; R171-style 121st);
  b4=(0x93+2off); b5=0x6f+(off>=55)+
  (off>=183); edges 79872/80000; 0
  stragglers. Staged w19-try-r179.py, sweep
  256/256 err0. Filed Q-235. Frontier P182
  @80073 (PB0 ce020000 NEW; PB1 == P181 SING
  sig).
- WT: R127 RECORD 2806 REC/0 FAIL (~36%, at
  g-z22744). Streak 36 (A-239/240 pending).
  No joint DONE.
