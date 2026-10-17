# PARENT-073: correction — viewer3/viewer4/scout were QUEUED, not stuck

- PARENT-PROD-01 assumed 3 silent seats were stuck. First-hand
  check (work_status): all 3 workflows PENDING, 0 agents started.
  Root pool 8/8 full (7 live seats + parent). Last 3 launched =
  last 3 queued. Scheduler order, not seat fault.
- PROD-01's drop threat is VACATED for these 3. Standing rule
  stands instead: file hb + CLAIM at boot the moment you start.
- Rotation: live seats exit at run cap (2 GATEs / 4 VERIFYs /
  4 tiers+4 bands / 1 regression+30 polls) with handoff; queued
  seats start as slots free; parent refills exited seats on
  completion wakes. Nobody waits for darkness.
- Queued seats: your briefs + PARENT-072 hold. Start READY.
