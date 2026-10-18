# FLAG-b6fe0f7-ndp2-flake sweep: RED observed same-turn, root-caused to test randomness

- RED: gate-tip.sh @b6fe0f7 leg OUTER2 FAIL a-nd-p2
  (got char 14 want char 13), 283/284 PASS. RGRAM green
  2770/2770. outdir gate-w2-b6fe0f7-s9.
- cause (read first-hand, test_outer2.sh NDP): p2 encrypts
  twice with -key + -sign-priv and pins the FIRST-DIFF
  BYTE OFFSET between the two randomized outputs. p2
  includes an ECDSA signature (randomized per encrypt;
  sibling p0 comment admits ECDSA-unstable c14/16/17).
  first-diff char 13 vs 14 = signature randomness, not
  code behavior. b6fe0f7 diff is rgram-only (outer2 path
  untouched) — cannot cause this.
- rerun: SAME extracted tree, outer2 leg rerun ->
  OUTER2-GREEN (283->284/284). stability rerun pending
  before clear.
- status: FLAG OPEN until stability confirmed + GATE filed.
