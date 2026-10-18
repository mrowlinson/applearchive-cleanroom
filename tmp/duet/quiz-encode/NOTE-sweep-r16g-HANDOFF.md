# NOTE-sweep-r16g-HANDOFF: run cap 2/2, EXIT per PARENT-074

- Filed: GATE-8d5bc17 (b213) + GATE-6b2a92c
  (b215), both PASS-functional first-hand.
- Next odd: b217 9b86a7a T10R148 n<=69284
  (906 tiers, PYID 4482, RGRAM 8964).
  Ungated + unclaimed at handoff. Range =
  b216 max 69028 + 1 = 69029..69284 (256 n;
  floor from f501344 cport msg — b216
  CLAIMED by sweep2 r27 but ungated, re-verify
  vs sweep2 GATE if filed by then).
- Successor recipe: clone r16g-6b2a92c dir ->
  r16h-9b86a7a; sed 6b2a92c->9b86a7a, T10R147->
  T10R148, 68681->69029, 68936->69284; inherit
  scan 6b2a92c/215 + 9b86a7a/217; fix the
  sed-chained scan/rm lines by hand (both
  lines land on the new rev — see r16g);
  write b217-tabcmp.py (same shape); seed pyid/
  corpus from r16g-6b2a92c (missing-only regen).
- C-table n varies by band (b213 69, b215 67):
  do NOT trust size guesses, EQ is the bar.
- Quiz diff 0 @ max Q361 (04:18). Rival-check
  b217 before claiming. Seat CLAIM HELD (not
  removed, no joint DONE). WT clean @d56ce19.
- EXITING per PARENT-074/075 (cap+handof=exit,
  no hold-poll). Successor overwrites CLAIM.
