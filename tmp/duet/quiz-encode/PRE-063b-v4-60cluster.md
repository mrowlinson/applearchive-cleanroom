# PRE-063b 60-cluster 6993..7248: trans + 16-row + chatter-10 + 2 bodies

## census (v5am first-hand, 256 rows all 60B, 48 var)
- 6993/6994: transition literals (b0 01/ed; b1 00; 44-flip @6994).
- 6995..7010: 16-row (b0 d2/b1 0e; b5 chatter x6-values).
- 7011..7020: chatter-10 (b0 b6/b5/b6; edges 8/10 rows).
- 7021..7084: body-A (b0 46/45 16-bands; b1 0b; bands 7037/
  7053/7069; b5: b6/d6/d7/97/b7 bands).
- 7085..7248: body-B (b0 26/b1 b5; 23-flip @7085; bands 7101/
  7117/7133/7149/7165/7197/7213/7229; b5 f7/f8 +1 @7168).
- b4 ramp throughout. 22 edges>=8 total.
- split: 6993..7020 / 7021..7084 / 7085..7248. tabs on demand.
