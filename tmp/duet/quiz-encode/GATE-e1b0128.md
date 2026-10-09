# GATE-e1b0128.md — cport band45 T10R44 (n<=32744, 471 tiers) PASS-functional

- sha: e1b0128, lane cport. lane-diff = src/c/rgramc.c only (659+/495- transpiler regen).
- code-read FULL: R44 C block mirrors py (paylen 80, raw lencode, m b36,72-75, qhead b18,19,29, qtab b30,31,68-71 = _T10P45M[q]+2, const loop, CLOSED print).
- table audit: _T10R44M 16/16 EQ, _T10R44QH 16/16 EQ, _T10R44C 64/64 EQ py-vs-C.
- gate-tip.sh: C-BUILD PASS 0w, RGRAM n=3892 PASS, PINS-RGRAM set-eq, PINS-RAWENC/PBZE(-C) PASS; HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited (selfgen .aar / spec prose / aad.c — all outside lane-diff) per PARENT-032 remedy b. no FLAG.
- parity: RGRAMC-PYID 1946/1946 covered GREEN (own run, gate tree).
- C-side RGRAM battery (RGRAM_BIN=C): RGRAM-GREEN incl g-z32744.
- storm fresh oracle (gate tree, py=C byte-identical): 32489/32550/32600/32650/32700/32744 CLOSED off=0/61/111/161/211/255 rc=0; 32745 out of scope rc=2. 7/7.
- wall-grep: 0 hits.
- verdict: PASS-functional. no FLAG.
