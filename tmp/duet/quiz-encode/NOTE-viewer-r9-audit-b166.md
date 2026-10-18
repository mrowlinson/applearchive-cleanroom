# NOTE-viewer-r9-audit-b166 (encode viewer r9 re-audit, GREEN)

Band166 3504728 T10P125 (merged):
fresh-oracle own-loop 60237..60328
first-hand vs merged master e7d64b3
(own build cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings; fresh
.rav bed audit-r9/b166).
- py+C agree CLOSED: pass=92 fail=0.
- Pins: 24/24 (closed+sha, fresh .rav
  hashes match).
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
VERDICT: GREEN, no drift.
