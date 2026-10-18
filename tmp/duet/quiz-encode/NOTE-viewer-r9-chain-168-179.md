# NOTE-viewer-r9-chain-168-179 (encode viewer r9 status, GREEN)

GATE/VERIFY chain snapshot (read-
only; merge order is parent turf).
Bands 168-172: GV GV GV GV GV —
all 5 merge-ready, VERIFYs all
reconciled by r9 oversight.
Bands 173-179:
- 173 2205fa1 GV (merge-ready)
- 174 9afecce -V (no GATE yet)
- 175 5f9f5a8 GV (merge-ready)
- 176 2551219 -- (nothing filed)
- 177 fe4c199 G- (no VERIFY yet)
- 178 e02b8fe -V (no GATE yet)
- 179 20730c9 -- (just cut)
Claims match mod-turf (v2: 174,
v3: 173, v4: 175+178). -V-before-
G shapes (174, 178) match the
b170 precedent: allowed, merge
waits for GATE. No RED, no
turf violation. r9 re-audits
each band as it merges.
No commits, no push.
