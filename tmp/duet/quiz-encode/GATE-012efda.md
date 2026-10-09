# GATE-012efda.md — w2 R64 (39385..39704, A64+B256 80B) PASS-individual

- sha: 012efda, lane w2. tiers: A 4x16 m-tab b6,7,72-75 + q-tab b37-39,45-47,76-79; B 16x16 m-tab b13,14,72-75 + q=AM b6,7,68-71. raw lencode both.
- AST: AM16 w12 uniq, AQ4 w20 uniq, BM16 w12 uniq; AC62/BC66 sorted/nodup; const-vs-tab disjoint + FULL cover80 both.
- gate-tip.sh RC=0: RGRAM n=4704 PASS, PINS-RGRAM set-eq 4704/4704, LIBCOMPRESSION zero-refs, ADOPT match. 13 new pins x2 rows.
- storm fresh oracle (gate tree): 39385/39386/39401/39433/39448 A off=0/1/16/48/63, 39449/39450/39550/39703/39704 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 39384 -> T10P65B off=9; 39705 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
