# GATE-38095eb sweep: PASS-individual (rgram 2302/2302; RANGE still HELD)

- tip: lanes/encode-writer2 @38095eb (parent 6c69085 gated PASS). rgram
  +9/-4, for-list +17145/17161/17176, pins +6 rows append-only.
- code read (FULL diff): Q2B 2->4 words; boundary 17144->17176 (off0-63,
  q0-3 fits 4 words ✓); b5 rule pay[5]==tab+((q==3)or(q==2 and m>=7)).
  old region q0/q1: int+False=+0 => byte-identical to 6c69085's
  full-6B compare (PURE EXTENSION, plus all prior pins re-green).
- battery: GATE-PASS shipped legs (outdir gate-w2-38095eb-s4): RGRAM
  n=2302, PINS-RGRAM set-eq 2302/2302 (new q2/q3 pins incl b5-rule
  cells verified on FRESH oracle bytes). HYGIENE/CONTAM/OSS/LIBCOMP/
  ADOPT clean.
- manual RED-cell re-verify @tip: N=15752 fresh bytes => CLOSED T9L1Q
  rc=0 (fix holds). for-list still LACKS 15752 (hold persists).
- NOTE (asserted-not-visible, arbitrated by battery): msg claims "fix
  Q2B[3] typo" but diff only ADDS words 2-3; battery on fresh oracle
  bytes is the arbiter => content correct => PASS stands.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (48ebfe0..38095eb unmergeable pending restore).
- coverage: 151/152 PASS + 1 RED-held (48ebfe0).
