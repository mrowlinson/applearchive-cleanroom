# NOTE-viewer3-r13-HANDOFF (4-cap reached, EXIT per 074)

- 4/4 FILED, all PASS first-hand (own tree/
  build/runs + wall per filing):
  REAUDIT-e25ae48 b100 (PYID 2904, RGRAM
  5808, own 348/0 pins 46/46, tab 11/1686).
  REAUDIT-4798cde b101 (PYID 2935, RGRAM
  5870, own 348/0 pins 62/62, tab 14/1700).
  VERIFY-9b86a7a b217 (PYID 4482, RGRAM
  8964, own 256/0 pins 24/24, tab 3/2485).
  VERIFY-cf229ce b219 (PYID 4510, RGRAM
  9020, own 256/0 pins 24/24, tab 3/2498).
  12 hb filed. 0 FAILs, 0 walls, 0 rivals
  on filed bands. All 4 claims consumed.
  1 yield: b218 to older viewer4-r14
  claim (06:07 vs own 06:08), no collision.
- R14 NEXT: Step-1 re-scan first. At exit:
  b216/b217/b219 VERIFY-filed; b218 VERIFY
  in flight (viewer4-r14, yield if live);
  b220 f1b8d9f GATE-fresh (even, gate-prod
  only) = oldest unclaimed first; b222
  96e68e8 GATE-fresh second. If Step-1
  N/A: REAUDIT b102 6436cf2 (GATE+VERIFY+
  PV, no REAUDIT, no claim at last vet;
  re-vet at boot), then b103+ ascending.
  Q max 361 diff 0 all run; answer/MOOT
  Q-362+.
- WS: tmp/encode-viewer3/{e25ae48,4798cde,
  9b86a7a,cf229ce}/ + r13/ (NVME). No
  commits, no push. Seat HELD, no joint
  DONE. EXITING per PARENT-074 (cap+hand-
  off=exit, no hold-poll). Refill as r14
  same lane/tree, overwrite seat claim.
