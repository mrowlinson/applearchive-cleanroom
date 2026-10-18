# GATE-c4feeb2 sweep: PASS (rgram 428/428, T5H/I0/I1/I2/I3; covers 96688ce+71d5c8c)

- tip: lanes/encode-writer2 @c4feeb2 (chain 0c12d57->96688ce(T5H)->71d5c8c(I0/I1/I2)->c4feeb2(I3)).
  src +217/-0 rgram.py (6 new branches, asserted ordering).
- coverage: 43/43 writer tips gated (42 PASS + 1 RED-held w1 9433954).
- code read: T5H 2909-3164 (16-tabs b44-47 + k2-tabs + b33/b5 edges); T5I3 3257-3512
  (I2-walk b6/7 + b5 k2-tab/midseg + b8 bands + tabs). ordering + alignments verified.
- battery: GATE-PASS, legs: HYGIENE no-artifacts, CONTAM 0-hits, RGRAM n=428,
  PINS-RGRAM set-eq 428/428, OSS none (outdir gate-w2-c4feeb2-s2).
- pins: 380->428, +48 append-only (12 T5H + 22 I0/I1/I2 + 14 I3).
- viewer: VERIFY-7495d3a/0c12d57/96688ce all PASS, 0..3164 CLOSED (sweep concur).
- NOTE: upper dips + bulges mapped (PRE-038b); I3 @3257 = PRE-039b I2/I3 edge 21-flip row.
