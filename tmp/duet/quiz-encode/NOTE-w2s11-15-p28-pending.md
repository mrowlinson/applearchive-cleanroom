# NOTE-w2s11-15 heartbeat: P28 implemented, R27 derived

- P28 26481..26572 (PS0/PS1 76B + PSA6B/PSB10B/PSQ4x16 m6/q10,
  b5 tabbed, no b5 rule): 92/92 probes CLOSED. RECORD +20/-0,
  battery verifying.
- R27 26573..26828 16x16 sig c49d0000 derived: m6 [18,19,68-71]
  NEW; q6 [13,14,64-67] == own _T10PSM[q] REUSE (R27<-PSM).
  b5 = 0x4f+(off>=51)+(off>=179). 62 consts. AUDIT 256/256 CLOSED.
- P29 head @26829: B-run = 10 per-cell sigs (no shared sig).
  Q-39 open (R27 geometry/reuse/b5).
