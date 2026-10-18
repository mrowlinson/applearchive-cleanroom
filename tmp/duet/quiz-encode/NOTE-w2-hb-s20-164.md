# NOTE-w2-hb-s20-164 — R135 DERIVE+SHADOW 256/256 + RECORD 27%

bump-20

- R135 (own, first-hand, cen-p137r135): sig 52760000 256/256, m/q indep 16/16, b4=f3+2off b5=f7+(>=7)+(>=135) fit, varpos tabs+{4,5}, consts 67 — A-151 all-3 CONFIRM reproduced
- MATCH: own MTAB/CONSTS == w2s15 r135-patch; own QTAB == _T10P137M 16/16 in place (77th q-carried)
- PATCH r5: _T10R135M + _T10R135Q (own-copy) + _T10R135C + handler; shadow stack R134+R135 SYNTAX-OK, SWEEP 256/256 CLOSED, 0 bad
- RECORD R134: 2242/~8174 (~27%), 0 FAIL; worktree still FROZEN
- INBOX: no new PARENT/A, no joint DONE
- NEXT: sleep-poll RECORD -> PINS-diff -> DET -> smoke.sh -> COMMIT R134 -> apply R135
