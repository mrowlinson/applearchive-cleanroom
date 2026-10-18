# NOTE-855b viewer attempt12 HANDOFF (successor: overwrite claim, continue)

## session record (attempt12)
- 20 PREs filed: PRE-1186b (R 34577) .. PRE-1205b (P61 37965).
  zones closed: R34577/P52/R34925/P53/R35273/P54/R35621/P55/
  R35969/P56/R36317/P57/R36665/P58/R37013/P59/R37361/P60/
  R37709/P61.
- 2 VERIFYs, both PASS: VERIFY-55fcd0d (256/256 + 10/10 sha,
  R13), VERIFY-6940ea2 (92/92 + 10/10 sha, P15). 0 new Q
  (newest Q-36 CLOSED). w2 tip at end: 6940ea2 (P15 ->22048).
- ~3900 oracle runs + ~380 VERIFY runs. no joint DONE (w2
  active) — seat stays alive, keep mapping + VERIFY per tip.

## resume state for attempt13
- FRONTIER: 38057+ sig 3a680000 96B (38057..38080 on disk,
  all same). expect R 16x16 ->38312. next: probe extent,
  then census + PRE-1206b. NOTE numbering: next NOTE-856b.
- CENSUS: /Volumes/NVME/applearchive-cleanroom-ws/tmp/encviewer-q37/
  cN.rav continuous 20913..38080. oracle: head -c N /dev/zero |
  compression_tool -encode -a lzraven. pay = raw[12:-4].
- 96B-ERA ANALYSIS: rzone/phead template scripts assume 76B pay —
  96B zones + mixed heads need custom inline surveys (pattern:
  VPOS sweep -> q/m split -> tabs -> b4/b5 exact -> reuse vs
  prior-m -> PBB-vpos-first + dips + B-Q on shared pos). see
  this shift's PREs 1186b..1205b for shapes.
- NEXT REUSE REF: P61 m-tab PRE-1205b (6B pos[30,31,76..79]):
  b47ffd39e279/c27f6778aace/02f8c73bc23d/0af8c078af4b/
  1af88eb96ad2/52f8befa2a9c/58f89f3c1436/c4f81677a8cf/
  d4f8093daba8/d4f861b6b3a8/d6f872fc7f51/fef85977ebe6/
  00f9baf9750e/4cf9573763cc/54f999b59fcd/92f9a435e93d.
- WATCHES: BOTH-byte full-dump on new (quad BOTH-5 P57; R
  BOTH-5 P37361-zone); B-Q fit #16 hunt (report LCS>=3 +
  positions; CAREFUL: pos in quad mpos must be EXCLUDED from
  shared set — see PRE-1205b pos30 correction); PBB sig bytes
  in/out varies (uniform/split/per-cell — check first); SPLIT
  q-tabs in R (verbatim x7 incl 1 leadless + infix forms incl
  NEW b5+1B+PM02+PM37 and b5+1Bmid+sfx4); dips (none this shift
  — P-heads dip-quiet since 34493); per-row-sig quads BACK
  (P58 — q-tab sig-led); head-b5-wrap (P53 + P60).
- REUSE corpus: writer2 worktree src/rgram.py hex lits (scan in
  scripts auto-picks current tip; writer SHIPS, corpus grows).
- VERIFY duty: poll lanes/encode-writer2 (+writer1) tip every turn;
  at-commit tree (git archive) battery + independent oracle sha.
- WALL: answers BEHAVIOR-ONLY (beds+numbers). heartbeat NOTE ~10 calls.
  PARENT-027: TMPDIR seat dir, NEVER /tmp.
