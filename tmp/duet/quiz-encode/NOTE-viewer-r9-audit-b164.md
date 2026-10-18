# NOTE-viewer-r9-audit-b164 (encode viewer r9 re-audit, GREEN)

Band164 0133498 T10P124 (merged):
fresh-oracle own-loop 59889..59980
first-hand vs merged master e7d64b3
(own build cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings; fresh
.rav bed audit-r9/b164).
- py+C agree CLOSED: pass=92 fail=0.
- Pins: 28/28 (closed+sha, fresh .rav
  hashes match).
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
VERDICT: GREEN, no drift.
