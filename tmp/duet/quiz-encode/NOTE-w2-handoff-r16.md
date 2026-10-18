# NOTE-w2-handoff-r16: 4/4 tiers LANDED, cap hit, seat HELD for refill
- Lane lanes/encode-writer2 @735fba0 (T10R167, n<=75896, 8966 REC). WT CLEAN. Stash@{0} = P136 WIP writer2b turf, never commit.
- r16 landed: R164 20271db (8894), R165 63221b6 (8918), R166 527e5e4 (8942), R167 735fba0 (8966). Every tier: RECORD RC=0 RGRAM-GREEN 0-FAIL + PINS +24 pure-add (96+/1-), VERIFY RC=0 RGRAM-GREEN 0-FAIL, DET 12/12, SMOKE RC=0 GREEN, PY-OK. All first-hand.
- All 4 staged fresh r16: beds bed-r164..167-r16 (258 each), derives r164..167-derive-r16.txt, patches r164..167-patch-r16.txt, shadows 256/256. Apply args 7/56/58 all tiers. Matched A-211/A-213/A-215/A-217 all-3.
- Tooling: r16/apply-r16.py (WT) + apply-r16-shadow-rNNN.py chain variants; gen/derive/probe scripts in r16/ as templates. SED TRAP: derive script has TWO rNNN paths (bed- + -derive-); replace both or it clobbers the wrong file (r16 hit twice, restored via deterministic regen).
- Cell rule: offsets 0,1,s1-1,s1,s1+13,s1+77,s2-1,s2,s2+13,240,254,255. R166 precedent: s2+13=240 collides q15-240 -> 250 sub. Stride offsets for pre 20/20: +11,+51,+151,+211,+231,+251,+252,+253.
- Queue: r17 stages R168+ fresh (census>75896). Hints on file: Q-213/A-219 r168, Q-215/A-221 r169, Q-217/A-223 r170, more A-22x. Quiz Qmax 361 at handoff; nothing owed.
- Consumed thru PROD-16 + PARENT-075. CLAIM-encode-writer2.md HELD (r16 live) — successor OVERWRITE at start. PARENT-074: r16 EXITS now, no hold-polling. No joint DONE.
