# GATE-4b20deb.md — w2 R65 (39733..40052, A64+B256 80B) PASS-individual

- sha: 4b20deb, lane w2. tiers: A 4x16 m-tab b24,72-75 + q-tab b0,10,11,18-21,76-79; B 16x16 m-tab b22,29-31,72-75 + q=AM b24,68-71. raw lencode both.
- AST: AM16 w10 uniq, AQ4 w22 uniq, BM16 w16 uniq; AC62/BC65 sorted/nodup; const-vs-tab disjoint + FULL cover80 both.
- gate-tip.sh RC=0 GATE-PASS: HYGIENE/CONTAM/LIBCOMPRESSION all PASS, ADOPT match; RGRAM n=4750 PASS, PINS-RGRAM set-eq 4750/4750; SMOKE/OUTER2/RB2/RAVFRAME PASS + pinsets eq.
- pins: +26 rows (13N x closed+sha).
- storm fresh oracle (gate tree): 39733/39734/39749/39781/39796 A off=0/1/16/48/63, 39797/39798/39898/40051/40052 B off=0/1/101/254/255 — all CLOSED rc=0.
- boundaries: 39732 -> T10P66B off=9; 40053 -> N out of scope rc=2. exact.
- wall-grep lane-diff: 0 hits.
- verdict: PASS-individual. no FLAG.
