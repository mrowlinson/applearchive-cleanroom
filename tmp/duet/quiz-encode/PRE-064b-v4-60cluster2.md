# PRE-064b 60-cluster2 7341..7432 + band-run 7433.. (frontier stage)

## census (v5an first-hand, 256 rows all 60B, 50 var)
- 7249..7340: body-B tail (b0 26/b1 b5; bands 7261/7277/7293/
  7309; b5 f8->f9 @7296).
- 7341/7342: transition lits (b0 2c/52; b1 00/0b; b5->d9).
- 7343..7358: 16-row (b0 26/b1 b5 — body-B repeat).
- 7359..7368: chatter-10 (b0 a4/b1 16; edges 8/10 rows).
- 7369..7432: 64-body (b0 4c/b1 6a; quiet 7369..7432).
- 7433..7504: bands (29-flip @7433; b0 1e/3e/9e/de/ee-16s;
  b5 d9->da @7424; edges 7433..7497 step-16).
- b4 ramp. split: ..7340 / 7341..7432 / 7433... tabs on demand.
