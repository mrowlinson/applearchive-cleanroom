# NOTE-w2s7-12 writer2: T4A shipped 52633d2 (122 pins, 257/257 fresh)

- rgram T4A branch (N 821..1076, off=N-821): unified L10=((N<<1)|1)&0x3FF
  + b5hi + 1024-flip bytes (b0/b8/b11/b15/b45) + b19/b27/b31 counters +
  38 consts. T0-T3 branches length-gated 44 (48 now passes through).
- dip1077: 44B literal pin (formula OPEN) + sha cell. T4A-FULL 257/257
  fresh CLOSED. pins append-only (+18, 0 churn). all suites GREEN.
- lane tip 52633d2. Q-29 (dipselect) open. next: plateau B/C (off 257..603).
