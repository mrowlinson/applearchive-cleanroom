# VERIFY-5a83dc4 viewer: PASS (outer2 3x GREEN, EC-key flake fix)

- tip: lanes/encode-writer2 @5a83dc4 (parent 5ada55e ✓, current w2 tip).
  delta test-only: +11/-1 test_outer2.sh (keygen loop until der[6]==0x20).
  vectors/ UNTOUCHED (284 rows, 0 churn ✓ as claimed).
- code read: loop regens EC key max 10 until DER OCTET len 0x20 (32B);
  check = der[5]==0x04(tag OCTET)+der[6]==0x20(len 32) — matches
  NOTE-w2s7-8 root-cause (LibreSSL strips leading zero, priv<2^248).
  worst case exits loop with 31B key (try-10 cap, no hard fail) — same
  flake 1/256^10, acceptable; pins unaffected either way.
- battery: 3x OUTER2-GREEN fresh workdirs (flake-hunt: 0/3 RED).
- NOTE-w2s7-8 landed: NOTE-065b pre-cite wart CLOSED.
- hygiene: no artifact paths. verdict: PASS for gate.
