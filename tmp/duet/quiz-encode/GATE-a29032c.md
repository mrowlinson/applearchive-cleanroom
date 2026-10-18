# GATE-a29032c sweep: PASS-individual (rgram 2310/2310; RANGE still HELD)

- tip: lanes/encode-writer2 @a29032c (parent 38095eb gated PASS). rgram
  +42/-0 (pure addition), for-list +17177/17280/17408/17432, pins +8
  rows append-only.
- code read (FULL): T10S n<=17432 (17177-432, 256 cells, follows Q2 end
  17176 contiguously ✓). m=off&15 -> SM 16 6B (b13,14,64-67); q=off>>4
  0..15 -> SB5 16 + Q2T[q][2:] 5B (q-index in-bounds for both, AST-
  verified 16/16/16); b5 = SB5[q]+(q in (6,14) and m>=7).
- battery: GATE-PASS shipped legs (outdir gate-w2-a29032c-s4): RGRAM
  n=2310, PINS-RGRAM set-eq 2310/2310 (4 storm probes incl the q6m7/
  q14m7 carry-boundary cells on FRESH oracle bytes). all other legs
  green incl OSS/LIBCOMP/ADOPT.
- storm diligence (beyond battery): 4 EXTRA unpinned cells on fresh
  bytes ALL CLOSED rc=0: N=17201 (q1m8), 17308 (q8m3), 17279 (q6m6,
  carry-boundary-adjacent), 17409 (q14m8). probe design sound.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (11 descendants, all individually-closed).
- coverage: 152/153 PASS + 1 RED-held (48ebfe0).
