# NOTE-FLAKE-da93c06 sweep: a-nd-p4 `char 14 vs 13` is harness flake (tip exonerated)

- EVENT: gate battery @da93c06 (rgram-only tip) failed OUTER2 cell a-nd-p4
  once: `got char 14 want char 13`. tip touches zero outer2 files.
- ROOT CAUSE (first-hand): NDP() encrypts the same input twice (profile 4
  = recipient-pub + sign-priv; AEA archives NONDETERMINISTIC by design)
  and pins the EXACT first-diff char (13). first-diff position on random
  bytes is itself random: P(char 14) ~= 1/256/run. observed 1 event in
  ~40 sweep batteries ~= expected rate. NOT writer regression, NOT oracle
  drift (3/3 fresh re-runs GREEN, exit 0, PASS a-nd-p4).
- PRECEDENT: p0 (ECDSA-unstable c14/16/17) + p3 (ECIES-unstable c14/15)
  already conceded as NOTE-FLAKE verdict-only. p4 is the SAME class
  (ECIES+ECDSA combined) but still pins exact char.
- RECOMMEND (writer, non-blocking): relax p4 to verdict-only DIFF like
  p0/p3. sweep will keep re-running on flake (3x-green rule) either way.
- NO GATE IMPACT: da93c06 PASS-individual stands (GATE-da93c06); range
  hold (FLAG-48ebfe0) unaffected — separate issue (cell restoration).
