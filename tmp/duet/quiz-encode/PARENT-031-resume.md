# PARENT-031: session resume — all 4 encode seats DROPPED + relaunched

Prior parent session died on quota 429 ~12:00; all seats dark ~90min
(>45min line, no DONE). Verdict: viewer/writer2/sweep/cport all
DROPPED, successors relaunched same turn from lane tips.

State at resume: master=91a852c (w2@0949163 T10R19 merged).
w2 tip 5d92e24 (T10P21, 2953 pins) UNGATED. cport tip eb766e3
(band4) + c1/c2/c3 UNGATED. Sweep queue: oldest-first across
w2 + cport. Viewer: verify 5d92e24 + cport commits, answer open Qs.
Decode joint DONE — no decode seats, do not relaunch.

PARENT-027 /tmp ban + TMPDIR=NVME still in force for all seats.
