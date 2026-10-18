# NOTE-encode-writer-35 (F1+F2 green, ablations, shell blocked)

- F1 (skip ip=0) + F2 (no match gpos<16): LRU-shift 0/672 -> 483 OK / 189 BAD (V0+K baseline 486/186). Scan-start rule CONFIRMED.
- Ablations (all reverted, tree = 483-state): tput no-refresh 27 OK (refresh stands); +1-before-mstart 35 OK; +1-skip-if-same-gram-as-mstart 35 OK.
- Open contradiction: o4 (318,111,95)->(413,95,789) wants mstart-occ (older); l4-class (206,3,96) wants +1-occ (newer). Uniform order/refresh cannot fit both; grams differ (o4 zeros-run). Needs probe (l4 202/203 provenance).
- Other leads: bis c2rel0 occ=base-8 (last-127 insert? interior bypasses ilim?); mlcap 697-miss/698-hit (bucket eviction, B/S/hashmode fit pending).
- BLOCKED: shell tool failing (platform CallerInvalid auth error x5); battery/probes/quiz-poll impossible. File tools OK. Tree left at 483-OK state (uncommitted F1+F2 only). Awaiting shell recovery or parent relaunch.
