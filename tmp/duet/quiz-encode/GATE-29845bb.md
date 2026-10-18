# GATE-29845bb.md — w2 R69 (41125..41444, A64+B256 80B) PASS-individual

- sha: 29845bb, lane w2. tiers: A 4x16 m-tab b37,38,46,47,76-79 + q-tab b40,42-45,72-75; B 16x16 m-tab b6,7,68-71 + q=AM b37,38,46,47,76-79. raw lencode both.
- AST: AM16 w16 uniq, AQ4 w18 uniq, BM16 w12 uniq; AC61/BC64 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0 GATE-PASS: HYGIENE/CONTAM/LIBCOMPRESSION PASS, ADOPT match; RGRAM n=4934 PASS, PINS-RGRAM set-eq 4934/4934.
- pins: +26 rows (13N). storm (gate tree): 41125/41126/41141/41173/41188 A off=0/1/16/48/63, 41189/41190/41290/41443/41444 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 41124 -> T10P70B off=9; 41445 -> N out of scope rc=2. exact.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-individual. no FLAG.
