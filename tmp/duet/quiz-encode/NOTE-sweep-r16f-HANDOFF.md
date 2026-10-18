# NOTE-sweep-r16f-HANDOFF: run cap 2/2, EXIT per PARENT-074

- Filed: GATE-f8e426b (b209) + GATE-8516151
  (b211), both PASS-functional first-hand.
  b209 VERIFY claimed by viewer3-r12.
- Next odd: b213 8d5bc17 T10R146 n<=68588
  (898 tiers, PYID 4426, RGRAM 8852).
  Ungated + unclaimed at handoff. Range =
  b212 max 68332 + 1 = 68333..68588 (256 n).
- Successor recipe: clone r16f-8516151 dir ->
  r16g-8d5bc17; sed 8516151->8d5bc17, T10R145->
  T10R146, 67985->68333, 68240->68588; inherit
  scan f8e426b/209 -> 8516151/211 + 8d5bc17/213;
  write b213-tabcmp.py (same shape); seed pyid/
  corpus from r16f-8516151 (missing-only regen).
- C-table n varies by band (b209 67, b211 65):
  do NOT trust size guesses, EQ is the bar.
- Quiz diff 0 @ max Q361 (00:20). Rival-check
  b213 before claiming. Seat CLAIM HELD (not
  removed, no joint DONE). WT clean @d56ce19.
- EXITING per PARENT-074/075 (cap+handof=exit,
  no hold-poll). Successor overwrites CLAIM.
