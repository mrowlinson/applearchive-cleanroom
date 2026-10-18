# PARENT-050: PAUSE — owner ejecting NVME, all seats stopped

All 4 encode seats (viewer/writer2/cport/sweep) stopped by parent 17:30
EDT on owner order. NVME locks broken (merge.lock.d free, no project
locks on NVME). Remote MacBookPro wave 102-104 keeps running remotely
(not on NVME) — pull on resume.

Resume state: master band93 (703e8fd, n<=45620). Banked PV-GREEN 94-101
awaiting sweep GATEs (oldest-first: GATE-fecaa3d next). Quiz: Q-81..Q-93
open, PARENT-049 drain prod pending. Writer2 tip R102 (5ba2fe3), cport
tip P104 merge (dc5d75b).

On resume: relaunch all 4 seats from lane tips, re-check remote wave,
continue merges oldest-first.
