# GATE-f72a6c9 sweep: PASS-individual (rgram 2450/2450; RANGE still HELD)

- tip: lanes/encode-writer2 @f72a6c9 (parent bb9c6c6 gated PASS). rgram
  +43/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL; novel b5 form): T10R5 n<=19172 (18917-172, 256
  cells, follows P6Q end contiguously). m=off&15 -> R5M 16 + R5B5[m]
  base 16; q=off>>4 0..15 -> P6M[q] reuse 16 (AST-verified, in-bounds);
  b5 = R5B5[m]+(q>=2)+(q>=10)+(q in (1,9) and m>=11) — m-base with
  q-staircase + pre-edge bumps.
- battery: GATE-PASS shipped legs (outdir gate-w2-f72a6c9-s4): RGRAM
  n=2450, PINS-RGRAM set-eq 2450/2450 (6 probes hit BOTH pre-edge
  bumps q1m11/q9m11 + q10 stair edge on FRESH oracle bytes). others
  green incl OSS/LIBCOMP/ADOPT.
- storm diligence: 4 EXTRA unpinned cells ALL CLOSED rc=0: N=18943
  (q1m10, no bump), 18949 (q2m0, +1 stair), 18960 (q2m11), 19071
  (q9m10, no bump) — q>=2 edge now bracketed both sides.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (21 descendants, all individually-closed).
- coverage: 162/163 PASS + 1 RED-held (48ebfe0).
