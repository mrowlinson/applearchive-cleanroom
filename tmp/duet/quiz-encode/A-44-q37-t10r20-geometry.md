# A-44 (Q-37): T10R20 R-zone 24137..24392 geometry — DERIVED

Bed: 256 fresh-oracle cells N=24137..24392, payload .rav[12:-4].
256/256 76B. (Post-hoc confirm: writer committed 055bb85
before this answer; derivation below is oracle-first, commit
cited only as agreement check.)

## 1. table geometry: 16x16, m 6B + q 5B+b5, b4 mixed
- m-varying-only bytes: b37, b38, b72, b73, b74, b75 (6B
  m-tab; 16/16 rows distinct, q-independent MINDEP true).
- q-varying-only bytes: b5, b32, b68, b69, b70, b71 (q-tab
  5B payload @ b32,68-71 + b5 q-stepped byte).
- b4 varies with BOTH (q-cycle 147,179,211,243,19,51,83,115
  + m-step +2/cell) — mixed function, not tabbed.
- head rows observed: M0 ae7836bacfc2, Q0 q-pay 1d851ee9aa.

## 2. reuse: NONE — all-NEW rows (0/16 every comparison)
- M20 rows vs R19 own-geometry m-rows (b18,19,68-71):
  0/16 shared. Q20 rows vs R19 q-rows (b13,14,64-67):
  0/16 substring-shared. vs R18 positional: 0/16, 0/16.
- geometries differ per zone (R18 q=[40,41,42,64-67] /
  R19 q=[13,14,64-67] / R20 q=[32,68-71]) — no n reuses.
- agrees with committed 055bb85 (m-tab + q-tab NEW).

## 3. b5 rule: q-stepped with 2 intra-row carries; NO dips
- b5 = 188 (q0-2) / 189 (q3-11) / 190 (q12-15); intra-row
  flip m7->m8 at exactly N=24192 (q3) and N=24320 (q11).
  boundary carries, not D-class.
- dip scan: 0 odd cells (all 76B, b5 in {188,189,190}) —
  no D markers, no lencode flips in zone.

## verdict: 16x16 m6B@37,38,72-75 + q5B@32,68-71 + b5-step;
ALL-NEW rows; b5 carries at 24192 + 24320; no dips
