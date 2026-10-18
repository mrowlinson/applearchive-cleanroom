# NOTE-cport-hb40: 90min handoff, P111 merge staged

- seat agent-1 done, SEAT FREE. tip c91ee06 (band C137).
- run totals: bands 2 (C136 80b550e PYID 3449 C+py 6898; C137 c91ee06 PYID 3461 C+py 6922), merges 1 (R108 2aec499 py 6922 + SMOKE fh). all fh, all builds 0w, all regens deterministic no-upto.
- P111 STAGED UNMERGED in worktree (merge -s ours 25e6dd7 --no-commit; 3 files M: +164 py, +26 pins, for-line only; py+pins == w2 blob, hook intact). regen preview fh rc=0 tables 1970/1974 -> $S/regen-fh-c138.c. pyidb138/corpus seeded 3461.
- successor: py bat $S/p111-py (expect 6948/6948 GREEN) + smoke > commit merge (msg: Merge lanes/encode-writer2@25e6dd7 (partial): rgram T10P111 (n<=55456, +2 tiers, +26 pins) ...) > cp regen-fh-c138.c > build-band138 (0w) > C bat (expect 6948) + PYID (expect 3474) + UNITS > commit band138 (n<=55456, 748 tiers).
- w2 tip 5c1f486 T10P120; backlog 19 (P111..P120) oldest-first. lesson kept: regen WITHOUT --upto; merge = -s ours --no-commit + checkout 2 files + for-line swap.
