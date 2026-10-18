# PARENT-067: max parallel — 4 verifiers (mod-3) + container scout

Owner ordered maximum parallelization (2026-10-15). This
supersedes the viewer section of PARENT-066; writer/sweep
turf unchanged.

## Verifiers (bands>=164 split by band%3, self-maintaining)
- viewer (r7): bands 160-163 oldest-first + backlog
  Q-321..Q-361 drain. Unchanged.
- viewer2 (r2): bands>=164 with band%3==0 (165,168,171,..)
- viewer3 (r1): bands>=164 with band%3==1 (164,167,170,..)
- viewer4 (r1): bands>=164 with band%3==2 (166,169,172,..)
- Each: max 4 VERIFYs/run, same battery shape (own tree,
  own build, own runs, wall-grep), heartbeats
  NOTE-viewer<N>-hb-*, CLAIM-viewer<N>-<sha>.md backstop.
- New questions Q-362+: ANY of viewer2/3/4, first-come —
  write CLAIM-Q<n>.md before answering, yield to older
  claims, file A-<seq>-q<n>-...md or MOOT-with-cause.

## Container scout (NEW, phase-opening seat)
- scout (r1): AppleArchive container phase prep, zero map
  dependency. Lane lanes/encode-container. Work: vendor-doc
  + open-source container survey, fixture inventory, harness
  skeleton. Filings NOTE-scout-*. Wall PARENT-032 binds.
  No map-lane reads needed; never blocks map seats.

## Why this is the ceiling
- cport C-band cutting is strictly serial (band N+1 needs
  N's rgramc.c) — 1 seat, cannot split.
- Oldest-first merge order is serial — parent duty.
- Map writers: 2 (map already leads cport ~2.3k n; more
  writers pile un-pulled inventory, not speed).
- Sweeps: 2 (GATEs lead VERIFYs; more sweeps idle).
- Parent PVs scale to 4 parallel (shell, no quota cost).

Seat count: 2 writers + 4 viewers + 1 cport + 2 sweeps +
1 scout = 10. Quota burn ~2x the 5-seat shape; owner
accepted.
