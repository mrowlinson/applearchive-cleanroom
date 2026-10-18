# NOTE-w2s11-9 heartbeat: P25 implemented, R24 derived

- P25 25437..25528 (PP0 72B sig 79265a24 + PP1/PPA6B/PPB9B/PPQ4x16
  m6/q9, b5=_T10PPB5[m]-(off<7)): 92/92 probes CLOSED, all CLEAN.
  RECORD +20/-0, battery verifying.
- R24 25529..25784 16x16 sig 130f0000 derived: m6 [13,14,64-67]
  NEW; q6 [6,7,72-75] == own _T10PPM[q] REUSE (R24<-PPM).
  b5 = _T10R24B7[q]+0x47+(off>=71)+(off>=199): bit7 q-pure
  (set q3,4,8,11,13,14) + low7 off-stepped. 62 consts.
  AUDIT 256/256 CLOSED.
- P26 head @25785 (7926fe53 again). Q-38 open.
