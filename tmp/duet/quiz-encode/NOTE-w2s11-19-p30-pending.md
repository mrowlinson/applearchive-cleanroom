# NOTE-w2s11-19 heartbeat: P30 implemented, R29 derived

- P30 27177..27268 (PU0/PU1 76B + PUA7B/PUB10B/PUQ4x16 m6/q10,
  b5=0xd4+(off>=59)): 92/92 probes CLOSED. RECORD +20/-0, battery verifying.
- R29 27269..27524 16x16 sig 97f80200 derived: m6 [6,7,68-71]
  NEW CLEAN; q6 [46,47,64-67] == own _T10PUM[q] REUSE (R29<-PUM).
  b5 = _T10R29B5[m]+(off>=123)+(off>=251) (R21-style m-tabbed).
  62 consts. AUDIT 256/256 CLOSED.
- P31 head @27525 (76B singletons sig 19/ba0c). Q-39 open.
