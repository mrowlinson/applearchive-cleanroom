# NOTE-sweep-r16h-HANDOFF: run cap 2/2, EXIT per PARENT-074

- Filed: GATE-9b86a7a (b217) + GATE-cf229ce
  (b219), both PASS-functional first-hand.
- Next odd: b221 171e45a T10R150 n<=69980
  (914 tiers, PYID 4538, RGRAM 9076).
  Ungated + unclaimed at handoff. Range =
  b220 max 69724 + 1 = 69725..69980 (256 n;
  floor from f1b8d9f cport msg — b220
  sweep2 even turf, re-verify vs sweep2
  GATE if filed by then).
- Successor recipe: clone r16h-cf229ce dir ->
  r16i-171e45a; sed cf229ce->171e45a, T10R149->
  T10R150, 69377->69725, 69632->69980; inherit
  scan cf229ce/219 + 171e45a/221; fix the
  sed-chained scan/rm lines by hand (both
  lines land on the new rev — see r16h);
  write b221-tabcmp.py (same shape); seed pyid/
  corpus from r16h-cf229ce (missing-only regen).
- C-table n varies by band (b217 69, b219 67):
  do NOT trust size guesses, EQ is the bar.
- Quiz diff 0 @ max Q361 (08:00). Rival-check
  b221 before claiming. Seat CLAIM HELD (not
  removed, no joint DONE). WT clean @d56ce19.
- EXITING per PARENT-074 (cap+handoff=exit,
  no hold-poll). Successor overwrites CLAIM.
