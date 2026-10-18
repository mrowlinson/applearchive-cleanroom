# NOTE-w2s11-11 heartbeat: P26 implemented, R25 derived

- P26 25785..25876 (PQ0 72B sig 7926fe53 + PQ1/PQA7B/PQB10B/PQQ4x16
  m7/q10, b5=0xc9+(off>=43)): 92/92 probes CLOSED, all CLEAN.
  RECORD +20/-0, battery verifying.
- R25 25877..26132 16x16 sig 571a0000 derived: m7 [28-30,68-71]
  NEW; q7 [21-23,64-67] == own _T10PQM[q] REUSE (R25<-PQM).
  b5 = 0xca+(off>=107)+(off>=235). 60 consts. AUDIT 256/256 CLOSED.
- P27 head @26133 (NEW 780b12d3 singleton family). Q-38 open.
