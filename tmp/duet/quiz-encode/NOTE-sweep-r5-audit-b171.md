# NOTE-sweep-r5-audit-b171: independent fresh-oracle re-confirm

- Seat-private rebuild of b171 rgramc (cc -O2 -Wall -Wextra
  -std=c11, rc=0, 0 warnings) + fresh compression_tool oracle
  over 61025..61280: 256 pass / 0 fail, new pins 24/24.
- Confirms GATE-4313f54 (r2) first-hand. Logs: NVME
  encode-sweep/r5-audit-b171/ (result.txt + g*.rav/out).
- (First attempt died on my sparse-extract harness bug —
  missing rgramc.h — rebuilt with header; this result is the
  clean rerun.)
