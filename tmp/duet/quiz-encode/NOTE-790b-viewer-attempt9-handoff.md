# NOTE-790b viewer attempt9 HANDOFF (successor: overwrite claim, continue)

## session record (attempt9)
- 16 PREs filed: PRE-1132b (R 25181) .. PRE-1147b (P32 27873).
  zones closed: R25181/P25/R25529/P26/R25877/P27/R26225/P28/
  R26573/P29/R26921/P30/R27269/P31/R27617/P32.
- 0 VERIFYs (no new w1/w2 commits all shift: w1=94c8d61,
  w2=7558ede). 0 new Q (newest Q-36 CLOSED). w2 attempt#10 live
  (T10R10 deriving, NOTE-w2s10-2 read — no action needed).
- 2736 fresh oracle runs + ~60 probes. no joint DONE (w2 active)
  — seat stays alive, keep mapping + VERIFY per tip.

## resume state for attempt10
- FRONTIER: 27965+ sig f18b0800, extend unknown. next: probe extent
  (expect R 16x16 ->28220), then census + PRE-1148b. NOTE numbering:
  next NOTE-791b.
- CENSUS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encviewer-q37/
  cN.rav continuous 20913..27964. oracle: head -c N /dev/zero |
  compression_tool -encode -a lzraven. pay = raw[12:-4].
- SCRIPTS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/
  q38-rzoneNNNN.py (per-zone, sed-clone + prior-m patch) +
  q38-pheadNNNN.py (PARAM template: PB0/PBA0/PBB0/N0 header line).
  PBB vpos varies on mixed-sig heads — check vpos first (P29/P32
  include sig bytes; P30 PBB vpos == QPOS).
- REUSE corpus: writer2 worktree src/rgram.py hex lits (scan in
  scripts auto-picks current tip; writer SHIPS, corpus grows).
- VERIFY duty: poll lanes/encode-writer2 (+writer1) tip every turn;
  at-commit tree (git archive) battery + independent oracle sha.
- WALL: answers BEHAVIOR-ONLY (beds+numbers). heartbeat NOTE ~10 calls.
