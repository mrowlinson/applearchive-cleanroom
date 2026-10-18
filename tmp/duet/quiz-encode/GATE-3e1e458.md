# GATE-3e1e458 sweep: PASS-individual (rgram 2528/2528; RANGE still HELD)

- tip: lanes/encode-writer2 @3e1e458 (parent 141e67e gated PASS). rgram
  +162/-0 (pure addition), for-list +8 cells, pins +16 rows append-only.
- code read (ALL 5 branches; no-dip head + b5-in-mtab quad): P90
  singleton (19869, b0=40, follows R7 end contiguously) + P91 singleton
  (19870, b0=04) + P9A 16-row (19871-86, off0-15, P9A 16) + P9B 10-row
  (19887-96, off0-9, P9B 10) + P9Q 4x16 (19897-960: m0-15 P9M 16 7B
  incl b5 — NO separate b5 rule; q0-3 P9Q 4 9B). AST-verified all
  rows + offsets.
- battery: GATE-PASS shipped legs (outdir gate-w2-3e1e458-s4): RGRAM
  n=2528, PINS-RGRAM set-eq 2528/2528; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- quad diligence: P9Q corner-only pinned (19897/19960) => 3 EXTRA
  unpinned cells ALL CLOSED rc=0: N=19919 (q1m6), 19941 (q2m12),
  19950 (q3m5) — all 4 quartets now sampled.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (26 descendants, all individually-closed).
- coverage: 167/168 PASS + 1 RED-held (48ebfe0).
