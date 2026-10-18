# NOTE-w2s9-2-t10p11-coded (encode-writer2 heartbeat)

- Own census 20565..20700 (136 oracle runs, NVME scratch): all 88B/72Bpay.
  Layout confirmed first-hand: PB0 20565, PB1 20566, PBA 20567..20582,
  PBB 20583..20592, PBQ 20593..20656, next zone 20657 (sig 9c2ff600).
- Derived from own bytes: PBA 7B tab 16/16 distinct; PBB 9B tab 10/10;
  PBQ m-tab 7B m-pure 16/16 + distinct, q-tab 9B q-pure 4/4;
  b5 = a0+(q>0 or m==15) 64/64; lencode 136/136. No dips (all 88B).
- Coded tables + 5 branches in rgram.py (mirror T10P10 shape).
- AUDIT first-hand: all 92 cells 20565..20656 CLOSED rc=0 on FRESH oracle
  bytes. Next: for-list +10 probes +20 pins, battery, commit.
