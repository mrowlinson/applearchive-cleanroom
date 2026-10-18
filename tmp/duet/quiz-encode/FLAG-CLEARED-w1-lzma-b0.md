# FLAG-CLEARED-w1-lzma-b0 (m4m fixed, holdout 12/12 GREEN @9895a19)

- HELD: GATE-9433954 RED (m4m tail-stream XZ b0 02-vs-03 +4B, holdout 11/12).
- FIX: 906081f b0-rule (4 iff unc>=2^21 else 2 iff unc,comp<128 else 3), py+C.
- PROOF: sweep holdout 12/12 GREEN first-hand x2 (tree+aae @9895a19), GATE-PASS
  full battery, m4m byte-identical py+C. GATE-9895a19 filed.
- w1 merge UNBLOCKED on lzma grounds. NOTE-RED-9433954-lzma-b0 HISTORICAL.
