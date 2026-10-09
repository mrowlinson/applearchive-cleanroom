# GATE-804eb41.md — w2 R46 (33185..33440, 16x16 80B) PASS-individual

- sha: 804eb41, lane w2. m-tab 16x7B b25-27,72-75; q=P47M exact: qhead b20,21 = P47M[q][:4], qtab b68-71 = P47M[q][4:]. paylen 80 + raw lencode.
- AST: M16 w14, P47M16 w12 ([:4]/[4:] = 2B+4B exact), C65 sorted/nodup/disjoint/FULL-cover80.
- gate-tip.sh RC=0: RGRAM n=3972 PASS, PINS-RGRAM set-eq, 15 PASS legs, zero FAIL lines.
- storm fresh oracle (gate tree): 33185/33200/33250/33300/33350/33440 CLOSED off=0/15/65/115/165/255 rc=0.
- boundaries: 33184 -> T10P47Q off=63; 33441 -> N out of scope rc=2. exact.
- wall-grep: 0 hits.
- verdict: PASS-individual. no FLAG.
