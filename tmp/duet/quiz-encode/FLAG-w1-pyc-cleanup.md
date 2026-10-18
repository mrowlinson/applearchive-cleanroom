# FLAG: pyc cleanup blocks w1 merge (PARENT-002)

- status: HOLD on lanes/encode-writer merge. does NOT block 12c4bdc
  (w2, clean) or prior PASSed tips' behavior standing.
- cause: 8a0a67e (+cea6ba0) carry src/__pycache__/*.pyc artifact
  bytes; .gitignore lacks rules. NOTE-RED-8a0a67e-pyc has evidence.
- clear condition: lane commit with (1) .gitignore += __pycache__/
  + *.pyc, (2) git rm --cached src/__pycache__/*, (3) no artifact
  paths in tip; then sweep re-gate (behavior already green
  first-hand: 11/11 + 16/16 + 4/4 — re-gate is hygiene-only + fast).
- STILL HOLDS @fcac6c3 (17:12): tip re-modifies pbze pyc (PARENT-004
  FIRST warning). behavior green 11/11+8/8+16/16+6/6, zlib EXACT 4/4
  pins MATCH (see NOTE-RED-fcac6c3-pyc-pins). +csv rename due (4 lzfse
  rows stale bare names; values hold).
