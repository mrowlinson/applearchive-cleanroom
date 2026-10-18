# FLAG: tmp/scratch cleanup blocks w2 merge (PARENT-005)

- status: HOLD on lanes/encode-writer2 merge @239a401.
  does NOT block w1 (e72aa4c clean) or behavior standing
  (71/71 green first-hand, see NOTE-RED-239a401-tmp).
- cause: tip carries tmp/scratch-encode2/* (probes +
  RESULTS). scratch lives UNTRACKED per PARENT-005.
- clear condition: lane commit with git rm -r --cached
  tmp/scratch-* + no tmp/scratch-* in tip; then sweep
  re-gate (behavior already green: re-gate is hygiene +
  fast). future tips with tmp/scratch-* FAIL on land.
