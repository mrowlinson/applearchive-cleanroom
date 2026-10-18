# NOTE-cport-hb41: 90min handoff, P112 merge staged

- seat agent-1 done, SEAT FREE. tip c56c1e6 (band C139).
- run totals: merges 2 (P111 e5b435f py 6948 + SMOKE fh; R109 c3a7a9b py 6972 + SMOKE fh), bands 2 (C138 b87079a PYID 3474 C+py 6948; C139 c56c1e6 PYID 3486 C+py 6972). all fh, all builds 0w, all regens deterministic no-upto.
- P112 STAGED UNMERGED in worktree (merge -s ours 9b465a7 --no-commit; 3 files M; py+pins == w2 blob, hook intact). regen preview fh rc=0 tables 1983/1987 -> $S/regen-fh-c140.c. pyidb140/corpus seeded.
- successor: py bat $S/p112-py (expect 6996/6996 GREEN) + smoke > commit merge (msg: Merge lanes/encode-writer2@9b465a7 (partial): rgram T10P112 (n<=55804, +2 tiers, +24 pins) ...) > cp regen-fh-c140.c > build-band140 (0w) > C bat (expect 6996) + PYID (expect 3498) + UNITS > commit band140 (n<=55804, 752 tiers).
- w2 tip 60a811d T10P121; backlog 19 (P112..P121) oldest-first. lesson kept: regen WITHOUT --upto; merge = -s ours --no-commit + checkout 2 files + for-line swap.
