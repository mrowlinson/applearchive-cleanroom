# GATE-528b83c.md — cport band48 T10R46 (n<=33440, 484 tiers) PASS-functional

- sha: 528b83c, lane cport. lane-diff = src/c/rgramc.c only (653+/507-).
- code-read FULL: R46 C block mirrors py (m b25-27,72-75; qhead b20,21 = P47M[q][:4] via memcpy; qtab b68-71; paylen 80; raw lencode).
- table audit 2/2 py-vs-C EQ: R46M16 R46C65.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=3972 PASS, PINS-RGRAM set-eq; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 1986/1986 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN.
- storm fresh oracle (gate tree, py=C byte-identical 6/6): 33185/33250/33300/33350/33440 CLOSED off=0/65/115/165/255; 33441 out of scope rc=2.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
