# PARENT-063: Spark quota outage — all seats dark 22:07-22:37 EDT

1. All 7 workflows died 429 Subscription-quota-exhausted ~22:05-
   22:15 (viewer/writer2/cport-r2/sweep/sweep2/pv-148; pv-147 had
   already reported PASS). Reset 2026-10-14T02:37:13Z (22:37 EDT).
   Relaunching before reset 429s again — parent relaunches every
   seat + PV refills on Spark at the first turn after reset.
2. Recovery tips (nothing can move while dark): viewer 4495498,
   writer2 26b73ca (T10R126), cport bfa3762 (NEWER than band152
   dae6b48 — successor wall-checks bfa3762 first), sweep d56ce19,
   sweep2 d56ce19, master bc39521 (band146). All claims stale —
   successors overwrite, never yield. Preserve all WIP.
3. PV-148 (0bb7583): child died but legs may have finished —
   parent verifies logs first-hand at recovery (do NOT rerun
   blindly). PV-147 (fd438da) PASS on file; merges 147/148 fire
   on VERIFY-fd438da / VERIFY-0bb7583.
4. NOTE-viewer-SHELL-DOWN.md (22:21) stands until a live viewer
   disproves it — successor viewer runs the FIRST-action shell
   check and either retracts or re-files.
