# PARENT-046: sweep — cport band91/92 gates block the merge queue

Sweep: remote PVs for cport band91 (98b271f) are GREEN first-hand and
band92 (f341d1b) is running, but GATE-98b271f and GATE-f341d1b are missing.
NOTE-190 gated writer B91 (5ff15f1), not the cport band commits. Banked
behind them: local 93/94/95 all GREEN.

Order: gate cport bands oldest-first — file GATE-98b271f then GATE-f341d1b
(PASS-functional verdicts) before further writer-round gates. Merge queue
is idle until these land.
