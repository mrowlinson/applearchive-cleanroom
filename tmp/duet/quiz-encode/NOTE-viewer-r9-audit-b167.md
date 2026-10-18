# NOTE-viewer-r9-audit-b167 (encode viewer r9 re-audit, GREEN)

Band167 86ae4e6 T10R123 (merged):
fresh-oracle own-loop 60329..60584
first-hand vs merged master e7d64b3
(own build cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings; fresh
.rav bed audit-r9/b167).
- py+C agree CLOSED: pass=256 fail=0.
- Pins: 24/24 (closed+sha, fresh .rav
  hashes match).
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
VERDICT: GREEN, no drift.
