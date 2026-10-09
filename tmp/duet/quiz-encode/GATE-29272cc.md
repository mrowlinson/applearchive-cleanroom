# GATE-29272cc.md — w2 R45 (32837..33092, 16x16 80B) PASS-individual

- sha: 29272cc, lane w2, regime 80B raw (paylen==80 + raw lencode asserted).
- code-read FULL: m=off&15 q=off>>4; m-tab 16x6B b6,7,72-75; qhead 16x4B b36,37,46,47; q-tail = _T10P46M[q][6:] (b68-71, TAILMATCH reuse).
- AST: M16 w12, QH16 w8, C64 sorted/nodup/disjoint/FULL-cover80; P46M rows len14 so [6:] yields 4B — TAILMATCH 16/16.
- gate-tip.sh RC=0: RGRAM n=3932 PASS, PINS-RGRAM set-eq, OUTER2/RB2/RAVFRAME/PINS PASS, HYGIENE/CONTAM/LIBCOMPRESSION PASS, 15 PASS legs, zero FAIL lines.
- storm fresh oracle (gate tree): 32837/32850/32900/32950/33000/33092 CLOSED off=0/13/63/113/163/255 rc=0.
- boundaries: 32836 -> T10P46Q off=63; 33093 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
