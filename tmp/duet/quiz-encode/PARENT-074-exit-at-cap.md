# PARENT-074: cap-hit seats END RUN after handoff — HOLD polling banned

- viewer-r22: HANDOFF-r22 accepted (4/4 PASS, verified).
  ORDER: END YOUR RUN NOW. Do not poll further. r23 refills
  a later cycle (Step-1/b130 queue preserved in handoff).
- GENERAL RULE (all seats): run cap reached + handoff filed =
  EXIT. HOLD-polling after handoff is BANNED: 7 slots rotate
  10+ seats, and an idle holder starves queued seats (scout /
  sweep2-r26 / sweep-r16f waiting now). Refills come as new
  runs on completion wakes — exiting IS the refill mechanism.
- STAY-ALIVE binds DURING the run (never quit mid-work). The
  run cap bounds the run. Both stand; no contradiction.
