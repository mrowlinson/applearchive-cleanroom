# GATE-6e7b76a sweep: PASS-individual (rgram 2556/2556; RANGE still HELD)

- tip: lanes/encode-writer2 @6e7b76a (parent bf43262 gated PASS). rgram
  +166/-0 (pure addition), for-list +8 cells, pins +16 rows append-only.
- code read (ALL 5 branches; PA-names for P10): PA0 singleton (20217,
  b0=7c, follows R8 end contiguously) + PA1 singleton (20218, b0=6a) +
  PAA 16-row (20219-34, off0-15, PAA 16) + PAB 10-row (20235-44,
  off0-9, PAB 10) + PAQ 4x16 (20245-308: m0-15 PAM 16 7B, q0-3 PAQ 4
  10B; b5 CONST 0x9e, no carry — corner pins adequate for b5).
  AST-verified all rows + offsets.
- battery: GATE-PASS shipped legs (outdir gate-w2-6e7b76a-s4): RGRAM
  n=2556, PINS-RGRAM set-eq 2556/2556; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- quad diligence: PAQ corner-only pinned (20245/20308) => 3 EXTRA
  unpinned cells ALL CLOSED rc=0: N=20268 (q1m7), 20290 (q2m13),
  20297 (q3m4) — all 4 quartets now sampled.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (28 descendants, all individually-closed).
- coverage: 169/170 PASS + 1 RED-held (48ebfe0).
