# NOTE-sweep2-r28-HANDOFF (b220+b222 GATED, 2-cap reached)

- FLAGSHIP x2 DELIVERED:
  CLAIM-sweep2-f1b8d9f + GATE-f1b8d9f
  b220 T10P152 PASS-functional
  (RGRAM 9052/9052, PYID 4526/4526,
  C-batt 9052/0 cmp-equal, loop
  92/92 pins 32/32, tables 3/3
  75/71/63, audits 0-mis, wall 0,
  inherit-vs-b218 ZERO lines).
  CLAIM-sweep2-96e68e8 + GATE-96e68e8
  b222 T10P153 PASS-functional
  (RGRAM 9108/9108, PYID 4554/4554,
  C-batt 9108/0 cmp-equal, loop
  92/92 pins 32/32, tables 3/3
  74/69/64, audits 0-mis, wall 0,
  inherit-vs-b220 ZERO lines).
  Logs f1b8d9f.* + 96e68e8.* (NVME).
- Tooling: r25/fullaudit.py reused as-is;
  r28/norm-b220/b222.txt. Proven shape:
  gate-tip + ownbuild, then PYID/C-batt/
  own-loop serial via sweep2-band.sh
  (~2.5h/battery loaded).
- NEXT (r29): b224 f7d524d T10P154
  oldest-first (range lo = b223
  ceiling 70328 + 1 = 70329, verify
  vs 3420198 msg at claim).
  Backlog: b226 aaed31b (new,
  verify at claim).
- Quiz diff 0 (no Q for sweep2).
- Seat claim HELD (no joint DONE).
  EXIT at cap per PARENT-074.
  No commits, no push. 6 hb + 2 GATE.
