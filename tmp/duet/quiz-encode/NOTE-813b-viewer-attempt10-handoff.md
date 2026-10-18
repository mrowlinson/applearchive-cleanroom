# NOTE-813b viewer attempt10 HANDOFF (successor: overwrite claim, continue)

## session record (attempt10)
- 22 PREs filed: PRE-1148b (R 27965) .. PRE-1169b (P43 31701).
  zones closed: R27965/P33/R28313/P34/R28661/P35/R29009/P36/
  R29357/P37/R29705/P38/R30053/P39/R30401/P40/R30749/P41/
  R31097/P42/R31445/P43.
- 4 VERIFYs, all PASS: VERIFY-68ff2b4 (6/6 + 256/256;
  1 PRE-correction to 1106b), VERIFY-9126bc1 (10/10 + 92/92),
  VERIFY-cbbea6e (8/8 + 256/256), VERIFY-30a6964 (10/10 + 92/92,
  landed during handoff). 0 new Q (newest Q-36 CLOSED).
  w2 tip at end: 30a6964 (P13 ->21352, R12 deriving).
- ~9.2k oracle runs + ~150 probes. no joint DONE (w2 active)
  — seat stays alive, keep mapping + VERIFY per tip.

## resume state for attempt11
- FRONTIER: 31793+ sig e389a130, extend unknown. next: probe extent
  (expect R 16x16 ->32048), then census + PRE-1170b. NOTE numbering:
  next NOTE-814b.
- CENSUS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encviewer-q37/
  cN.rav continuous 20913..31792. oracle: head -c N /dev/zero |
  compression_tool -encode -a lzraven. pay = raw[12:-4].
- SCRIPTS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/
  q38-rzoneNNNN.py (per-zone, sed-clone + prior-m patch) +
  q38-pheadNNNN.py (PARAM template: PB0/PBA0/PBB0/N0 header line).
  latest: q38-rzone31445.py, q38-phead31701.py.
- PBB vpos check first on every head (sig bytes in/out varies).
  B/Q fit watch: instances P34/P36/P37/P38/P40/P41 — report LCS>=3
  with exact positions. BOTH-byte watch beyond b4/b5 (pos29/pos17/
  pos21 seen — dump full 4x16/16x16 on any new BOTH).
- SPLIT q-tabs now common in R: check suffix-vs-PRIOR-M at every
  offset (seen: full+PFX, 6B-suffix, 4B-suffix, 2B+full).
- REUSE corpus: writer2 worktree src/rgram.py hex lits (scan in
  scripts auto-picks current tip; writer SHIPS, corpus grows).
- VERIFY duty: poll lanes/encode-writer2 (+writer1) tip every turn;
  at-commit tree (git archive) battery + independent oracle sha.
- WALL: answers BEHAVIOR-ONLY (beds+numbers). heartbeat NOTE ~10 calls.
