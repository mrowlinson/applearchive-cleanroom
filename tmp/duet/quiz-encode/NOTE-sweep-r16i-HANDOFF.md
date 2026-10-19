# NOTE-sweep-r16i-HANDOFF: run cap 2/2, EXIT per PARENT-074

- Filed: GATE-171e45a (b221) + GATE-3420198
  (b223), both PASS-functional first-hand.
- Next odd: b225 99edcdec T10R152 n<=70676
  (922 tiers, PYID 4594, RGRAM 9188).
  Ungated + unclaimed at handoff. Range =
  b224 max 70420 + 1 = 70421..70676 (256 n;
  floor from filed GATE-f7d524d, re-verify
  vs quiz at claim time).
- Successor recipe: clone r16i-3420198 dir ->
  r16j-99edcdec; sed 3420198->99edcdec, T10R151->
  T10R152, 70073->70421, 70328->70676; inherit
  scan 3420198/223 + 99edcdec/225; fix the
  sed-chained scan/rm lines by hand (both
  lines land on the new rev — see r16i);
  write b225-tabcmp.py (same shape); seed pyid/
  corpus from r16i-3420198 (missing-only regen).
- C-table n varies by band (b221 71, b223 68):
  do NOT trust size guesses, EQ is the bar.
- Quiz diff 0 @ max Q361 (18:07). Rival-check
  b225 before claiming. Seat CLAIM HELD (not
  removed, no joint DONE). WT clean @d56ce19.
- EXITING per PARENT-074 (cap+handoff=exit,
  no hold-poll). Successor overwrites CLAIM.
