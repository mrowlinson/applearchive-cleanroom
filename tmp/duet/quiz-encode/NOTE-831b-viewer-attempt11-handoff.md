# NOTE-831b viewer attempt11 HANDOFF (successor: overwrite claim, continue)

## session record (attempt11)
- 16 PREs filed: PRE-1170b (R 31793) .. PRE-1185b (P51 34485).
  zones closed: R31793/P44/R32141/P45/R32489-96/P46/R32837-96/
  P47/R33185-96/P48/R33533-96/P49/R33881-96/P50/R34229-96/P51.
- 2 VERIFYs, both PASS: VERIFY-5d1715c (8/8 + 256/256, b5
  exact vs own census), VERIFY-2da13fb (10/10 + 92/92, b5
  split verified in lits). 0 new Q (newest Q-36 CLOSED).
  w2 tip at end: 2da13fb (P14 ->21700).
- ~3400 oracle runs + ~360 VERIFY runs. no joint DONE (w2
  active) — seat stays alive, keep mapping + VERIFY per tip.

## resume state for attempt12
- FRONTIER: 34577+ sig 6c000000 96B (34577..34600 on disk,
  all same). expect R 16x16 ->34832. next: probe extent,
  then census + PRE-1186b. NOTE numbering: next NOTE-832b.
- CENSUS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encviewer-q37/
  cN.rav continuous 20913..34600. oracle: head -c N /dev/zero |
  compression_tool -encode -a lzraven. pay = raw[12:-4].
- 96B-ERA ANALYSIS: rzone/phead template scripts assume 76B pay —
  96B zones + mixed heads need custom inline surveys (pattern:
  VPOS sweep -> q/m split -> tabs -> b4/b5 exact -> reuse vs
  prior-m -> PBB-vpos-first + dips + B-Q on shared pos). see
  this shift's PREs 1174b..1185b for shapes.
- NEXT REUSE REF: P51 m-tab PRE-1185b (6B pos[41,42,76..79]):
  1bbe73b7e9f5/1bbe8937552c/29be48f995e0/33be21f7a66e/
  33be73fbbf91/33be1ff9d091/6cbe85ba98ab/6dbe11fd4985/
  6dbe02bd8388/6dbe9bf98388/11de707aa6df/12de17bb83fc/
  37de38f9ccd1/42de2279dcca/62de70f9aa81/6cde447992eb.
- WATCHES: BOTH-byte full-dump on new (seen 14/25/32/40 + b5-
  BOTH twice); B-Q fit 9 instances (report LCS>=3 + positions);
  PBB sig bytes in/out varies (check first); SPLIT q-tabs in R
  (full+PFX/6B/4B/2B+full/3B+1B+4B-infix/verbatim seen); dips
  (FIRST LCR3 hit 34493 vs E1 — P-heads now dip-active?).
- REUSE corpus: writer2 worktree src/rgram.py hex lits (scan in
  scripts auto-picks current tip; writer SHIPS, corpus grows).
- VERIFY duty: poll lanes/encode-writer2 (+writer1) tip every turn;
  at-commit tree (git archive) battery + independent oracle sha.
- WALL: answers BEHAVIOR-ONLY (beds+numbers). heartbeat NOTE ~10 calls.
  PARENT-027: TMPDIR seat dir, NEVER /tmp.
