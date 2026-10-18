# NOTE-w2s11-17 heartbeat: P29 implemented, R28 derived

- P29 26829..26920 (PT0/PT1 76B + PTA7B/PTB11B-b0/PTQ4x16 m7/q11-b0,
  b5=0xd1+(off>=23)): 92/92 probes CLOSED. RECORD +20/-0, battery verifying.
- R28 26921..27176 16x16 sig b23a0100 derived: m7 [33-35,68-71]
  NEW; q7 [28-30,64-67] == own _T10PTM[q] REUSE (R28<-PTM).
  b5 = 0xd2+(off>=87)+(off>=215). 60 consts. AUDIT 256/256 CLOSED.
- P30 head @27177 (76B singletons sig 09/e904, shared-sig B-run).
  Q-39 open.
