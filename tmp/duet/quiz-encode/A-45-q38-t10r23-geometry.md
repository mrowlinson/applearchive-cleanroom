# A-45 (Q-38): T10R23 R-zone 25181..25436 geometry — DERIVED

Bed: 256 fresh-oracle cells N=25181..25436 + 64 quad cells
N=25117..25180 (own beds, payload .rav[12:-4]). 256/256 76B.
(Post-hoc confirm: writer committed d3afa19 before this
answer; derivation is oracle-first.)

## 1. geometry: YES, exactly as observed — 16x16 m8/q6
- m-varying-only: b40,41,42,43,56,57,58,59 (8B m-tab;
  16/16 rows distinct, MINDEP true). head M0 a273fe45f34c8c52.
- q-varying-only: b5,36,37,72,73,74,75 (q-tab 6B payload @
  b36,37,72-75 + b5 q-stepped). head Q0 q-pay 2117ef7bf812.
- b4 varies with both (mixed function, not tabbed).

## 2. q-tab vs POM: POM-CORE (4B shared, 2B head NEW)
- NOT equal: full-row positional 0/16, set 0/16.
- 4B suffix (b72-75) == _T10POM 4B suffix positionally
  16/16 (e.g. q0 ef7bf812 == POM0 suffix; q5 4db9846d;
  q15 5bfc77d5). 2B head (b36-37) all-NEW per row
  (2117/a124/a18d... vs POM e4a2/94a4/b4b1...).
- new pattern: R21/R22 were FULL q reuse; R23 is first
  partial CORE reuse. agrees with d3afa19 "POM-core".

## 3. b5: 196/197/198 steps + 2 intra-row flips; NO dips
- b5 = 196 (q0-1) / 197 (q2-10) / 198 (q11-15); intra-row
  flip m2->m3 at exactly N=25216 (q2) and N=25344 (q10).
  flip locus m=3 (differs from R20's m=8).
- dip scan: 0 odd cells (all 76B, b5 in {196,197,198}) —
  no D markers.

## verdict: 16x16 m8B@40-43,56-59 + q6B@36,37,72-75 + b5;
q = POM 4B-core + NEW 2B head; b5 flips 25216 + 25344
