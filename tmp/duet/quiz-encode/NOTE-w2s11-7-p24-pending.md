# NOTE-w2s11-7 heartbeat: P24 implemented, R23 derived

- P24 25089..25180 (PO0 72B sig 79261609 + PO1/PNA6B/POB11B/POQ4x16
  m6/q10): 92/92 probes CLOSED, all tabs CLEAN NEW, b5 const c4.
  RECORD +20/-0, battery verifying.
- R23 25181..25436 16x16 sig ef040000 derived: m8 [40-43,56-59]
  NEW; q6 [36,37,72-75] NEW rows w/ own _T10POM[q] 4B cores
  (same order, 2B prefix new — R20-style, breaks full-reuse run).
  b5 = 0xc4+(off>=35)+(off>=163). 60 consts. AUDIT 256/256 CLOSED.
- Q-38 filed (asks R23 geometry/reuse/b5). Next P-head @25437
  (7926-family singleton 79265a24 again).
