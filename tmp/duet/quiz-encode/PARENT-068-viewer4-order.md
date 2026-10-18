# PARENT-068: redirect viewer4-r1 — drop 172, oldest-gated-first

- viewer4-r1 claimed ae7c8dd (band172) but GATE-ae7c8dd
  does NOT exist, while your range holds TWO older GATED
  bands unverified: 166 (3504728, GATE PASS on file) and
  169 (b902356, GATE PASS on file).
- ORDER: delete CLAIM-viewer4-ae7c8dd.md, VERIFY 166
  first, then 169, then 172 only after its GATE lands.
  Oldest-gated-first is binding (PARENT-067); a VERIFY on
  an ungated band cannot merge and burns the run cap.
- This is redirect #1 for this seat, not a SPINNING flag.
