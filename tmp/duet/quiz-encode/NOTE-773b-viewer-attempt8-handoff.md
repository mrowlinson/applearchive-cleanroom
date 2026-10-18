# NOTE-773b viewer attempt8 HANDOFF (successor: overwrite claim, continue)

## session record (attempt8, ~09:00-09:15 EDT)
- 19 PREs filed: PRE-1113b (P15 21957) .. PRE-1131b (P24 25089).
  zones closed: P15/R22049/P16/R22397/P17/R22745(76B)/P18(mixed)/
  R23093/P19/R23441/P20/R23789/P21/R24137/P22/R24485/P23/P24.
- 2 VERIFYs: VERIFY-ef1317e PASS (15752 restore; FLAG-lift = sweep
  re-gate) + VERIFY-7558ede PASS (T10P11 Q-36 landing, == A-43).
- 3208 fresh oracle runs. no new Q (newest Q-36 CLOSED). no joint DONE
  (w2 active) — seat stays alive, keep mapping + VERIFY per tip.

## resume state for attempt9
- FRONTIER: 25181+ 76B tier (sig ef040000), 48 cells on disk
  (25181..25228), extends past. next: census 25229+ (expect R 16x16
  ->25436), then PRE-1132b. NOTE numbering: next NOTE-774b.
- CENSUS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encviewer-q37/
  cN.rav continuous 20913..25228. oracle: head -c N /dev/zero |
  compression_tool -encode -a lzraven. pay = raw[12:-4].
- SCRIPTS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-viewer/
  q38-rzoneNNNN.py (per-zone, sed-clone) + q38-phead24045.py (PARAM
  template: PB0/PBA0/PBB0/N0 header line; PBB vpos range 72 vs 76 —
  check PBB paylen first, mixed-size heads vary).
- REUSE corpus: writer2 worktree src/rgram.py hex lits (3786 at
  7558ede; re-poll tip — writer SHIPS, corpus grows, rescan counts).
- VERIFY duty: poll lanes/encode-writer2 tip every turn; at-commit
  tree (git archive) battery + independent oracle sha corroboration.
- WALL: answers BEHAVIOR-ONLY (beds+numbers). heartbeat NOTE ~10 calls.
